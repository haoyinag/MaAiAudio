# 通用技巧 · 本维精选

阅读层。出处路径指向 `v0/inbox/...`；数字/作者自报保留「待核」。

## 1. 参考包与质检先于开渲

- 参考包至少正 / ¾ / 侧 / 背 + 面部特写；换装、受伤、时间跳跃单独做「状态表」。
- 质检阶梯盯眼距、下颌等硬指标；手挡脸视为硬失败，先修参考再重生，不从零重抽角色。
- 七步清单收束为：锚镜锁定 → 单镜修复；master 人设 + 跨镜固定模型/画幅；末帧续接短视频。

来源日：09-10、09-11。原子：`v0/inbox/2026-09-10/dimensions/general/2026-09-10-seedance-refpack-qc.md`、`.../2026-09-10-soulvid-consistency-checklist.md`、`.../2026-09-10-piclumen-master-endframe.md`、`v0/inbox/2026-09-11/dimensions/general/2026-09-11-state-sheet-shot-chain.md`。

## 2. 同场连续镜引用上一镜实际输出

- shot chaining：同场连续镜挂上一镜**实际输出**，不挂概念图。
- 剧本规避：长对白口型、跨镜固定道具、群演、单镜硬切、>5s 情绪凝视；优先反应镜头、旁白、短句。
- 分镜阶段拍板，生成阶段只批选；高成本戏先竖向复合关键帧再喂生成器。

来源日：09-11。原子：`v0/inbox/2026-09-11/dimensions/general/2026-09-11-write-around-model-limits.md`、`.../2026-09-11-approve-storyboard-batch-select.md`。

## 3. 资产与分镜表对模型无关

- 剧本、分镜表、角色 bible、提示词库、发布检查清单可复用；换生成器是生产决策，不是推倒重来。
- 分镜用 JSON/Excel 结构化字段，可直接粘贴下游生图；主角色备 3–5 张多角度参考；每镜抽 3–4 张选 1，风格关键词全程统一。
- 一致性漂移、叙事不连贯、手/群演崩、口型难、版权备案写入质检，不当成模型玄学。

来源日：09-12。原子：`v0/inbox/2026-09-12/general-01-storyboard-table-batch.md`、`v0/inbox/2026-09-12/general-03-model-agnostic-assets.md`。

## 4. 时间盒与成片抛光

- 工作室 8 步时间盒（约 3 小时）：能并行就并行；先 60 分跑通再抠画质。
- 发布前查：引导关注、时长 60–180s、音画同步、字幕错字、串脸。
- 终剪约 3:1 生成比（每镜约 3 候选）；多模型默认调色不同，成片统一一条 cinematic LUT。
- 即便 Veo/Kling 有原生环境音，仍加一层音乐床——AI 环境音当纹理，不宜当唯一音轨；在自然动作完成点剪，不在动作中途硬切。

来源日：09-12、09-13。原子：`v0/inbox/2026-09-12/general-02-three-hour-parallel-sop.md`、`v0/inbox/2026-09-13/general-01-3to1-lut-ambient-texture.md`。
