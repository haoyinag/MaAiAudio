# 日摘要 · 2026-09-13

> 默认入口：先读本页。原子稿仅作溯源，不必逐篇打开。

- 扫描范围：中文社区 / 英文社区 / 工具链工作流 / 平台公告转述（公开源）
- 入库条目：19（上午双扫 10 + 下午补扫 9）
- 分布：制作管线 9 · 通用 3 · 类型 2 · 增长 2 · 平台 2 · 合规 1
- 原子目录：[INDEX.md](./INDEX.md)

相对 2026-09-10 / 2026-09-11 / 2026-09-12（含下午 21 条）已入库内容不重复收录。上午禁止再写：戏型分模 Veo/Kling/Seedance、R2V 宽镜链、即梦权重 0.7–0.8、接受标准批量审、模型无关资产、为生成而写、四路径叠变现、Creativity/YPP 门槛、权利元数据四线、道具声线、分模矩阵+extend、即梦+可灵 2–4s、7-panel bible、物理向提示词、表格分镜、3小时 SOP、漫剧选题、抖音→红果漏斗、供给过剩、海外目录付费墙、红果质量闸、Kling Subject Binding、C2PA 等。上午只补「五层分镜 / 八层提示词+模型调试层 / 行为型提示词 / 即梦入口分流 / 角色参考预审 / 3:1 抽卡+LUT+环境音纹理 / 60–90s 完播连载 / Growth Max IAA·IAP / 参考包 vs 分镜表选型 / 红果高频 AI 脸+肖像预检」。

下午补扫相对上午与更早日继续跳过：五层分镜、八层提示词、行为型提示词、即梦首尾帧/全能参考/@素材名、角色参考预审、3:1 抽卡+LUT、60–90s 完播、Growth Max IAA/IAP、参考包 vs 分镜表、红果高频 AI 脸、戏型分模 Veo/Kling/Seedance、R2V、即梦权重、接受标准批量审、模型无关资产、为生成而写、四路径叠变现、Creativity/YPP、权利元数据、道具声线、分模矩阵+extend、即梦+可灵 2–4s、7-panel、物理提示词、表格分镜、3h SOP、漫剧选题、抖音→红果、供给过剩、海外目录墙、红果质量闸、Kling Subject Binding、C2PA、微短剧办法「三级」概要。本轮合规未另开新条（可选「沉迷算法禁令 / 11 条红线」易与办法三级、红果脸撞车，跳过，保持恰好 9 条）。

---

## 一句话结论

分镜从「表」升到 goal/sequence/shot/prompt/check 五层，转场对写进分镜；提示词通用八层、失败只改一层，再按最难点叠模型调试层。海外微短剧盯 60–90s 完播与悬念连载，Growth Max 把 IAA/IAP 拆成两条 tROAS；国内红果专项打高频 AI 脸，标「AI生成」不能替代肖像/版权预检。

---

## 按维度速览

### 制作管线（5）

1. **五层分镜系统**：goal → sequence → shot → prompt → check。短片常用 3–6 镜；每镜写 framing / 运镜 / 动作 / 光 / 转场。prompt 模板含 Continuity + Constraints。开渲前写死接受标准（产品可辨、服装不变、运镜平滑、末帧可接下一镜）。转场对（运动 / 形状 / 色 / 动作 / 景别匹配）写进分镜，不只靠剪辑。结构例：Hook→problem→transformation→result，或 establishing→action→detail→hero。
2. **八层提示词 + 模型调试层**：通用八层 Reference / Shot label / Subject / Action / Camera / Scene+lighting / Audio|timing / Constraints；失败只改一层。模型层：Runway Gen-4.5 用 force-reaction + Motion Sketch；Kling 3.0 用 Elements/Bind Subject，对白须写 face+camera；Veo 3.1 用 `says:` / `SFX:` / `Ambient:`；Seedance 2.0 用 `@character/@product/@scene/@style`。选型按最难点：物理→Runway、脸一致/对白→Kling、伪真+原生音频→Veo、品牌资产锚定→Seedance。
3. **行为型 vs 电影语言**：Kling 常用 cinematic 词库（景深 / 胶片颗粒 / golden hour）有效；同一套搬到 Seedance 常变差。Seedance 更吃 behavioral prompts（主体在做什么、表情如何变化）。角色一致：正脸中性头像 + 45° 侧脸双锚；单镜约 4–6s 防漂移；约 60s 成片拆 12–15 短镜再剪（作者经验，待核）。
4. **即梦入口分流**：仅首帧图+prompt →「首尾帧」；多模态（图/视频/音频/文本）→「全能参考」（智能多帧/主体参考不可选时以手册为准）。用 `@素材名` 指定用途。社区称全能参考常见上限约 9 图 + 3 视频 + 3 音频、素材时长约 ≤15s（以产品实际 UI 为准，待核）。
5. **角色参考预审再进视频**：写实真人角色易撞内容审核；先把参考图导入资产库完成审核，再用于视频生成，否则「真人视频」类调用常无明确原因失败。瓶颈常在资产工作流与上下文切换，不在再装一个工具。成片用多段稳定短镜拼接，生成约一半、剪辑约一半（作者经验，待核）。

