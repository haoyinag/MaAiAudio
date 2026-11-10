# 2026-11-09 海外一手来源研究记录

> 采集日期：2026-11-09（Asia/Shanghai）  
> 范围：仅海外官方平台、模型厂商与监管来源；候选用于主流程二次取舍，不代表已写入知识库。  
> 去重范围：`docs/ai-short-video` 下现有正式版、历史 inbox、DIGEST 与原子条目。

## 扫描概况

爬虫候选的海外部分只有 1 条 Roblox 股票新闻，和 AI 短视频增长无直接关系，不能作为事实来源。本轮不沿用它的主题边界，而是按六维重新检索官方来源。

| 维度 | 海外初筛候选数 | 建议晋升 | 待核验/并入既有条目 | 淘汰 |
| --- | ---: | ---: | ---: | ---: |
| `general` | 4 | 1 | 0 | 3 |
| `platforms` | 6 | 0 | 1 | 5 |
| `types` | 4 | 1 | 1 | 2 |
| `pipeline` | 7 | 2 | 1 | 4 |
| `growth` | 5 | 1 | 1 | 3 |
| `compliance` | 10 | 1 | 1 | 8 |

主要检索词（均优先限定官方域名）：

- `general`：`AI video prompting camera consistency official 2026`、`video A/B testing cuts audience attention official`、`Runway Gen-4.5 prompting official`
- `platforms`：`YouTube Shorts AI creation update official 2026`、`TikTok micro-series platform official 2026`、`Gemini Omni Flash Shorts reference images official`
- `types`：`creator-led vertical micro-series official`、`branded episodic social-first series TikTok`、`microdrama docuseries game show creator series`
- `pipeline`：`Firefly video timeline quick cut official 2026`、`Sora discontinuation export official`、`Veo reference images workflow official`
- `growth`：`qualified Shorts views YPP official 2026`、`creator rewards original play duration search value official`、`original Reels monetization official 2026`
- `compliance`：`AI-generated content label C2PA policy official 2026`、`YouTube likeness claim AI voice face official`、`EU AI Act Article 50 code practice official 2026`

## `general`

### 建议晋升：用最多三个成片剪辑版本做留存 A/B 测试

- **来源：** YouTube 官方博客，2026-09-23  
  https://blog.youtube/news-and-events/innovation-youtube-era-made-on-viewers-creators/
- **来源等级 / 状态：** 平台官方；`单一来源`
- **来源明确事实：** YouTube 宣布 Studio 的 Video A/B testing 可让创作者提交最多三个不同剪辑版本，比较哪一个更能保持观众注意力。该页同时把它与早期草稿建议、缩略图生成分开列为 Studio 能力。
- **可执行含义：** 同一短视频实验应保持选题、标题和发布条件尽量一致，只改剪辑节奏或镜头版本；将“哪个版本留住注意力”作为版本选择证据，而不是凭主观挑片。官方页没有公开统计口径、样本分流方式或显著性判定，原子中不可补写胜出阈值。
- **新颖性 / 关系：** 未发现现有条目记录“最多三个剪辑版本”的平台内 A/B 测试。它是通用迭代方法，不等于 YouTube 推荐算法承诺，也不能外推至其他平台。
- **建议：** `promoted`，主维度只设 `general`。

### 淘汰

- Runway Gen-4.5 的“从最小运动描述逐步加细”、文本生视频适合 B-roll/背景板：已由 `inbox/2026-11-03/通用技巧-Runway文本生视频从最小运动描述逐步加细.md` 覆盖。
- Runway 静态镜头应同时描述画面内运动、用自然语言强化相机不动：属于既有 Runway 提示词条目的模型细节增补，当前不足以另立新主题。
- Veo 3 提示词的镜头、风格、光线、声音分层：是长期官方基础指南，和既有结构化提示词条目高度重叠，无当日增量。

## `platforms`

### 待并入/待核验：YouTube Shorts 的 Gemini Omni Flash 生成入口

- **来源：** TeamYouTube 官方社区帖，2026-06-25 更新  
  https://support.google.com/youtube/thread/433730507
