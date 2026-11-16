# SCAN 2026-11-16

> 模式：每日采集；时区：Asia/Shanghai。执行顺序为“六维广泛发现 → 打开一手来源核验 → 全库去重 → 分层写入”。爬虫候选只作线索，不作事实。

## 覆盖总览

- 爬虫起点：`general=0 / platforms=2 / types=1 / pipeline=0 / growth=0 / compliance=1`；地区为国内 1、海外 1，且只有 2 条实际候选。
- 六维均低于每维至少 8 条的发现目标，`general`、`pipeline`、`growth` 完全缺席；因此六维均使用中文与海外词补扫，国内优先监管、平台、开放平台和模型厂商当前文档。
- 补扫并全库去重后：66 条线索，国内 42、海外 24（约 64:36）；六维均达到至少 8 条发现线索。
- 最终晋升 6 个普通 atom：六维各 1 个；发布集为国内 2、海外 4。发布比例由可靠增量决定，没有为贴近发现池比例采用较弱线索。
- 最近一个有完整六维账本的采集日 2026-11-11 六维均有晋升；本日不存在“连续两次采集无晋升”而必须优先扩词的维度。爬虫空白维度仍已优先扩展来源类型。

| 维度 | 去重后候选数 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 12 | 8 / 4 | 1 | 3 | 8 |
| platforms | 10 | 6 / 4 | 1 | 3 | 6 |
| types | 10 | 7 / 3 | 1 | 3 | 6 |
| pipeline | 12 | 7 / 5 | 1 | 3 | 8 |
| growth | 11 | 7 / 4 | 1 | 3 | 7 |
| compliance | 11 | 7 / 4 | 1 | 2 | 8 |
| **合计** | **66** | **42 / 24** | **6** | **17** | **43** |

## general｜通用技巧

### 搜索尝试

- 中文：`site:volcengine.com/docs 视频生成 提示词 一致性 官方 2026 AI 视频`、`site:help.aliyun.com 万相 视频生成 提示词 官方 2026`、`即梦 视频 提示词 多主体 动作 官方`。
- 海外：`site:help.runwayml.com video prompting guide official consistency 2026`、`site:helpx.adobe.com firefly generate video prompt guide official 2026`。

### 已晋升

- [万相 3.0 对台词与背景音乐使用显式空约束](./通用技巧-万相3对台词与背景音乐使用显式空约束.md)：区分“模型自选 / 明确指定 / 明确禁止”，不再用空白同时表达三种音频意图。

### 待核验

1. 万相 3.0 提供提示词优化 Skill，但缺 Skill 版本、更新机制、许可范围及可复现前后对照，暂不写成通用优化方法。
2. Seedance 当前 API 建议中文提示不超过 500 字、英文不超过 1,000 词并称过长会分散信息；缺同一 brief 的长度分组成功率和跨模型证据，不能外推为统一上限。
3. 即梦当前指南给出连续动作与多人各自动作模板，但与既有动作拆分条目接近；缺独立失败样本与足以单独成条的增量。

### 淘汰 / 合并

