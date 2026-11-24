# SCAN 2026-11-24

> 模式：每日采集；时区：Asia/Shanghai。先完成六维中外广泛发现（技巧、端到端工作流、行业困境/失败/成本边界、变现），再打开原始来源分层核验、全库去重并写入。

## 覆盖总览

- crawler `coverage`：`general=0 / platforms=1 / types=1 / pipeline=0 / growth=0 / compliance=1`；`region_counts`：国内 1、海外 0。唯一 Sohu 条目只是二手发现线索，不能定义今日广度。
- 六维均低于每维 8 条发现目标，因此全部补扫；负向检索显式覆盖制作瓶颈、失败拆解、废片/credit burn、拒审/限流、demonetization、ROI 和变现困局。
- 定向搜索与全库去重后形成 51 条主题/来源候选：国内 33、海外 18（约 65:35）。晋升 6、待核验 12、淘汰/合并 33；计数按主维度归档，跨维来源只计一次。

| 维度 | 去重后候选 | 国内 / 海外 | 晋升 | 待核验 | 淘汰 / 合并 |
| --- | ---: | ---: | ---: | ---: | ---: |
| general | 8 | 5 / 3 | 1 | 2 | 5 |
| platforms | 9 | 6 / 3 | 1 | 2 | 6 |
| types | 8 | 5 / 3 | 1 | 2 | 5 |
| pipeline | 9 | 6 / 3 | 1 | 2 | 6 |
| growth | 8 | 5 / 3 | 1 | 2 | 5 |
| compliance | 9 | 6 / 3 | 1 | 2 | 6 |
| **合计** | **51** | **33 / 18** | **6** | **12** | **33** |

## general｜通用技巧

### 搜索尝试

- 中文：`AI 视频 控制项 互斥 首尾帧 参考 官方`、`视频生成 失败拆解 参考冲突 废片`、`Seedance 可灵 万相 控镜 边界`。
- 海外：`AI video controls incompatible first last frame official`、`generation artifacts failure modes reference conflict`、`video prompt control boundary`。

### 处理

- **已晋升：** [生成前先选兼容的控镜家族](./general-firefly-control-family-preflight.md)。
- **待核验：** Firefly 控制互斥是否随 Beta 退出而变化；相同 Seed 的镜头级相似性缺可审计重复实验。
- **淘汰 / 合并：** Runway 错误分流、输入净化、固定 Seed 单变量迭代均已有条目；营销稿中的“成功率提升”缺基线与样本。

## platforms｜平台技巧

### 搜索尝试

- 中文：`AI 微短剧 平台 专项治理 同质化 首页 榜单`、`抖音 快手 B站 AI 内容 限流 拒审`、`微短剧 换名 重播 宣推 治理`。
- 海外：`YouTube AI mass produced demonetization official`、`TikTok AI label distribution official`、`Facebook Reels originality enforcement`。

### 处理

- **已晋升：** [微短剧发布前验收正片与宣推全包](./platforms-microdrama-whole-package-preflight.md)。
- **待核验：** 国内平台没有公开同质化检测阈值与申诉 SLA；B站个人创作激励资格与 AI 影视片场能否叠加缺同一官方规则闭环。
- **淘汰 / 合并：** YouTube 模板内容不可变现、Facebook 低价值改动、TikTok AI 标签不自动降分发均已有条目；crawler 的 Sohu 评论由广电总局一手来源替代。

## types｜类型技巧

### 搜索尝试

- 中文：`AI 漫剧 片场 签约 完整度 断更 官方`、`AI 微短剧 类型 同质化 失败样本`、`数字人口播 漫剧 连载 验收`。
- 海外：`AI vertical series narrative completion official`、`faceless series failure retention`、`AI microdrama genre acceptance`。

### 处理