- **来源等级 / 状态：** 平台官方；`单一来源`
- **来源明确事实：** YouTube 称 Gemini Omni Flash 已加入 Shorts 与 YouTube Create 的 Create Video；最长可生成 10 秒视频，可上传最多 3 张参考图，并建议在需要生成音频时给出明确指令。Shorts 入口限部分市场的 Android/iOS 且设备语言为英语；YouTube Create 应用的入口可使用任意语言。
- **缺失证据：** 页面没有列出完整国家清单、账号灰度比例、生成配额和费用；也没有证明该入口会提高分发。
- **新颖性 / 关系：** `inbox/2026-10-27/平台技巧-YouTube内置AI短片自动披露与地区边界.md` 已覆盖“最长 10 秒、参考图、地区/语言边界和自动披露”。本次只有“最多 3 张参考图”和 Gemini Omni Flash 型号是小幅增量。
- **建议：** 不另建原子，记作 `待核验/可在未来更新当前能力清单`；若主流程需要严格一日一主题，则以重复项淘汰。

### 淘汰

- YouTube 把 Shorts 组织为 seasons/episodes：已由 `inbox/2026-10-23/类型技巧-YouTube-Shorts-Series季集化微短剧.md` 覆盖。
- YouTube 内置 AI 自动披露：已由 2026-10-27 平台条目覆盖。
- TikTok 与 MADE BY US / PineDrama 的合作：已由 `inbox/2026-10-27/类型技巧-TikTok创作者主导竖屏微系列.md` 覆盖。
- Facebook 原创内容优先分发：已由 `inbox/2026-10-22/增长变现-Facebook-Reels原创性门槛.md` 覆盖。
- 爬虫的 Roblox 股票新闻：主题无关，`rejected: noisy/off-topic`。

## `types`

### 建议晋升：品牌短视频从一次植入转向创作者主导的连载格式

- **来源：** TikTok Newsroom（澳大利亚/新西兰），2026-09-14  
  https://newsroom.tiktok.com/tiktok-and-amplify-launch-new-creator-led-content-series-for-brands?lang=en-AU
- **来源等级 / 状态：** 平台官方；`单一来源`
- **来源明确事实：** TikTok 与 Amplify 推出 The Next Episode，覆盖微短剧、访谈、游戏节目、纪录系列和真人秀；列出两种品牌结构：品牌进入创作者的连载内容（Creator Content Series），或以品牌为中心制作创作者主导的 Brand Content Series。符合条件的品牌可把平台制作支持与媒体投入结合。
- **可执行含义：** 类型设计阶段应先明确“创作者世界观中嵌入品牌”还是“品牌作为系列主体”，再确定微短剧/访谈/真人秀等载体；不要把单条植入简单拉长成连续剧。
- **边界：** 适用于 TikTok 澳大利亚/新西兰公布的商业项目；“长期互动”“商业影响”是平台的项目主张，页面没有给出项目级留存、转化或 ROI，不应写成已验证效果。
- **新颖性 / 关系：** 与 2026-10-27 的“创作者主导竖屏微系列”同属连载趋势，但新增品牌参与的两种结构和五类可选节目形态，主题足够独立。
- **建议：** `promoted`，主维度只设 `types`。

### 待核验

- 同一来源声称连载能建立“sustained engagement”并创造可规模化机会；缺少第三方数据和具体指标，保留为项目假设，不晋升为增长事实。

### 淘汰

- TikTok/MADE BY US 的 `Player`、`The Knock` 及 `Screen Time`：2026-10-27 已晋升，平台自报 5.8 亿观看不能证明类型因果或项目 ROI。
- TikTok/HOORAE 的免费广告支持微系列：发布日期较早，且已被后续 MADE BY US 条目吸收其“creator-led、built for feed”结论。

## `pipeline`

### 建议晋升一：Firefly Quick Cut 先按对白/纯视觉分流，再生成人工可编辑初剪

- **来源：** Adobe Firefly Help，页面更新于 2026-10-28  
  https://helpx.adobe.com/firefly/web/firefly-video-editor/create-quick-cut/create-video-quick-cut.html