- 万相文生 / 图生提示字段裁剪已在 2026-10-22 晋升；万相 3.0 原生音视频边界已在 2026-10-30 晋升，重复部分合并。
- Runway Gen-4 / Gen-4.5 的直接物理动作、最小描述和 B-roll 适用边界已在 2026-11-03 晋升。
- Adobe Enhance Prompt 与基础视频提示指南没有公开变换规则或独立效果证据，且与现有结构化提示条目重叠。
- Kickart 七字段结构已在 2026-11-11 晋升；火山“爆款视频智造官”教程基于旧模型入口且偏示例搭建，不作为当前通用技巧。
- 未采用模型宣传页中的“质量”“一致性”等形容词作为可验证效果结论。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 视频 发布 审核 人工智能生成 标识 官方`、`快手 短剧 AIGC 创作者 规则 官方`、`快手开放平台 视频 发布 审核 状态`、`国内短视频 AI 发布 标签 审核`。
- 海外：`YouTube Shorts AI generated content official`、`YouTube Shorts Reimagine AI remix official 2026`、`TikTok AI-generated content creator official`、`YouTube Shorts AI creation update official 2026`。

### 已晋升

- [YouTube Reimagine 用自动回链保留二创来源](./平台技巧-YouTube-Reimagine用自动回链保留二创来源.md)：平台原生二创入口会回链原作，但回链不等于获得全部权利。

### 待核验

1. 快手开放平台发布接口返回不代表视频已同步到用户页，需按 `photo_id` 再查；缺 AI 标识入参、审核结果字段和端内展示一致性的当前官方证据。
2. YouTube `Make me move` 要求单人全身照并提示使用他人照片须获许可；缺完整国家 / 账号灰度清单、输出长度和相对既有参考图条目的独立增量。
3. TikTok 只宣布测试政治时事、金融和医疗等主题的 AI spam 账号检测；缺正式上线范围、处置阈值和申诉流程，不能推断普通 AI 视频会被限流。

### 淘汰 / 合并

- 抖音第三方发布、审核中可见性和失败状态已由 2026-11-10 平台 atom 覆盖。
- 中国短视频六类必选标签、YouTube 内置 AI 自动披露与地区边界、TikTok AIGC / C2PA 标签均已有条目。
- 爬虫 A2E AI / Yahoo Finance 候选不可访问，且是产品发布型聚合 / 营销稿；缺一手能力文档、模型路由、商用权利和费用条款，淘汰。

## types｜类型技巧

### 搜索尝试

- 中文：`AI 微短剧 漫剧 创作计划 官方 2026`、`广电总局 微短剧 精品 创作 类型 2026`、`国际短视频大赛 创作方向 指南 2026`、`AI 微短剧 培训 AIGC 漫剧 官方`。
- 海外：`YouTube audio-first video to Shorts official`、`YouTube microdrama Shorts Series official 2026`、`TikTok creator-led content series microdrama official 2026`、`vertical micro-series storytelling official`。

### 已晋升

- [YouTube 把音频优先静态视频按转录区间转为 Shorts](./类型技巧-YouTube把音频优先静态视频按转录区间转为Shorts.md)：先逐词锁定语义区间，再选择不可直接回切的视觉样式。

### 待核验

1. 广电总局 2026 国际短视频大赛方向附件提出从具体人物连接全球议题及非遗、文物、文旅等方向；缺赛事主通知、技术 / 时长要求和可复用评审标准，不能当作 AI 方法。
2. 广电总局第三批拟扶持项目附件只有项目、题材和机构列表；缺创作方法、AI 使用范围、成片类型和评审理由。
3. 北京“追光计划”覆盖真人微短剧、AIGC 微短剧和 AI 漫剧并提供孵化 / 平台对接；缺课程正文、可验证方法、结业表现和当前开放资格。

### 淘汰 / 合并

- 精品微短剧秋季点评会和 2026 精品创作大会仍是价值导向与产业统计，相关精品化结论已在 2026-11-10 晋升。
- YouTube Shorts Series 的季 / 集结构和 TikTok 品牌连载参与结构已在 2026-11-09～10 晋升。
- 不从拟扶持名单、播放量或题材分布反推某类 AI 短视频更有效。
- 爬虫搜狐“明星 AI 换脸”同时命中 types，但没有可核验类型方法，且案件事实证据不足，淘汰。

## pipeline｜制作管线

### 搜索尝试

- 中文：`site:docs.volcengine.com 视频 生成 工作流 分镜 质检 API 官方 2026 Seedance`、`site:help.aliyun.com wan3 视频 生成 API 工作流 参考 视频 编辑 2026`、`火山剧创 新功能 分镜 Seedance 2026`。
- 海外：`site:help.runwayml.com workflow storyboard video editor official AI 2026`、`site:helpx.adobe.com firefly quick cut video editor official 2026`、`site:labs.google/fx/tools/flow official video workflow 2026`、`site:developers.google.com veo video generation workflow official 2026`。

### 已晋升

- [Seedance 样片确认后在有效期内转正式视频](./制作管线-Seedance样片确认后在有效期内转正式视频.md)：用 Draft 作为正式生成前的审批门，并记录 14 天任务有效期。

### 待核验

1. 万相 3.0 的首尾帧输入与全模态参考输入互斥，且图片 / 视频 / 音频分别编号；需继续与 2026-10-22、10-30 的入口和参考视频条目逐字段去重后再决定是否成 atom。
2. Adobe Firefly 2026-11 新增 Auto Reframe，可在改比例时持续保持主体入框；缺当前支持格式、批量上限、失败恢复和竖屏复杂遮挡样本。
3. Runway Workflows 提供节点化、分支和可复用管线；缺当前节点版本固定、费用上限、失败重试和导出稳定性说明，且与既有代理 / 时间线工作流部分重叠。

### 淘汰 / 合并

- Google Flow“筛选—精修—放大”、Firefly Quick Cut、Runway Agent 计划审核和 Firefly 项目时间线均已有近期 atom。
- 万相迁移矩阵、CLI 包装、模型清单和 Token Plan 接入是产品 / 调用入口，不单独构成制作方法。
- Runway Multi-Shot、Seedance 2.0 示例页与既有多镜头、故事板和参考素材条目重复。
- Adobe 旧版编辑器概览和 Quick Cut 概览由当前功能页替代；未采用定价页作为稳定流程证据。

## growth｜增长变现

### 搜索尝试

- 中文：`site:creator.douyin.com 官方 创作者 收益 短视频 2026 AI 内容`、`site:open.kuaishou.com 创作者 任务 收益 官方 短视频`、`快手 星火计划 短视频 分成 官方`、`B站 创作激励 官方 短视频 收益 2026`。
- 海外：`site:support.google.com/youtube Shorts monetization original content official 2026`、`site:newsroom.tiktok.com creator rewards monetization official 2026 original content`。

### 已晋升

- [YouTube 2027 分开计算入驻、活跃与 Shorts 月度收益门槛](./增长变现-YouTube-2027分开计算入驻活跃与Shorts月度收益门槛.md)：同一官方 URL 已更新，本条替代 2026-10-23 对未来规则的旧读取。

### 待核验

1. 快手星火计划官方文档列出广告分成、收入分成和线索转化三类任务及结算方式；缺 AI 生成内容资格、当前创作者端准入和跨行业稳定结算口径。
2. TikTok Creator Rewards 公开稿仍强调原创、播放时长、搜索价值与互动，但主要规则稿为 2024 年；缺 2026 当前统一条款、完整地区与账户资格页。
3. YouTube 新 Shorts 激励只说明可能提供 Shopping 奖金、品牌制作积分和文化趋势加成；缺项目上线时间、资格、计费和是否可叠加的细则。

### 淘汰 / 合并

- 快手 2026 AIGC 四项扶持已在 2026-11-11 晋升；西瓜中视频 MVP 缺当前 AI 资格和完整收益公式。
- YouTube 合格观看、Shopping、连续发布奖金和旧 YPP 未来条款已有条目；本日只保留官方页面发生变化的部分。
- 快手小程序新手流量券是活动奖励且有效期易变，不外推为 AI 短视频常态收入。
- Bilibili 旧活动页、平台总体 GMV、营销案例收益和第三方 RPM 估算均不能证明账号级收益，淘汰。

## compliance｜合规与风控

### 搜索尝试

- 中文：`人工智能生成合成内容 标识 视频 官方`、`网信办 无 AI 标识 虚假视频 2026`、`最高法 AI 换脸 声音 肖像 2026 官方`、`广电总局 AI 微短剧 专项治理 2026`。
- 海外：`YouTube AI features privacy data prompts C2PA official`、`YouTube altered synthetic disclosure official 2026`、`EU AI Act Article 50 deepfake transparency official 2026`、`TikTok AIGC C2PA policy official`。

### 已晋升

- [YouTube 内置 AI 功能先做数据分级与脱敏](./合规与风控-YouTube内置AI功能先做数据分级与脱敏.md)：补充提示 / 输出留存、人工审核和机密信息禁入，不把 C2PA 当作保密措施。

### 待核验

1. TikTok 的 AI spam 检测仍处测试期；缺最终政策、上线市场、处置与申诉阈值，只保留为风险观察。
2. 快手 / 抖音开放平台文档能核验发布和审核状态，但未发现当前公开接口返回六类标签或隐式标识检测结果；缺 API 字段、端内回执和跨版本一致性。

### 淘汰 / 合并

- 中国生成合成内容显式 / 隐式标识、短视频六类标签、无标识虚假内容治理、微短剧盗脸偷声、最高法换脸拟声意见均已有 atom。
- YouTube 写实合成披露、TikTok C2PA 标签与欧盟 AI 法案第 50 条的机器标记 / 观众披露已在 10 月下旬至 11 月 11 日覆盖。
- 爬虫搜狐“明星 AI 换脸事件”页面不可访问；标题和摘要为耸动叙事，且未给裁判文书、案号、平台公告或当事人声明。与已核验的最高法规则相比证据更弱，淘汰；若后续取得法院文书和平台处置公告可重开。

## 爬虫候选与发现渠道处置

- 搜狐“明星 AI 换脸事件”：不可访问、缺原始案件证据且摘要疑似叙事性拼接；在 `platforms / types / compliance` 均不晋升。
- A2E AI / Yahoo Finance：不可访问的聚合发布稿；缺厂商当前文档、模型清单、费用、商用权利和可用地区，不晋升。
- Google News RSS 共 24 个中文 / 英文查询被 robots 拒绝；未绕过访问控制。改用可访问的官方站点定向搜索形成可信账本。

## 地区与质量说明

- 发现池为国内 42、海外 24，约 64:36；国内优先网信部门、广电部门、法院、平台开放文档和模型厂商文档。
- 发布集为国内 2、海外 4。海外本日出现 4 个可核验且全库未覆盖的平台增量；没有为发布比例淘汰它们，也没有为补国内数量降低证据门槛。
- 6 个 atom 均分开写来源事实、分析推断、可执行含义和既有关系。17 个待核验项均写明缺失证据；重复、噪声、不可访问和被当前官方来源替代的线索均保留了处置理由。
