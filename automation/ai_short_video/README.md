# AI short-video automation

This repository uses a **Local + Cloud Dual-Insurance (主备双保险)** schedule that commits validated `docs/ai-short-video/` updates directly to `master` (zero PR merge conflicts) and keeps your local working tree in sync:

1. **Local Windows Task Scheduler (Primary, uses ChatGPT subscription)**:
   - Runs at fixed morning times **AND automatically 2 minutes after every Windows logon (`AtLogOn` + `StartWhenAvailable` + battery-enabled)**.
   - Every run first syncs `origin/master` to local `master`, then checks `is_due()` on `master`: if today's output already exists on `master`, it exits in <1 second; if not yet done today, it runs immediately upon boot/login and pushes directly to `master`.
2. **Cloud GitHub Actions (`.github/workflows/ai-video-research.yml`, Off-peak Catch-up)**:
   - Runs at staggered afternoon times (12:17 daily / 14:43 release / Monday 15:47 audit, Asia/Shanghai).
   - If your PC already ran in the morning, the cloud job sees today's files on `master` and skips in 5 seconds (`should_run=false`).
   - If your PC is powered off all day, the cloud job runs automatically using repository secret `OPENAI_API_KEY` and pushes directly to `master`.

## Schedule (Asia/Shanghai)

- Daily discovery: Local **08:30 + On Boot/Logon (`PT2M` delay)**; Cloud catch-up **12:17**.
- Release eligibility: Local **Every 3 days at 10:00 + On Boot/Logon**; Cloud catch-up **14:43**.
- Weekly audit: Local **Monday 11:00**; Cloud catch-up **Monday 15:47**.
- Manual cloud run: Actions → AI short-video research → Run workflow (`daily`, `release`, or `audit`).

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
