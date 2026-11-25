# SCAN 2026-11-25

> 模式：每日采集；时区：Asia/Shanghai。严格执行“六维广泛发现 → 原始来源分层核验 → 全库去重 → 分级写入”。crawler 只作发现线索。

## 覆盖总览

- crawler `coverage`：`general=0 / platforms=0 / types=0 / pipeline=1 / growth=0 / compliance=0`；`region_counts`：国内 0、海外 1。唯一海外 pipeline 聚合稿未通过一手来源门槛。
- 六维全部低于每维 8 条发现目标，故全部用中文与海外词补扫；显式覆盖制作瓶颈、失败拆解、废片/credit burn、拒审/限流、demonetization、ROI 与变现困局。
- 搜索与全库去重后记录 52 条主题/来源候选：国内 34、海外 18（约 65:35）。晋升普通原子 5、待核验原子 1、淘汰或合并 46。计数按主维度归档，跨维来源只计一次。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 8 | 5 / 3 | 1 | 0 | 7 |
| platforms | 9 | 6 / 3 | 1 | 0 | 8 |
| types | 8 | 5 / 3 | 1 | 0 | 7 |
| pipeline | 10 | 7 / 3 | 1 | 0 | 9 |
| growth | 8 | 5 / 3 | 0 | 1 | 7 |
| compliance | 9 | 6 / 3 | 1 | 0 | 8 |
| **合计** | **52** | **34 / 18** | **5** | **1** | **46** |

## general｜通用技巧

### 搜索尝试

- 中文：`AI 视频 提示词 参考冲突 废片 官方`、`Seedance 可灵 即梦 失败 边界`、`视频生成 分辨率 积分 成本`。
- 海外：`AI video artifacts failure modes official`、`Firefly video credits resolution queue limit`、`Runway prompt mismatch refund`。

### 处理

- **已晋升：** [探索稿先按分辨率设积分上限再升清](./general-firefly-resolution-credit-preflight.md)。
- **待核验：** 不同分辨率探索稿升清后的构图/动作保持率缺同 brief 可审计样本。
- **淘汰 / 合并：** Seedance 宫格少于 15 格、参考负载、Runway 最小运动描述与错误分流已有 atom；营销稿“成功率提升”缺样本。

## platforms｜平台技巧

### 搜索尝试

- 中文：`抖音 快手 B站 AI 内容 审核 限流 官方`、`微短剧 平台 重新审核 同质化`、`AI 视频 平台 申诉 SLA`。
- 海外：`YouTube Shorts series seasons episodes official`、`TikTok AI label distribution official`、`AI mass produced demonetization`。

### 处理

- **已晋升：** [YouTube Shorts 连载按季集元数据与顺序播放打包](./platforms-youtube-shorts-series-package.md)。
- **待核验：** Shorts series 的账号/地区开放范围、推荐权重与申诉 SLA 未公开。
- **淘汰 / 合并：** YouTube 批量模板不可变现、TikTok AI 标签不自动影响分发、国内微短剧正片与宣推整包审核均已有 atom。

## types｜类型技巧

### 搜索尝试

- 中文：`AI 漫剧 微短剧 类型 失败 完结 官方`、`数字人口播 连载 评审`、`AI 微短剧 精品 创作 标准`。
- 海外：`creator-led vertical micro-series feed native official`、`microdrama retention failure`、`faceless series originality`。

### 处理

- **已晋升：** [TikTok 竖屏微系列先验证创作者与信息流原生性](./types-tiktok-creator-led-feed-native-series.md)。
- **待核验：** 海外平台仍未公开竖屏系列落选/弃剧的分集漏斗和可复制成本样本。
- **淘汰 / 合并：** B站赛事评审维度只适用于赛事且与昨日条目重叠；播放战报不反推类型成功公式；YouTube 微短剧 60 秒案例不外推为硬时长规则。

## pipeline｜制作管线

### 搜索尝试

- 中文：`视频生成 API 并发 失败计费 资源包 用尽`、`即梦 Seedance 样片 成片 独立计费`、`制作瓶颈 返工 积分`。
- 海外：`AI video credit burn cancel stuck generation`、`Veo pricing count bottleneck`、`video generation concurrency failure refund`。

### 处理

- **已晋升：** [即梦 API 把成功计费、并发与资源包溢出设成三道门](./pipeline-jimeng-concurrency-overage-gate.md)。
- **待核验：** 技术成功但业务不可用的真实比例、并发扩容 SLA 和项目级平均排队时间未公开。
- **淘汰 / 合并：** Runway 预占/返还、Seedance 资源包到期、Kickart 预扣/净扣已有条目；crawler 聚合稿缺厂商原始参数，淘汰。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 短剧 投流 ROI 亏损 回款 复盘`、`创作激励 结算 回撤 官方`、`AI 漫剧 变现 成本`。
- 海外：`AI video creator ROI failure breakdown`、`Shorts series membership monetization official`、`demonetization repetitive content`。

### 处理

- **已晋升：** 无。现有可靠来源没有给出可复用的全成本—归因回款闭环。
- **待核验原子：** [YouTube 连载会员续集漏斗先验证功能再计收入](./growth-youtube-members-only-series-funnel-pending.md)：缺完整上线范围、资格、结算和转化基线。
- **淘汰 / 合并：** TikTok Creator Rewards 的一分钟、原创与排除 Duet/Stitch/赞助内容已多次记录但仍缺 AI 原创细则；YPP 合格观看、B站三门槛和 Facebook 合格观看已有 atom；奖金上限不当作 ROI。
- **缺口原因：** 当前一手来源多为资格/功能公告，不披露创作者项目的制作、投放、退款、回撤与净回款全账；因此不把潜在功能晋升为确定变现策略。

## compliance｜合规与风控

### 搜索尝试

- 中文：`AI 视频 商业使用 条款 平台 官方`、`生成合成 标识 备案 处罚`、`肖像 声音 AI 微短剧 授权`。
- 海外：`AI video commercial use terms official`、`synthetic media disclosure copyright`、`likeness voice takedown enforcement`。

### 处理

- **已晋升：** [B站内置 AI 产物商用前先核单独授权](./compliance-bilibili-ai-function-commercial-boundary.md)。
- **待核验：** B站各具体 AI 功能是否存在活动或企业合同的另行商用授权，需按实际功能逐项查证。
- **淘汰 / 合并：** 中国显式/隐式标识、AI 微短剧逐集标识、肖像声音授权、重新播出再审核和版权通知包均已有 atom；海外跨法域统一授权模板不存在可靠一手闭环。

## 访问、噪声、反证与去重记录

1. crawler 的 Google News RSS 全部被 robots 拒绝；未绕过访问控制，也未把搜索摘要当事实。
2. crawler 唯一 NetNewsLedger 文章为泛化二手稿，缺原始产品参数和失败/成本证据，被 Adobe、火山引擎、YouTube、TikTok 与 B站一手来源替代。
3. Sora 旧模型价格页与当前停用公告冲突；以停用公告为准，旧价格不晋升。
4. “AI 标签必然限流”继续被 TikTok 官方说明反驳；作为已知反证合并，不重复落条。
5. YouTube/TikTok 的平台战报和合作项目播放量只证明案例发生，不证明普通账号 ROI 或因果。

## 地区与质量说明

发现池约 65:35；国内优先监管、平台和模型厂商官方，海外优先 YouTube、TikTok、Adobe、Google 与 Runway 官方。未为比例加入弱来源。`growth` 今日没有普通原子，但有明确待核验项；昨日该维度已有晋升，因此尚未触发连续两日优先补扫，仍将全成本 ROI 作为下一轮首要缺口。

