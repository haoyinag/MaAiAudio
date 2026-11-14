# 2026-11-14 一手来源补扫笔记

> 用途：为当日 `SCAN.md` 与原子稿提供独立的一手来源发现材料；不是最终事实清单。采集日与时区：2026-11-14，Asia/Shanghai。所有“建议晋升”仍须由主流程完成原页复核、全库去重与原子字段整理。

## 起点审计

- `.automation/ai-short-video/candidates.json` 的 `coverage` 为：`general=0`、`platforms=3`、`types=3`、`pipeline=3`、`growth=1`、`compliance=2`；六维全部低于每维 8 条的发现目标，`general` 完全缺席。
- `region_counts` 为国内 3、海外 1。文件只有 4 个独立页面，`coverage` 是多标签计数，不能当作 12 个独立候选。
- 四条爬虫线索均非一手规则或产品文档：凤凰财经“短剧出海”、腾讯新闻“赵丽颖起诉红果”、新浪财经“红果金币”、Yahoo Finance / Business Wire 的 YouArt 发布稿。它们只保留为待核验或淘汰线索，未直接作为事实。
- 人工补扫记录 51 个按主维度归类的候选：国内 33、海外 18，约 **65:35**。各维均使用中文和海外检索词，并达到至少 8 条发现线索。
- 去重重点：2026-10-22 至 2026-11-11 的全部 `DIGEST.md`、`SCAN.md` 与原子稿；另以关键词检查历史版本中的 Shorts Series、AI 标识、Article 50、Seedance/Firefly、TikTok Creator Rewards、Facebook 原创性和微短剧备案主题。

## general｜通用技巧（8 条：国内 5 / 海外 3）

### 搜索尝试

