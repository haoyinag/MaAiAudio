from __future__ import annotations

import argparse
import ctypes
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
COMMAND_TIMEOUT_SECONDS = 15 * 60
CODEX_TIMEOUT_SECONDS = 3 * 60 * 60

class CommandError(RuntimeError):
    pass


def decoded_output(value: str | bytes | None) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value or ""

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

def run(
    command: list[str],
    cwd: Path = ROOT,
    timeout: int = COMMAND_TIMEOUT_SECONDS,
) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise CommandError(f"Command timed out after {timeout}s: {' '.join(command[:3])}") from exc
    if result.returncode:
        detail = (result.stderr or result.stdout or "").strip()
        raise CommandError(f"Command failed ({result.returncode}): {' '.join(command[:3])}\n{detail}")
    return result


def pid_is_running(pid: int) -> bool:
    if pid <= 0:
        return False
    if os.name == "nt":
        process = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if not process:
            return False
        try:
            exit_code = ctypes.c_ulong()
            if not ctypes.windll.kernel32.GetExitCodeProcess(process, ctypes.byref(exit_code)):
                return False
            return exit_code.value == 259
        finally:
            ctypes.windll.kernel32.CloseHandle(process)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def reclaim_stale_lock(path: Path) -> bool:
    try:
        lock_pid = int(path.read_text(encoding="ascii").strip())
    except (OSError, ValueError):
        lock_pid = -1
    if pid_is_running(lock_pid):
        return False
    try:
        path.unlink()
    except FileNotFoundError:
        pass
    return True

@contextmanager
def exclusive_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(2):
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError as exc:
            if attempt or not reclaim_stale_lock(path):
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


def open_pr_url(branch: str, cwd: Path = ROOT) -> str | None:
    result = subprocess.run(
        [executable("gh"), "pr", "list", "--head", branch, "--state", "open", "--json", "url", "--jq", ".[0].url"],
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    return result.stdout.strip() if result.returncode == 0 and result.stdout.strip() else None


def select_branch(mode: str, date_text: str) -> str:
    branch = f"research/{mode}-{date_text}"
    if branch_exists_remote(branch) and not open_pr_url(branch):
        branch = f"{branch}-retry-{datetime.now().strftime('%H%M%S')}"
    return branch


def sync_local_master() -> None:
    try:
        current = git_output(["rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT)
        if current == "master" and not git_output(["status", "--porcelain"], cwd=ROOT):
            git_output(["merge", "--ff-only", "origin/master"], cwd=ROOT)
    except CommandError:
        pass


def prepare_worktree(mode: str, date_text: str) -> tuple[str, Path]:
    branch = f"research/{mode}-{date_text}"
    worktree = WORKTREES_DIR / f"{mode}-{date_text}"
    if worktree.exists():
        if git_output(["status", "--porcelain"], cwd=worktree):
            raise CommandError(f"Stale worktree has uncommitted changes; inspect it before retrying: {worktree}")
        git_output(["worktree", "remove", "--force", str(worktree)])
    git_output(["fetch", "origin", "master"])
    sync_local_master()
    git_output(["worktree", "add", "-B", branch, str(worktree), "origin/master"])
    return branch, worktree

def stage_policy(worktree: Path) -> None:
    source = Path(__file__).with_name("research_policy.md")
    target = worktree / ".automation" / "ai-short-video" / "research_policy.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_daily_candidates(worktree: Path, state: dict) -> None:
    since_text = state.get("daily", {}).get("completed_at")
    since = datetime.fromisoformat(since_text) if since_text else None
    candidates, errors = collector.collect(
        collector.load_config(collector.DEFAULT_CONFIG),
        collector.STATE_DB,
        collector.CANDIDATES_FILE,
        since,
        mark_seen=False,
    )
    if not candidates and errors:
        raise CommandError("All discovery feeds failed; refusing to create an empty daily run")
    target = worktree / ".automation" / "ai-short-video" / "candidates.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(collector.CANDIDATES_FILE, target)

def run_codex(mode: str, worktree: Path) -> None:
    prompt = (PROMPTS_DIR / f"{mode}.md").read_text(encoding="utf-8")
    log_dir = AUTOMATION_DIR / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{mode}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
    try:
        result = subprocess.run(
            [
                executable("codex.cmd"),
                "exec",
                "-c",
                "mcp_servers={}",
                "--sandbox",
                "workspace-write",
                "--cd",
                str(worktree),
                "-",
            ],
            input=prompt,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=CODEX_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        log_path.write_text(
            decoded_output(exc.stdout)
            + "\n--- STDERR ---\n"
            + decoded_output(exc.stderr)
            + f"\nTimed out after {CODEX_TIMEOUT_SECONDS}s.\n",
            encoding="utf-8",
        )
        raise CommandError(f"Codex timed out after {CODEX_TIMEOUT_SECONDS}s; see {log_path}") from exc
    log_path.write_text((result.stdout or "") + "\n--- STDERR ---\n" + (result.stderr or ""), encoding="utf-8")
    if result.returncode:
        raise CommandError(f"Codex failed with exit code {result.returncode}; see automation log")

def changed_paths(worktree: Path) -> list[str]:
    paths = []
    output = run([executable("git"), "-c", "core.quotepath=false", "status", "--porcelain", "--untracked-files=all"], cwd=worktree).stdout
    for line in output.splitlines():
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
    run([git, "push", "origin", "HEAD:master"], cwd=worktree)
    commit_sha = git_output(["rev-parse", "HEAD"], cwd=worktree)
    sync_local_master()
    return commit_sha

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run isolated AI short-video research and push validated changes to master.")
    parser.add_argument("mode", choices=("daily", "release", "audit"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    now = datetime.now(timezone(timedelta(hours=8), name="Asia/Shanghai"))
    date_text = now.strftime("%Y-%m-%d")
    if args.dry_run:
        for name in ("python", "git", "codex.cmd"):
            print(f"{name}: {executable(name)}")
        print(f"mode={args.mode} date={date_text} root={ROOT}")
        return 0
    with exclusive_lock(LOCK_FILE):
        state = load_run_state()
        worktree: Path | None = None
        branch: str | None = None
        try:
            branch, worktree = prepare_worktree(args.mode, date_text)
            stage_policy(worktree)
            if args.mode == "daily":
                copy_daily_candidates(worktree, state)
            run_codex(args.mode, worktree)
            commit_sha = publish(args.mode, date_text, branch, worktree)
            if args.mode == "daily":
                collector.mark_candidates_seen(collector.STATE_DB, collector.CANDIDATES_FILE)
            state[args.mode] = {"completed_at": now.isoformat(), "branch": "master", "commit": commit_sha}
            save_run_state(state)
            print(f"Pushed to master: {commit_sha}" if commit_sha else "No verified changes; nothing pushed.")
        finally:
            if worktree and worktree.exists():
                try:
                    git_output(["worktree", "remove", "--force", str(worktree)])
                except CommandError as exc:
                    print(f"warning: failed to remove worktree: {exc}", file=sys.stderr)
            if branch:
                subprocess.run([executable("git"), "branch", "-D", branch], cwd=ROOT, capture_output=True)
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except CommandError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