- **来源等级 / 状态：** 模型/工具厂商官方；`已核验`
- **来源明确事实：** Firefly Timeline（beta）的 Quick Cut 可把上传的视频、图像和音频组织成初剪；先选择 `Dialogue-driven` 或 `Visual-only`，再选择当前项目、当前时间线或选中素材。它支持 9:16、3:4、1:1 等竖屏/社交比例及 30 秒至 15 分钟等时长。对白型可选生成补充 B-roll，纯视觉型不支持该选项；结果仍可调整转录、片段时长、转场和效果。
- **可执行含义：** 入库素材先按“对白驱动/视觉驱动”标记，限制 Quick Cut 的素材范围，生成后把它当 rough cut 而非成片；对白型才规划自动 B-roll，并保留人工复核节奏、事实与画面对应关系。
- **新颖性 / 关系：** `inbox/2026-10-22/制作管线-Firefly项目资产与时间线闭环.md` 记录项目资产与时间线，本条新增 2026-10-28 的 Quick Cut 分流、素材范围和 B-roll 边界，可独立成原子。
- **建议：** `promoted`，主维度 `pipeline`。

### 建议晋升二：Sora 停用后立即导出资产并迁出生产依赖

- **来源：** OpenAI Help Center，页面于采集前 3 天更新  
  https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
- **来源等级 / 状态：** 模型厂商官方；`已核验`
- **来源明确事实：** Sora Web 与 App 已于 2026-04-26 停用，Sora API 已于 2026-09-24 停用。用户仍可通过 `sora.chatgpt.com/sunset` 请求导出；官方称最终导出窗口结束后会永久删除与 Sora 使用相关的数据，并建议尽快导出。
- **可执行含义：** 停止把 Sora URL、项目历史或 API 当作生产依赖；立即导出原视频、提示词旁证和项目清单，在替代模型上重跑验收样本。来源没有承诺最终导出窗口日期，也没有指定替代视频模型，不得补写迁移目的地。
- **新颖性 / 关系：** 未发现现有 Sora 停用条目；与 2026-11-03 的 Gemini 视频端点迁移属于同类“停服前迁移”风险，但对象、截止日期和处置入口不同。
- **建议：** `promoted`，主维度 `pipeline`；时效极高。

### 待核验/不单立

- Adobe 2026-10-28 的 Firefly Video 可直接从时间线 playhead 取首/尾帧、用同 seed 生成相似片段：官方事实可靠，但与 2026-10-22 Firefly 时间线条目重叠较大；可作为 Quick Cut 原子的关联资料，不建议另建第三条。

### 淘汰

- Veo 3.1 的 Ingredients、首尾帧、延长场景和对象插入：2025 年能力，现有条目已多次覆盖参考资产与首尾帧工作流。
- Runway Gen-4.5 基础规格和提示词指南：已由 2026-11-03 原子覆盖。
- Adobe 生成 B-roll 作为 Premiere 占位符：官方只给用途建议，没有短视频成效证据，且可并入 Firefly 管线条目。
- 第三方“最佳 AI 视频工作流”聚合页：来源等级低，未采用。

## `growth`

### 建议晋升：YouTube YPP 的 Shorts 资格只看公开短片的 engaged views，循环不计

- **来源：** YouTube 官方博客 / Creator Liaison Rene Ritchie，2026-08-12  
  https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/
- **来源等级 / 状态：** 平台官方；`已核验`
- **来源明确事实：** YPP 的 qualified Shorts views 必须来自公开 Shorts 且属于 engaged views；engaged view 指观众越过开头数秒继续观看，不包含循环。私密、非公开、已删除、作为广告观看、长视频观看以及 Shorts feed 中的图片帖均不计入该门槛。创作者可在 YouTube Analytics 查看每条视频的 engaged views。
- **可执行含义：** 增长台账应把展示/播放、engaged views、循环与广告观看拆开；评估 YPP 距离时只使用 Analytics 中符合口径的 engaged views，不能拿总播放量或循环播放推算资格。
- **新颖性 / 关系：** 现有 2026-10-23/11-03 条目涉及 YPP 条款与邀请奖金，但未记录 2026-08-12 的 qualified Shorts views 排除项和“不含循环”口径。
- **建议：** `promoted`，主维度 `growth`；平台口径易变，需标注核验日期。

### 待核验

- TikTok/Amplify 称品牌连载可形成长期互动和可规模化机会；没有公开样本、转化或 ROI，不能晋升为增长因果。

### 淘汰

