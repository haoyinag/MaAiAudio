# 制作管线精选

## 当前最优解法 (Do)

- **Runway 预扣与净成本分列。** 以预扣检查提交额度，待退款入账后用扣款减退款对账；异常或未配对项目保留待对账状态。
- **Flow 切换前复跑代表镜头。** 导出在制片段和逐镜配置，分别测试普通、长时和延展镜头，按套餐记录产出份数、时长和净扣积分。

## 已知困境与避坑边界 (Don't / Bottlenecks)

- **Runway 预扣与净成本分列。** Runway 将部分自动时长或视频编辑任务按上限预扣。净积分仍需结合实际购买成本和废片记录，退款时间以账单为准。 [inbox 原子稿](../../../inbox/2026-11-23/pipeline-runway-reserved-final-credit-reconciliation.md) · [原始来源](https://help.runwayml.com/hc/en-us/articles/55412733862675-Why-do-I-see-a-charge-and-a-refund-for-the-same-generation)
- **Flow 切换前复跑代表镜头。** Google Flow 帮助公告 2026-12-05 停用 Veo 3.1 Fast、Quality 和 Omni Flash 1.1，建议迁往 Omni Flash 1.2 或 Veo 3.1 Lite。新模型功能与计费不同，一次请求可生成多份结果；这个日期只适用于 Flow。 [inbox 原子稿](../../../inbox/2026-11-26/pipeline-flow-december-migration.md) · [原始来源](https://support.google.com/flow/answer/16526234?hl=en-GB)

来源复核于 2026-11-26（Asia/Shanghai）。Do 为根据来源整理的执行建议。
