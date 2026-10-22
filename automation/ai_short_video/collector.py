from __future__ import annotations

import argparse
import hashlib
import html
import json
import sqlite3
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = Path(__file__).with_name("config.json")
STATE_DIR = ROOT / ".automation" / "ai-short-video"
STATE_DB = STATE_DIR / "state.sqlite3"
CANDIDATES_FILE = STATE_DIR / "candidates.json"


@dataclass(frozen=True)
class Candidate:
    title: str
    url: str
    published_at: str | None
    collected_at: str
    region: str
    dimensions: list[str]
    source_query: str
    source_feed: str
    summary: str
    score: int
    fingerprint: str


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonicalize_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value.strip())
    if parsed.netloc.lower().endswith("bing.com") and parsed.path.lower().endswith("/news/apiclick.aspx"):
        redirect = urllib.parse.parse_qs(parsed.query).get("url", [])
        if redirect:
            parsed = urllib.parse.urlsplit(redirect[0])
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(key, val) for key, val in query if not key.lower().startswith("utm_")]
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/"), urllib.parse.urlencode(query), "")
    )


def text_fingerprint(title: str, summary: str) -> str:
    normalized = " ".join(html.unescape(f"{title} {summary}").lower().split())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def repair_mojibake(value: str) -> str:
    if not any(marker in value for marker in ("鐭", "瑙", "棰", "鍒", "锛", "銆")):
        return value
    try:
        return value.encode("gb18030").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value


def classify(text: str, dimensions: dict[str, list[str]], dimension_hint: str | None = None) -> list[str]:
    lowered = text.lower()
    matches = [name for name, words in dimensions.items() if any(word.lower() in lowered for word in words)]
    if dimension_hint in dimensions and dimension_hint not in matches:
        matches.append(dimension_hint)
    return matches or ["general"]


def iter_queries(config: dict) -> Iterable[tuple[str, str | None, str]]:
    for region, query_groups in config["queries"].items():
        if isinstance(query_groups, list):
            for query in query_groups:
                yield region, None, query
            continue
        for dimension, queries in query_groups.items():
            for query in queries:
                yield region, dimension, query


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def build_feeds(query: str, region: str) -> list[str]:
    encoded = urllib.parse.quote_plus(query)
    if region == "domestic":
        google = f"https://news.google.com/rss/search?q={encoded}&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
        bing = f"https://www.bing.com/news/search?q={encoded}&format=rss&setlang=zh-cn"
    else:
        google = f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"
        bing = f"https://www.bing.com/news/search?q={encoded}&format=rss&setlang=en-us"
    return [google, bing]


def may_fetch(url: str, user_agent: str, cache: dict[str, bool]) -> bool:
    parsed = urllib.parse.urlsplit(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin in cache:
        return cache[origin]
    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(urllib.parse.urljoin(origin, "/robots.txt"))
    try:
        parser.read()
        allowed = parser.can_fetch(user_agent, url)
    except (OSError, urllib.error.URLError, ValueError):
        allowed = True
    cache[origin] = allowed
    return allowed


def fetch(url: str, user_agent: str, timeout: int) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": user_agent, "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.5"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read(5_000_000)


def node_text(node: ET.Element, names: tuple[str, ...]) -> str:
    for child in node.iter():
        if child.tag.rsplit("}", 1)[-1].lower() in names and child.text:
            return child.text.strip()
    return ""


def parse_feed(payload: bytes) -> Iterable[tuple[str, str, str | None, str]]:
    root = ET.fromstring(payload)
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1].lower() not in {"item", "entry"}:
            continue
        title = node_text(node, ("title",))
        summary = node_text(node, ("description", "summary", "content"))
        published = node_text(node, ("pubdate", "published", "updated")) or None
        link = node_text(node, ("link",))
        if not link:
            for child in node:
                if child.tag.rsplit("}", 1)[-1].lower() == "link" and child.attrib.get("href"):
                    link = child.attrib["href"]
                    break
        if title and link:
            yield title, link, published, summary


def init_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.execute("CREATE TABLE IF NOT EXISTS seen (url TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, first_seen TEXT NOT NULL)")
    connection.execute("CREATE INDEX IF NOT EXISTS seen_fingerprint_idx ON seen(fingerprint)")
    return connection


def is_seen(connection: sqlite3.Connection, url: str, fingerprint: str) -> bool:
    return connection.execute(
        "SELECT 1 FROM seen WHERE url = ? OR fingerprint = ? LIMIT 1", (url, fingerprint)
    ).fetchone() is not None


