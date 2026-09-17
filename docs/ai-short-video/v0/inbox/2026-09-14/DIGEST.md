# 日摘要 · 2026-09-14

> 默认入口：先读本页。原子稿仅作溯源，不必逐篇打开。

- 扫描日：2026-09-14（Asia/Shanghai 上午+下午）
- 扫描范围：中文社区 / 英文社区 / 工具链工作流 / 第三方频道数据（公开源）
- 入库条目：19（上午双扫 10 + 下午补扫 9）
- 分布：制作管线 8 · 通用 4 · 类型 2 · 增长 4 · 平台 1（下午新增：pipeline 4 · general 2 · platforms 1 · growth 2）
- 原子目录：[INDEX.md](./INDEX.md)

相对 2026-09-10 / 09-11 / 09-12 / 09-13（含下午补扫）已入库内容不重复收录。本轮禁止再写：五层分镜、八层提示词、行为型提示词、即梦首尾帧/全能参考/@素材名粗讲、角色参考预审、3:1 抽卡+LUT、60–90s 完播、Growth Max IAA/IAP、参考包 vs 分镜表、红果高频 AI 脸、戏型分模 Veo/Kling/Seedance、R2V、即梦权重/运动三要素、接受标准批量审、模型无关资产、为生成而写、四路径叠变现、Creativity/YPP 门槛粗讲、权利元数据、道具声线、分模矩阵+extend、即梦+可灵 2–4s、7-panel、物理提示词、表格分镜、3h SOP、漫剧选题、抖音→红果、供给过剩、海外目录墙、红果质量闸、Kling Subject Binding、C2PA、微短剧办法三级、渲前四门、口型侧远兜底、负面词库、首尾固定法、竖屏安全区 UI、钩子 premium 解锁、cold open 四型悬念、shot primary job、cost/retry ceiling、Kling i2v 时长分档、Kling 时间戳分镜。可选 YPP Shorts 2027 门槛与 09-10 / 09-12 已有门槛条撞车，跳过。

上午只补净增量：节拍向时长封顶与生成乘数、硬接触绕开、声线先于画面+5s 成对剪、Seedance 2.0 多模态上限与 `@` 分工、提示词注意力顺序、角色/背景解耦、季表即产品、10 集试点规模、AIR Shorts RPM/混合比、Shorts→长视频发现桥。

下午禁止再写上午 10 条主题（节拍时长封顶、硬接触绕开、声线先于画面+悬崖成对、Seedance2 多模态上限、SAC 顺序、角色背景解耦、季表即产品、10 集试点、Shorts RPM 混合比、Related 桥）。下午只补：Kling 元素建档+绑声线、Native Audio 口型清单、按秒计价、声线卡一句一意图、硬身份锚点、成片 audio bleed/缓推、ReelShort 交付规格、付费墙钉最强未解节拍、免费段当获客+权力反转前一拍。

---

## 一句话结论

生成便宜，季表才是产品——单镜按对白/反应/硬接触拆预算，账单看「镜数×约 3 次」乘数，不看单价；YouTube Shorts 当发现漏斗，混合比约 0.28–0.40，钱多在下游长视频。下午补：Kling 元素绑声线后 prompt 勿再设音色；付费墙钉最强未解节拍，节拍位置优先于集号。

---

## 按维度速览

### 制作管线（8）

