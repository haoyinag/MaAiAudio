# SCAN 2026-11-11

> 模式：每日采集；时区：Asia/Shanghai。严格按“六维广泛发现 → 原始来源核验 → 全库去重 → 分层写入”执行。爬虫候选只作发现线索，不作事实。

## 覆盖总览

- 爬虫起点：general=3 / platforms=1 / types=0 / pipeline=4 / growth=1 / compliance=0；地区为国内 0、海外 6。
- 六维均低于每维至少 8 条的发现目标，types、compliance 完全缺席，国内来源完全缺席；因此六维均追加中文与海外检索，并优先补扫类型、合规、平台、增长和国内来源。
- 人工补扫后：去重后纳入账本约 70 条，国内约 46、海外约 24（约 66:34）；六维均达到至少 8 条发现线索。
- 最终晋升 6 个普通 atom（国内 4、海外 2，约 67:33）：六维各 1 个。
- 2026-11-10 六维均有晋升，本日不存在连续两天无晋升而必须优先扩词的维度；但仍按爬虫缺口优先扩大 types 与 compliance 的监管、产品文档和平台帮助来源。

| 维度 | 去重后候选数 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: |
| general | 11 | 1 | 2 | 8 |
| platforms | 11 | 1 | 3 | 7 |
| types | 12 | 1 | 3 | 8 |
| pipeline | 13 | 1 | 3 | 9 |
| growth | 11 | 1 | 3 | 7 |
| compliance | 12 | 1 | 3 | 8 |

## general｜通用技巧

### 搜索尝试

- 中文：AI 视频 创作 提示词 一致性 官方 2026；火山引擎 即梦 多主体 动作 提示词；可灵 视频模型 一致性 多镜头 官方。
- 海外：official AI video prompting guide consistency 2026；Sora video prompting guide；Adobe Firefly effective video prompts official。

### 已晋升

- [Kickart 把视频提示拆成七类约束](./通用技巧-Kickart把视频提示拆成七类约束.md)。

### 待核验

- 即梦 3.0 Pro 官方文档区分“单主体连续动作”和“多主体各自动作”，但与现有单镜头动作拆分条目重叠；缺跨模型对比与独立失败样本。
- Adobe Firefly 的“镜头类型 + 角色 + 动作 + 地点 + 美学”提示结构可访问，但与万相、Runway 和本日 Kickart 结构化提示高度相似；缺足以独立成条的增量。

### 淘汰 / 合并

- Sora 2 Prompting Guide 已在 2026-10-23、10-27 记录为归档/可能过时，重复合并。
- Runway Gen-4 从最小运动逐步加细已在 2026-11-03 晋升，重复。
- 可灵 3.0 参考资产、镜头和声音约束已在 2026-11-10 晋升，重复。
- 爬虫 Hedra Model Factory 为二手报道且偏物理 AI 训练/推理基础设施，不构成短视频创作技巧，淘汰。

## platforms｜平台技巧

### 搜索尝试

- 中文：抖音 开放平台 视频发布 官方 2026；快手 AIGC 创作者 平台 规则 官方；国内 短视频 AI 发布 标签 审核。
- 海外：TikTok publish micro-series official 2026；YouTube Shorts discovery official 2026；Facebook Reels creator official AI 2026。

### 已晋升

- [TikTok 微短剧先选发布与解锁路径](./平台技巧-TikTok微短剧先选发布与解锁路径.md)。

### 待核验

- YouTube Shorts 当前帮助页确认观看选择、平均观看时长、平均观看百分比等发现信号，但未公开权重，且缺 AI 短视频独立口径。
- 抖音/Xigua MVP 页面可见跨西瓜、抖音、头条的原创横屏收益入口，但缺当前准入、结算和 AI 内容资格规则。
- TikTok Mini Centre 页面只写“部分市场”，缺完整地区清单、账户类型与迁移规则。

### 淘汰 / 合并

