# SCAN 2026-11-09

> 模式：每日采集；时区：Asia/Shanghai。严格按“六维广泛发现 → 原始来源核验 → 全库去重 → 分层写入”执行。爬虫候选只作发现线索，不作事实。

## 覆盖总览

- 爬虫起点：`general=0 / platforms=4 / types=4 / pipeline=1 / growth=1 / compliance=0`；地区为国内 4、海外 1。`general`、`compliance` 完全缺席，`pipeline`、`growth` 严重不足，唯一海外条目为与 AI 短视频无关的 Roblox 股票新闻。
- 优先补扫：2026-11-03 的 `platforms`、`compliance` 均无晋升，本次先扩大官方帮助中心、监管通报、平台产品更新和执法案例检索；两维均取得可发布增量，未形成连续两次运行缺席。
- 广泛发现：六维分别使用中文与海外词检索；国内优先网信、广电、平台开放文档、模型 / 云厂商，海外优先平台帮助中心、官方博客、模型与工具厂商文档。
- 去重后纳入账本的发现线索 61 条，国内约 40、海外约 21（约 66:34）；每维均达到至少 8 条发现目标。海外初筛曾有 36 个跨维命中，合并同页、同主题和既有条目后计为 21 个独立线索。
- 最终晋升 12 个普通 atom：`general` 2、`platforms` 1、`types` 2、`pipeline` 3、`growth` 2、`compliance` 2。发布结果由证据质量和新颖性决定，不用地区配额淘汰可靠增量。

| 维度 | 去重后候选数 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: |
| `general` | 10 | 2 | 2 | 6 |
| `platforms` | 9 | 1 | 2 | 6 |
| `types` | 9 | 2 | 2 | 5 |
| `pipeline` | 12 | 3 | 3 | 6 |
| `growth` | 10 | 2 | 3 | 5 |
| `compliance` | 11 | 2 | 3 | 6 |

## general｜通用技巧

### 搜索尝试

- 中文：`Seedance 2.5 提示词 官方 多宫格 分镜 多关键帧`、`即梦 视频 角色一致性 运镜 官方 2026`、`AI 视频 提示词 分镜 角色一致性 官方`。
- 海外：`official AI video prompting camera consistency 2026`、`video A/B testing cuts audience attention official`、`Runway Gen-4.5 prompting official`。

### 已晋升

- [分镜宫格用于讲清叙事，严格镜头对齐改用多关键帧](./通用技巧-分镜宫格与多关键帧分工.md)：Seedance 2.5 当前官方指南明确宫格不会严格对齐，严格控制应转多关键帧。
- [用最多三个剪辑版本做观众注意力 A/B 测试](./通用技巧-最多三个剪辑版本做留存AB测试.md)：YouTube Studio 提供最多三个剪辑版本的注意力测试入口，但未公开显著性口径。

### 待核验

- Seedance 2.5 的时间戳密度建议可靠，但缺同素材“稀疏 / 过密”对照和可复现失败率；先并入分镜 atom 的使用边界。
- 即梦 OmniHuman 1.5 对长音频、一致性和极端角度给出厂商限制；与既有数字人口播 atom 重叠，待获得真实失败样本后再决定是否升级。

### 淘汰 / 合并

- Runway 最小运动描述、Seedance 素材职责、万相结构化提示词均已有 atom，合并时效复核。
- 火山引擎营销型教程、聚合工具榜单和“免费专业生成器”内容缺可复现实验或产品边界，淘汰。
- “一键生成必然提高留存”“更多参考素材必然更稳定”等主张无一手对照，不采用。

### 缺口