1. **按节拍封顶单镜时长**：[pipeline-14](./pipeline-14-clip-duration-caps-by-beat.md) — 对白镜约 3–5s，反应镜约 2s，单镜不超过约 8s。每镜预算约 3 次生成；乘数决定账单，不只看单价（ScreenWeaver，待核）。不替代 Kling 风险分档或通过单价公式。
2. **硬接触绕开**：[pipeline-15](./pipeline-15-board-around-hard-contacts.md) — 接吻/打斗/两体接触易崩，分镜写成接近→切→余波；穿门换景拆成两镜；手机/文字屏先生成空白再后期叠字。
3. **台词先于视频 + 悬崖成对剪**：[pipeline-16](./pipeline-16-voice-before-cut-cliff-pair.md) — 先出对白轨锁定时长，剪辑贴台词；每集末约 5s 悬念与下一集首约 5s「被扣住的反应」当成一对来剪。不重开悬念四型。
4. **Seedance 2.0 多模态上限**：[pipeline-17](./pipeline-17-seedance2-multimodal-caps.md) — 作者手册口径（待核）：图≤9；视频≤3 且总时长≤15s；音频≤3 且总时长≤15s；生成时长可选约 4–15s。`@素材名` 分工：图锁人/风格，视频锁动作运镜，音频锁节奏口型。首尾帧入口 vs 全能参考入口只作分流提醒，细则仍见 09-13。
5. **Kling 元素绑声线（下午）**：[pipeline-18](./pipeline-18-kling-element-voice-bind.md) — 建角色元素用 2–4 张参考图或 3–8 秒角色视频；元素可绑声线（视频提取或另传音频）；绑完后 prompt 不要再设音色。样音需干净、无叠声无大声音乐；多图+音频路径音频建议 ≥3s。相对 Subject Binding 粗讲，只记建档规格。
6. **Native Audio 口型清单（下午）**：[pipeline-19](./pipeline-19-kling-lipsync-script-checklist.md) — 说话人脸可读；姓名+台词紧挨；复杂句拆短；可写环境声；多角色用 `Name (tone): line`。交付注记仅在有用时加。支持中/英/日/韩/西及方言口音标签（以产品为准）。不重开口型侧远兜底。
7. **Kling 按秒计价（下午）**：[pipeline-20](./pipeline-20-kling-credits-per-second.md) — 官方表（产品页可能变动，待核）：Native Audio 1080p 12 Credits/s、720p 9/s；No Native Audio 1080p 8/s、720p 6/s；Voice Tone Control 另加 2/s。例：5s Native Audio 1080p = 60，再开音色控制 = 70。开渲前「秒数 × 单价 × 尝试次数」，与上午「镜数×约 3 次」联用。不重开 retry ceiling。
8. **声线卡 + 一句一意图（下午）**：[pipeline-21](./pipeline-21-voice-card-one-intent-per-line.md) — 多角色声线卡含年龄感/音色/语速/音量/情绪上限/停顿/口头禅/禁区。台词一句一意图；15s 内对话要短；30s+ 拆多回合，用反应镜/沉默拼接；按角色分轨。口型失败先查句长/站位/说话人标签，勿无限抽卡。相对上午「台词先于视频」，本条管卡与分轨。

### 通用技巧（4）

- **提示词顺序**：[general-06](./general-06-subject-action-camera-style-order.md) — Subject→Action→Camera→Style（→Constraints）。靠前信息权重更高；每镜一个动作 + 一个运镜；可加物理细节。不替代八层字段表。
- **角色与背景解耦**：[general-07](./general-07-decouple-char-bg-action-first.md) — 先出角色表；复杂动作先在中性背景完成再合成进场景；长段切成约 2–3s 微镜降漂移（社区经验，待核）。不替代角色预审与 7-panel。
- **硬身份锚点（下午）**：[general-08](./general-08-hard-identity-anchors-forbid-change.md) — 选 3–5 个硬锚点（脸型/发型轮廓/眼色/外套剪裁/耳饰等），少而硬。定妆照正脸、中性表情、干净背景、均匀光。禁改写「不得改变」，勿写「尽量保持」。审片先一致性再美感；主角/高频配角要三视图。不重开 7-panel 或预审流程。
- **成片胶合（下午）**：[general-09](./general-09-capcut-audio-bleed-push-in.md) — 邻镜音频尾首轻微叠化（audio bleed）减分段感；片头约 3–5s 处加约 5–10% 关键帧缓推，降低掉出。剪掉 filler / 长停顿 / 怪动作。一次只改一个变量做钩子 A/B（社区帖，待核）。

### 类型技巧（2）

