# 当前版本

## 当下全局最佳实践手册（实操置顶）

- **唯一当前最佳实践主文档**：[PLAYBOOK.md](./PLAYBOOK.md)
  - 持续整合全库已核验的**端到端 7 步制作 SOP、主流模型分镜路由表、四大赛道作战卡、8 大行业困境与避坑边界、变现分账模型与上线前 10 项门禁清单**。日常动手做视频请直接查阅该手册。

---

## 最新可读（每日增量）

默认阅读路径：**PLAYBOOK（全局最佳实践） → CURRENT → 日 DIGEST**。原子稿仅作溯源，不必逐篇打开。

- 最新日摘要：[inbox/2026-11-18/DIGEST.md](./inbox/2026-11-18/DIGEST.md)
- 最近周审计：[audits/2026-11-16.md](./audits/2026-11-16.md)

### 一句话结论

预检通过不等于已获授权：红果承认融脸与修改原始肖像可能使部分前置拦截失效；成功生成也不等于可交付，Runway 对完成但不可用的成片不自动退积分；Seedance 含输入视频任务还存在最低 token 计费地板。制作侧应同时建立授权 / 投诉闭环、三态废片账本和实际用量对账。

### 当日原子稿（溯源）

#### platforms

- [红果肖像预检仍需投诉闭环](./inbox/2026-11-18/platforms-hongguo-portrait-precheck-complaint-loop.md)

#### pipeline

- [Runway 成片不满意仍消耗积分](./inbox/2026-11-18/pipeline-runway-completed-rejected-credit-cost.md)
- [Seedance 含输入视频按最低用量算账](./inbox/2026-11-18/pipeline-seedance-input-video-minimum-billing.md)

`general`、`types`、`growth`、`compliance` 今日无晋升，原因见摘要与账本。扫描账本：[inbox/2026-11-18/SCAN.md](./inbox/2026-11-18/SCAN.md) · 日目录：[inbox/2026-11-18/README.md](./inbox/2026-11-18/README.md) · inbox 指针：[inbox/README.md](./inbox/README.md)

## 最近正式发版

- 最新三日发版：**[v2026.11.14](./v2026.11.14/README.md)**（版摘要见 [v2026.11.14/CHANGELOG.md](./v2026.11.14/CHANGELOG.md)，复核记录见 [v2026.11.14/VERIFICATION.md](./v2026.11.14/VERIFICATION.md)）
- 首个基线正式版：**[v2026.09.13](./v2026.09.13/README.md)**（版摘要见 [v2026.09.13/CHANGELOG.md](./v2026.09.13/CHANGELOG.md)）

## 路径约定

知识库根目录：`docs/ai-short-video/`

| 用途 | 相对路径 | 说明 |
| --- | --- | --- |
| 全局最佳实践手册 | `docs/ai-short-video/PLAYBOOK.md` | 面向实操的唯一当下最佳实践主文档（随版本滚动更新） |
| 知识库总述 | `docs/ai-short-video/README.md` | 用途、维度、节奏、来源约束 |
| 当前阅读层 | `docs/ai-short-video/CURRENT.md` | 本文件；PLAYBOOK 置顶 + 日 DIGEST + 结论 + 当日原子链接 |
| Wiki 入口说明 | `docs/ai-short-video/WIKI.md` | Wiki 首页应链到本知识库 |
| 每日 inbox | `docs/ai-short-video/inbox/` | 2026-09-17 起的扫描草稿；最新为 2026-11-18 |
| 日摘要 | `docs/ai-short-video/inbox/YYYY-MM-DD/DIGEST.md` | 当日总览；原子稿仅溯源 |
| 最近正式快照 | `docs/ai-short-video/v2026.11.14/` | 最新三日发版产物（基线大版为 `v2026.09.13/`） |
| 历史扫描草稿 | `docs/ai-short-video/v0/inbox/` | 2026-09-10～09-13 积累；不删除 |

六个维度目录名固定为：`general`、`platforms`、`types`、`pipeline`、`growth`、`compliance`。引用条目时使用仓库相对路径，不在正文写本机绝对路径。
