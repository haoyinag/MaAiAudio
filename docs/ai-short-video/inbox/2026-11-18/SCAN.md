# SCAN 2026-11-18

> 模式：每日采集；时区：Asia/Shanghai。顺序为“六维广泛发现 → 打开原始来源分层核验 → 全库去重 → 分层写入”。爬虫候选只作线索。

## 覆盖总览

- 爬虫 `coverage`：`general=1 / platforms=3 / types=3 / pipeline=5 / growth=1 / compliance=3`；六维均低于每维 8 条目标。
- `region_counts`：国内 5、海外 2；实际候选仅 7 条且多维交叉计数，不能定义今日广度。
- 六维均追加中外搜索，并加入“制作瓶颈 / failure breakdown”“废片 / credit burn”“最低计费”“demonetization / reused content”“ROI / qualified views”等负面词。
- 补扫、打开来源并去重后记录 58 条线索，国内 37、海外 21（约 64:36）；晋升 3 个普通 atom，没有为配额降低门槛。
- 11 月 15、16 日六维均有晋升，没有连续两次缺维度的强制补扫项；仍按爬虫缺口对六维全部扩词。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 9 | 6 / 3 | 0 | 2 | 7 |
| platforms | 10 | 6 / 4 | 1 | 2 | 7 |
| types | 9 | 6 / 3 | 0 | 3 | 6 |
| pipeline | 12 | 7 / 5 | 2 | 3 | 7 |
| growth | 9 | 6 / 3 | 0 | 3 | 6 |
| compliance | 9 | 6 / 3 | 0 | 2 | 7 |
| **合计** | **58** | **37 / 21** | **3** | **15** | **40** |

计数按主维度和去重后的来源 / 主题线索记录；同一 URL 命中多维时只计一次。

## general｜通用技巧

### 搜索尝试

- 中文：`万相3 视频 提示词 参考图 工作流 官方 2026`、`Seedance 2.5 多镜头 参考素材 限制`、`AI 视频 生成失败 废片 原因 官方`。
- 海外：`official AI video prompt mismatch failure breakdown`、`Runway generation doesn't match prompt credits`、`Firefly video workflow limitations`。

### 已晋升

- 无。可靠候选均与既有结构化提示、素材职责、复杂度预算或单变量迭代条目重复。

### 待核验

1. 万相 3.0 支持文件 / 网页参考输入，但缺来源更新、网页快照固定、版权和注入防护说明。
2. Runway 说明提示漂移需要多轮调整，但没有题材 / 模型分层废片率；缺可比实测。

### 淘汰 / 合并

- Seedance 主体数、参考时长、宫格与关键帧边界已由 11-09、11-13 atom 覆盖。
- 万相多模态编号及台词 / BGM 显式约束已覆盖；Flova 发布稿缺原始能力、计费和权利文档，淘汰。

## platforms｜平台技巧

### 搜索尝试

- 中文：`红果 肖像侵权 预检 官方 2026`、`抖音 AI生成 标识 审核`、`快手 AIGC 创作者 政策`。
- 海外：`YouTube Shorts AI remix official`、`TikTok AI-generated content distribution`、`platform AI video demonetization`。

### 已晋升

- [红果肖像预检仍需投诉闭环](./platforms-hongguo-portrait-precheck-complaint-loop.md)：新增融脸 / 修改原始肖像会使部分前置拦截失效的当前边界。

### 待核验

1. 未找到稳定的红果官方公告 URL；缺工具入口、资格、检测阈值和申诉 SLA。
2. YouTube Reimagine 当前参考图与自动音频能力缺完整地区 / 账号灰度，且与 11-16 atom 重合。

### 淘汰 / 合并

- 抖音、TikTok、YouTube 的 AIGC 标签已有 atom；快手 AIGC 扶持已于 11-11 晋升。
- Top168、Sina 的未决案件评论由平台公告和监管原文替代，不作为责任事实。

## types｜类型技巧

### 搜索尝试

- 中文：`广电总局 AI 微短剧 精品创作 2026`、`AI 漫剧 失败 同质化`、`数字人口播 质量边界`。
- 海外：`vertical micro-series creator-led official 2026`、`YouTube audio-first Shorts`、`AI animation production bottleneck`。

### 已晋升

- 无。9 条线索或已重复，或只有项目 / 题材名单而无可复用方法。

### 待核验

1. 广电总局第三批拟扶持项目缺评审理由、AI 使用比例和制作方法。
2. 国内治理指出 AI 微短剧质量与同质化问题，但未公开类型化失败样本、废片率或验收指标。
3. 海外无脸 / 动画工具营销稿缺平台表现、完整成本和权利链证据。

