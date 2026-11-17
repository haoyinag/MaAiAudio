AI短视频经验积累

知识库入口：[docs/ai-short-video](./docs/ai-short-video/README.md)
- **当下全局最佳实践手册（实操首读）**：[PLAYBOOK.md](./docs/ai-short-video/PLAYBOOK.md)
- **当前版本与最新日增量指针**：[CURRENT.md](./docs/ai-short-video/CURRENT.md)
- **最新正式版摘要**：[v2026.11.14/CHANGELOG.md](./docs/ai-short-video/v2026.11.14/CHANGELOG.md)（基线大版见 [v2026.09.13/CHANGELOG.md](./docs/ai-short-video/v2026.09.13/CHANGELOG.md)）
- **最新日摘要**：[inbox/2026-11-16/DIGEST.md](./docs/ai-short-video/inbox/2026-11-16/DIGEST.md)

## 自动采集

AI 短视频知识库采用“公开 RSS/Python 发现 → Codex 核验整理 → 隔离 worktree 校验 → 自动合入 `master` 并同步本机”的方式维护（无需手动处理 PR 冲突）。

- 每日 08:30：采集最近增量（含制作技巧、工作流、困境避坑与变现），写入 inbox 并直推 `master`。
- 每三天 10:00：整理已合入 `master` 的未发版 inbox，生成正式版本 `vYYYY.MM.DD` 并滚动更新 `PLAYBOOK.md`。
- 每周一 11:00：审计来源质量、时效和导航一致性。
- 机器错过计划时间后，Windows 任务设置为尽快补跑；每日任务从上次成功时间继续补采。

配置和任务入口见 `automation/ai_short_video/`。手动检查环境可运行：

```powershell
python automation\ai_short_video\runner.py daily --dry-run
```

安装或移除本机计划任务：

```powershell
powershell -ExecutionPolicy Bypass -File automation\ai_short_video\install_schedules.ps1
powershell -ExecutionPolicy Bypass -File automation\ai_short_video\install_schedules.ps1 -Uninstall
```
