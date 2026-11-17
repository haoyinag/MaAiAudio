# AI short-video automation

The primary scheduler is the local Windows Task Scheduler (`automation/ai_short_video/install_schedules.ps1`), which uses your local Codex CLI session and commits validated `docs/ai-short-video/` updates directly to `master` (eliminating daily PR merge conflicts) while keeping your local working tree in sync.

`.github/workflows/ai-video-research.yml` is retained as an on-demand manual workflow (`workflow_dispatch`) so it does not consume duplicate quota or open conflicting PRs.

## Schedule (Asia/Shanghai)

- Daily discovery: 08:30 (`StartWhenAvailable` catch-up enabled if the machine was asleep/off).
- Release eligibility: Every 3 days at 10:00 (consolidates new inbox entries into `vYYYY.MM.DD/` and rolls forward `docs/ai-short-video/PLAYBOOK.md`).
- Weekly audit: Monday 11:00.
- Manual cloud run (optional): Actions → AI short-video research → Run workflow (`daily`, `release`, or `audit`).

## Reliability behavior

- Runs execute in an isolated temporary Git worktree starting from `origin/master`.
- Strict scope validation (`validate_scope`) ensures Codex can only modify files under `docs/ai-short-video/` and must pass `git diff --check`.
- Candidate URLs are marked as `seen` in `.automation/ai-short-video/state.sqlite3` only after Codex succeeds and validation passes, preventing candidate loss on transient failures or quota limits.
- Validated commits push directly to `origin/master` and automatically fast-forward the local `master` checkout when clean.

## Managing local schedules

Install or update the Windows scheduled tasks:

```powershell
powershell -ExecutionPolicy Bypass -File automation\ai_short_video\install_schedules.ps1
```

Remove the Windows scheduled tasks:

```powershell
powershell -ExecutionPolicy Bypass -File automation\ai_short_video\install_schedules.ps1 -Uninstall
```

For a dependency-only check without running research:

```powershell
python automation\ai_short_video\runner.py daily --dry-run
```