### 淘汰 / 合并

- TikTok creator-led 微系列、品牌连载和发布 / 解锁路径均已有 atom；YouTube audio-first 转 Shorts 已于 11-16 晋升。
- 不从扶持名单或平台自报播放量反推类型 ROI。

## pipeline｜制作管线

### 搜索尝试

- 中文：`Seedance 计费 失败 最低 token`、`万相 生成失败 不收费`、`AI 短剧 积分 成本 瓶颈`。
- 海外：`Runway credits refund failed generation`、`AI video credit burn unusable output`、`generation stuck cancel refund`。

### 已晋升

- [Runway 成片不满意仍消耗积分](./pipeline-runway-completed-rejected-credit-cost.md)：将错误、完成但拒收、完成且通过拆成三态成本。
- [Seedance 含输入视频按最低用量算账](./pipeline-seedance-input-video-minimum-billing.md)：含输入视频存在最低 token 地板，并按实际 `completion_tokens` 对账。

### 待核验

1. Runway 取消卡住任务不返积分，但缺卡住状态判定、恢复和账单申诉 SLA。
2. 万相失败不消耗免费额度已有官方证据；缺“成功但不可用”的退款边界，不能与 Runway 类比。
3. Seedance Draft 两步计费已处理；仍需项目账单比较 Draft 与直出的总 ROI。

### 淘汰 / 合并

- Silicon Review 视频延长二手概览被官方文档替代；搜狐 AI 广告工作流缺参数、失败率和成本对账。
- Seedance 复杂度预算、样片转正式和剧集积分看板已有 atom。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 短视频 收益 分成 ROI 失败 官方 2026`、`快手 AIGC 收益 扶持资格`、`抖音 短剧 变现 拒审`。
- 海外：`YouTube Shorts demonetization reused content`、`TikTok Creator Rewards sponsored content`、`AI video ROI monetization pitfall`。

### 已晋升

- 无。当前一手规则没有形成相对既有条目的独立增量。

### 待核验

1. TikTok Creator Rewards 要求一分钟以上、原创、高质量，并排除 Duet、Stitch 和赞助内容；缺 2026 完整地区、账户资格与 AI 原创细则。
2. 快手 AIGC 燎原计划覆盖零粉至收益，但缺申请入口、结算公式、期限和退出条件。
3. AI SaaS 结果收费讨论不能证明创作者账号 ROI。

### 淘汰 / 合并

- YouTube 2027 门槛与定向广告已于 11-16 处理；非原创观看与版权主张边界也已有条目。
- 第三方 RPM、收益截图、奖金池和平台总 GMV 不用于推导账号回报。

## compliance｜合规与风控

### 搜索尝试

- 中文：`AI 微短剧 肖像 声音 盗脸 偷声 监管 2026`、`微短剧 逐集 AI 标识`、`红果 肖像侵权 投诉`。
- 海外：`TikTok prohibited AI likeness`、`YouTube AI likeness privacy`、`AI video disclosure demonetization`。

### 已晋升

- 无。平台公告的操作增量归入 `platforms`；监管结论均已覆盖。

### 待核验

1. 赵丽颖等相关案件缺裁判文书或公开一手诉讼材料，不得把律师评论写成已决责任。
2. 红果三类自报统计口径不同且缺独立审计，不能计算侵权率或识别准确率。

### 淘汰 / 合并

- 逐集 AI 标识已于 10-23 晋升；盗脸偷声、换名重播与榜单同质化治理已于 11-09 晋升。
- TikTok 仿冒限制和 YouTube 肖像申诉已有条目。

## 爬虫候选逐项处置

1. Top168 红果评论：未决案件二手评论；淘汰为事实来源。
2. 澎湃红果治理：晋升平台 atom，保留 `单一来源` 与平台自报边界。
3. 新浪明星撞脸：缺裁判文书；待核验。
4. Flova 发布稿：缺一手能力 / 计费 / 权利文档；淘汰。
5. 腾讯 SaaS 商业模式：与创作者变现缺直接证据链；淘汰。
6. Silicon Review 视频延长：二手概览，被官方文档替代。
7. 搜狐 AI 广告制作：服务营销稿，缺参数、失败率和成本；淘汰。

## 地区与质量说明

- 发现池 37:21（约 64:36），接近 65:35；不以弱来源凑比例。
- 国内优先火山引擎、阿里云、广电总局及平台公告；海外优先 Runway、YouTube、TikTok 官方帮助中心。
- `general`、`types`、`growth`、`compliance` 今日无晋升；若下次仍无晋升，应优先扩展实测、申诉案例、账单样本和裁判来源。
