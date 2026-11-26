# 当前版本

> **实操主入口：** [PLAYBOOK.md](./PLAYBOOK.md)

## 当下全局最佳实践手册（实操置顶）

- **唯一当前最佳实践主文档**：[PLAYBOOK.md](./PLAYBOOK.md)
  - 持续整合全库已核验的**端到端 7 步制作 SOP、主流模型分镜路由表、四大赛道作战卡、8 大行业困境与避坑边界、变现分账模型与上线前 10 项门禁清单**。日常动手做视频请直接查阅该手册。

---

## 最新可读（每日增量）

默认阅读路径：**PLAYBOOK（全局最佳实践） → CURRENT → 日 DIGEST**。原子稿仅作溯源，不必逐篇打开。

- 最新日摘要：[inbox/2026-11-26/DIGEST.md](./inbox/2026-11-26/DIGEST.md)
- 最近周审计：[audits/2026-11-23.md](./audits/2026-11-23.md)

### 一句话结论

重复特效验收留出镜头，连载按剧情功能审核造型，转码与音画返工单独验收，投流试验和实际收入分别对账，合规按内容及发行版本核验。

### 当日原子稿（溯源）

- `general`　[重复特效先对照提示词，再验证万相微调](./inbox/2026-11-26/general-wan-finetune-holdout.md)
- `platforms`　[YouTube Studio 按通知状态分流发布限制](./inbox/2026-11-26/platforms-youtube-studio-notice-triage.md) · [快手小说剧确认转码再提审](./inbox/2026-11-26/platforms-kuaishou-noveldrama-transcode-preflight.md)
- `types`　[志怪改编先验人物造型能否承载剧情](./inbox/2026-11-26/types-chouhu-character-adaptation.md)
- `pipeline`　[短剧Lab分镜音色漂移时保留画面重配](./inbox/2026-11-26/pipeline-duanjulab-voice-repair.md) · [Google Flow 在 12 月停用节点前试跑替代模型](./inbox/2026-11-26/pipeline-flow-december-migration.md)
- `growth`　[TikTok 投放先隔离受众做素材拆分测试](./inbox/2026-11-26/growth-tiktok-paid-creative-split.md) · [TikTok 短剧分开看进剧、支付动作和混合 ROAS](./inbox/2026-11-26/growth-tiktok-microseries-reporting.md)
- `compliance`　[AI 健康内容核验身份、证据和康复案例](./inbox/2026-11-26/compliance-cn-health-video-claims-and-credentials.md) · [欧盟深度伪造披露按实际发行版本判断](./inbox/2026-11-26/compliance-eu-deepfake-fiction-vs-shopping-disclosure.md)

扫描账本：[SCAN.md](./inbox/2026-11-26/SCAN.md) · 日目录：[README.md](./inbox/2026-11-26/README.md) · [inbox 指针](./inbox/README.md)

## 最近正式发版（稳定快照，不等于每日最新）

- 最新三日正式版本候选：**[v2026.11.26](./v2026.11.26/README.md)**（[变更记录](./v2026.11.26/CHANGELOG.md) · [六维精选](./v2026.11.26/dimensions/README.md)）
- 最近已发布正式版：**[v2026.11.20](./v2026.11.20/README.md)**（版摘要见 [v2026.11.20/CHANGELOG.md](./v2026.11.20/CHANGELOG.md)，六维精选见 [v2026.11.20/dimensions/](./v2026.11.20/dimensions/README.md)）
- 较早正式版：**[v2026.11.14](./v2026.11.14/README.md)**（复核记录见 [v2026.11.14/VERIFICATION.md](./v2026.11.14/VERIFICATION.md)）
- 首个基线正式版：**[v2026.09.13](./v2026.09.13/README.md)**（版摘要见 [v2026.09.13/CHANGELOG.md](./v2026.09.13/CHANGELOG.md)）

## 路径约定

知识库根目录：`docs/ai-short-video/`

| 用途 | 相对路径 | 说明 |
| --- | --- | --- |
| 全局最佳实践手册 | `docs/ai-short-video/PLAYBOOK.md` | 面向实操的唯一当下最佳实践主文档（随版本滚动更新） |
| 知识库总述 | `docs/ai-short-video/README.md` | 用途、维度、节奏、来源约束 |
| 当前阅读层 | `docs/ai-short-video/CURRENT.md` | 本文件；PLAYBOOK 置顶 + 日 DIGEST + 结论 + 当日原子链接 |
| Wiki 入口说明 | `docs/ai-short-video/WIKI.md` | Wiki 首页应链到本知识库 |
| 每日 inbox | `docs/ai-short-video/inbox/` | 2026-09-17 起的扫描草稿；最新为 2026-11-26 |
| 日摘要 | `docs/ai-short-video/inbox/YYYY-MM-DD/DIGEST.md` | 当日总览；原子稿仅溯源 |
| 最新正式版本候选 | `docs/ai-short-video/v2026.11.26/` | 本轮复核后的固定快照，待 runner 发布 |
| 最近正式快照 | `docs/ai-short-video/v2026.11.20/` | 最近完成复核的稳定发版；不替代每日 DIGEST（基线大版为 `v2026.09.13/`） |
| 历史扫描草稿 | `docs/ai-short-video/v0/inbox/` | 2026-09-10～09-13 积累；不删除 |

六个维度目录名固定为：`general`、`platforms`、`types`、`pipeline`、`growth`、`compliance`。引用条目时使用仓库相对路径，不在正文写本机绝对路径。
