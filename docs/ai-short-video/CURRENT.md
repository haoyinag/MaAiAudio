# 当前版本

## 最新可读

默认阅读路径：**总览 → 日摘要 / 版摘要**。原子稿仅作溯源，不必逐篇打开。

- 最新日摘要：[v0/inbox/2026-09-13/DIGEST.md](./v0/inbox/2026-09-13/DIGEST.md)
- 当前版本说明：[v0/README.md](./v0/README.md)

正式版摘要在三日发版时写入 `vYYYY.MM.DD/CHANGELOG.md`。v0 为脚手架期，占位见 [v0/CHANGELOG.md](./v0/CHANGELOG.md)（尚无发版增量）。

当前生效版本：**v0（脚手架）**

v0 只提供目录骨架与写作约定，**尚无实质经验条目**。后续发版时，将本文件中的版本号与路径改到最新的 `vN/`。

## 路径约定

知识库根目录：`docs/ai-short-video/`

| 用途 | 相对路径 | 说明 |
| --- | --- | --- |
| 知识库总述 | `docs/ai-short-video/README.md` | 用途、维度、节奏、来源约束 |
| 当前版本指针 | `docs/ai-short-video/CURRENT.md` | 本文件；永远指向正在使用的 `vN/` |
| Wiki 入口说明 | `docs/ai-short-video/WIKI.md` | Wiki 首页应链到本知识库 |
| 当前版本根 | `docs/ai-short-video/v0/` | 当前快照；发新版时新增 `v1/`、`v2/`… |
| 版本说明 | `docs/ai-short-video/v0/README.md` | 该版范围与状态 |
| 扫描草稿 | `docs/ai-short-video/v0/inbox/` | 每日巡扫的未定稿内容 |
| 日摘要（默认入口） | `docs/ai-short-video/v0/inbox/YYYY-MM-DD/DIGEST.md` | 当日总览；原子稿仅溯源 |
| 版摘要 | `docs/ai-short-video/v0/CHANGELOG.md` | v0 占位；三日发版后改为 `vYYYY.MM.DD/CHANGELOG.md` |
| 维度条目 | `docs/ai-short-video/v0/dimensions/<维度>/` | 正式条目按维度归档 |

六个维度目录名固定为：

- `general` — 通用技巧
- `platforms` — 平台技巧
- `types` — 类型技巧
- `pipeline` — 制作管线
- `growth` — 增长变现
- `compliance` — 合规与风控

引用条目时使用仓库相对路径，例如：

`docs/ai-short-video/v0/dimensions/general/README.md`

不要在正文中写本机绝对路径。
