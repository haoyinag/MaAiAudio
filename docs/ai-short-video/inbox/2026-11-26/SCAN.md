# SCAN 2026-11-26

亚洲/上海每日采集。爬虫先读 `coverage` 和 `region_counts`，两条 URL 分布为国内 1、海外 1，标签覆盖 general 0、platforms 1、types 1、pipeline 2、growth 0、compliance 0。36 条 Google News RSS 搜索报告 robots 拒绝，改用公开网页搜索。两条 crawler 原页均未取得正文，已在相应维度保留处置记录。

六维先补搜技巧、端到端制作、废片和返工、积分成本、拒审与取消变现、投放亏损，再查原始页面并按主题、来源和适用范围比对现有原子稿、历日日摘要、正式版及 PLAYBOOK。以下统计是进入分层裁决的候选，搜索结果页上的重复和不相关条目未计入。共 53 条去重候选，国内 32 条、海外 21 条，国内约 60%。逐维计数共 55 次，含《丑狐》爬虫链接的跨维记录；晋升 10、待核验 18、淘汰 27 次。

近两日 11-24 六维均有晋升，11-25 增长只有待核验条目。今日扩大搜索增长亏损样本与平台报表，六维均有晋升。

## general

- 中文搜索　AI 视频 生成 运镜 崩坏 废片 可灵 万相 提示词 官方 图生视频 镜头；site:alibabacloud.com 万相 视频 风格重绘 人像 非人像 限制 动漫化
- 海外搜索　AI video generation failure breakdown motion artifacts prompting image to video official Luma Adobe Runway；site:docs.lumalabs.ai video generation keyframes loop limitations credits failed
- 候选 8 条（其中爬虫 0 条、国内 6 条）；晋升 1、待核验 2、淘汰 5。
- 缺口　缺同镜头条件下可复查的失败率、重试成本和微调后泛化样本。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [万相图生视频微调](https://www.alibabacloud.com/help/zh/model-studio/wan-video-generation-finetune-guide) | 中 | 晋升 | [原子稿](./general-wan-finetune-holdout.md) |
| [万相多镜头提示](https://www.alibabacloud.com/help/zh/model-studio/text-to-video-prompt) | 中 | 淘汰 | 多镜头时间戳与参考职责已有条目 |
| [万相 3.0 提示](https://www.alibabacloud.com/help/zh/model-studio/wan3-video-generation-prompt-guide) | 中 | 淘汰 | 已有 11-20 高频运动及 11-16 音轨约束 |
| [可灵 O1 视频控镜](https://docs.qingque.cn/d/home/eZQCg5xHvxDaE-jP2GcnaNc6O) | 中 | 淘汰 | 参考/首尾帧与既有控镜入口重叠，宣传页无失败门槛 |
| [BitShovel 运镜案例](https://bitshovel.site/applications/ai-video) | 中 | 待核验 | 缺同输入、同设置的未剪失败样本和重试账 |
| [ZenStory 可灵首帧模板](https://zenstory.ai/zh/drama-skills/kling-image-to-video-prompt-template) | 中 | 淘汰 | 纸面示例，未执行验证，模板职责已覆盖 |
| [Runway 图生运动冲突](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) | 外 | 淘汰 | 与 11-12 清理冲突运动线索重复 |
| [Adobe 一致性报道](https://www.creativebloq.com/ai/has-adobe-just-solved-one-of-ai-videos-biggest-problems) | 外 | 待核验 | 缺对应功能版本和不同镜位的首尾对照原片 |

## platforms

- 中文搜索　AI 短视频 抖音 快手 B站 限流 拒审 违规 申诉 官方 AI 漫剧；AI短视频 抖音 快手 视频号 AI漫剧 违规 限流 拒审 官方 申诉 转载 2026；AI漫剧 红果 抖音 B站 文生视频 投稿 运营 平台 画质 故障 官方 2026；site:trust.douyin.com 2026 11月 AI 短视频 治理 处置 造假；site:cnsa.cn 2026 11月 快手 抖音 微信 AI魔改 专项 治理；丑狐 夜梦人 AI 创作 央视 2026 11 25 抖音 访谈 原始；site:open.douyin.com 短视频 投稿 审核失败 回调 失败原因 发布 抖音 视频 状态；site:open.kuaishou.com 短视频 发布 审核 失败 回调 视频 审核中 快手
- 海外搜索　AI YouTube Shorts TikTok demonetization appeals repetitive content official video evidence；YouTube Shorts Instagram Reels TikTok AI creator video upload rejection format reach official help 2026；TikTok Meta Youtube AI short video demonetization recommendation ineligible appeal processing official；site:support.google.com/youtube shorts restrictions detected AI notice content tab appeal allowlist Shorts upload
- 候选 12 条（其中爬虫 1 条、国内 7 条）；晋升 2、待核验 2、淘汰 8。
- 缺口　平台公开材料能确认个别告警和转码流程，缺推荐权重及账号级拒审至申诉的完整时间线。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [crawler《丑狐》评论](https://finance.sina.com.cn/wm/2026-11-25/doc-inizyefx9409010.shtml) | 中 | 淘汰 | 原链接未取得正文，无法证明推荐或审查机制 |
| [《丑狐》创作者抖音](https://www.douyin.com/video/7709908322752793866) | 中 | 待核验 | 缺可读原稿、后台触达与审核日志 |
| [TikTok 内容违规和封禁](https://support.tiktok.com/en/safety-hc/account-and-user-safety/content-violations-and-bans) | 外 | 待核验 | 需可读当期帮助或端内状态与申诉凭证 |
| [Shorts 原创指南](https://support.google.com/youtube/thread/470890423?hl=en&msgid=474034934) | 外 | 淘汰 | 与 11-23 原创验收重复 |
| [YPP 申诉](https://support.google.com/youtube/answer/9564590?hl=en) | 外 | 淘汰 | 频道级申诉，无法说明单条视频告警状态 |
| [快手 AI 魔改](https://www.cnsa.cn/art/2026/9/10/art_1957_49288.html) | 中 | 淘汰 | 打开返回错误或超时 |
| [微信 AI 魔改](https://www.cnsa.cn/art/2026/10/9/art_1957_49393.html) | 中 | 淘汰 | 打开返回错误或超时 |
| [抖音虚假人设](https://www.cnsa.cn/art/2026/11/6/art_1957_49521.html) | 中 | 淘汰 | 原页超时 |
| [Remuxe TikTok 申诉](https://remuxe.com/articles/tiktok-unoriginal-content-appeal) | 外 | 淘汰 | 营销转述，缺可复查当事账号 |
| [快手通用发布接口](https://open.kuaishou.com/platformDocs/openAbility/contentManagement/createAVideo) | 中 | 淘汰 | 11-16 已记录常规发布路径 |
| [YouTube Studio 告警](https://support.google.com/youtube/answer/17011221?co=GENIE.Platform%3DDesktop&hl=en-A) | 外 | 晋升 | [原子稿](./platforms-youtube-studio-notice-triage.md) |
| [快手短剧转码](https://open.kuaishou.com/docs/operate/specification/integrationGuide/apiGuide.html) | 中 | 晋升 | [原子稿](./platforms-kuaishou-noveldrama-transcode-preflight.md) |

## types

- 中文搜索　AI短剧 丑狐 夜梦人 制作 水墨 分镜 剪辑 同质化 创作者；夜梦人 丑狐 新浪娱乐 专访 原采访 创作者 即梦 丑狐
- 海外搜索　AI microdrama vertical faceless video production creator case study retention failure digital avatar dubbing official；AI microdrama faceless short series creator behind the scenes vertical storytelling official ReelShort production failure retention
- 候选 8 条（其中爬虫 1 条、国内 5 条）；晋升 1、待核验 5、淘汰 2。
- 缺口　国内获得一例具体返工；海外依然缺未入选、弃剧或无脸口播失败的逐集留存原始数据。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [crawler《丑狐》评论](https://finance.sina.com.cn/wm/2026-11-25/doc-inizyefx9409010.shtml) | 中 | 淘汰 | 原链接未取得正文；另寻原访谈 |
| [新浪娱乐原访谈](https://m.weibo.cn/2/detail/5367291182057848) | 中 | 晋升 | [原子稿](./types-chouhu-character-adaptation.md) |
| [《丑狐》结局争议转述](https://k.sina.com.cn/article_7879776356_1d5abd86406801altz.html) | 中 | 待核验 | 缺可归因的逐集留存、完结数据及相关完整原访谈段落 |
| [《丑狐》成本整理](https://promangofund.com/ai/trends/ai-short-drama-chouhu) | 中 | 待核验 | 缺作者工时账、订阅消耗和到账凭证 |
| [AI 短剧受众洞察报告](https://oss.ibos.cn/53ai/bot/files/a734a874d1dff5bcd95c0ecbb3fac47a/2026AI%E7%9F%AD%E5%89%A7%E8%A1%8C%E4%B8%9A%E5%8F%91%E5%B1%95%E4%B8%8E%E5%8F%97%E4%BC%97%E6%B4%9E%E5%AF%9F%E6%8A%A5%E5%91%8A.pdf) | 中 | 待核验 | 缺机构原始发布页与重制剧项目级完播对照 |
| [ReelShort CEO 访谈](https://time.com/7173765/reelshort-crazy-maple-studio-joey-jia-interview/) | 外 | 待核验 | 缺 AI 制作归因及按集失败样本 |
| [Hollywood 移动短剧](https://apnews.com/article/087b042a6eac08e159410e29689606b9) | 外 | 淘汰 | 行业报道未提供可迁移的 AI 返工动作 |
| [西班牙竖屏制作](https://elpais.com/television/series/2026-07-19/rodar-dos-temporadas-en-dos-semanas-con-las-camaras-giradas-asi-se-hace-una-microserie-en-vertical-espanola.html) | 外 | 待核验 | 缺 AI 生成段落、样片和传统拍摄的对照 |

## pipeline

- 中文搜索　AI 漫剧 数字人口播 工作流 分镜 到发布 瓶颈 废片 积分 成本 火山 阿里 云 官方；site:alibabacloud.com 百炼 视频 生成 失败 不计费 任务 过期 24 小时
- 海外搜索　AI video end to end editing production workflow credit burn failed jobs bottleneck Google Flow Luma official；AI video failed generation credits refund Luma Runway Google Flow official credit
- 候选 9 条（其中爬虫 2 条、国内 5 条）；晋升 2、待核验 3、淘汰 4。
- 缺口　厂商功能和停用日可复查，缺同一 brief 的可交付秒成本、返工率、音画一致率及公开账单。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [crawler《丑狐》评论](https://finance.sina.com.cn/wm/2026-11-25/doc-inizyefx9409010.shtml) | 中 | 淘汰 | 原链接未取得正文，未确认流程；人物改编另核 |
| [crawler PC Tech Magazine 素材转视频](https://pctechmag.com/2026/11/from-image-library-to-video-strategy-how-image-to-video-ai-is-changing-digital-content-production) | 外 | 淘汰 | 原页未取得正文，线索摘要无可验流程 |
| [短剧Lab 分镜管理](https://doc.duanjulab.com/manual/storyboard/) | 中 | 晋升 | [原子稿](./pipeline-duanjulab-voice-repair.md) |
| [阿里云漫剧工坊](https://www.aliyun.com/solution/tech-solution/use-bailian-to-intelligently-create-comics/) | 中 | 待核验 | 仅单个完整漫剧体验估算，缺每集长度、重试与人工账；逐步审核已有 |
| [百炼 Token Plan](https://www.alibabacloud.com/help/zh/model-studio/token-plan-video-generation) | 中 | 待核验 | 确认任务 ID 24 小时；缺项目级过期重跑率、控制台消耗分解和各模型视频 URL 时限对照 |
| [即梦每秒报价转载](https://jishuzhan.net/article/2120018246431408129) | 中 | 待核验 | 缺产品 SKU、地域、分辨率、积分换算和可交付秒分母 |
| [Google Flow 生成功能与积分](https://support.google.com/flow/answer/16526234?hl=en-GB) | 外 | 晋升 | [原子稿](./pipeline-flow-december-migration.md) |
| [Runway 同任务扣返](https://help.runwayml.com/hc/en-us/articles/55412733862675-Why-do-I-see-a-charge-and-a-refund-for-the-same-generation) | 外 | 淘汰 | 与 11-23 预扣和最终积分对账重复 |
| [Flow 剪辑与合成](https://support.google.com/flow/answer/16935718) | 外 | 淘汰 | 粗剪拼接与既有 Flow/Firefly 先筛后剪重叠 |

## growth

- 中文搜索　AI 漫剧 短剧 投流 ROI 亏损 分账 广告 巨量引擎 磁力引擎 官方 失败复盘；site:oceanengine.com 巨量引擎 短剧 素材 投流 回收 ROI 归因 官方；AI 漫剧 失败 亏损 停更 成本 制作 投流 回款 2026 采访
- 海外搜索　AI short videos creator ROI pitfalls demonetization TikTok Creator Rewards qualified views paid promoted official；site:ads.tiktok.com help creative split test video attribution ROI creative fatigue；TikTok short drama advertising creator rewards payout ROI attribution TikTok for Business drama case study
- 候选 8 条（其中爬虫 0 条、国内 5 条）；晋升 2、待核验 4、淘汰 2。
- 缺口　延续昨日增长缺口，补扫投放工具、短剧报表、实际亏损与停更访谈。可核实测试和报表规则，仍缺同部剧的制作、投流、退款与实际回款完整账。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [第一财经漫剧回本调查](https://www.yicai.com/news/103440969.html) | 中 | 待核验 | 已读个案，缺归因回款、投流与工时全账，不能把访谈成本推广为行业值 |
| [36氪价格下跌报道](https://www.36kr.com/p/4044045316019078) | 中 | 待核验 | 缺同品类同周期合同样本、清结算与样本分母 |
| [巨量引擎广告素材管理](https://www.oceanengine.com/publicity/1211) | 中 | 淘汰 | 历史处置支持已有宣推一致性检查，无新增回报口径 |
| [停更与版权访谈](https://finance.sina.cn/stock/jdts/2026-08-21/detail-iniparan1306837.d.html) | 中 | 待核验 | 缺账号停更前后变现资格、处置记录及到账对照 |
| [文投控股中报](https://static.cninfo.com.cn/finalpage/2026-08-29/1225531739.PDF) | 中 | 待核验 | 缺同部 AI 剧的成本与实收拆分 |
| [TikTok Ads 拆分测试](https://ads.tiktok.com/resources/help/article/split-testing) | 外 | 晋升 | [原子稿](./growth-tiktok-paid-creative-split.md) |
| [TikTok 短剧 Growth Max 报表](https://ads.us.tiktok.com/resources/help/article/how-to-set-up-reporting-for-tiktok-growth-max-mini-drama-ad-campaigns?lang=en) | 外 | 晋升 | [原子稿](./growth-tiktok-microseries-reporting.md) |
| [TikTok Creator Rewards 帮助](https://support.tiktok.com/en/business-and-creator/creator-rewards-program/creator-rewards-program) | 外 | 淘汰 | 本次未取得正文；计划资格已有基线，缺当期可审计页面和结算账 |

## compliance

- 中文搜索　AI 生成 视频 版权 肖像 判决 AI短剧 违规 标识 行政处罚 官方；AI 短剧 漫剧 AI换脸 侵权 裁判 案例 2026 site:court.gov.cn；AI 短视频 虚假 抖音 标识 案例 2026 site:cac.gov.cn；site:cac.gov.cn 2026 11 AI 假冒 短视频 专家 治理 成果 虚假人设
- 海外搜索　synthetic media copyright AI video takedown enforcement digital replica official case short video；AI video short-form deepfake disclosure enforcement case FTC AI impersonation social video 2026 official；AI reels shorts copyright AI-generated refusal copyright office case deepfake enforcement platform 2026 official；site:oversightboard.com AI-Generated Video of Female Campaigner 2026 AI Info
- 候选 10 条（其中爬虫 0 条、国内 6 条）；晋升 2、待核验 2、淘汰 6。
- 缺口　缺国内个案申诉时序、Meta 执行覆盖范围以及可复查的重复仿冒处置结果。

| 来源与线索 | 地区 | 结果 | 理由或缺失证据 |
| --- | --- | --- | --- |
| [网信办 AI 健康科普](https://www.cac.gov.cn/2026-11/06/c_1795719652932799.htm) | 中 | 晋升 | [原子稿](./compliance-cn-health-video-claims-and-credentials.md) |
| [欧盟深度伪造指引](https://publications.europa.eu/resource/cellar/caabe0cd-de39-11f1-ba80-01aa75ed71a1.0006.01/DOC_1) | 外 | 晋升 | [原子稿](./compliance-eu-deepfake-fiction-vs-shopping-disclosure.md) |
| [Meta 监督委员会个案](https://www.oversightboard.com/decision/fb-40oc4fcm/) | 外 | 待核验 | 个案可查，缺 Meta 对非性虚构动作或声音和重复仿冒的执行答复 |
| [司法机关 AI 相似肖像释法](https://ipc.court.gov.cn/zh-cn/news/view-6039.html) | 中 | 待核验 | 独立自动生成抗辩需底层裁判及完整事实认定 |
| [网信办公众人物恶搞](https://www.cac.gov.cn/2026-11/06/c_1795720746219974.htm) | 中 | 淘汰 | 与 11-09 仿冒条目重叠 |
| [网信办 9 月虚假人设](https://www.cac.gov.cn/2026-09/30/c_1792520301987752.htm) | 中 | 淘汰 | 与 11-09、11-11 条目重叠 |
| [最高法历史模板争议](https://www.court.gov.cn/zixun/xiangqing/462881.html) | 中 | 淘汰 | 历史案例且素材授权已覆盖 |
| [网信办未标识伪造画面](https://www.cac.gov.cn/2026-02/12/c_1772636033171974.htm) | 中 | 淘汰 | 11-18 来源笔记已记录 |
| [美国版权局 AI 索引](https://copyright.gov/ai/) | 外 | 淘汰 | 索引缺独立可操作短视频案例 |
| [英国 AI 版权报告](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence) | 外 | 淘汰 | 偏训练政策研究，未带来发布工作流证据 |
