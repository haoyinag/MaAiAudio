# pipeline 精选｜参考视频成本同时计算输入与成功输出

## 当前最优解法 (Do)

- Wan 3.0 成本台账记录 `task_type / region / input_seconds / successful_output_seconds / current_price`；含视频输入任务按输入与成功输出秒数之和估算。
- 输入前裁掉无用片头片尾，但保留任务所需动作和时序；每次预算评审重新打开官方价格页。
- 来源：阿里云百炼当前价格页；provenance 见 [原子稿](../../../inbox/2026-11-20/pipeline-wan3-input-output-billing-boundary.md)。

## 已知困境与避坑边界 (Don't / Bottlenecks)

- 不把只按成功输出计费的其他任务公式套到含视频输入任务，也不把失败不收费理解为成功但不可用可退款。
- 2026-11-20 复核时，Wan 3.0 当前价格页列明无免费额度；原子稿中的旧免费额度读取未晋升。具体单价、折扣与区域都属易变事实。