- 仍缺中文跨模型、同 brief、同预算的公开 A/B 数据；厂商边界不外推为通用成功率。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 快手 B站 小红书 AI 视频 创作者 官方 公告 2026`、`平台 AI 微短剧 播放器 创作者规则`。
- 海外：`YouTube Shorts AI creation update official 2026`、`TikTok AI generated content label distribution official`、`Instagram Reels AI creator update official`。

### 已晋升

- [TikTok 的 AI 标签本身不等于限流，但不能替代内容合规](./平台技巧-TikTok-AI标签不等于限流.md)：当前官方帮助页可访问并明确标签开关本身不影响分发，禁止内容仍不因标注而放行。

### 待核验

- YouTube Shorts 的 Gemini Omni Flash 入口新增最多 3 张参考图等小规格，但与既有内置 AI atom 高度重叠；缺完整国家、配额和账号灰度清单。
- 国内抖音、B站、小红书当前 AI 声明 UI 与自动识别后的修改权限仍缺无需登录的一手帮助正文。

### 淘汰 / 合并

- YouTube Shorts Series、内置 AI 自动披露、原创内容优先和快手 AI 微短剧播放器均已有 atom。
- 爬虫的 4 条国内平台 / 类型候选实际都围绕同一轮监管治理，不能用媒体稿推导平台推荐、限流或收益规则。
- 非官方红果站、平台活动二手转述和无版本号的创作者截图不可追溯，淘汰。

### 缺口

- 国内平台公开推荐机制仍不足；不能从治理公告反推 AI 内容加权、降权或收益变化。

## types｜类型技巧

### 搜索尝试

- 中文：`国家广电总局 AI 微短剧 漫剧 精品 2026`、`微短剧 类型 创作 官方 现实题材 漫剧`。
- 海外：`official vertical microdrama storytelling series 2026`、`creator-led branded episodic social-first series TikTok`、`YouTube microdrama long tail localization official`。

### 已晋升

- [YouTube 微短剧按长尾发现与本地化维护首集](./类型技巧-YouTube微短剧按长尾与本地化运营.md)：平台自报样本显示部分观看和点击发生在 30 天后，支持把首集作为长期入口维护，但不外推单剧结果。
- [TikTok 品牌连载先选“进入创作者世界”或“品牌主导系列”](./类型技巧-TikTok品牌连载先选两种参与结构.md)：澳新官方项目给出两种品牌参与结构与五类连载形态。

### 待核验

- 广电总局 2026 精品创作大会称 AI 已进入视听全链路，但宏观表述缺可复现的类型方法，留作趋势背景。
- YouTube 评论驱动人物决定和 TikTok“长期互动”均为平台案例总结，缺项目级留存、转化与创作成本。

### 淘汰 / 合并

- YouTube 6.5 亿播放、Shorts Series 季集结构及 TikTok 创作者主导微系列已有 atom，重复数据不再晋升。
- 候选媒体稿的“43 万部”“九成以上”等数字未在其页面完成一手核验；仅采用可直接打开的广电官方表述，不把口径不明数字写入 atom。
- 非官方“爆款题材”“固定集长”和营销模板缺对照数据，淘汰。

### 缺口

- 官方案例仍偏平台趋势和项目结构，缺同题材、同预算下的单集节奏与跨集续看对照。

## pipeline｜制作管线

### 搜索尝试

- 中文：`火山剧创 短剧创作 分镜 批量生成 官方`、`Seedance 视频工作流 分镜 回溯 官方`、`AI 短剧 制作 算子 剪辑 官方 2026`。
- 海外：`Firefly video timeline quick cut official 2026`、`Sora discontinuation export official`、`official AI video workflow storyboard editing migration`。

### 已晋升

- [批量生成前逐镜确认，并保留候选与提示词回溯](./制作管线-批量生成前逐镜确认并保留回溯.md)：火山剧创文档把分镜确认、候选选择、提示词回溯与最终导出串成可验收流程。
- [Firefly Quick Cut 先按对白驱动与纯视觉分流](./制作管线-Firefly-Quick-Cut按对白与视觉分流.md)：当前 beta 明确两类粗剪路由、素材范围和 B-roll 边界。
- [Sora 停用后立即导出资产并迁出生产依赖](./制作管线-Sora停用后立即导出并迁移.md)：官方确认 Web / App 与 API 均已停用，并提示尽快导出以避免最终删除。

### 待核验

- 万相 3.0 多模态素材顺序引用与现有万相 atom 重叠；需跨版本迁移实测。
- Seedance 2.5 视频编辑、续写和无缝转场有官方示例，缺项目级错误率、耗时与音量变化对照。
- Adobe 从时间线 playhead 取首尾帧及同 seed 变体与既有 Firefly 时间线条目相近，待形成失败恢复方法再单立。

### 淘汰 / 合并

- Gemini 端点迁移、结构化资产表、可灵多镜故事板和 Firefly 项目闭环已有 atom。
- 第三方 Pika、CapCut 榜单、SOLO 宣传教程和“端到端一键成片”缺稳定产品边界或独立验收，淘汰。
- 爬虫管线候选实为治理媒体稿，未提供制作流程证据，不按 `pipeline` 采用。

### 缺口

- Sora 导出未承诺包含完整提示词、参数和项目关系；迁移质量仍需项目自测。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 短剧 投流 素材 官方 算子 2026`、`抖音 短剧 推广任务 创作者 官方`、`快手 短剧 AI 营销 财报`。
- 海外：`qualified Shorts views YPP official 2026`、`creator rewards original Reels official`、`AI short video monetization official`。

### 已晋升

