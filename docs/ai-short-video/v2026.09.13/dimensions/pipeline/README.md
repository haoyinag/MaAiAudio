# 制作管线 · v2026.09.13

选题、脚本、生成、剪辑、发布的流程。本版约 35 条净入库（09-10=12 / 09-11=9 / 09-12=9 / 09-13=5），是本版最大维度。

默认先读 [本维精选](./highlights.md)。原子稿仅溯源，不在此整锅粘贴。

## 本维主题

- 资产锁定：角色卡 / 定妆表 / 参考预审 → 再分镜
- 分镜系统：表格字段 → 五层（goal / sequence / shot / prompt / check）
- 分模路由：Veo / Kling / Seedance / Runway / 即梦；好片 extend
- 即梦入口分流、参考权重、2–4s（或 3–5s）单镜
- 渲前四门 + 接受标准批量评审
- 音频：原生出声 vs 后期 TTS；口型分轨；道具/声线车道

## inbox 原子（按日）

### 2026-09-10

- [Seedance 2.0：角色卡 + 分镜提示词](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-seedance-rolecard-storyboard.md)
- [可灵 I2V 不崩脸参数流](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-kling-i2v-nofacebreak.md)
- [可灵导出 + 剪映后期](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-kling-capcut-post.md)
- [一人 8 分钟 AI 短剧 13 步](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-ai-drama-13step-huangguo.md)
- [四层流水线](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-four-layer-pipeline-tencent.md)
- [先分镜再生成：时长上限 + 六段式提示词](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-storyboard-sixfield-prompt.md)
- [不用 LoRA：4K 多角度定妆表](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-character-sheet-nolora.md)
- [Trae：剧本→三视图→批量 API→配音→剪映](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-trae-jimeng-batch.md)
- [HeyGen + ElevenLabs 音频先行](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-heygen-elevenlabs-audiofirst.md)
- [可灵 / Runway / HeyGen 选型](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-kling-runway-heygen-stack.md)
- [ComfyUI + Kling Motion Control](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-comfyui-kling-motion.md)
- [个人创作者推荐栈](../../../v0/inbox/2026-09-10/dimensions/pipeline/2026-09-10-creator-stack-2026.md)

### 2026-09-11

- [微短剧镜数经济学](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-microdrama-shot-economics.md)
- [开渲前锁定角色表与复发场景](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-lock-sheets-before-render.md)
- [Runway 英雄镜 + Kling 过场](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-runway-kling-hybrid-cost.md)
- [千问分镜表字段](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-qwen-storyboard-table-prompt.md)
- [Seedance：原生出声 vs 后期配音](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-seedance-native-vs-post-audio.md)
- [多智能体剧组](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-agent-crew-script-to-episode.md)
- [Kling 3.0 Subject Binding + 多镜](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-kling3-subject-binding-multishot.md)
- [渲前四道评审门](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-review-gates-before-render.md)
- [Comfy：I2V 与口型镜分轨](../../../v0/inbox/2026-09-11/dimensions/pipeline/2026-09-11-comfy-i2v-lipsync-split-lanes.md)

### 2026-09-12

- [道具连续性与声线分轨](../../../v0/inbox/2026-09-12/pipeline-01-prop-voice-lanes.md)
- [按镜分模矩阵与 extend](../../../v0/inbox/2026-09-12/pipeline-02-model-matrix-extend.md)
- [即梦+可灵：2–4s 单镜](../../../v0/inbox/2026-09-12/pipeline-03-jimeng-kling-batch.md)
- [电影感资产圣经](../../../v0/inbox/2026-09-12/pipeline-04-cinematic-asset-bible.md)
- [物理调度提示词](../../../v0/inbox/2026-09-12/pipeline-05-physical-prompt-direction.md)
- [戏型分模：Veo / Kling / Seedance](../../../v0/inbox/2026-09-12/pipeline-06-veo-kling-seedance-shot-routing.md)
- [Seedance R2V 宽镜链](../../../v0/inbox/2026-09-12/pipeline-07-seedance-r2v-spatial-chain.md)
- [即梦参考权重与运动三要素](../../../v0/inbox/2026-09-12/pipeline-08-jimeng-ref-weight-motion-capcut.md)
- [开渲前接受标准 + 批量评审](../../../v0/inbox/2026-09-12/pipeline-09-acceptance-criteria-batch-review.md)

### 2026-09-13

- [五层分镜](../../../v0/inbox/2026-09-13/pipeline-01-seedance-five-layer-storyboard.md)
- [八层提示词 + 模型调试层](../../../v0/inbox/2026-09-13/pipeline-02-eight-layer-prompt-model-debug.md)
- [Seedance 行为型 vs Kling 电影语言](../../../v0/inbox/2026-09-13/pipeline-03-seedance-behavioral-vs-kling-cinematic.md)
- [即梦首尾帧 vs 全能参考](../../../v0/inbox/2026-09-13/pipeline-04-jimeng-first-last-vs-omni-ref.md)
- [角色参考预审再进视频](../../../v0/inbox/2026-09-13/pipeline-05-character-ref-precheck-before-gen.md)
