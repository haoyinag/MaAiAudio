# 四层流水线：Shot List→关键帧→图生视频→后期

标签: 工程化,Runway,可灵,ElevenLabs

## 要点
- LLM 结构化 Shot List（景别/运镜/对白/时长）
- 文生图关键帧 + LoRA/IP-Adapter/ControlNet 锁角色风格
- 图生视频 2–5 秒，优先首尾帧控制；同场景同 seed、CFG 约 7–9
- 导入 PR/达芬奇 + 超分插帧 + ElevenLabs/EdgeTTS

## 来源
- URL: https://developer.cloud.tencent.com/article/2737763
- 日期: 2026-09-05
- 扫描日: 2026-09-10