- [投流素材的批量生成能力与真实效果验证分开记账](./增长变现-投流素材批量生成与效果验证分账.md)：LAS 可批量输出投流变体，但官方未提供转化或 ROI，必须与真实投放分账。
- [YouTube YPP 门槛只按公开 Shorts 的合格参与观看计算](./增长变现-YouTube-YPP只按合格Shorts观看计门槛.md)：官方明确 engaged views 不含循环，并排除非公开、广告等观看。

### 待核验

- 候选《持械入宋》宣称百万投入、千万回报和大规模播放；缺制作方财务材料、平台后台、收入构成和净回款证明，保留为 `待核验`。
- TikTok / Amplify 所称长期互动与商业影响没有项目级转化、抽成和 ROI。
- 快手二季度财报的短剧供给与营销消耗增长已入库；仍缺创作者侧成本、回款周期和净收入。

### 淘汰 / 合并

- YouTube 奖金邀请制、YPP 2027 条款、Facebook 原创 Reels 和抖音短剧推广任务均已有 atom。
- 爬虫 Roblox 股票新闻与 AI 短视频增长无关，判定 `rejected: noisy/off-topic`。
- 课程、工具商和二手榜单的“降本增效 / 高 ROI”无可复核对照，淘汰。

### 缺口

- 国内仍缺可公开复核的单部 AI 短剧成本、付费漏斗、回款周期和净收入；工具供给能力不等于商业回报。

## compliance｜合规与风控

### 搜索尝试

- 中文：`网信办 AI 仿冒 公众人物 2026 11`、`广电总局 微短剧 低俗化 同质化 专项治理 AI 盗脸 偷声`、`AI生成 视频 标识 版权 肖像 声音 官方`。
- 海外：`YouTube likeness claim AI face voice official`、`synthetic media AI video policy 2026 official`、`EU AI Act Article 50 code practice official 2026`。

### 已晋升

- [换名重播与公众人物仿冒进入当前专项治理范围](./合规与风控-换名重播与公众人物仿冒专项治理.md)：广电与网信 11 月 6 日一手材料共同把正片、宣推、引流、换名重播和公众人物仿冒纳入当前治理 / 处置范围。
- [YouTube 肖像主张与版权主张分流，AI 标识不能替代许可](./合规与风控-YouTube肖像主张与版权主张分流.md)：平台官方明确 likeness claim 可阻断整条视频，且披露 AI 不会免除人物许可。

### 待核验

- TikTok 正在测试识别 AI spam 账号，但缺测试地区、判定阈值、处置级别、申诉流程和正式上线时间。
- 候选媒体稿提到“高频 AI 脸”“换皮”等治理解读；已有广电原文支撑的部分被官方 atom 取代，媒体独有扩展缺原始文件。
- 国内六选一标签处理多属性内容的具体平台 UI 仍无统一公开说明。

### 淘汰 / 合并

- 中国短视频六类标签、AI 微短剧逐集标识、最高法换脸拟声责任和欧盟 AI 法案第 50 条均已有 atom。
- Sohu、MSN、大众网候选不可访问或为同一广电治理的二手转述，采用官方原文后淘汰重复来源。
- 仅靠“已标注 AI”推导肖像授权、版权许可或平台放行，均与当前官方规则冲突，判定不成立。

### 缺口

- 公众人物“轻微相似”、戏仿和跨境发布没有统一安全比例；具体项目仍需按地区、平台和授权文本复核。

## 爬虫候选逐条处置

1. Sohu《43 万部微短剧，AI 剧占比超九成……》：原页不可访问，核心治理事实已回到广电总局 2026-11-06 原文；`rejected: inaccessible + superseded by primary source`。
2. 大众网《作品与传播同步治理……》：原页不可访问，属于同一治理事件评论；`rejected: duplicate secondary commentary`。
3. MSN“盗脸偷声、换皮”报道：原页不可访问，官方治理原文已核验；`rejected: inaccessible duplicate`。
4. 腾讯新闻《持械入宋》：成本、播放和回报缺制作方财务材料、平台后台和收入拆分；`pending`，精确缺失证据为投入明细、总 / 净回款、渠道分成、统计窗口和可审计播放口径。
5. Globe and Mail Roblox 股票稿：与 AI 短视频无直接关系；`rejected: noisy/off-topic`。

## 去重与写入边界

- 已对 `docs/ai-short-video` 既有正式版、历史 inbox、DIGEST、SCAN 和 atom 标题 / 核心来源做语义去重。
- 未创建 `vYYYY.MM.DD`，未修改历史正式版本，未执行 Git / GitHub 命令。
- 海外专项发现的完整中间记录保存在 [OVERSEAS-RESEARCH.md](./OVERSEAS-RESEARCH.md)；它是研究账本，不替代本 `SCAN.md` 的最终分层结果。

