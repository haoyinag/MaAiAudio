# 当前版本

## 当下全局最佳实践手册（实操置顶）

- **唯一当前最佳实践主文档**：[PLAYBOOK.md](./PLAYBOOK.md)
  - 持续整合全库已核验的**端到端 7 步制作 SOP、主流模型分镜路由表、四大赛道作战卡、8 大行业困境与避坑边界、变现分账模型与上线前 10 项门禁清单**。日常动手做视频请直接查阅该手册。

---

## 最新可读（每日增量）

默认阅读路径：**PLAYBOOK（全局最佳实践） → CURRENT → 日 DIGEST**。原子稿仅作溯源，不必逐篇打开。

- 最新日摘要：[inbox/2026-11-16/DIGEST.md](./inbox/2026-11-16/DIGEST.md)
- 最近周审计：[audits/2026-11-16.md](./audits/2026-11-16.md)

### 一句话结论

生成默认值要显式控制（万相 3.0 不需要台词或 BGM 时不能只留空，须写显式空约束）、低成本预览与正式产出要分阶段（Seedance 2.5 Draft 样片任务 ID 有效期为 14 天）、平台入口与数据责任拆开看（YouTube Reimagine 回链不等于授权，平台内置 AI 功能不应输入机密/未脱敏资料）；同时 YouTube 2027 YPP 官方页面明确区分新创作者入驻、既有频道活跃与 Shorts 月度池收益（过去 90 天 1,000 万合格观看）四套门槛。

### 当日原子稿（溯源）

#### general

- [万相 3.0 对台词与背景音乐使用显式空约束](./inbox/2026-11-16/通用技巧-万相3对台词与背景音乐使用显式空约束.md)

#### platforms

- [YouTube Reimagine 用自动回链保留二创来源](./inbox/2026-11-16/平台技巧-YouTube-Reimagine用自动回链保留二创来源.md)

#### types

- [YouTube 把音频优先静态视频按转录区间转为 Shorts](./inbox/2026-11-16/类型技巧-YouTube把音频优先静态视频按转录区间转为Shorts.md)

#### pipeline

- [Seedance 样片确认后在有效期内转正式视频](./inbox/2026-11-16/制作管线-Seedance样片确认后在有效期内转正式视频.md)

#### growth

- [YouTube 2027 分开计算入驻、活跃与 Shorts 月度收益门槛](./inbox/2026-11-16/增长变现-YouTube-2027分开计算入驻活跃与Shorts月度收益门槛.md)

#### compliance

- [YouTube 内置 AI 功能先做数据分级与脱敏](./inbox/2026-11-16/合规与风控-YouTube内置AI功能先做数据分级与脱敏.md)

扫描账本：[inbox/2026-11-16/SCAN.md](./inbox/2026-11-16/SCAN.md) · 日目录：[inbox/2026-11-16/README.md](./inbox/2026-11-16/README.md) · inbox 指针：[inbox/README.md](./inbox/README.md)

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
| 每日 inbox | `docs/ai-short-video/inbox/` | 2026-09-17 起的扫描草稿；最新为 2026-11-16 |
| 日摘要 | `docs/ai-short-video/inbox/YYYY-MM-DD/DIGEST.md` | 当日总览；原子稿仅溯源 |
| 最近正式快照 | `docs/ai-short-video/v2026.11.14/` | 最新三日发版产物（基线大版为 `v2026.09.13/`） |
| 历史扫描草稿 | `docs/ai-short-video/v0/inbox/` | 2026-09-10～09-13 积累；不删除 |

六个维度目录名固定为：`general`、`platforms`、`types`、`pipeline`、`growth`、`compliance`。引用条目时使用仓库相对路径，不在正文写本机绝对路径。