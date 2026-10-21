AI短视频经验积累

知识库入口：[docs/ai-short-video](./docs/ai-short-video/README.md)（当前版本见 [CURRENT.md](./docs/ai-short-video/CURRENT.md)）。
## 自动采集

AI 短视频知识库采用“公开 RSS/Python 发现 → Codex 核验整理 → 隔离 worktree → 自动 PR”的方式维护，自动合并保持关闭。

- 每日 08:30：采集最近增量，写入 inbox 候选 PR。
- 每三天 10:00：只整理已经合入 `master` 的 inbox，创建正式版本候选 PR。
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