def score_candidate(url: str, dimensions: list[str], preferred_domains: list[str], published: datetime | None) -> int:
    host = urllib.parse.urlsplit(url).netloc.lower()
    score = len(dimensions) * 2
    if any(host == domain or host.endswith(f".{domain}") for domain in preferred_domains):
        score += 8
    if published:
        age_hours = (datetime.now(timezone.utc) - published).total_seconds() / 3600
        score += max(0, 4 - int(age_hours // 24))
    return score


def select_balanced(
    candidates: list[Candidate],
    domestic_ratio: float,
    limit: int,
    dimension_names: Iterable[str],
    min_per_dimension: int,
) -> list[Candidate]:
    region_targets = {
        "domestic": round(limit * domestic_ratio),
        "overseas": limit - round(limit * domestic_ratio),
    }
    selected: list[Candidate] = []
    selected_urls: set[str] = set()
    region_counts = {"domestic": 0, "overseas": 0}

    def add(item: Candidate) -> None:
        selected.append(item)
        selected_urls.add(item.url)
        region_counts[item.region] = region_counts.get(item.region, 0) + 1

    def rank(item: Candidate) -> tuple[bool, int, str]:
        region_full = region_counts.get(item.region, 0) >= region_targets.get(item.region, limit)
        return region_full, -item.score, item.title

    for dimension in dimension_names:
        while sum(dimension in item.dimensions for item in selected) < min_per_dimension and len(selected) < limit:
            choices = [
                item for item in candidates
                if item.url not in selected_urls and dimension in item.dimensions
            ]
            if not choices:
                break
            add(min(choices, key=rank))

    while len(selected) < limit:
        choices = [item for item in candidates if item.url not in selected_urls]
        if not choices:
            break
        add(min(choices, key=rank))

    return sorted(selected, key=lambda item: (-item.score, item.region, item.title))


def collect(config: dict, state_db: Path, output: Path, since: datetime | None = None) -> tuple[list[Candidate], list[str]]:
    now = datetime.now(timezone.utc)
    cutoff = since or now - timedelta(hours=int(config["lookback_hours"]))
    connection = init_db(state_db)
    robots_cache: dict[str, bool] = {}
    candidates_by_url: dict[str, Candidate] = {}
    errors: list[str] = []
    try:
        for region, dimension_hint, query in iter_queries(config):
            for feed_url in build_feeds(query, region):
                if not may_fetch(feed_url, config["user_agent"], robots_cache):
                    errors.append(f"robots denied: {feed_url}")
                    continue
                try:
                    items = list(parse_feed(fetch(feed_url, config["user_agent"], config["request_timeout_seconds"])))
                except (ET.ParseError, OSError, urllib.error.URLError, ValueError) as exc:
                    errors.append(f"{feed_url}: {type(exc).__name__}: {exc}")
                    continue
                for title, raw_url, published_raw, summary in items:
                    published = parse_date(published_raw)
                    if published and published < cutoff:
                        continue
                    url = canonicalize_url(raw_url)
                    title = repair_mojibake(html.unescape(title)).strip()
                    clean_summary = " ".join(repair_mojibake(html.unescape(summary)).split())[:1000]
                    fingerprint = text_fingerprint(title, clean_summary)
                    if url in candidates_by_url or is_seen(connection, url, fingerprint):
                        continue
                    dimensions = classify(f"{title} {clean_summary}", config["dimensions"], dimension_hint)
                    candidates_by_url[url] = Candidate(
                        title=title,
                        url=url,
                        published_at=published.isoformat() if published else None,
                        collected_at=now.isoformat(),
                        region=region,
                        dimensions=dimensions,
                        source_query=query,
                        source_feed=feed_url,
                        summary=clean_summary,
                        score=score_candidate(url, dimensions, config["preferred_domains"], published),
                        fingerprint=fingerprint,
                    )
        selected = select_balanced(
            list(candidates_by_url.values()),
            float(config["domestic_ratio"]),
            int(config["max_candidates"]),
            config["dimensions"],
            int(config.get("min_candidates_per_dimension", 0)),
        )
        coverage = {
            dimension: sum(dimension in item.dimensions for item in selected)
            for dimension in config["dimensions"]
        }
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps({
            "generated_at": now.isoformat(),
            "cutoff": cutoff.isoformat(),
            "candidate_count": len(selected),
            "coverage": coverage,
            "region_counts": {
                region: sum(item.region == region for item in selected)
                for region in ("domestic", "overseas")
            },
            "errors": errors,
            "candidates": [asdict(item) for item in selected],
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        with connection:
            connection.executemany(
                "INSERT OR IGNORE INTO seen(url, fingerprint, first_seen) VALUES (?, ?, ?)",
                [(item.url, item.fingerprint, item.collected_at) for item in selected],
            )
        return selected, errors
    finally:
        connection.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Collect AI short-video research candidates from public RSS indexes.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--state-db", type=Path, default=STATE_DB)
    parser.add_argument("--output", type=Path, default=CANDIDATES_FILE)
    parser.add_argument("--since", help="UTC/offset ISO timestamp for catch-up collection")
    args = parser.parse_args(argv)
    config = load_config(args.config)
    since = datetime.fromisoformat(args.since.replace("Z", "+00:00")) if args.since else None
    if since and since.tzinfo is None:
        parser.error("--since must include a timezone offset")
    candidates, errors = collect(config, args.state_db, args.output, since)
    print(json.dumps({"candidates": len(candidates), "errors": len(errors), "output": str(args.output)}, ensure_ascii=False))
    return 0 if candidates or not errors else 2


if __name__ == "__main__":
    sys.exit(main())
