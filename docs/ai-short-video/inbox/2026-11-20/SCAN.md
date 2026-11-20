# SCAN 2026-11-20

> 模式：每日采集；时区：Asia/Shanghai。严格按“六维中外广泛发现 → 打开原始来源分层核验 → 全库去重 → 分层写入”执行。爬虫候选只作发现线索。

## 覆盖总览

- 爬虫 `coverage`：`general=1 / platforms=0 / types=2 / pipeline=4 / growth=1 / compliance=2`；六维均低于每维 8 条发现目标，`platforms` 为零。
- 爬虫 `region_counts`：国内 3、海外 1；仅 4 条候选且多维交叉计数，不能定义今日广度。
- 六维全部追加中外定向搜索；负向词覆盖制作瓶颈、失败拆解、废片 / credit burn、拒审 / 限流、demonetization、ROI 与变现困局。
- 定向检索、原文核验与全库去重后记录 54 条主题 / 来源线索：国内 35、海外 19（约 65:35）。晋升 5 个普通 atom；待核验 10；淘汰 / 合并 39。
- 11-19 六维均有晋升，因此没有连续两天缺维度的强制补扫项；仍对爬虫为零或不足的六维全部补扫。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 10 | 7 / 3 | 2 | 2 | 6 |
| platforms | 8 | 5 / 3 | 0 | 2 | 6 |
| types | 8 | 6 / 2 | 0 | 2 | 6 |
| pipeline | 11 | 6 / 5 | 2 | 2 | 7 |
| growth | 8 | 4 / 4 | 0 | 2 | 6 |
| compliance | 9 | 7 / 2 | 1 | 0 | 8 |
| **合计** | **54** | **35 / 19** | **5** | **10** | **39** |

计数以主维度归档；同一 URL 同时命中多个维度时只计一次。

## general｜通用技巧

### 搜索尝试

- 中文：`万相3 提示词 高频动作 失败 官方`、`Seedance 2.5 参考素材 崩坏 废片 官方`、`AI 视频 眼睛 异常 失败样例`。
- 海外：`official AI video generation artifacts failure modes`、`Seedance 2.5 glowing eyes prompt guide`、`Runway image artifacts motion prompt`。

### 处理

- **已晋升：** [万相 3.0 把高频动作改写为可观察状态变化](./general-wan3-high-frequency-motion-boundary.md)；[Seedance 2.5 强情绪词先过眼部异常预检](./general-seedance-emotion-eye-artifact.md)。
- **待核验：** Seedance 2.0 / 2.5 混用存在风格漂移，但缺同一资产的跨版本验收样本；Seedance 高分辨率参考图密集纹理可能产生指纹状纹理，缺题材与分辨率分层发生率。
- **淘汰 / 合并：** Runway 最小运动描述、图生视频输入净化、万相结构化提示与音频空约束、Seedance 参考负载稳定区均已有 atom；没有新增同义条目。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 AIGC 原创 审核 限流 官方`、`快手 AI 微短剧 审核 收益 官方`、`B站 AI 标识 创作者规则`。
- 海外：`YouTube Shorts original content recommendation 2026 official`、`TikTok AI label distribution official`、`Facebook Reels originality demonetization official`。

### 处理

- **已晋升：** 无。当前可核验规则均与既有条目重复。
- **待核验：** 抖音 / 快手未检得可访问且足以说明 AI 内容分发阈值、申诉 SLA 的一手页；YouTube 超过一分钟 Shorts 的版权主张后果在当前帮助页之间出现表述冲突，需确认唯一当前口径。
- **淘汰 / 合并：** YouTube 10 月原创分发已于 10-23 晋升；TikTok AI 标签不自动限流已有 atom；Facebook 原创性账号级处罚已于 11-19 晋升。
- **缺口原因：** 一手平台规则没有相对既有条目的独立增量；不以二手“限流经验”补位。

## types｜类型技巧

### 搜索尝试

- 中文：`广电总局 AI 微短剧 精品 失败 同质化 评审`、`AI 漫剧 类型 瓶颈 废片`、`数字人口播 广告 体验 边界`。
- 海外：`vertical micro-series failure retention official`、`faceless AI series originality`、`audio-first Shorts format boundary`。

### 处理

- **已晋升：** 无。
- **待核验：** 广电精品计划提供全过程跟踪与质量导向，但未公开入选 / 落选样本的类型化评审理由；国内公开材料称供给激增且同质化严重，但缺可复用的类型失败量表。
- **淘汰 / 合并：** YouTube Shorts Series、TikTok creator-led micro-series、微短剧完整情节边界、数字人口播四轴验收均已有 atom；项目名单和总播放量不用于反推类型 ROI。
- **缺口原因：** 可靠来源主要是政策方向或项目名单，不能转化为新的可执行类型方法。

## pipeline｜制作管线

### 搜索尝试

- 中文：`万相3 计费 输入 输出 失败 免费额度 到期 官方`、`Seedance credit burn 失败 退款`、`AI 视频 制作返工 瓶颈`。
- 海外：`Adobe Firefly build story limitations official`、`Runway failed generation refund unusable output`、`AI video production workflow immutable settings`。

### 处理

- **已晋升：** [万相参考视频按输入与成功输出总秒数算账](./pipeline-wan3-input-output-billing-boundary.md)；[Firefly 故事板生成首帧前冻结画幅与分辨率](./pipeline-firefly-story-project-settings-lock.md)。
- **待核验：** 万相成功但审美不可用的退款边界未见官方承诺；跨模型真实可交付秒成本仍缺同 brief、同验收标准和人工返工工时。
- **淘汰 / 合并：** Runway 完成但不满意仍扣积分、Seedance 输入视频最低计费与资源包到期 / 超额已在 11-18～19 晋升；搜狐“本入剧出”产品稿缺原始参数、失败率与账单。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 微短剧 投流 ROI 亏损 失败 官方`、`AI 漫剧 变现 分账 平台集中`、`短视频 AI 虚拟人 商业化 处罚`。
- 海外：`YouTube AI generic template demonetization official`、`TikTok Creator Rewards AI original eligibility`、`AI video creator ROI failure breakdown`。

