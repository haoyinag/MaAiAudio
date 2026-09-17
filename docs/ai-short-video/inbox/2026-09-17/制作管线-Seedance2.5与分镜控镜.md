# 制作管线：Seedance 2.5 / 控镜 / 角色一致 / 成本记账

- https://domer.io/blog/ai-video-creation-workflow-guide-ba6e225a （2026-09-15）
- https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 （2026-07-31）
- http://www.pwwt.cn/news/4476539/
- https://www.seeddance.io/blog/create-ai-short-drama-videos-seedance-2-5
- https://www.kling4.co/blog/how-to-make-ai-micro-drama-2026

## 要点
1. 2–6s（可用常仅 1–3s）一动作一镜；音效杠杆最高；对白约 -12~-6 dBFS，音乐低 6–12dB；先音后画。
2. Seedance 2.5：单次最长约 30s + 多轮续写；最多约 30 图 / 10 视频 / 10 音频参考；时间戳级编辑。
3. 角色一致性：固定描述词 → 定妆参考图 → 首帧图生视频 → 进阶 LoRA；负向提示防崩脸/多肢。
4. 成本记账单位：`approved shots + rejects + audio/lip-sync + edit`，勿报死单价。
5. 第三方量级参考：约 18 镜/集、5s/镜、一季约 60 集；瓶颈是脸一致而非渲染价。