- 爬虫 TechJunkie“最佳 AI 视频生成器”是二手/导购型比较，价格和商用权利易变，淘汰。
- 中国短视频六类必选标签已在 2026-10-22～23 晋升，重复。
- YouTube 2026 AI 标签覆盖层、自动标签和“标签本身不降推荐”已存在 atom，重复。
- Facebook Creator Fast Track 已在 2026-10-22 扫描账本判定为非 AI 短视频专属且数字易变，不重开。

## types｜类型技巧

### 搜索尝试

- 中文：网信办 AI 交互叙事 漫短剧 官方；广电总局 AI 微短剧 漫剧 类型 2026；火山剧创 AI 短剧 AI 解说漫 官方。
- 海外：official vertical microdrama animation series 2026；TikTok micro-series creator-led official；YouTube vertical microdrama official 2026。

### 已晋升

- [交互漫短剧先限定分支边界](./类型技巧-交互漫短剧先限定分支边界.md)。

### 待核验

- 火山剧创官方文档区分 AI 短剧与 AI 解说漫的资产/声音检查点，但与既有资产表和分镜工作流重叠；需确认类型分流是否有足够独立增量。
- Kickart 对 TVC、剧情演绎、主播带货给出不同提示重点，其中口播字数是厂商经验，缺跨模型验证。
- Adobe 虚拟主播文档能确认脚本到头像视频流程，但缺短视频平台适配、效果和制作成本比较。

### 淘汰 / 合并

- TikTok 与 MADE BY US 的 creator-led 竖屏微系列已在 2026-10-27 晋升，重复。
- YouTube 把竖屏微短剧视为连续剧集格式已在 2026-11-10 晋升，重复。
- 国家广电总局 2026 年第二季度优秀网络视听节目名单只列作品和机构，不能据此推导 AI 类型方法或效果，淘汰为方法证据。
- 政府/行业材料中的播放量、题材趋势未隔离 AI 制作、平台分发和样本口径，不写类型因果。

## pipeline｜制作管线

### 搜索尝试

- 中文：AI 视频 工作流 分镜 质检 官方 2026；Seedance 视频生成 API 首尾帧 全模态参考；火山引擎 视频 参考图 时间线 官方。
- 海外：official AI video workflow storyboard editing 2026；Adobe MAX 2026 Firefly video workflow；AI video production agent plan mode official。

### 已晋升

- [Firefly 代理执行前先审计计划与跨项目约束](./制作管线-Firefly代理执行前先审计计划与跨项目约束.md)。

### 待核验

- Seedance 当前 API 文档显示严格首尾帧与全模态参考属于不同输入路由，但需继续与 2026-09-13、10-27 的 Seedance 参考/首尾帧条目逐字段去重。
- Kickart 的“先参考图、再片段、后时间线”流程与既有资产优先管线相近；商品占画面比例等厂商建议缺独立实测。
- Adobe Always-on agents 仅为 preview，缺账号开放范围、失败恢复、费用和自动质检准确率。

### 淘汰 / 合并

- 爬虫 Adobe MAX 二手报道由 2026-11-10 Adobe 官方发布稿替代，二手页面不作为事实来源。
- 爬虫 WellSaid Producer 为二手营销报道，且主要是语音工作流；缺产品文档、地区和当前可用性，淘汰。
- 爬虫 Gaxos ArtGen Muse 来自财经聚合页，缺官方能力文档、成本口径和短视频工作流证据，淘汰。
- 爬虫 Hedra Model Factory 与短视频制作距离过远；TechJunkie 工具清单无可追溯工作流；均淘汰。
- Google Flow“筛选—精修—放大”和 Firefly 项目资产/时间线已于 2026-11-10、10-22 晋升，不重复。

## growth｜增长变现

### 搜索尝试

