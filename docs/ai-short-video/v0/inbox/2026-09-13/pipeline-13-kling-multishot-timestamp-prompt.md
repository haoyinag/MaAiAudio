# Kling 3.0 用时间戳分镜提示，不要写单段散文

- 维度：制作管线
- 日期：2026-09-13

## 一句话

Kling 3.0 multi-shot 把提示写成「Shot N: 00:00–00:03 + 景别/动作」的导演分镜；需要连续性时再用 start/end frame 卡住。

## 要点

- 相对 09-11「Subject Binding + 单次多镜」与上午「Kling = shot-led」：本条只记时间戳提示写法，不重开 Binding、元素库或参考包 vs 分镜表选型。
- 社区写法：先一句风格/场面，再逐镜 `Shot N: 00:00–00:03` + 景别 + 动作（例见来源帖，待核）。模型更像按导演分镜切，而不是把一段散文糊成一条长镜。
- 相邻镜写清景别变化与动作节拍，避免「一整段描写、指望它自己会切」。
- 可用 start frame / end frame 约束连续性（社区评论与另一篇管线帖均提到，待核）。
- 本条是提示结构，不是官方 API 字段说明。

## 可执行

- 开 Multi-Shot 后，提示按镜写：`Shot N: 起止时间 + 景别 + 主体动作`；禁止只丢一段场面散文。
- 时间轴先加总再写词，避免各镜秒数对不齐。
- 需要跨切不断人/不断光时，给 start frame，必要时再加 end frame；不要只靠散文里的「然后」。
- 日志保留所用分镜提示原文，便于对照哪一镜的时间戳被吃掉。

## 来源

- URL: https://www.reddit.com/r/klingO1/comments/1rt09s0/how_to_create_a_multishot_sequence_scenes_with/
- URL: https://www.reddit.com/r/generativeAI/comments/1u5io88/kling_30_video_generation_pipeline_guide/
- 日期: 见扫描日（社区帖，无稳定文内日期）
- 扫描日: 2026-09-13
- 备注: 下午补扫；时间戳格式与 start/end frame 用法为社区实操，待核