### 通用技巧（1）

- 终剪约 3:1 生成比（每镜约 3 候选）；多模型默认调色不同，成片统一一条 cinematic LUT。即便 Veo/Kling 有原生环境音，仍加一层音乐床——AI 环境音当纹理，不宜当唯一音轨。在自然动作完成点剪，不在动作中途硬切。

### 类型技巧（1）

- 海外 TikTok/Reels 微短剧常见单集 60–90s、9:16、日更或近日更；完播+追更信号优先；结尾悬崖驱动下集；角色锁定跨集。TikTok Series 付费墙作者报约 $0.99–$4.99/集（待核）；Shorts/Reels 可作引流回 TikTok；亦可整季授权 ReelShort 等目录 App（本条只记完播连载，不重开目录墙细则）。

### 增长变现（1）

- Growth Max 把短剧连载接到广告自动化。两条 tROAS：IAA（片内广告解锁）平台自报测试约 3× D0 ROAS vs 标准 app/web；IAP（付费解锁）约 1.5×（TikTok 内部测试 Apr–May 2026，待核）。Minis Center 支持 IAA+IAP，公告时约 11 市场；全球信息流分发多为仅嵌入广告、无付费墙。IAA/IAP 勿混同一优化目标。Growth Max 多需销售对接非纯自助；有机分发需 Business Account。

### 平台技巧（1）

- Seedance 2.0 = reference-led（图/音/视频参考包）；Kling VIDEO 3.0 = shot-led（Multi-Shot / Custom Multi-Shot、element binding、原生对白）。有参考包先 Seedance；有分镜表+具名元素+对白先 Kling；纯文本两边都测。公平对比：固定 5 个真实 brief、同次数、同评分（主体保真 / 动作时机 / 构图 / 音频 / 返工量）；勿混版本。

### 合规与风控（1）

- 媒体转述（非平台原文）：红果短剧约 2026-08 发布《关于规范AI剧角色创作的公告》，治理高频 AI 脸 / 同质化 / 素材违规（「千人一面」）。抖音短剧创作者中心报道称上线肖像权/版权预检。第三方称备案通过率不到约 30%（待核，非官方白皮书）。标识「AI生成」不能替代肖像/版权责任；创作侧应自建差异化角色资产，避免共用同款脸模。

---

## 今日可执行清单（优先 5 条）

1. 开渲前写死五层分镜；每镜带 Continuity+Constraints；转场对写进分镜；check 勾选产品可辨 / 服装不变 / 运镜平滑 / 末帧可接
2. 提示词先填通用八层，失败只改一层；按最难点选型（物理 Runway / 脸+对白 Kling / 伪真+原生音频 Veo / 品牌锚定 Seedance）
3. 即梦：单首帧走「首尾帧」，多模态走「全能参考」并用 `@素材名` 指定用途
4. 写实角色参考图先导入资产库完成审核，再进视频生成；成片用稳定短镜拼接
5. 红果/抖音发行前过肖像预检、自建差异化角色资产；Growth Max 的 IAA 与 IAP 分两条 tROAS，勿混同一优化目标

---

## 下午补扫

### 一句话结论

下午不重开分镜层数或分模表，只补「每镜一个 primary job + 默认/专长启用门槛」「按通过镜计价 + retry ceiling」、Kling 按时长风险分档与时间戳分镜提示；类型侧补冷开场三型/悬念四型，增长侧只写钩子经济学（墙仍落最强未解悬念）。

### 按维度速览（下午增量 9）

#### 制作管线（+4）

