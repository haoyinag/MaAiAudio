# Wiki 入口说明

仓库已开启 Wiki（`has_wiki=true`）。Wiki 用于浏览入口，**权威内容在本 docs 树**。

## 约定

Wiki 首页（`Home`）默认应链到 **CURRENT + 最新 DIGEST**，让浏览入口直接落到摘要层：

- 当前版本 / 最新可读：`docs/ai-short-video/CURRENT.md`
- 最新日摘要：`docs/ai-short-video/v0/inbox/2026-09-12/DIGEST.md`（含 15:00 PM 补扫）
- 知识库总述：`docs/ai-short-video/README.md`

建议首页只放导航，不另写一份会漂移的正文副本。原子稿不作为 Wiki 默认入口。

## 建议首页内容（镜像草稿）

可将下面这段粘贴到 Wiki `Home`，作为镜像入口：

```markdown
# AI 短视频 / 短剧知识库

权威文档在仓库 docs，不在 Wiki 正文中维护。

- [当前版本 / 最新可读](../blob/master/docs/ai-short-video/CURRENT.md)
- [最新日摘要 · 2026-09-12（含 PM）](../blob/master/docs/ai-short-video/v0/inbox/2026-09-12/DIGEST.md)
- [知识库总述](../blob/master/docs/ai-short-video/README.md)
- [v0 脚手架](../blob/master/docs/ai-short-video/v0/README.md)

维度：通用技巧、平台技巧、类型技巧、制作管线、增长变现、合规与风控。
```

GitHub Wiki 的相对链接写法以仓库实际渲染为准；若 Wiki 尚未初始化，先保证本目录结构完整，再补 Wiki 首页。
