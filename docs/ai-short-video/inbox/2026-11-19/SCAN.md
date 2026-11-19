# SCAN 2026-11-19

> 模式：每日采集；时区：Asia/Shanghai。先完成六维中外广泛发现，再打开原始来源分层核验、全库去重并写入。爬虫候选仅作线索。

## 覆盖总览

- 爬虫 `coverage`：`general=0 / platforms=0 / types=0 / pipeline=1 / growth=1 / compliance=0`；`region_counts`：国内 1、海外 0。唯一候选同时计入 pipeline / growth，不能代表两个独立事实。
- `general`、`types`、`growth`、`compliance` 在 11-18 无晋升，今天优先扩大官方文档、监管原文、失败 / 成本 / 变现与处罚词。
- 定向检索后记录 52 条去重线索：国内 32、海外 20（约 62:38）。来源质量优先，因此未为凑 65:35 降级来源。
- 晋升 6 个普通 atom（六维各 1）；待核验线索 8；淘汰 / 合并 38。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 9 | 6 / 3 | 1 | 1 | 7 |
| platforms | 9 | 5 / 4 | 1 | 1 | 7 |
| types | 8 | 6 / 2 | 1 | 2 | 5 |
| pipeline | 10 | 6 / 4 | 1 | 1 | 8 |
| growth | 9 | 5 / 4 | 1 | 2 | 6 |
| compliance | 7 | 4 / 3 | 1 | 1 | 5 |
| **合计** | **52** | **32 / 20** | **6** | **8** | **38** |

## general｜通用技巧

### 搜索尝试

- 中文：`Seedance 2.5 提示词 主体数量 稳定性 抽卡 官方`、`万相3 多镜头 提示词 失败 边界 官方`、`AI 视频 参考素材 冲突 废片 官方`。
- 海外：`official AI video prompting conflicting reference failure`、`Runway source image artifacts motion prompt`、`AWS video prompt seed one variable`。

### 处理

- **已晋升：** [先把参考素材压到稳定区再扩容](./general-seedance-reference-load-boundaries.md)。
- **待核验：** Runway / AWS 的正向、具体、单变量提示建议缺同一测试集的跨模型废片率；需项目级 A/B 账本。
- **淘汰 / 合并：** 最小运动描述、素材净化、固定 seed 与单变量迭代均已有 atom；营销稿宣称的成功率无原始测试集。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 AI 内容 低质 同质化 治理 官方`、`快手 AIGC 创作者 规则 原创 收益`、`B站 AI 标识 上传审核 权利`。
- 海外：`Facebook Reels original content demonetized official 2026`、`TikTok AI label distribution official`、`YouTube AI mass produced monetization`。

### 处理

- **已晋升：** [Facebook 原创性按持续行为处罚而非只看单条](./platforms-facebook-originality-enforcement.md)。
- **待核验：** TikTok 正在测试针对 AI 垃圾账号的检测，但未公开判定阈值、覆盖地区和申诉 SLA。
- **淘汰 / 合并：** TikTok 标签不等于限流、抖音 / B站 AI 标识已有 atom；“AI 标签自动压流”被 TikTok 官方说明反驳。

## types｜类型技巧

### 搜索尝试

- 中文：`广电总局 AI 微短剧 创作 精品 同质化 失败`、`微短剧 定义 情节完整 人物角色 官方`、`AI 漫剧 降量增质 瓶颈`。
- 海外：`AI vertical series production bottleneck storyboard official`、`faceless series originality failure`、`audio first shorts format boundary`。

### 处理

- **已晋升：** [微短剧按项目级主线与完整情节验收](./types-microdrama-project-acceptance-boundary.md)。
- **待核验：** 广电公开稿指出 AI 漫剧同质化，但没有类型化失败样本、废片率或统一验收量表；海外无脸内容仍缺权利成本与平台表现闭环。
- **淘汰 / 合并：** creator-led 微系列、音频转 Shorts、季级连续性已有 atom；扶持项目名单不用于反推类型 ROI。

## pipeline｜制作管线

### 搜索尝试

- 中文：`Seedance 资源包 到期 自动按量 计费 官方`、`万相 视频 失败 不收费`、`AI 视频 credit burn 成本 返工 瓶颈`。
- 海外：`Runway failed generation credit refund official`、`Adobe Firefly video credits per second`、`AI video unusable output credit burn`。

### 处理

- **已晋升：** [Seedance 资源包同时设到期与超额门禁](./pipeline-seedance-resource-pack-expiry-overage.md)。
- **待核验：** 不同模型真实“可交付秒成本”缺同一素材、同一质量门槛和人工返工数据。
- **淘汰 / 合并：** Runway 失败退款 / 完成但不满意不退款、Seedance 单次最低 token 地板已由 11-18 atom 覆盖；阿里云失败不收费只作对照，不新建同义条目。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 短剧 收益 ROI 失败 投流 回收 官方`、`快手 漫剧 营销消耗 创作者 收益`、`抖音 AI 短视频 变现 原创`。
- 海外：`Facebook qualified views earnings rate official 2026`、`YouTube AI generic templates demonetization`、`TikTok Creator Rewards original sponsored one minute`。

### 处理

- **已晋升：** [Facebook 用合格观看而非总播放核算收益](./growth-facebook-qualified-view-ledger.md)。
- **待核验：** TikTok Creator Rewards 已确认一分钟以上、原创、高质量并排除 Duet / Stitch / 赞助内容，但仍缺 2026 完整地区、账户资格和 AI 原创细则；通用 AI 视频 CPM / ROI 缺全成本与归因证据。
- **淘汰 / 合并：** YouTube 批量模板不变现已在 11-18 来源笔记；公司总收入、平台营销消耗和奖金池不能外推单账号 ROI。

## compliance｜合规与风控

### 搜索尝试

- 中文：`微短剧 内容提供者 推广者 常态巡查 退出机制`、`AI 广告 肖像 声音 监管 指引`、`AI 内容 标识 元数据 不得删除`。
- 海外：`TikTok AI likeness disclosure child safety`、`YouTube synthetic media privacy complaint`、`AI video demonetization disclosure policy`。

### 处理

- **已晋升：** [微短剧内容方与推广方都进入常态巡查](./compliance-microdrama-provider-promoter-audit.md)。
- **待核验：** 上海市场监管 AI 广告指引属于单一地方口径，需明确地域适用范围并与国家法律逐项对照后再晋升。
- **淘汰 / 合并：** 显式 / 元数据标识、逐集标识、肖像声音授权和 YouTube 肖像申诉已有 atom；未取得裁判文书的案例评论不写成已决责任。

## 爬虫候选处置与访问失败

1. 搜狐“太原餐饮 AI 营销视频机构推荐”：营销软文，缺原始样本、成本账单和可审计 ROI，淘汰。
2. Google News RSS：robots 拒绝，记录失败且未绕过。
3. 可灵部分官方价格页：robots 拒绝；未用聚合站价格替代，保留缺口。

## 地区与质量说明

发现池约 62:38，略低于 65:35 国内目标，但所有晋升来源均为监管 / 平台 / 厂商一手材料；没有为比例加入弱来源。六维均有晋升，不存在连续两天缺维度。完整后台来源补充见 [RESEARCH-NOTES.md](./RESEARCH-NOTES.md)。

