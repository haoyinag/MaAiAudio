from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path

import collector

ROOT = Path(__file__).resolve().parents[2]
AUTOMATION_DIR = ROOT / ".automation" / "ai-short-video"
WORKTREES_DIR = ROOT / ".automation" / "worktrees"
RUN_STATE = AUTOMATION_DIR / "runs.json"
LOCK_FILE = AUTOMATION_DIR / "runner.lock"
PROMPTS_DIR = Path(__file__).with_name("prompts")
ALLOWED_MODIFIED_ROOT = "docs/ai-short-video/"

class CommandError(RuntimeError):
    pass

def executable(name: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    if name == "python":
        candidate = Path(os.environ["LOCALAPPDATA"]) / "Programs" / "Python" / "Python313" / "python.exe"
        if candidate.exists():
            return str(candidate)
    if name == "codex.cmd":
        candidates = sorted((Path.home() / ".vscode" / "extensions").glob("openai.chatgpt-*-win32-x64/bin/windows-x86_64/codex.exe"), reverse=True)
        if candidates:
            return str(candidates[0])
    raise CommandError(f"Required executable not found: {name}")

def run(command: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace", capture_output=True)
    if result.returncode:
        detail = (result.stderr or result.stdout or "").strip()
        raise CommandError(f"Command failed ({result.returncode}): {' '.join(command[:3])}\n{detail}")
    return result

@contextmanager
def exclusive_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise CommandError(f"Another research run is active: {path}") from exc
    try:
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        os.close(descriptor)
        yield
    finally:
        path.unlink(missing_ok=True)

def load_run_state() -> dict:
    return json.loads(RUN_STATE.read_text(encoding="utf-8")) if RUN_STATE.exists() else {}

def save_run_state(state: dict) -> None:
    RUN_STATE.parent.mkdir(parents=True, exist_ok=True)
    RUN_STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def git_output(args: list[str], cwd: Path = ROOT) -> str:
    return run([executable("git"), *args], cwd=cwd).stdout.strip()

def assert_github_auth() -> None:
    run([executable("gh"), "auth", "status"])

def branch_exists_remote(branch: str) -> bool:
    result = subprocess.run([executable("git"), "ls-remote", "--exit-code", "--heads", "origin", f"refs/heads/{branch}"], cwd=ROOT, text=True, capture_output=True)
    return result.returncode == 0

def prepare_worktree(mode: str, date_text: str) -> tuple[str, Path]:
    branch = f"research/{mode}-{date_text}"
    worktree = WORKTREES_DIR / f"{mode}-{date_text}"
    if worktree.exists():
        raise CommandError(f"Stale worktree exists; inspect it before retrying: {worktree}")
    git_output(["fetch", "origin", "master"])
    start = f"origin/{branch}" if branch_exists_remote(branch) else "origin/master"
    git_output(["worktree", "add", "-b" if start == "origin/master" else "-B", branch, str(worktree), start])
    return branch, worktree

def stage_policy(worktree: Path) -> None:
    source = Path(__file__).with_name("research_policy.md")
    target = worktree / ".automation" / "ai-short-video" / "research_policy.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_daily_candidates(worktree: Path, state: dict) -> None:
    since_text = state.get("daily", {}).get("completed_at")
    since = datetime.fromisoformat(since_text) if since_text else None
    candidates, errors = collector.collect(collector.load_config(collector.DEFAULT_CONFIG), collector.STATE_DB, collector.CANDIDATES_FILE, since)
    if not candidates and errors:
        raise CommandError("All discovery feeds failed; refusing to create an empty daily run")
    target = worktree / ".automation" / "ai-short-video" / "candidates.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(collector.CANDIDATES_FILE, target)

def run_codex(mode: str, worktree: Path) -> None:
    prompt = (PROMPTS_DIR / f"{mode}.md").read_text(encoding="utf-8")
    result = subprocess.run([executable("codex.cmd"), "exec", "--sandbox", "workspace-write", "--cd", str(worktree), "-"], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True)
    log_dir = AUTOMATION_DIR / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    (log_dir / f"{mode}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log").write_text((result.stdout or "") + "\n--- STDERR ---\n" + (result.stderr or ""), encoding="utf-8")
    if result.returncode:
        raise CommandError(f"Codex failed with exit code {result.returncode}; see automation log")

def changed_paths(worktree: Path) -> list[str]:
    paths = []
    for line in git_output(["status", "--porcelain", "--untracked-files=all"], cwd=worktree).splitlines():
        if line:
            path = line[3:].replace("\\", "/")
            normalized = path.split(" -> ", 1)[-1]
            if not normalized.startswith(".automation/"):
                paths.append(normalized)
    return paths

def validate_scope(worktree: Path) -> list[str]:
    paths = changed_paths(worktree)
    outside = [path for path in paths if not path.startswith(ALLOWED_MODIFIED_ROOT)]
    if outside:
        raise CommandError(f"Codex changed files outside allowed documentation root: {outside}")
    run([executable("git"), "diff", "--check"], cwd=worktree)
    return paths

def publish(mode: str, date_text: str, branch: str, worktree: Path) -> str | None:
    if not validate_scope(worktree):
        return None
    git = executable("git")
    run([git, "add", "--", "docs/ai-short-video"], cwd=worktree)
    run([git, "commit", "-m", f"docs(ai-short-video): {mode} {date_text}"], cwd=worktree)
    run([git, "push", "--set-upstream", "origin", branch], cwd=worktree)
    view = subprocess.run([executable("gh"), "pr", "view", branch, "--json", "url", "--jq", ".url"], cwd=worktree, text=True, encoding="utf-8", errors="replace", capture_output=True)
    if view.returncode == 0 and view.stdout.strip():
        return view.stdout.strip()
    title = f"AI short-video {mode}: {date_text}"
    body = "Automated research candidate for human review.\n\n- Base: `master`\n- Auto-merge: disabled\n- Scope: `docs/ai-short-video/`"
    return run([executable("gh"), "pr", "create", "--base", "master", "--head", branch, "--title", title, "--body", body], cwd=worktree).stdout.strip()

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run isolated AI short-video research and open a review PR.")
    parser.add_argument("mode", choices=("daily", "release", "audit"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    now = datetime.now(timezone(timedelta(hours=8), name="Asia/Shanghai"))
    date_text = now.strftime("%Y-%m-%d")
    if args.dry_run:
        for name in ("python", "git", "gh", "codex.cmd"):
            print(f"{name}: {executable(name)}")
        print(f"mode={args.mode} date={date_text} root={ROOT}")
        return 0
    with exclusive_lock(LOCK_FILE):
        assert_github_auth()
        state = load_run_state()
        branch, worktree = prepare_worktree(args.mode, date_text)
        stage_policy(worktree)
        if args.mode == "daily":
            copy_daily_candidates(worktree, state)
        run_codex(args.mode, worktree)
        pr_url = publish(args.mode, date_text, branch, worktree)
        state[args.mode] = {"completed_at": now.isoformat(), "branch": branch, "pr_url": pr_url}
        save_run_state(state)
        git_output(["worktree", "remove", "--force", str(worktree)])
        print(pr_url or "No verified changes; no PR created.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except CommandError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