- 中文：快手 AIGC 创作者 扶持 2026 官方；抖音 创作者 变现 计划 官方 2026；AI 短视频 商业化 收益 官方。
- 海外：TikTok creator monetization official 2026 micro series；YouTube Shorts monetization official 2026；Meta Reels creator monetization official 2026。

### 已晋升

- [快手 AIGC 扶持计划与常态收益分账](./增长变现-快手AIGC扶持计划与常态收益分账.md)。

### 待核验

- 快手 AIGC 四项政策目前只获得 IR 站转载摘要，缺完整规则、资格、流量口径和结算条款；因此 atom 不估算收益。
- TikTok Creator Rewards 旧公告强调原创、播放时长、搜索价值与互动，但缺 2026 当前地区名单、账户门槛和统一条款。
- 抖音/Xigua MVP 缺当前收益公式、结算规则和 AI 生成内容资格。

### 淘汰 / 合并

- 爬虫 CIOL 的 dubdub CEO 访谈讨论消费科技留存，不能证明 AI 短视频创作者的留存因果，淘汰。
- YouTube Shorts 广告池、合格观看与 YPP 门槛已有多篇 atom，重复。
- Facebook Creator Fast Track 是总体创作者迁移计划，不作为 AI 短视频稳定收益模型。
- Reddit 收益截图、平台整体 GMV 和厂商 ARR 均不能替代单账号成本与收入账本，淘汰。

## compliance｜合规与风控

### 搜索尝试

- 中文：网信办 无 AI 标识 虚假 视频 2026；AI 生成 视频 标识 去标识 典型案例；广电总局 AI 微短剧 专项治理 2026。
- 海外：YouTube AI generated video disclosure policy 2026 official；EU AI Act deepfake transparency 2026 official；TikTok AI generated content labeling official 2026。

### 已晋升

- [AI 标识不能替代虚假与内容安全审核](./合规与风控-AI标识不能替代虚假与内容安全审核.md)。

### 待核验

- TikTok AIGC 帮助页存在地区版本差异，缺统一的 2026 全球适用范围和不可移除标签条件。
- 欧盟透明度准则已覆盖机器标记与观众披露，但各视频平台转码后元数据保留和标签展示仍缺实施证据。
- 中国平台对“应标未标”内容的具体推荐、限流和申诉阈值未公开，不能从治理通报反推算法权重。

### 淘汰 / 合并

- 中国 AI 显式/隐式标识、短视频六类标签、AI 微短剧逐集提示和片头许可信息均已有 atom，重复。
- 2026-11-06 微短剧专项治理及公众人物仿冒已在 2026-11-09 晋升，重复。
- YouTube AI 披露覆盖层与自动标签、最高法 AI 换脸拟声责任、欧盟 AI 法案第 50 条均已有条目。
- Google News RSS 全部被 robots 拒绝；未绕过访问控制，记为不可访问发现渠道。

## 爬虫候选处置汇总

- Adobe MAX 二手稿：找到 Adobe 官方稿后替代，官方事实晋升至 pipeline。
- Hedra Model Factory：偏物理 AI 基础设施且只有二手报道，淘汰。
- WellSaid Producer：二手营销稿、短视频相关性弱且缺可用性文档，淘汰。
- TechJunkie 工具榜单：导购型二手比较，价格/商用权利易变，淘汰。
- Gaxos ArtGen Muse：财经聚合稿，缺官方能力与成本证据，淘汰。
- dubdub 留存访谈：泛消费科技观点，缺 AI 短视频创作者证据，淘汰。

## 地区与质量说明

- 发现池约 66:34（国内:海外），发布集为 67:33；未为追求精确比例采用低质量来源。
- 国内优先采用网信部门、火山引擎官方文档与快手 IR 站材料；海外采用 TikTok 和 Adobe 官方页面。
- 六个普通 atom 均明确区分来源事实、分析推断和适用边界。所有待核验项都写明缺失证据；重复、噪声、不可访问或被官方来源替代的线索保留在本账本。