- **季表是产品**：[types-04](./types-04-season-grid-is-the-product.md) — 先季表后生成；每集一个悬崖；付费墙集 / 中点 / 全失 / 终章要钉死。竖剧常 40–100 集、单集约 1–3 分钟、常在约第 8–12 集后付费墙（Sensor Tower Q1 2026 经来源转述，待核）。
- **首项目试点规模**：[types-05](./types-05-pilot-10ep-three-char-two-loc.md) — 别做 70 集：建议 10 集×60–90s、一套路、三角色、两场景，社交平台无付费墙试水；约 250–400 镜量级（作者口径，待核）。

### 增长变现（4）

- **Shorts RPM 与混合比**：[growth-07](./growth-07-shorts-rpm-mixed-ratio.md) — AIR 274 频道 Studio API（更新标注约 2026-06-23）：多数垂类 Shorts RPM 约为长视频的 3–14%；约需 1.1 万–3.4 万 Shorts 播放才抵 1k 长视频收入。混合策略 Short ratio 约 0.28–0.40；多数垂类甜区约 1–5 Shorts/月，21+/月风险升高。Entertainment 同频道对比压缩信号强（相关非因果，待核）；Music Content ID 例外。
- **发现桥接**：[growth-08](./growth-08-shorts-discovery-related-bridge.md) — Shorts 作发现漏斗而非主变现；Related Video 元数据桥接长视频；片尾约 3s 口头 CTA；Short 做成不完整答案由长视频收束。案例中收入增长多来自下游长视频（作者案例，待核）。
- **付费墙钉最强未解节拍（下午）**：[growth-09](./growth-09-paywall-at-strongest-unresolved-beat.md) — 墙钉最强未解决节拍，不要钉死固定集数；免费首段后硬币解锁；单集约 1.5–2 分钟使解锁价相对「继续看的痒」显得小；每集结尾开环。与 types-04 互补：节拍位置优先于集号。
- **免费段当获客（下午）**：[growth-10](./growth-10-free-block-as-acq-power-flip-wall.md) — ReelShort 模型下前约 3–8 集=获客成本，墙后才是变现车；墙集常是权力反转前一拍的微悬崖。Ep1：10 秒内冲突，60s 内立清权力失衡与主角。平台盯 Ep1/Ep3 留存与墙转化——墙前流失=制作失败。不重开 Growth Max tROAS。

### 平台技巧（1）

- **ReelShort 交付规格（下午）**：[platforms-04](./platforms-04-reelshort-delivery-specs.md) — 9:16 无黑边；单集 60–90s（常见约 75s）；混音按手机扬声器验收；字幕小屏可读；系列常 70–120 集才够硬币经济窗口。音频脏 / 横转竖是常见拒收信号（作者/平台侧归纳，待核）。

本轮无新的合规条目（可选 YPP Shorts 2027 门槛与已有门槛条撞车，跳过）。

---

## 可执行清单

1. 分镜按时长封顶：对白 3–5s、反应约 2s、单镜 ≤约 8s；开渲前按「终剪镜数 × 约 3 次」排 credits，Kling 再乘「秒数 × 单价」（Native Audio 1080p 12 Credits/s，待核）
2. 硬接触标红并改写为接近→切→余波；穿门/换景拆两镜；手机与路牌先出空白再叠字
3. 先出对白轨再渲视频；集末约 5s 与下集首约 5s 放进同一时间线成对审；多角色先填声线卡，一句一意图、按角色分轨
4. Kling 建元素：2–4 图或 3–8s 视频；绑声线后 prompt 勿再设音色；口型提示姓名+台词紧挨，复杂句拆短，多角色用 `Name (tone): line`
5. Seedance 2.0 按手册上限配参考（图≤9 / 视频≤3·≤15s / 音频≤3·≤15s，待核）；提示词用 `@素材名` 写清图锁人、视频锁动作、音频锁节奏
6. 提示词固定 Subject→Action→Camera→Style；每镜一个动作、一个运镜。硬身份锚点只留 3–5 个，禁改写「不得改变」；主角/高频配角补三视图
7. 开渲前先钉季表四颗钉；付费墙对准最强未解节拍（节拍优先于集号）；首项目只批 10 集×60–90s、三角色、两场景
8. ReelShort 交付：9:16 无黑边、单集 60–90s、手机扬声器混音；前 3–8 集当获客，墙钉权力反转前一拍；Ep1 须 10 秒内冲突
9. Shorts 当发现：Related Video + 片尾约 3s CTA；上传比先落 0.28–0.40；Entertainment 盯同频道 RPM 压缩，勿把 Shorts 当主进账
10. 成片邻镜做短 audio bleed；片头约 3–5s 处加约 5–10% 缓推（社区经验，待核）；钩子 A/B 一次只改一个变量

