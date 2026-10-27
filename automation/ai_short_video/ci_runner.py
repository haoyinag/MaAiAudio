from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

import collector


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "docs" / "ai-short-video"
STAGING_DIR = ROOT / ".automation" / "ai-short-video"
ALLOWED_MODIFIED_ROOT = "docs/ai-short-video/"
SHANGHAI = timezone(timedelta(hours=8), name="Asia/Shanghai")


class CiError(RuntimeError):
    pass


def git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if result.returncode:
        raise CiError((result.stderr or result.stdout or "git failed").strip())
    return result.stdout.strip()


def dated_directories(parent: Path, prefix: str = "") -> list[date]:
    values: list[date] = []
    if not parent.exists():
        return values
    for path in parent.iterdir():
        if not path.is_dir() or not path.name.startswith(prefix):
            continue
        try:
            values.append(date.fromisoformat(path.name[len(prefix):].replace(".", "-")))
        except ValueError:
            continue
    return sorted(values)


def latest_inbox_date(docs_root: Path = DOCS_ROOT) -> date | None:
    values = dated_directories(docs_root / "inbox")
    return values[-1] if values else None


def release_due(run_date: date, docs_root: Path = DOCS_ROOT, interval_days: int = 3) -> bool:
    versions = dated_directories(docs_root, "v")
    return not versions or (run_date - versions[-1]).days >= interval_days


def prepare(mode: str, run_date: date) -> None:
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    policy_source = Path(__file__).with_name("research_policy.md")
    (STAGING_DIR / "research_policy.md").write_text(policy_source.read_text(encoding="utf-8"), encoding="utf-8")
    if mode != "daily":
        return
    previous = latest_inbox_date()
    since = datetime.combine(previous, time.min, SHANGHAI).astimezone(timezone.utc) if previous else None
    candidates, errors = collector.collect(
        collector.load_config(collector.DEFAULT_CONFIG),
        STAGING_DIR / "state.sqlite3",
        STAGING_DIR / "candidates.json",
        since,
    )
    if not candidates and errors:
        raise CiError("All discovery feeds failed; refusing to create an empty daily run")


def changed_paths() -> list[str]:
    paths: list[str] = []
    output = git(["-c", "core.quotepath=false", "status", "--porcelain", "--untracked-files=all"])
    for line in output.splitlines():
        if not line:
            continue
        path = line[3:].replace("\\", "/").split(" -> ", 1)[-1]
        if not path.startswith(".automation/"):
            paths.append(path)
    return paths


def validate(mode: str, run_date: date) -> list[str]:
    paths = changed_paths()
    outside = [path for path in paths if not path.startswith(ALLOWED_MODIFIED_ROOT)]
    if outside:
        raise CiError(f"Codex changed files outside allowed documentation root: {outside}")
    git(["diff", "--check", "HEAD"])
    if mode == "daily" and paths:
        day_root = DOCS_ROOT / "inbox" / run_date.isoformat()
        required = [day_root / "README.md", day_root / "DIGEST.md", day_root / "SCAN.md"]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
        if missing:
            raise CiError(f"Daily output is missing required files: {missing}")
    return paths


def emit_plan(mode: str, run_date: date, force: bool) -> dict[str, str]:
    if mode == "daily":
        due = not (DOCS_ROOT / "inbox" / run_date.isoformat()).exists()
    elif mode == "release":
        due = release_due(run_date)
    else:
        due = True
    should_run = force or due
    return {
        "mode": mode,
        "date": run_date.isoformat(),
        "should_run": str(should_run).lower(),
        "prompt_file": f"automation/ai_short_video/prompts/{mode}.md",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare and validate cloud AI short-video research runs.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("plan", "prepare", "validate"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--mode", required=True, choices=("daily", "release", "audit"))
        sub.add_argument("--date", required=True)
        if command == "plan":
            sub.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    run_date = date.fromisoformat(args.date)
    if args.command == "plan":
        print(json.dumps(emit_plan(args.mode, run_date, args.force)))
    elif args.command == "prepare":
        prepare(args.mode, run_date)
    else:
        print(json.dumps({"changed_paths": validate(args.mode, run_date)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except CiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