- **已晋升：** [B站 AI 连载先按完整性与持续更新门禁立项](./types-bilibili-ai-series-format-gate.md)。
- **待核验：** B站 AI 创作大赛的故事/技术/创意/艺术评分只适用于赛事；海外竖屏系列仍缺公开的类型落选复盘。
- **淘汰 / 合并：** 只公布播放战报或入选名单的来源不反推类型方法；季级连续性、故事辨识度和音频转 Shorts 已覆盖。

## pipeline｜制作管线

### 搜索尝试

- 中文：`AI 商品视频 素材未使用 分镜 手动替换 官方`、`视频生成 预扣 失败退款 创点`、`制作瓶颈 返工 废片 积分`。
- 海外：`AI video credit burn failed generation refund official`、`video generation control workflow bottleneck`、`Veo pricing audio resolution`。

### 处理

- **已晋升：** [Kickart 分镜先锁素材再把预扣与净扣分账](./pipeline-kickart-asset-and-credit-gates.md)。
- **待核验：** Google Cloud Veo 价格页的适用区域 SKU 与项目实际计费单位需闭环；Kickart 返还到账时延和素材选择命中率未公开。
- **淘汰 / 合并：** Runway 预占—退款、失败返积分、Seedance 资源包到期和万相输入输出计费均已有条目；搜索结果页中的无来源成本数字淘汰。

## growth｜增长变现

### 搜索尝试

- 中文：`AI 影视 片场 激励 结算 回撤 独家 官方`、`AI 漫剧 分账 ROI 亏损 回款`、`短剧 投流 全成本 失败复盘`。
- 海外：`AI video creator ROI failure breakdown`、`Shorts demonetization cost boundary`、`creator rewards qualified views clawback`。

### 处理

- **已晋升：** [B站 AI 影视激励按三门槛、回撤与独家成本算账](./growth-bilibili-three-gate-incentive-ledger.md)。
- **待核验：** 平台未披露平均签约/回撤率与自然分发增量；跨平台同项目的全成本—归因回款样本仍缺。
- **淘汰 / 合并：** 爱奇艺平台收入基数、YouTube/YPP 合格观看、Facebook 合格观看和 TikTok Creator Rewards 旧公告已有条目或既有待核验；奖金最高档不当作普遍收益。

## compliance｜合规与风控

### 搜索尝试

- 中文：`微短剧 版权 通知 删除 批量投诉 24小时 官方`、`AI 视频 盗脸 偷声 授权 判决`、`生成合成 标识 备案 处罚`。
- 海外：`AI likeness voice takedown official`、`synthetic media disclosure copyright complaint`、`AI impersonation enforcement`。

### 处理

- **已晋升：** [微短剧版权投诉先备齐可批量核验的通知包](./compliance-microdrama-copyright-notice-package.md)。
- **待核验：** 24 小时目标在各平台的实际完成率与补件规则未公开；海外拟声/肖像商业使用仍无可跨法域复用的统一通知模板。
- **淘汰 / 合并：** crawler 的“盗脸/偷声”评论与既有明确授权条目重复且为二手；AI 显式/隐式标识、逐集标识与委托方审核已覆盖。

## 访问、噪声与反证记录

1. crawler 的 Google News RSS 均被 robots 拒绝；未绕过，也未把摘要当事实来源。
2. Sohu “盗脸/偷声”评论与现有原子重复，且可被广电总局、国家版权局等一手来源替代，淘汰。
3. 火山引擎文章聚合页存在无原始参数或内部不一致数字；只采用产品文档中心可直接核验内容。
4. “AI 标签必限流”被 TikTok 官方说明反驳；继续按既有条目处理，不重复晋升。

## 地区与质量说明

发现池约 65:35；国内优先监管部门、平台与模型厂商官方，海外优先 Adobe、Google、YouTube、TikTok、Meta 与 Runway 官方。没有为比例加入弱来源。六维今日均有晋升，无连续两日缺席维度；但海外类型失败复盘和跨平台可审计 ROI 仍是结构性缺口。