6. **primary job + 默认/专长**：每镜一个 primary、最多两个 secondary；先定必须保住项再选型。默认模型扛常规镜，专长模型只在默认反复失败或刚需能力时启用。不重开戏型分模表。
7. **通过单价 + retry ceiling**：Cost per approved shot = 该镜总 credits ÷ 通过数；时间含排队/审片/返工。短时长低分辨率先验证，draft 与 final 分路由。开渲前设连续约 2–3 次失败后换模型/简化/拆镜/加强参考（来源建议，待核），禁止盲抽。
8. **Kling i2v 时长按风险**：环境/空镜可较长（社区例约 15s）；人脸/袍服类约 10s 上限；强运动高潮约 5–8s，越长越易「熔脸」。每镜约 2–3 takes 取最稳；氛围向 CFG/relevance 偏松（社区自报，待核）。
9. **时间戳分镜提示**：Kling 3.0 multi-shot 写成 `Shot N: 00:00–00:03` + 景别/动作，像导演分镜而非单段散文；可用 start/end frame 约束连续性。不重开 Subject Binding。

#### 类型技巧（+1）

- **冷开场三型 + 悬念四型**：形状为 cold open（约 0–3s）→ 中段恰一个 reversal → 末镜 cliffhanger。开场用脸部反应 / 一句冲击台词 / 已在进行的揭示，禁止建立镜/片头卡。悬念四型 reveal / threat / revelation / decision，一律停在解决前一拍。钩子与悬念先静帧审批；钩子建议约 3–4 候选全取（来源建议，待核）。

#### 通用技巧（+2）

- **单张标准参考 + 负面库**：固定一张标准化参考跨镜，勿随镜换图；负面库排除换装/脱龄/多余肢体等漂移。先分镜再独立生镜后组装，比赌长镜连贯更可控（社区自报，待核）。
- **首尾固定法 + 口型兜底**：生图提示开头+结尾重复关键角色特征，中间写场景动作。口型差改侧面/远景，不死磕正脸。不重开即梦权重。

#### 平台技巧（+1）

- **竖屏安全区**：对白放画面中三分之一；底部约 1/4 留给字幕/平台 UI；发布前用手机审每一集前约 3 秒（来源教程，待核）。

#### 增长变现（+1）

- **钩子经济学**：冷开场是留存决策镜，premium + 约 3–4 覆盖；悬念镜同样高优先。付费解锁常落最强未解悬念。与四路径条目互补，不重写四条路径清单。

### 可执行清单（下午追加）

6. 每镜先填 primary job（及 ≤2 个 secondary）再选型；默认模型扛常规，专长只在反复失败或刚需时启用
7. 用「该镜总 credits ÷ 通过数」记账，时间含排队/审/返工；开渲前写下 2–3 次 ceiling，达顶换路不盲抽
8. Kling i2v 按空镜 / 人脸袍服 / 强运动分档时长；每镜 2–3 takes；氛围 CFG 偏松（社区例，待核）
9. 钩子与悬念先静帧审批再烧视频 credits；钩子约 3–4 候选全取；付费墙切在最强未解悬念
10. 竖屏对白落中三分之一、底约 1/4 让 UI；每集用手机审前约 3 秒

### 溯源（下午原子稿）

- [pipeline-10-shot-primary-job-default-specialist.md](./pipeline-10-shot-primary-job-default-specialist.md)
- [pipeline-11-cost-per-approved-retry-ceiling.md](./pipeline-11-cost-per-approved-retry-ceiling.md)
- [pipeline-12-kling-i2v-duration-by-risk.md](./pipeline-12-kling-i2v-duration-by-risk.md)
- [pipeline-13-kling-multishot-timestamp-prompt.md](./pipeline-13-kling-multishot-timestamp-prompt.md)
- [types-03-cold-open-cliffhanger-four-types.md](./types-03-cold-open-cliffhanger-four-types.md)
- [general-04-negative-prompt-library.md](./general-04-negative-prompt-library.md)
- [general-05-prompt-bookend-character-lock.md](./general-05-prompt-bookend-character-lock.md)
- [platforms-02-vertical-safe-zone-ui.md](./platforms-02-vertical-safe-zone-ui.md)
- [growth-06-hook-premium-unlock-at-cliff.md](./growth-06-hook-premium-unlock-at-cliff.md)

---

## 溯源（按需点开）

完整条目列表见 [INDEX.md](./INDEX.md)。需要细节参数时再进对应原子稿。
