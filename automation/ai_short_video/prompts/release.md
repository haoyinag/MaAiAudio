Read `.automation/ai-short-video/research_policy.md` completely and follow its three-day release mode.

Build a formal release candidate only from unpublished inbox material already present in this worktree. Do not use unmerged remote PR branches or crawler staging data. Verify volatile claims again, consolidate duplicates, retain provenance, and leave uncertain claims in inbox.

Create `docs/ai-short-video/vYYYY.MM.DD/` with `CHANGELOG.md`, a version README, and six dimension indexes/highlights (explicitly structuring each dimension into `当前最优解法 (Do)` and `已知困境与避坑边界 (Don't / Bottlenecks)`). Roll forward and update `docs/ai-short-video/PLAYBOOK.md` so it always integrates the latest verified global best practices across production techniques, end-to-end workflows, pitfalls/cost boundaries, and monetization (preserving any `[实测]` user feedback section intact). Update `CURRENT.md`, root `README.md`, and `WIKI.md` so `PLAYBOOK.md`, daily latest-readable, and most-recent-formal-version semantics remain distinct and consistent.

Do not edit outside `docs/ai-short-video`, and do not run Git or GitHub commands. If there is no eligible unpublished material, make no changes.