---

## 来源表

| 来源 | 日期 | 用于 |
| --- | --- | --- |
| [ScreenWeaver · How to Make a Short Drama With AI](https://www.screenweaver.ai/blog/ai-short-drama) | 2026-09-03 | pipeline-14 / 15 / 16 · types-04 / 05 |
| [即梦 Seedance 2.0 使用手册](https://www.seedancetwo.com/zh/manual) | 手册页无稳定文内日期；扫描日 2026-09-14 | pipeline-17 |
| [WaveSpeed · Seedance 2.0 多模态指南](https://wavespeed.ai/blog/zh-TW/posts/seedance-2-0-complete-guide-multimodal-video-creation/) | 2026-05-10 | pipeline-17 交叉 |
| [YouMind · Seedance 2.0 提示词指南](https://youmind.com/zh-TW/blog/seedance-2-0-prompt-guide-zh) | 2026-03-22 | general-06 |
| [Reddit r/ChatArt · 角色一致工作流](https://www.reddit.com/r/ChatArt/comments/1rpq6bc/my_personal_workflow_for_nailing_ai_video/) | 帖文无稳定日期；扫描日 2026-09-14 | general-07（社区，待核） |
| [AIR · Shorts RPM vs Long-Form 2026](https://air.io/en/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026) | 约 2026-06-23 | growth-07 / 08 |
| [AIR · 18,000 频道 Shorts 是否助长视频](https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels) | 约 2026-05-28 | growth-08 交叉 |
| [Kling · Video 3 Model User Guide](https://kling.ai/quickstart/klingai-video-3-model-user-guide) | 文标 Feb 6, 2026 | pipeline-18 / 19 / 20 |
| [Kling · Omni Native Lip-Sync Audio Guide](https://kling.ai/blog/kling-video-3-omni-native-lip-sync-audio-guide) | Jul 3, 2026 | pipeline-18 / 19 |
| [Delton · 多角色配音一致性](https://arcloop.ai/handbook/zh-CN/multi-character-voiceover-consistency) | 2026-09-03 | pipeline-21 |
| [Delton · 跨镜角色一致性](https://arcloop.ai/handbook/zh-CN/character-consistency-cross-shot) | 2026-09-07 | general-08 |
| [Reddit r/aipractice · Seedance 2.0 podcast clips](https://www.reddit.com/r/aipractice/comments/1t30n6n/how_i_use_seedance_20_to_make_fake_podcast_clips/) | 帖文无稳定日期；扫描日 2026-09-14 | general-09（社区，待核） |
| [Axis AI Studios · ReelShort 平台画像](https://www.axisaistudios.com/blog/reelshort-complete-platform-profile-and-content-strategy) | 2026-05-29 | platforms-04 · growth-10 |
| [InVideo · AI micro-drama monetization](https://invideo.io/blog/ai-micro-drama-monetization/) | 2026-07-15 | growth-09 |

数字凡未亲自复核官方后台或白皮书的，正文已标「待核」或「作者/平台自报」。

---

## 怎么读

原子稿只作溯源。默认读本 DIGEST；需要参数或边界句时再下钻 [INDEX.md](./INDEX.md)。本轮不是新发版，正式阅读层仍是 v2026.09.13。