- TikTok Creator Rewards 的 originality/play duration/search value/engagement 四指标：2024 年旧公告，无 2026 当日增量。
- Meta 原创 Reels 获得更多触达与变现机会：2026-10-22 已有完整原子。
- Roblox 股票新闻：与 AI 短视频增长无关。

## `compliance`

### 建议晋升：YouTube likeness claim 与版权 claim 分流，前者可直接阻断整条视频

- **来源：** YouTube Help，页面未标发布日期，采集于 2026-11-09  
  https://support.google.com/youtube/answer/17133929
- **辅助来源：** YouTube Help（Likeness detection）  
  https://support.google.com/youtube/answer/16440338
- **来源等级 / 状态：** 平台官方帮助文档；`交叉验证`
- **来源明确事实：** 当视频中的 AI 修改/生成内容匹配某人的脸或声音时，可能收到 likeness claim。该主张不同于版权 claim，可完全阻止视频被观看；它作用于视频而非频道/账号。一条视频含多个人的肖像时可能收到多个主张。检测工具目前为实验性、需符合资格并由本人/授权代表处理；未检出的内容仍可走隐私投诉流程。
- **可执行含义：** 发布台账将肖像/声音授权与版权授权分成两栏；每个出镜或拟声对象逐项留存授权。收到 likeness claim 时不要按 Content ID 争议处理，先核对人物、授权范围和 AI 改动事实；披露“由 AI 生成”不替代肖像授权。
- **边界：** 官方帮助页没有承诺检测覆盖率；“可阻断视频”不等于每个主张都会成立。音频检测仍在逐步推出，不能写成所有账号已全面可用。
- **新颖性 / 关系：** 既有条目记录中国肖像声音授权、YouTube AI 披露和自动标签；本条新增 YouTube 的 likeness claim 后果、多人多主张以及与版权 claim 的流程分流。
- **建议：** `promoted`，主维度 `compliance`。

### 待核验：TikTok 测试识别 AI 垃圾账号

- **来源：** TikTok Newsroom，2026-07-13  
  https://newsroom.tiktok.com/helping-people-spot-and-understand-ai-generated-content-on-tiktok-sg?lang=en-SG
- **来源明确事实：** TikTok 宣布正在测试改进的检测系统，目标是识别专门发布 AI-generated spam、挤压原创创作者的账号，并加入 C2PA Steering Committee。
- **缺失证据：** 未公布 spam 判定标准、测试国家、处置级别、申诉流程、准确率或正式上线时间。
- **建议：** `待核验`，只留扫描账本；不能据此声称平台已降权所有批量 AI 视频。

### 淘汰

- 欧盟 Article 50 自 2026-08-02 适用、机器可读标记与首次接触显式披露分工：已由 `inbox/2026-10-28/合规与风控-欧盟AI法案第50条区分机器标记与观众披露.md` 完整覆盖。
- YouTube 更显眼的 AI 标签、Shorts 画面叠加、自动检测与 C2PA 永久标签：历史 v0 中已有两条，且 2026-10-27 已覆盖平台自动披露边界。
- TikTok 的创作者标签、C2PA 自动标签、标签不影响分发：长期规则，现有历史合规条目已覆盖，无当日新增政策。
- 美国版权局 Digital Replicas 报告：2024 年旧材料，能说明权利风险但不是当前平台处置更新。

## 给主流程的取舍建议

建议优先写入 6 个海外原子候选：

1. `general`：YouTube 最多三个剪辑版本的 Video A/B testing。
2. `types`：TikTok/Amplify 品牌连载的两种结构与节目类型。
3. `pipeline`：Firefly Quick Cut 的对白/纯视觉分流与人工初剪。
4. `pipeline`：Sora 停用、导出与迁移。
5. `growth`：YPP qualified Shorts views 的 engaged-view 口径。
6. `compliance`：YouTube likeness claim 与版权 claim 分流。

`platforms` 本轮没有足够新颖且不重复的海外原子；应在主 `SCAN.md` 明确写出缺口，而不是把 Gemini Omni Flash 的小幅规格增量包装成新主题。若国内平台来源也未补足，该维度应在下一次采集扩大官方产品更新、创作者后台公告和地区灰度帮助页检索。
