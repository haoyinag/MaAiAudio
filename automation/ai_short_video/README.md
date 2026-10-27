# AI short-video automation

The primary scheduler is `.github/workflows/ai-video-research.yml`. It runs on GitHub-hosted infrastructure, so the local Windows machine does not need to be powered on.

## Schedule (Asia/Shanghai)

- Daily discovery: 08:37, with a 12:17 idempotent catch-up check.
- Release eligibility: 10:13, with a 14:43 catch-up check. A release runs only when the latest formal version is at least three days old.
- Weekly audit: Monday 11:17, with a 15:47 idempotent catch-up check.
- Manual recovery: Actions → AI short-video research → Run workflow, then select `daily`, `release`, or `audit`. Use `force` only when intentionally rerunning an already completed date.

## Required repository setup

1. Add an Actions secret named `OPENAI_API_KEY` in repository settings. Never commit or paste the key into workflow files or logs.
2. Allow GitHub Actions to create pull requests and grant workflow write permissions where repository or organization policy requires it.
3. Keep automatic merging disabled; every generated PR remains review-only.

The workflow separates the Codex generation job from publication. The generation job receives the API secret but has read-only repository permission. The publication job receives only the validated patch and has no OpenAI credential.

## Reliability behavior

- GitHub Actions concurrency prevents the same schedule from overlapping.
- The second daily/release/audit schedule is a catch-up check; it skips when a matching PR or merged run already exists.
- Failures create or update the `AI short-video automation failure` issue. A later successful run closes it.
- Each run reconstructs its state from the repository and pull requests instead of depending on one machine's `.automation` directory.
- Local fallback runs reclaim dead-PID lock files, time out long child processes, remove clean stale worktrees, and use a retry branch when the date's original PR is already closed.

## Local fallback

The Windows scheduled tasks are temporary fallback only. Once a cloud run has generated a valid review PR, remove them with:

```powershell
.\automation\ai_short_video\install_schedules.ps1 -Uninstall
```

For a dependency-only check without running research:

```powershell
python automation\ai_short_video\runner.py daily --dry-run
```
