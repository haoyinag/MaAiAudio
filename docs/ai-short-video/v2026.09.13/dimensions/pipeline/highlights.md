# 制作管线 · 本维精选

阅读层。出处路径指向 `v0/inbox/...`。镜数、时长、价格均为作者/厂商自报，保留「待核」。

## 1. 先锁资产，再开分镜

- 角色卡 / 定妆表 / 参考包 → 再分镜生成；漂变先修参考再重生。定妆表可无 LoRA（4K 多角度）。
- 开渲前锁定角色正/侧/¾/面部特写 + 复发场景；迭代一律改锁定底图，禁止从零重生。
- 写实真人角色：参考图先导入资产库完成审核，再用于视频生成，否则「真人视频」类调用常无明确原因失败。
- 电影感资产圣经：角色 7-panel turnaround、场景 wide plate、复发道具独立参考、每角一条音色；中途禁止重生 bible。
- 终场关键道具须在更早场出现并写入 continuity note。

来源日：09-10、09-11、09-12、09-13。原子例：`v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-character-sheet-nolora.md`、`v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-lock-sheets-before-render.md`、`v0/inbox/2026-09-12/pipeline-04-cinematic-asset-bible.md`、`v0/inbox/2026-09-13/pipeline-05-character-ref-precheck-before-gen.md`。

## 2. 分镜：从表到五层

- 四层流水线仍成立：LLM Shot List → 关键帧 → 2–5s 图生视频 → PR/达芬奇/剪映；单镜一动作；先通 1 镜再批量。
- 千问分镜表字段：镜头号|时长|景别|运镜|画面描述(≤50字)|台词|角色|BGM/音效|情绪|转场；前 3 秒强视觉钩子。
- 本版升级为五层：goal → sequence → shot → prompt → check。短片常用 3–6 镜；每镜写 framing / 运镜 / 动作 / 光 / 转场。
- prompt 含 Continuity + Constraints；转场对（运动/形状/色/动作/景别匹配）写进分镜，不只靠剪辑。
- 开渲前写死接受标准：产品可辨、服装不变、运镜平滑、末帧可接下一镜；批量生成、批量评审，只重生失败镜。
- 渲前四道门：角色 / 分镜 / 声线 / 预算过门再渲；一镜一职。

来源日：09-10、09-11、09-12、09-13。原子例：`v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-four-layer-pipeline-tencent.md`、`v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-qwen-storyboard-table-prompt.md`、`v0/inbox/2026-09-13/pipeline-01-seedance-five-layer-storyboard.md`、`v0/inbox/2026-09-12/pipeline-09-acceptance-criteria-batch-review.md`。

## 3. 分模路由与成本

- 按最难点选型：物理 → Runway（force-reaction + Motion Sketch）；脸一致/对白 → Kling（Elements/Bind Subject，对白须写 face+camera）；伪真+原生音频 → Veo（`says:` / `SFX:` / `Ambient:`）；品牌资产锚定 → Seedance（`@character/@product/@scene/@style`）。
- 戏型：情绪特写/英雄钩子 → Veo；双人对白/正反打 → Kling；主角/复现场景 → Seedance 2.0 R2V。
- 矩阵补充：PixVerse C1≈分镜面板连续；Wan≈量大便宜预览。identity 用 R2V，有起止用 first-last-frame，动作用 motion control。
- 好片 extend、坏片才 regenerate。Kling 3.0 Bind Subject 后约 15s 内最多 6 切（待核）。
- 混模降本：Runway 做 5–8 个英雄镜，Kling 做大量过场；宣称可降视频生成成本约 50–70%（作者宣称，待核）。
- 镜数经济学：9:16、单集 60–120s、约 5s/镜 → 90s ≈ 18 次渲；Lite≈$18/集 到 Omni≈$73/集（厂商自报待核）；便宜档打通节奏，只对情绪英雄镜升档。

来源日：09-10、09-11、09-12、09-13。原子例：`v0/inbox/2026-09-12/pipeline-06-veo-kling-seedance-shot-routing.md`、`v0/inbox/2026-09-13/pipeline-02-eight-layer-prompt-model-debug.md`、`v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-runway-kling-hybrid-cost.md`。

## 4. 提示词：八层通用 + 按模型调试

- 通用八层：Reference / Shot label / Subject / Action / Camera / Scene+lighting / Audio|timing / Constraints；失败只改一层。
- Kling 常用 cinematic 词库（景深 / 胶片颗粒 / golden hour）有效；同一套搬到 Seedance 常变差。Seedance 更吃 behavioral prompts（主体在做什么、表情如何变化）。
- 物理调度：写肌肉级微表情与机位遮挡，不写叙事情绪词；静止须显式约束；VO 后期加，口播才进 prompt。
- 角色一致：正脸中性头像 + 45° 侧脸双锚；单镜约 4–6s 防漂移；约 60s 成片拆 12–15 短镜再剪（作者经验，待核）。

来源日：09-12、09-13。原子：`v0/inbox/2026-09-13/pipeline-02-eight-layer-prompt-model-debug.md`、`v0/inbox/2026-09-13/pipeline-03-seedance-behavioral-vs-kling-cinematic.md`、`v0/inbox/2026-09-12/pipeline-05-physical-prompt-direction.md`。

## 5. 即梦与可灵实操

- 可灵：优先 I2V；脸静布料动；5s 多抽一选；extend 只一次；成片进剪映补色与口型。
- 即梦入口：仅首帧图+prompt →「首尾帧」；多模态 →「全能参考」，用 `@素材名` 指定用途。社区称全能参考常见上限约 9 图 + 3 视频 + 3 音频、素材时长约 ≤15s（以产品实际 UI 为准，待核）。
- 人物参考权重约 0.7–0.8（过高僵、过低锁不住脸，待核）；提示词首尾重复五官/服装。
- I2V 写人物动作+运镜+环境动态，幅度轻微/缓慢；单镜黄金约 2–4s（上午）与常见 3–5s（下午）并存，均为作者口径待核。可导出剪映工程。
- Seedance R2V：每场先宽建立镜作空间锚，后续镜挂上一镜**视频**作空间/光/站位参考。

来源日：09-10、09-12、09-13。原子例：`v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-kling-i2v-nofacebreak.md`、`v0/inbox/2026-09-13/pipeline-04-jimeng-first-last-vs-omni-ref.md`、`v0/inbox/2026-09-12/pipeline-08-jimeng-ref-weight-motion-capcut.md`、`v0/inbox/2026-09-12/pipeline-07-seedance-r2v-spatial-chain.md`。

## 6. 音频、口型、口播栈

- Seedance：提示词原生出声（快、口型难精控，适合试播）vs 只出画面后期 TTS（统一音色与字幕）；环境音不齐则压原声铺整集 BGM。
- 多角色建 voice lane，对白可落反应镜/插入镜；草稿画质先判节奏再终渲。
- Comfy：keyframe 签字后再 Wan I2V；口型镜（SadTalker/S2V）单独，勿与普通 I2V 混生成；单镜 3–6s，约 1 分钟 ≈ 10–15 镜。
- 口播栈：ElevenLabs 锁音频 → HeyGen 渲染；改词必重渲。
- 成片用多段稳定短镜拼接；生成约一半、剪辑约一半（作者经验，待核）。

来源日：09-10、09-11、09-12、09-13。原子例：`v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-seedance-native-vs-post-audio.md`、`v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-comfy-i2v-lipsync-split-lanes.md`、`v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-heygen-elevenlabs-audiofirst.md`。
