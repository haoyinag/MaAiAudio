# 增长变现：YouTube YPP 门槛只按公开 Shorts 的合格参与观看计算

- **主维度：** `growth`（增长变现）
- **来源 URL：** https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/
- **发布机构 / 作者：** YouTube / Rene Ritchie（Creator Liaison）
- **发布日期：** 2026-08-12
- **采集日期：** 2026-11-09（Asia/Shanghai）
- **来源等级：** 平台官方
- **核验状态：** `已核验`
- **适用平台 / 地区：** YouTube Partner Program；适用地区以 YPP 开放范围为准
- **时效：** 极高；资格口径易变，核验至 2026-11-09

## 来源明确事实

1. YPP 的 qualified Shorts views 必须来自公开 Shorts，并属于 engaged views。
2. 官方把 engaged view 定义为观众越过开头数秒继续观看，且不包含循环；创作者可在 YouTube Analytics 查看单条视频数据。
3. 私密、非公开、已删除、作为广告观看的 Shorts，以及长视频观看和 Shorts Feed 中的图片帖不计入该门槛。

## 分析推断

- 总播放量、循环量和投放观看不能直接用于估算 YPP 资格距离；增长台账必须保留平台口径字段。
- 合格观看是资格口径，不等于每次观看的收入，也不能反推单条内容 RPM。

## 可执行含义

1. 周报分开记录 `总播放 / engaged views / 广告观看 / 循环 / qualified views`。
2. 资格预测只读取 Analytics 中公开 Shorts 的 engaged views，不用外部播放截图相加。
3. 删除或转为非公开前先评估其对滚动资格窗口的影响，并保留变更日期。

## 与既有条目的关系

- **增量：** `inbox/2026-10-23/增长变现-YouTube-2027-YPP条款与活跃门槛.md` 记录门槛；本条补充合格观看的排除项与“不含循环”口径。
- **关联：** 与 `inbox/2026-11-03/增长变现-YouTube-Shorts连续发布奖金不等于稳定收入.md` 的邀请奖金分账，不混为广告分成资格。