### 处理

- **已晋升：** 无。
- **待核验：** TikTok Creator Rewards 确认一分钟以上、原创、高质量且排除 Duet / Stitch / 赞助内容，但缺完整地区、账户资格及 AI 格式判定；国务院发展研究中心页面提供行业成本与平台集中数据，但不能证明单项目 ROI，需项目全成本与回款样本。
- **淘汰 / 合并：** YouTube 通用 AI 模板批量生产不可变现已进入 PLAYBOOK；Facebook 合格观看已于 11-19 晋升；奖金池、平台总收入和营销消耗不外推为账号回报。
- **缺口原因：** 没有一手来源给出可审计的通用 CPM、废片率或盈亏平衡模型。

## compliance｜合规与风控

### 搜索尝试

- 中文：`AI 虚拟人 广告 虚构体验 监管 官方`、`AI 广告 处罚 推荐证明 标识`、`生成式 AI 广告 肖像 声音 授权`。
- 海外：`synthetic media endorsement disclosure official`、`AI likeness advertising enforcement`、`AI video copyright takedown official`。

### 处理

- **已晋升：** [AI 虚拟人广告不得虚构体验且标识不能补救失实](./compliance-ai-virtual-person-ad-claims.md)。
- **待核验：** 无独立 atom；“方桃子”具体罚款线索留在爬虫处置，等待可直接核验的行政处罚决定书。
- **淘汰 / 合并：** AIGC 显式 / 元数据标识、肖像声音授权、逐集标识和微短剧专项治理均已有 atom；登记完成消息不能证明具体视频产品合规。

## 爬虫候选逐项处置与访问失败

1. 新浪“方桃子被罚”：与监管边界相关，但原文不是处罚决定书；金额与个案责任留待核验，通用规则改用监管一手来源交叉验证。
2. 搜狐“本入剧出 2.0”：产品营销稿，缺可审计样本、失败率和成本账单；淘汰。
3. 凤凰网“问今 AI 完成登记”：登记消息不构成短视频制作、平台或合规方法增量；淘汰。
4. Note MiniMax H3：个人二手概览，缺官方限制、计费与失败边界；淘汰。
5. Google News RSS 与 `klingai.com`：robots 拒绝；未绕过，未以摘要替代原文。

## 地区与质量说明

发现池约 65:35，国内优先监管、广电、阿里云与火山引擎官方文档；海外优先 Adobe、YouTube、TikTok、Meta、Runway / BytePlus 官方页。比例建立在可核验候选之上，没有为凑数加入营销软文。完整高价值来源与失败渠道见 [RESEARCH-NOTES.md](./RESEARCH-NOTES.md)。