- 中文：`火山引擎 AI 视频 提示词 参考图 2026`、`Seedance 视频提示词 官方 2026`、`视频 Prompt 生成 算子 模型档位`。
- 海外：`official AI video prompting guide consistency 2026`、`Adobe Firefly motion reference official`、`Firefly video prompt guide 2026`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [火山引擎：自由创作新手指南](https://docs.volcengine.com/docs/creative-agent/free-creation-beginners-guide?lang=zh)（当前文档） | 给出“参考图主体、视频类型、运镜、动作、环境、音频、一致性”七字段，并要求多参考图逐次完整指代。 | 与 11-11 Kickart 七字段 atom 高度重复；合并为时效复核。 |
| 2 | 国内 | [火山引擎 LAS：视频 Prompt 生成](https://docs.volcengine.com/docs/LakeAIService/video_prompt_generation?lang=zh)（当前文档） | `requirements` 可同时写现有 Prompt、修改要求和保持不变项；`model_tier` 允许服务端维护具体模型，固定版本才用 `model_name`，两者不可同时传。 | **建议晋升候选**：把“保持不变项”设为提示词迭代的一等字段；仍缺跨模型失败率或独立效果比较，不能写成质量提升因果。 |
| 3 | 国内 | [火山方舟：视频生成快速入门](https://docs.volcengine.com/docs/ark/video-generation-tutorial?lang=zh)（当前文档） | 建议抽象描述改为具象描述、删除不重要部分、把重要内容前置；明确预期时先生图再图生视频。 | 与既有结构化提示、首帧控制条目重复。 |
| 4 | 国内 | [火山方舟：创建视频生成任务 API](https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh)（当前文档） | 当前 Seedance 2.5 支持的提示语言多于 2.0；中文建议不超过 500 字、英文不超过 1000 词，过长可能分散模型注意。 | 易变规格；需要记录核验日期。与既有模型限制主题小幅增量，单独成条价值不足。 |
| 5 | 国内 | [火山引擎：智能视频](https://docs.volcengine.com/docs/large-model-of-image-generation/smart-video?lang=zh)（更新 2026-09-18） | 区分文生、图生、首尾帧和全能参考；首尾帧用于固定起止状态，全能参考接收多模态素材。 | 已被 9 月和 10 月多篇入口选择 atom 覆盖，重复。 |
| 6 | 海外 | [Adobe Learn：Borrow camera motion from real footage](https://www.adobe.com/learn/firefly/web/video-motion-reference)（2026-04-14） | Firefly 可从上传视频抽取镜头运动并作为生成参考。 | 更适合 `pipeline`；缺支持格式、长度、地区和失败边界，暂不在 general 晋升。 |
| 7 | 海外 | [Adobe Help：Generate videos using text prompts](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-text-prompts.html)（更新 2026-06-16） | 文本可指定内容、情绪、场景和机位；Motion reference 可提取平移、缩放、俯仰与运动路径。 | 与 #6 交叉确认能力存在，但仍是同一厂商证据；不证明效果优于文字运镜。 |
| 8 | 海外 | [Adobe：Firefly Video Guide](https://www.adobe.com/cc-shared/assets/pdf/business/teams/resources/whitepapers-ebooks/sdk/firefly-video-guide.pdf)（2026） | 官方指南把镜头运动、镜头类型和角度列为提示组成。 | 与现有结构化提示 atom 重复；作为 #6 的操作背景，不单独晋升。 |

## platforms｜平台技巧（8 条：国内 5 / 海外 3）

### 搜索尝试

- 中文：`抖音 开放平台 视频发布 审核 官方`、`抖音 第三方发布 审核状态`、`快手 AIGC 平台 官方 2026`。
- 海外：`YouTube Shorts AI creation update official 2026`、`Facebook creator assistant Reels official 2026`、`TikTok AI generated content label official`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [抖音开放平台：内容发布接入方案](https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-publish-solution/)（当前文档） | 第三方发布与端内上传使用相同审核逻辑；不相关话题和强导流可能影响正常分发；小程序落地页要求与视频高相关。 | 已由 11-10 抖音 atom 覆盖，重复。 |
| 2 | 国内 | [抖音开放平台：创建视频](https://open.douyin.com/platform/resource/docs/openapi/video-management/douyin/create/create-video)（当前文档） | 创建后先进入审核、期间仅自己可见；代用户创建时每次都要让用户明确感知。 | 可作为自动发布验收依据，但与现有第三方发布条目重叠。 |
| 3 | 国内 | [抖音开放平台：拍摄器接入方案](https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-camera-solution/)（当前文档） | Webhook 可关联 `share_id` 与 `item_id`；审核中与审核失败需要产品分别呈现。 | **建议晋升候选**：发布流水线区分“已上传、审核中、审核失败、可见”；需确认现有 pipeline 是否已有同义状态机。 |
| 4 | 国内 | [抖音开放平台：状态码](https://open.douyin.com/platform/resource/docs/develop/common-tools/status-code/)（当前文档） | 分开给出超出每日发布量、投稿能力封禁、素材审核不通过等错误。 | 与 #3 合并作为错误恢复证据；页面未给重试时机与申诉 SLA。 |
| 5 | 国内 | [快手 IR：2026 光合大会 AIGC 四项政策](https://ir.kuaishou.com/zh-hans/node/11836/pdf)（2026-09-03） | “燎原计划”覆盖入驻、零粉起步到流量/收益；另有 12 周奖金赛。 | 11-11 growth atom 已覆盖；不是平台分发规则，重复。 |
| 6 | 海外 | [YouTube Community：2025/2026 Shorts AI creation updates](https://support.google.com/youtube/blog/372291417/new-youtube-updates-to-help-you-create-connect-with-fans-drive-business?hl=en-BD)（2025-09-16，页面当前可访问） | Edit with AI、Speech to song、Veo 3 等按市场分阶段推出。 | 地区与功能已被 10-22/10-27/11-09 条目覆盖；页面发布时间较旧，淘汰为当日增量。 |
| 7 | 海外 | [Meta：Creator Assistant 与 Reels AI 翻译](https://about.fb.com/news/2026/06/creator-assistant-more-languages-for-ai-translations-on-facebook/)（2026-06-04） | Creator Assistant 读取创作者自身表现和受众趋势；首批美国、加拿大、印度；Reels AI 翻译继续扩语言。 | 11-10 SCAN 已留待核验；缺 11 月当前国家、账户、语言及人工校对边界。 |
| 8 | 海外 | [TikTok Help：AI-generated content](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)（当前帮助页） | 真实感 AIGC 必须披露；启用标签本身不会影响分发，违规内容仍可被移除。 | 11-09 平台 atom 已完整覆盖，重复。 |

## types｜类型技巧（8 条：国内 5 / 海外 3）

### 搜索尝试

- 中文：`广电总局 AI 微短剧 类型 精品 2026`、`AI 短剧 AI 解说漫 官方`、`短漫剧 投流 出海 配音 官方`。
- 海外：`YouTube vertical microdrama official 2026`、`TikTok creator-led micro-series official`、`Adobe virtual avatar video official 2026`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [广电总局：2026 精品创作大会致辞](https://www.nrta.gov.cn/art/2026/11/5/art_3901_74407.html)（2026-11-05） | 官方称 AI 已进入选题、制作、译制、审核等环节，并强调题材丰富、类型多样与安全治理。 | 宏观讲话不能推出具体类型方法或单项目效果；保留扫描，不晋升。 |
| 2 | 国内 | [火山剧创：短剧创作](https://docs.volcengine.com/docs/drama-creation/short-play-creation?lang=zh)（当前文档） | 产品区分 AI 短剧与 AI 解说漫；Agent 流程为剧本、设定、分镜、视频，并在设定阶段保存角色、场景、道具。 | 11-11 已留待核验；仍缺两类型分别适用的叙事/镜头验收差异。 |
| 3 | 国内 | [火山剧创：更新记录](https://docs.volcengine.com/docs/drama-creation/new-feature-release-record?lang=zh)（至 2026-11-06） | AI 解说剧可在设定阶段配置旁白音色以保持全片解说声音。 | **待核验**：可形成“解说剧把统一旁白设为全局资产”，但只有产品功能证据，缺类型效果/失败案例。 |
| 4 | 国内 | [火山 LAS：短漫剧集](https://docs.volcengine.com/docs/lake-ai-service/short-manga-series?lang=zh)（当前文档） | 官方按投流素材、漫剧复刻、短漫剧换脸、出海配音翻译四类场景组织算子。 | **建议晋升候选**：按交付目的拆类型分支；“爆款复刻”涉及权利/同质化风险，不能照抄为方法。 |
| 5 | 国内 | [广电总局：2026 年第二批“微短剧+”推荐](https://www.nrta.gov.cn/module/download/downfile.jsp?classid=0&filename=35ce192d52ab438e955eb861c06c7577.pdf&showname=2026%E5%B9%B4%E7%AC%AC%E4%BA%8C%E6%89%B9%E2%80%9C%E5%BE%AE%E7%9F%AD%E5%89%A7+%E2%80%9D%E8%A1%8C%E5%8A%A8%E8%AE%A1%E5%88%92%E6%8E%A8%E8%8D%90%E5%89%A7%E7%9B%AE.pdf)（2026-10） | 推荐名单含 AI 动漫解读传统文化、非遗融合等项目。 | 名单只能证明入选与官方简介，不能推导“某类型更易获推荐”；淘汰为方法证据。 |
| 6 | 海外 | [YouTube Blog：Microdramas on Shorts](https://blog.youtube/culture-and-trends/the-evolution-of-web-series-on-youtube-microdramas/)（2026-10-29 左右） | 给出竖屏优先构图、普遍主题、评论参与和季集化工具，并公布平台汇总数据。 | 11-09 类型 atom 已覆盖长尾、本地化与季集结构，重复。 |
| 7 | 海外 | [TikTok：与 MADE BY US 共制 creator-led micro-series](https://newsroom.tiktok.com/tiktok-and-made-by-us-studios-enter-partnership-to-co-produce-creator-led-micro-series?lang=en)（2026-10-14） | 微系列从创意到制作由创作者与专业编剧、导演、演员共同参与，面向 TikTok 与 PineDrama。 | 10-27 atom 已覆盖，重复。 |
| 8 | 海外 | [Adobe Help：Text to avatar](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-virtual-avatars.html)（更新 2026-08-18） | beta 支持脚本、头像、声音/口音、背景和预览。 | 与口播类型相关，但缺短视频平台适配、肖像/声音授权说明及效果比较；留待核验。 |

## pipeline｜制作管线（8 条：国内 5 / 海外 3）

### 搜索尝试

- 中文：`AI 短剧 工作流 分镜 资产 画布 官方 2026`、`火山剧创 更新记录 分镜`、`视频 Prompt 算子 保持不变`。
- 海外：`official AI video workflow motion reference 2026`、`virtual avatar workflow official`、`YouTube conversational editing Shorts official 2026`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [火山剧创：短剧创作](https://docs.volcengine.com/docs/drama-creation/short-play-creation?lang=zh)（当前文档） | 剧本解析形成大纲、人物小传、分集剧情；资产设定后再进入分镜；单镜可生成最多 4 个候选。 | 与既有“资产表—分镜—候选筛选”管线重复。 |
| 2 | 国内 | [火山剧创：灵感片场](https://docs.volcengine.com/docs/drama-creation/inspiration-studio?lang=zh)（当前文档） | 资产工作台、剧集画布和分镜序列相互连通；从序列拖出分镜视频节点会删除分镜页对应分镜。 | **建议晋升候选**：同步画布操作前保存检查点，并把删除视为跨视图破坏性操作；需产品实测确认撤销、版本和协作冲突行为。 |
| 3 | 国内 | [火山剧创：更新记录](https://docs.volcengine.com/docs/drama-creation/new-feature-release-record?lang=zh)（至 2026-11-06） | 11 月更新含自定义分镜 Skill 2.0、协作光标开关；历史记录含错误信息复制、资产批量上传与审核校验。 | 可为 #2 提供当前时效，但未公开冲突解决与回滚语义。 |
| 4 | 国内 | [LAS：视频 Prompt 生成](https://docs.volcengine.com/docs/LakeAIService/video_prompt_generation?lang=zh)（当前文档） | 可传最多 9 张参考图；返回请求次数与 Token 用量；不支持的固定模型直接失败，不自动降级或重试。 | **建议晋升候选**：固定版本调用必须显式失败并由调用方处理，不把降级当作默认；缺错误码与重试策略。 |
| 5 | 国内 | [火山点播：AI 文字成片](https://docs.volcengine.com/docs/video-on-demand/ai-text-to-video?lang=en)（当前文档） | 文本、画面、配音和字幕形成约 30 秒视频；生成、存储、分发分开计费；输入与输出均做安全审核。 | 可用于成本分账，但价格易变且既有管线已覆盖分账思想；不单独晋升。 |
| 6 | 海外 | [Adobe Learn：Video motion reference](https://www.adobe.com/learn/firefly/web/video-motion-reference)（2026-04-14） | 先上传真实视频抽取镜头运动，再将其用于生成。 | 与 Adobe Help 交叉确认；**单一厂商建议晋升候选**，但需记录参考素材权利和未公开限制。 |
| 7 | 海外 | [Adobe Help：Text to avatar](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-virtual-avatars.html)（更新 2026-08-18） | 提供预览后再生成、脚本可编辑、背景可定制。 | 与既有“先审计划/预览再生成”原则重复；beta 可用范围待核。 |
| 8 | 海外 | [Made on YouTube 2026](https://blog.youtube/madeonyoutube/)（2026） | Shorts / YouTube Create 的对话式编辑可按提示裁剪语音、同步音乐、加文字钩子和重排帧。 | 平台内置工具，缺地区/账户/回滚和手动编辑边界；留在 platforms/pipeline 待核验。 |

## growth｜增长变现（9 条：国内 6 / 海外 3）

### 搜索尝试

- 中文：`快手 AIGC 创作者 扶持 收益 官方 2026`、`抖音 短剧 推广 任务 官方`、`短漫剧 投流 素材 官方`、`微短剧 扶持 官方 2026`。
- 海外：`YouTube Shorts monetization current official`、`TikTok Creator Rewards official`、`Meta creator monetization AI 2026`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [快手 IR：AIGC 四项专属政策](https://ir.kuaishou.com/zh-hans/node/11836/pdf)（2026-09-03） | 区分成长支持与 12 周奖金赛。 | 11-11 atom 已晋升，重复；完整资格、流量和结算条款仍缺。 |
| 2 | 国内 | [火山 LAS：短漫剧集](https://docs.volcengine.com/docs/lake-ai-service/short-manga-series?lang=zh)（当前文档） | 以多集正片做钩子识别、镜头筛选、节奏重组并输出投流变体。 | 11-09“生成与效果验证分账”atom 已覆盖，重复；官方未给转化或 ROI。 |
| 3 | 国内 | [抖音开放平台：内容发布接入方案](https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-publish-solution/)（当前文档） | 小程序落地页与视频相关性高才可申请挂载；诱导分享、引导下载等可能导致权限取消。 | 可限制转化链路设计，但不提供收益公式；与 11-10 相关性 atom 重复。 |
| 4 | 国内 | [广电总局 2025 通知：促进微短剧健康繁荣](https://www.nrta.gov.cn/art/2025/2/5/art_113_70148.html)（2025-02-05） | 对重点目录作品可指导平台优先排播、算法推荐、分账支持。 | 不能外推到普通 AI 短剧；项目目录、资格和金额缺失，待核验而非收入承诺。 |
| 5 | 国内 | 爬虫：凤凰财经“短剧出海变红海”（2026-11-13） | 二手采访声称 AI 短剧制作成本远低于海外实拍。 | **待核验**：缺合同、预算口径、质量等级、返工与投流成本；不得采用“20 倍”结论。 |
| 6 | 国内 | 爬虫：新浪财经“红果金币功能”（2026-11-13） | 二手报道讨论金币拉新及功能变化。 | **待核验**：缺红果官方公告、灰度范围、生效时间及对创作者结算的影响。 |
| 7 | 海外 | [YouTube Help：Shorts monetization policies](https://support.google.com/youtube/answer/12504220?hl=en)（当前帮助页） | Shorts Feed 广告池与长视频分开；分配基于合格 engaged views，创作者获得其分配额的 45%。 | 多篇既有 growth atom 已覆盖；重复。 |
| 8 | 海外 | [TikTok Newsroom：Creator Rewards Program](https://newsroom.tiktok.com/introducing-the-new-creator-rewards-program/?lang=en)（2024） | 旧公告列 originality、play duration、search value、engagement 四因素，并要求视频超过 1 分钟。 | 不是 2026 当前完整条款；缺国家、门槛、资格和 AI 内容细则，待核验。 |
| 9 | 海外 | [Meta：Creator Assistant](https://about.fb.com/news/2026/06/creator-assistant-more-languages-for-ai-translations-on-facebook/)（2026-06-04） | 可基于账号自身表现回答某条 Reel 为何表现更好并给建议。 | 平台自述不等于因果归因；缺推荐计算方法、实验设计和收益影响，不能晋升为增长规律。 |

## compliance｜合规与风控（10 条：国内 7 / 海外 3）

### 搜索尝试

- 中文：`网信办 AI 生成 视频 标识 2026`、`广电总局 微短剧 管理办法 2026`、`AI 微短剧 肖像 声音 授权 官方`、`短视频 六类标签`。
- 海外：`EU AI Act Article 50 transparency official 2026`、`TikTok AIGC policy official`、`YouTube altered synthetic content official`。

| # | 地区 | 一手来源与日期 | 来源明确事实 | 初步处置 / 缺失证据 |
| --- | --- | --- | --- | --- |
| 1 | 国内 | [广电总局令第 16 号：微短剧发展管理办法](https://www.nrta.gov.cn/art/2026/7/31/art_113_73785.html)（2026-07-31；2026-09-01 起施行） | 微短剧按类别实行备案公示和发行许可；一、二类播前审核，三类由符合条件的播出单位审核并标节目编号。 | 10-22/10-23 atom 已覆盖，重复。 |
| 2 | 国内 | [网信办：整治无 AI 标识虚假不实信息](https://www.cac.gov.cn/2026-02/12/c_1772636033171974.htm)（2026-02-12） | 通报虚构救援、事故、公众人物仿冒等案例，AI 标识缺失与虚假/侵权风险并行。 | 11-11 atom 已覆盖，重复。 |
| 3 | 国内 | [网信办：人工智能生成合成内容标识办法](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)（2025-03-14） | 区分显式与隐式标识；视频起始画面和播放周边设置显式提示，文件元数据保存隐式标识。 | 历史 atom 已覆盖，重复。 |
| 4 | 国内 | [网信办：规范短视频内容标注答记者问](https://www.cac.gov.cn/2026-05/12/c_1780328273108117.htm)（2026-05-12） | 发布环节六类必选标签包括 AI、虚构演绎、营销、转载、个人观点和无需标注。 | 10-22/10-23 atom 已覆盖，重复。 |
| 5 | 国内 | [广电总局：新一轮微短剧专项治理](https://www.nrta.gov.cn/art/2026/11/6/art_114_74410.html)（2026-11-06） | 当前治理覆盖正片、片名、宣推、弹幕、引流、换名重播、“盗脸”“偷声”和榜单同质化。 | 11-09 atom 已覆盖，重复。 |
| 6 | 国内 | [AI 微短剧“融像”“融声”权益保护座谈会](https://ynsgbdsj.yn.gov.cn/xyxx/202609/t20260907_4190477.html)（2026-09-07，转载广电总局） | 强调明确授权、事前授权管理、事中技术筛查与人工复核、事后可追溯存证。 | 10-22 肖像声音 atom 已覆盖，重复。 |
| 7 | 国内 | 爬虫：腾讯新闻“赵丽颖起诉红果短剧”（2026-11-13） | 新闻标题指向疑似知名演员肖像被 AI 短剧使用。 | **待核验**：缺法院立案/裁判文书、当事人声明、涉案内容和请求权基础；不得写成侵权已成立。 |
| 8 | 海外 | [欧盟委员会：Article 50 transparency guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems)（2026-08） | Article 50 透明度义务自 2026-08-02 适用，并发布 provider/deployer 指南。 | 10-28/10-30 atom 已覆盖，重复。 |
| 9 | 海外 | [TikTok Help：AI-generated content](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)（当前帮助页） | 未标识的真实感 AIGC、危机事件伪造、特定公众人物情境和未经许可的私人个体肖像可能被处置。 | 既有 TikTok 合规与平台 atom 已覆盖；地区版本仍可能有差异。 |
| 10 | 海外 | [YouTube Help：Spam policy](https://support.google.com/youtube/answer/2801973?hl=en)（当前帮助页） | 社区规则同样适用于 AI 生成或修改内容；诈骗、误导和批量垃圾内容不因 AI 制作而例外。 | 只证明一般规则适用，不能替代 altered/synthetic disclosure 专页；作为辅助证据，不独立晋升。 |

## 爬虫四条线索的分层处置

1. 凤凰财经“短剧出海变红海”：`growth` 待核验；确切缺口为项目级预算、质量等级、返工、投流和收入账本。
2. 腾讯新闻“赵丽颖起诉红果短剧”：`compliance` 待核验；确切缺口为法院/当事人一手文件与案件进度，不能从标题认定侵权。
3. 新浪财经“红果金币功能”：`growth/platforms` 待核验；确切缺口为红果官方公告、灰度范围、生效时间和结算影响。
4. Yahoo Finance / Business Wire “YouArt Desktop”：`pipeline` 淘汰为当日事实来源；营销发布稿缺产品文档、版本、地区、价格、失败恢复和短视频验收证据。

## 建议主流程优先复核的增量

- `general`：LAS Prompt 算子的“修改要求 + 保持不变项”结构，以及 `model_tier` / 固定 `model_name` 的选择边界。
- `platforms`：抖音第三方发布的审核状态与错误码能否整理成一个最小发布状态机；先与 11-10 atom 去重。
- `types`：LAS 把投流、复刻、换脸、出海译配分成四个交付分支；必须同时写权利和同质化边界。
- `pipeline`：火山剧创画布与分镜页双向联动中的删除语义；需要实测撤销、版本与协作冲突后再决定是否普通晋升，否则保持 `待核验`。
- `growth`：没有找到可同时满足“当前一手、创作者级收益口径、AI 短视频直接相关、全库新颖”的候选；建议当日不为配额造 atom。
- `compliance`：当前高质量一手线索全部被 10 月下旬至 11 月 11 日条目覆盖；爬虫诉讼标题缺法院/当事人证据，建议保持 `待核验`。

## 地区与证据说明

- 51 条手工发现中，国内 33、海外 18（64.7:35.3）；比例用于检查发现广度，不作为晋升配额。
- 国内以网信办、广电总局、抖音开放平台、火山引擎与快手 IR 为主；海外以 YouTube、TikTok、Meta、Adobe 与欧盟委员会为主。
- 本笔记未绕过登录、验证码或访问限制。搜索结果页只作发现入口；表中事实均来自可打开的一手页面摘要或正文。
- 高可信但重复的材料明确标为合并；营销稿、二手报道与无法确认当前条款的页面均未提升为事实。
