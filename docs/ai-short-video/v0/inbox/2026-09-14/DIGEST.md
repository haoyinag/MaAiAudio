# 日摘要 · 2026-09-14

> 默认入口：先读本页。原子稿仅作溯源，不必逐篇打开。

- 扫描日：2026-09-14（Asia/Shanghai 上午）
- 扫描范围：中文社区 / 英文社区 / 工具链工作流 / 第三方频道数据（公开源）
- 入库条目：10（上午双扫；未另开下午补扫）
- 分布：制作管线 4 · 通用 2 · 类型 2 · 增长 2
- 原子目录：[INDEX.md](./INDEX.md)

相对 2026-09-10 / 09-11 / 09-12 / 09-13（含下午补扫）已入库内容不重复收录。本轮禁止再写：五层分镜、八层提示词、行为型提示词、即梦首尾帧/全能参考/@素材名粗讲、角色参考预审、3:1 抽卡+LUT、60–90s 完播、Growth Max IAA/IAP、参考包 vs 分镜表、红果高频 AI 脸、戏型分模 Veo/Kling/Seedance、R2V、即梦权重/运动三要素、接受标准批量审、模型无关资产、为生成而写、四路径叠变现、Creativity/YPP 门槛粗讲、权利元数据、道具声线、分模矩阵+extend、即梦+可灵 2–4s、7-panel、物理提示词、表格分镜、3h SOP、漫剧选题、抖音→红果、供给过剩、海外目录墙、红果质量闸、Kling Subject Binding、C2PA、微短剧办法三级、渲前四门、口型侧远兜底、负面词库、首尾固定法、竖屏安全区 UI、钩子 premium 解锁、cold open 四型悬念、shot primary job、cost/retry ceiling、Kling i2v 时长分档、Kling 时间戳分镜。可选 YPP Shorts 2027 门槛与 09-10 / 09-12 已有门槛条撞车，跳过。

本轮只补净增量：节拍向时长封顶与生成乘数、硬接触绕开、声线先于画面+5s 成对剪、Seedance 2.0 多模态上限与 `@` 分工、提示词注意力顺序、角色/背景解耦、季表即产品、10 集试点规模、AIR Shorts RPM/混合比、Shorts→长视频发现桥。

---

## 一句话结论

生成便宜，季表才是产品——单镜按对白/反应/硬接触拆预算，账单看「镜数×约 3 次」乘数，不看单价；YouTube Shorts 当发现漏斗，混合比约 0.28–0.40，钱多在下游长视频。

---

## 按维度速览

### 制作管线（4）

1. **按节拍封顶单镜时长**：[pipeline-14](./pipeline-14-clip-duration-caps-by-beat.md) — 对白镜约 3–5s，反应镜约 2s，单镜不超过约 8s。每镜预算约 3 次生成；乘数决定账单，不只看单价（ScreenWeaver，待核）。不替代 Kling 风险分档或通过单价公式。
2. **硬接触绕开**：[pipeline-15](./pipeline-15-board-around-hard-contacts.md) — 接吻/打斗/两体接触易崩，分镜写成接近→切→余波；穿门换景拆成两镜；手机/文字屏先生成空白再后期叠字。
3. **台词先于视频 + 悬崖成对剪**：[pipeline-16](./pipeline-16-voice-before-cut-cliff-pair.md) — 先出对白轨锁定时长，剪辑贴台词；每集末约 5s 悬念与下一集首约 5s「被扣住的反应」当成一对来剪。不重开悬念四型。
4. **Seedance 2.0 多模态上限**：[pipeline-17](./pipeline-17-seedance2-multimodal-caps.md) — 作者手册口径（待核）：图≤9；视频≤3 且总时长≤15s；音频≤3 且总时长≤15s；生成时长可选约 4–15s。`@素材名` 分工：图锁人/风格，视频锁动作运镜，音频锁节奏口型。首尾帧入口 vs 全能参考入口只作分流提醒，细则仍见 09-13。

### 通用技巧（2）

- **提示词顺序**：[general-06](./general-06-subject-action-camera-style-order.md) — Subject→Action→Camera→Style（→Constraints）。靠前信息权重更高；每镜一个动作 + 一个运镜；可加物理细节。不替代八层字段表。
- **角色与背景解耦**：[general-07](./general-07-decouple-char-bg-action-first.md) — 先出角色表；复杂动作先在中性背景完成再合成进场景；长段切成约 2–3s 微镜降漂移（社区经验，待核）。不替代角色预审与 7-panel。

### 类型技巧（2）

- **季表是产品**：[types-04](./types-04-season-grid-is-the-product.md) — 先季表后生成；每集一个悬崖；付费墙集 / 中点 / 全失 / 终章要钉死。竖剧常 40–100 集、单集约 1–3 分钟、常在约第 8–12 集后付费墙（Sensor Tower Q1 2026 经来源转述，待核）。
- **首项目试点规模**：[types-05](./types-05-pilot-10ep-three-char-two-loc.md) — 别做 70 集：建议 10 集×60–90s、一套路、三角色、两场景，社交平台无付费墙试水；约 250–400 镜量级（作者口径，待核）。

### 增长变现（2）

- **Shorts RPM 与混合比**：[growth-07](./growth-07-shorts-rpm-mixed-ratio.md) — AIR 274 频道 Studio API（更新标注约 2026-06-23）：多数垂类 Shorts RPM 约为长视频的 3–14%；约需 1.1 万–3.4 万 Shorts 播放才抵 1k 长视频收入。混合策略 Short ratio 约 0.28–0.40；多数垂类甜区约 1–5 Shorts/月，21+/月风险升高。Entertainment 同频道对比压缩信号强（相关非因果，待核）；Music Content ID 例外。
- **发现桥接**：[growth-08](./growth-08-shorts-discovery-related-bridge.md) — Shorts 作发现漏斗而非主变现；Related Video 元数据桥接长视频；片尾约 3s 口头 CTA；Short 做成不完整答案由长视频收束。案例中收入增长多来自下游长视频（作者案例，待核）。

本轮无新的平台技巧 / 合规条目（可选 YPP Shorts 2027 门槛与已有门槛条撞车，跳过）。

---

## 可执行清单

1. 分镜按时长封顶：对白 3–5s、反应约 2s、单镜 ≤约 8s；开渲前按「终剪镜数 × 约 3 次」排 credits
2. 硬接触标红并改写为接近→切→余波；穿门/换景拆两镜；手机与路牌先出空白再叠字
3. 先出对白轨再渲视频；集末约 5s 与下集首约 5s 放进同一时间线成对审
4. Seedance 2.0 按手册上限配参考（图≤9 / 视频≤3·≤15s / 音频≤3·≤15s，待核）；提示词用 `@素材名` 写清图锁人、视频锁动作、音频锁节奏
5. 提示词固定 Subject→Action→Camera→Style；每镜一个动作、一个运镜
6. 先交角色表；复杂动作在中性背景锁定后再合成；超过约 3s 的想法拆微镜
7. 开渲前先钉季表四颗钉（付费墙/中点/全失/终章）；首项目只批 10 集×60–90s、三角色、两场景
8. Shorts 当发现：Related Video + 片尾约 3s CTA；上传比先落 0.28–0.40；Entertainment 盯同频道 RPM 压缩，勿把 Shorts 当主进账

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

数字凡未亲自复核官方后台或白皮书的，正文已标「待核」或「作者/平台自报」。

---

## 怎么读

原子稿只作溯源。默认读本 DIGEST；需要参数或边界句时再下钻 [INDEX.md](./INDEX.md)。本轮不是新发版，正式阅读层仍是 v2026.09.13。
