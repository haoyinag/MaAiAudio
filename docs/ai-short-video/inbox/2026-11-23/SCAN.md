# SCAN 2026-11-23

> 模式：每日采集；时区：Asia/Shanghai。严格按“六维中外广泛发现（技巧、端到端工作流、行业困境/失败/成本边界、变现）→ 打开原始来源分层核验 → 全库去重 → 分层写入”执行。

## 覆盖总览

- crawler `coverage`：`general=0 / platforms=1 / types=1 / pipeline=2 / growth=0 / compliance=0`；`region_counts`：国内 1、海外 2。三条均只是线索，不能定义今日广度。
- `types`、`growth` 在 11-18 与 11-20 连续两次无晋升，今日优先扩大监管点评、项目复盘、全成本账单、demonetization 与 ROI 失败词；`platforms` 也针对 11-20 缺口补扫。
- 定向检索并去重后记录 59 条主题/来源线索：国内 38、海外 21（约 64:36）。晋升六维各 1 篇；待核验 12；淘汰/合并 41。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 9 | 6 / 3 | 1 | 2 | 6 |
| platforms | 10 | 6 / 4 | 1 | 2 | 7 |
| types | 8 | 6 / 2 | 1 | 2 | 5 |
| pipeline | 12 | 7 / 5 | 1 | 2 | 9 |
| growth | 9 | 6 / 3 | 1 | 2 | 6 |
| compliance | 11 | 7 / 4 | 1 | 2 | 8 |
| **合计** | **59** | **38 / 21** | **6** | **12** | **41** |

计数按主维度归档；跨维 URL 只计一次。

## general｜通用技巧

### 搜索尝试

- 中文：`AI 视频 生成失败 参考素材冲突 废片 官方`、`Seedance 提示词 失败 分辨率 官方`、`万相 动作 崩坏 失败边界`。
- 海外：`AI video generation failure breakdown official`、`Runway prompt reference conflict error`、`video model artifacts bottleneck retry`。

### 处理

- **已晋升：** [先按错误状态分流再改提示或换模型](./general-runway-error-state-triage.md)。
- **待核验：** 分辨率过高/过低导致失败仍缺模型和题材分层阈值；跨模型切换能否降低废片率缺同素材实测。
- **淘汰 / 合并：** Seedance/万相参考负载、动作拆分、输入净化与单变量迭代均已有 atom；无数据营销成功率淘汰。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 AI 内容 原创 审核 限流 官方`、`快手 AI 微短剧 宣推 同质化 治理`、`B站 AI 标识 变现`。
- 海外：`YouTube AI content monetization original story official`、`TikTok AI label distribution demonetization`、`Facebook Reels unoriginal payout`。

### 处理

- **已晋升：** [YouTube 用原创叙事验收 AI 内容而非只看工具](./platforms-youtube-ai-originality-story-gate.md)。
- **待核验：** YouTube 未公开模板相似度阈值和申诉 SLA；国内平台仍缺 AI 内容分发阈值的一手页面。
- **淘汰 / 合并：** TikTok 标签不自动限流、Facebook 原创性、国内六类必选标签已有 atom；“AI 标签必限流”被官方说明反驳。

## types｜类型技巧

### 搜索尝试（连续缺口优先补扫）

- 中文：`广电 AI 微短剧 精品 点评 辨识度 落选`、`AI 漫剧 同质化 失败样本`、`数字人口播 类型 验收`。
- 海外：`AI vertical series story failure retention`、`faceless series originality bottleneck`、`AI microdrama genre evaluation`。

### 处理

- **已晋升：** [微短剧先验收故事辨识度再决定真人或 AI 形态](./types-microdrama-story-distinctiveness-gate.md)。
- **待核验：** 精品点评没有量化评分表与落选原因；海外竖屏系列仍缺平台级类型失败样本。
- **淘汰 / 合并：** 项目名单、播放战报不反推类型方法；完整情节、季级连续性、音频转 Shorts 已覆盖。

## pipeline｜制作管线

### 搜索尝试

- 中文：`AI 视频 制作 流程 积分 预占 退款`、`Seedance credit burn Draft 失败`、`万相 输入输出 计费 返工`。
- 海外：`AI video credit hold refund final charge`、`Runway production bottleneck failed generation`、`video generation unusable output cost`。

### 处理

- **已晋升：** [Runway 自动时长任务按预占减退款核最终成本](./pipeline-runway-reserved-final-credit-reconciliation.md)。
- **待核验：** 各模型退款入账时延没有稳定 SLA；跨模型可交付秒成本仍缺同 brief 与人工工时。
- **淘汰 / 合并：** Seedance 最低 token、资源包到期、Runway 完成不满意不退款、万相输入输出计费均已有 atom。

## growth｜增长变现

### 搜索尝试（连续缺口优先补扫）

- 中文：`AI 短剧 3000 成本 澄清 人力`、`AI 漫剧 投流 ROI 亏损 回款`、`微短剧 变现 分账 失败复盘`。
- 海外：`AI video creator ROI failure breakdown`、`YouTube AI demonetization template`、`creator rewards qualified views cost`。

### 处理

- **已晋升：** [AI 短剧 ROI 不得把算力成本当项目总成本](./growth-ai-drama-full-cost-roi-denominator.md)。
- **待核验：** 项目真实总成本与回款未公开；通用 CPM、投流回收和废片率仍无一手可审计样本。
- **淘汰 / 合并：** 平台 GMV、奖金池、播放战报不外推账号 ROI；YouTube 批量模板与 Facebook 合格观看已有条目。

## compliance｜合规与风控

### 搜索尝试

- 中文：`最高法 AI 拟声 带货 委托 审核 典型案例`、`AI 视频 肖像 声音 授权 判决`、`生成合成 标识 处罚`。
- 海外：`AI likeness voice advertising enforcement`、`synthetic media disclosure takedown`、`AI impersonation creator policy`。

### 处理

- **已晋升：** [委托 AI 带货视频仍要审核肖像与声音授权](./compliance-commissioner-likeness-voice-audit-duty.md)。
- **待核验：** 委托方责任必须结合合同与审核权限，不能概括成自动连带；海外拟声商业使用仍缺可跨地区复用的统一规则。
- **淘汰 / 合并：** AIGC 显式/隐式标识、逐集标识、肖像声音授权已有 atom；未决评论不写成责任事实。

## crawler 候选与访问失败

1. MSN 转述“让 AI 短剧走得更远”：二手评论且编码异常，被广电总局原文替代。
2. GoViral 发布稿：营销内容，缺可审计失败率、账单与权利边界，淘汰。
3. Lemonlight/Hero 发布稿：二手产品发布，缺原始参数与生产失败样本，淘汰。
4. Google News RSS：robots 拒绝；未绕过，未以摘要替代原文。

## 地区与质量说明

发现池约 64:36，接近 65:35；国内优先广电总局、最高法、网信办、火山引擎和行业协会，海外优先平台/模型厂商官方。没有为比例加入弱来源。核验页见 [SOURCE-NOTES.md](./SOURCE-NOTES.md)。
