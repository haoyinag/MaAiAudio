# 2026-11-16 背景研究：platforms / types / compliance

> 采集日期：2026-11-16（Asia/Shanghai）。本文件是后台研究账本，不是最终 `SCAN.md` 或 atom。先完成中英文广泛发现，再打开一手来源核验，并与 `docs/ai-short-video` 全库关键词去重。爬虫候选只作线索。

## 覆盖摘要

| 维度 | 去重后候选 | 国内 | 海外 | 建议晋升 | 待核验 | 重复 / 淘汰 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| platforms | 10 | 6 | 4 | 1 | 3 | 6 |
| types | 10 | 7 | 3 | 1 | 3 | 6 |
| compliance | 11 | 7 | 4 | 1 | 2 | 8 |
| 合计 | 31 | 20 | 11 | 3 | 8 | 20 |

本批发现池国内/海外约为 65:35。比例来自优先补扫中国监管、平台开放文档和广电来源，没有为比例采用营销稿。三维均达到至少 8 条发现线索。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 视频 发布 审核 人工智能生成 标识 官方`、`快手 短剧 AIGC 创作者 规则 官方`、`快手开放平台 视频 发布 审核 状态`、`国内短视频 AI 发布 标签 审核`。
- 海外：`YouTube Shorts AI generated content official`、`YouTube Shorts Reimagine AI remix official 2026`、`TikTok AI-generated content creator official`、`YouTube Shorts AI creation update official 2026`。

### 建议晋升

#### YouTube Reimagine 用“合格原 Short + 自动回链”约束 AI 二创入口

- **来源：** YouTube 官方博客，[Reimagine: A new AI-powered Remix tool in YouTube Shorts](https://blog.youtube/news-and-events/reimagine-new-ai-powered-remix-tool-youtube-shorts/)，2026-03-18。
- **核验状态建议：** `单一来源`。
- **来源明确事实：** Reimagine 位于合格 Shorts 的 Remix 入口；它把原 Short 的单帧变为 8 秒有声新片段，允许最多两张图库参考图和 Gemini 建议或自写提示；每条 Reimagined Short 会直接链接原作品。
- **分析推断：** 对需要做 AI 二创的账号，平台原生 Remix 入口提供比“下载—生成—重传”更明确的来源回链。官方页面没有说明该回链能替代版权许可，也没有公开合格视频判定、国家范围或推荐增益。
- **可执行含义：** 发布流程先检查原视频是否出现 Reimagine 入口；保留自动回链，不把平台可 Remix 等同于素材全部权利已获授权。
- **新颖性：** 全库未检出 `Reimagine`、单帧转 8 秒或自动回链条目；与现有“YouTube 内置 AI 短片自动披露与地区边界”不同，本条增量是二创来源关系和平台原生回链。

### 待核验

1. **快手开放平台异步发布状态。** [创建视频](https://open.kuaishou.com/platformDocs/openAbility/contentManagement/createAVideo)（更新 2025-05-23）明确发布接口返回不代表已同步到用户页，需按 `photo_id` 再查；但页面没有说明 AI 内容标签字段、审核结果字段或当前创作者端一致性。缺失证据：AI 标识入参/回执、审核状态 API 与实际端内展示的当前官方说明。
2. **YouTube “Make me move”。** [Shorts AI 功能帮助页](https://support.google.com/youtube/answer/15260303?hl=en)（页面未标日期，2026-11-16 核验）说明可用单人全身照套用预设动作，且要求使用他人照片须获许可；EEA、英国、瑞士不可用。缺失证据：完整国家/账号灰度清单、输出长度及和现有“最多三张参考图”条目的独立增量。
3. **TikTok AI spam 检测。** [TikTok 官方公告](https://newsroom.tiktok.com/helping-people-spot-and-understand-ai-generated-content-on-tiktok-sg?lang=en-SG)（2026-07-13）只说明“测试”针对政治时事、金融和医疗等主题的 AI spam 账号检测。缺失证据：正式上线范围、账号处置阈值、申诉流程；不得推断普通 AI 视频会被限流。

### 重复 / 淘汰

1. [抖音内容发布接入方案](https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-publish-solution/)：第三方发布、审核状态与端内同等审核已由 `inbox/2026-11-10/平台技巧-抖音第三方发布仍需端内同等审核.md` 晋升，重复。
2. [抖音拍摄器接入方案](https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-camera-solution/)：审核中仅本人可见及失败状态仍属于同一发布审核主题，合并到既有条目。
3. [中央网信办短视频六类必选标签](https://www.cac.gov.cn/2026-05/12/c_1780328273038196.htm)（2026-05-12）：已由 2026-10-22～23 平台/合规 atoms 覆盖。
4. [YouTube Shorts AI 生成功能帮助页](https://support.google.com/youtube/answer/15260303?hl=en)中的最多 3 张参考图、10 秒片段、自动披露和地区边界已被 2026-10-27、11-09 记录；除 `Make me move` 外不另开条目。
5. [TikTok AIGC 帮助页](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)：创作者标签、C2PA 自动标签与“合规标注本身不影响分发”已有历史条目，重复。
6. 爬虫候选 A2E AI / Yahoo Finance 聚合稿：产品发布型营销稿，缺可访问的一手能力文档、模型路由清单、商用权利和费用条款；不晋升。

## types｜类型技巧

### 搜索尝试

- 中文：`AI 微短剧 漫剧 创作计划 官方 2026`、`广电总局 微短剧 精品 创作 类型 2026`、`国际短视频大赛 创作方向 指南 2026`、`AI 微短剧 培训 AIGC 漫剧 官方`。
- 海外：`YouTube audio-first video to Shorts official`、`YouTube microdrama Shorts Series official 2026`、`TikTok creator-led content series microdrama official 2026`、`vertical micro-series storytelling official`。

### 建议晋升

#### YouTube 把 audio-first 静态视频转成 Shorts 时先锁定文字区间和视觉样式

- **来源：** YouTube Help，[Create content for Shorts using AI-generated features](https://support.google.com/youtube/answer/15260303?hl=en)，页面未标发布日期，2026-11-16 核验。
- **核验状态建议：** `单一来源`。
- **来源明确事实：** YouTube Studio 可把带英文文字转录的 audio-first 静态视频转成 8 秒至 3 分钟 Shorts；当前限澳大利亚、加拿大、英国、美国桌面端。用户可选择系统建议片段或按转录文本确定起止词，再从四种视觉样式中选择；生成后不能直接换样式，需回到原视频重新开始。
- **分析推断：** 这是“播客/音频优先内容再利用”为短视频类型的明确平台入口；先按语义完整性锁定转录区间，再选视觉风格，可把内容选择和视觉包装分成两个验收点。来源没有证明建议片段优于人工选择，也没有公开视觉样式的生成稳定性。
- **可执行含义：** 先清理英文转录并选出自洽的 8 秒～3 分钟语义段；视觉样式只在片段确认后选，并把换样式视为一次重新生成。
- **新颖性：** 全库只检出一般“长内容转短”和字幕主题，未检出 `audio-first`、按转录词确定起止或四种不可回切视觉样式。

### 待核验

1. **2026 国际短视频大赛方向指南。** [广电总局附件](https://www.nrta.gov.cn/cms_files/jcms1/web1/site/attach/0/100ec1bfa5074f71b43229f0c715cbb8.pdf?fileName=100ec1bfa5074f71b43229f0c715cbb8.pdf)（检索显示 2026-11 发布）提出从具体人物连接全球议题、本土与全球、传统与未来，并列出非遗、文物、文旅等叙事方向。缺失证据：它是赛事选题指南，不是 AI 视频方法；需赛事主通知、技术/时长要求和可复用的评审标准后再判断是否成 atom。
2. **广电总局第三批拟扶持项目。** [项目附件](https://www.nrta.gov.cn/cms_files/jcms1/web1/site/attach/0/082ee4101fb745dba9c3c704e6e9f60f.pdf?fileName=082ee4101fb745dba9c3c704e6e9f60f.pdf)（2026-11，检索显示发布于本周）只有项目、题材和机构列表。缺失证据：创作方法、成片类型、AI 使用范围和评审理由，不能从入选反推有效打法。
3. **北京“追光计划”AI 微短剧培训。** [北京市广电局公告](https://gdj.beijing.gov.cn/zwxx/gzbg1/202606/t20260622_4710290.html)（2026-06-22）确认覆盖真人微短剧、AIGC 微短剧和 AI 漫剧，并有项目发现、孵化、平台对接机制。缺失证据：课程正文、可验证方法、结业项目表现和当前开放资格。

### 重复 / 淘汰

1. [2026 精品微短剧秋季点评会](https://www.nrta.gov.cn/art/2026/9/30/art_114_74171.html)（2026-09-30）强调“横/竖、长/短、真人/AI”均可容纳，但方法仅为扎根生活、打磨叙事；与 2026-11-10 精品化条目重复且不足以推导类型效果。
2. [2026 中国广播电视精品创作大会致辞](https://www.nrta.gov.cn/art/2026/11/5/art_112_74402.html)（2026-11-05）关于 AI 剧占比和全链条应用已在 2026-11-10 类型 atom 与扫描账本处理；统计不能推导某类型更优。
3. [微短剧论坛](https://weihu.nrta.gov.cn/art/2026/11/5/art_112_74408.html)（2026-11-05）的精品化、大众化、国际化框架已在 2026-11-10 atom 覆盖。
4. [微短剧精品创作传播计划](https://www.nrta.gov.cn/art/2026/5/26/art_113_73378.html?xxgkhide=1)（2026-05-26）是扶持方向和价值导向，不是 AI 短视频类型技巧；与既有精品化结论重复。
5. [YouTube Shorts Series](https://blog.youtube/news-and-events/made-on-youtube-creators-shorts-series-tv-features/)（2026-09-23）的季/集、顺序播放和多屏观看已由 `inbox/2026-11-10/类型技巧-YouTube把竖屏微短剧视为连续剧集格式.md` 晋升。
6. [TikTok / Amplify The Next Episode](https://newsroom.tiktok.com/tiktok-and-amplify-launch-new-creator-led-content-series-for-brands?lang=en-AU)（2026-09-14）已由 `inbox/2026-11-09/类型技巧-TikTok品牌连载先选两种参与结构.md` 晋升。

## compliance｜合规与风控

### 搜索尝试

- 中文：`人工智能生成合成内容 标识 视频 官方`、`网信办 无 AI 标识 虚假视频 2026`、`最高法 AI 换脸 声音 肖像 2026 官方`、`广电总局 AI 微短剧 专项治理 2026`。
- 海外：`YouTube AI features privacy data prompts C2PA official`、`YouTube altered synthetic disclosure official 2026`、`EU AI Act Article 50 deepfake transparency official 2026`、`TikTok AIGC C2PA policy official`。

### 建议晋升

#### YouTube 内置 AI 功能使用前先做数据分级并检查活动留存

- **来源：** YouTube Help，[Your data and using AI features on YouTube](https://support.google.com/youtube/answer/14772770?hl=en-CN)，页面未标发布日期，2026-11-16 核验。
- **核验状态建议：** `单一来源`。
- **来源明确事实：** 官方要求不要在 YouTube AI Features 中提交机密或个人信息；Google 可能收集提示、输出、上传的图像/视频、相关内容与反馈，用于提供、改进和开发产品及机器学习技术。AI Feature Activity 默认开启；与账号关联的提示、输出和相关内容最长保存 18 个月，未关联账号的最长 3 年。部分提示和输出可能由人工审核员（含第三方）阅读、标注和处理；删除活动后相关数据仍可随账号保存最长 30 天。页面还说明生成内容可能带签名 C2PA manifest，外部平台可读取该元数据。
- **分析推断：** 内置 AI 入口不应直接接收未脱敏客户素材、未公开剧本或个人敏感素材；“从活动页删除”也不等于即时物理删除。C2PA 可读性是来源透明度能力，不是保密控制。
- **可执行含义：** 在上传/提示前执行素材数据分级和脱敏；记录 AI Feature Activity 设置与删除时间；需要保密的资产改用经过合同、账户和数据处理条款审查的工作流。
- **新颖性：** 全库未检出 YouTube AI 功能提示/输出留存、人工审核或机密信息禁入；与已有 AI 标签、肖像主张和 C2PA 自动披露条目不同。

### 待核验

1. **TikTok AI spam 检测。** [2026-07-13 官方公告](https://newsroom.tiktok.com/helping-people-spot-and-understand-ai-generated-content-on-tiktok-sg?lang=en-SG)披露检测仍处测试期。缺失证据：最终政策文本、上线市场、处置与申诉阈值；保留为风险观察，不写“AI 内容会被降权”。
2. **快手/抖音发布接口与 AI 标识回执。** 开放平台文档能核验发布、审核和状态，但未发现当前公开接口返回六类标签或隐式标识检测结果。缺失证据：平台 API 字段、端内回执和跨版本一致性。

### 重复 / 淘汰

1. [《人工智能生成合成内容标识办法》](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)（2025-03-14，2025-09-01 施行）：显式/隐式标识及传播平台义务已有多篇 atoms，重复。
2. [中央网信办短视频六类标签](https://www.cac.gov.cn/2026-05/12/c_1780328273038196.htm)（2026-05-12）：必选发布标签和补标机制已有 2026-10-22～23 atoms。
3. [无 AI 标识虚假不实信息治理通报](https://www.cac.gov.cn/2026-02/12/c_1772636033171974.htm)（2026-02-12）：虚构事故、公众人物仿冒等已由 2026-11-11 合规 atom 晋升。
4. [广电总局 2026-11-06 微短剧专项治理](https://www.nrta.gov.cn/art/2026/11/6/art_114_74410.html)：盗脸偷声、换名重播和同质化治理已由 2026-11-09 atom 晋升。
5. [最高法 AI 纠纷意见答记者问](https://enipc.court.gov.cn/zh-cn/news/view-6032.html)与[网络法治典型案例](https://www.court.gov.cn/zixun/xiangqing/512041.html)：换脸、拟声、肖像和合理审核义务已由 2026-10-27、11-09 atoms 覆盖。
6. [YouTube GenAI 披露帮助](https://support.google.com/youtube/answer/14328491?hl=en-GB)：写实内容披露、片上/描述标签和自动标签已有历史 atoms，重复。
7. [欧盟 AI 法案第 50 条 FAQ](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)：机器标记与面向观众披露、艺术作品例外及 2026-08-02 起适用已由 2026-10-28、10-30、11-10 atoms 覆盖。
8. 爬虫候选搜狐“明星 AI 换脸事件”稿：标题和摘要为耸动叙事，未给出可核验裁判文书、案号、平台公告或当事人声明；与最高法已核验规则相比证据更弱，淘汰为事实来源。若后续获得法院文书和平台处置公告，可作为案例重新核验。

## 给主扫描账本的结论

- 三维都完成了中文与海外检索，候选数量达到发现目标；高质量中国一手来源占多数，但大部分政策、平台审核和精品化主题已在 10 月下旬至 11 月 11 日晋升。
- 建议各晋升 1 个不重复的普通 atom：`platforms` 的 YouTube Reimagine 自动回链、`types` 的 audio-first 转 Shorts、`compliance` 的 YouTube AI 功能数据分级与留存。
- 三个建议均为单一官方来源，不应扩写未公布的推荐权重、版权许可效果、生成质量或地区范围。
- 爬虫两条候选均未通过：搜狐稿缺原始案件证据，A2E 聚合稿缺一手产品与权利文档。它们应在最终 `SCAN.md` 明确记录为淘汰，不能静默消失。
