# Comfy 漫剧：I2V 与口型镜分轨再剪

标签: ComfyUI,图生视频,口型

## 要点
- 产线：角色库 → 分镜表 → 静帧 batch → 锁定 keyframe → Wan I2V → 口型镜（SadTalker/S2V）单独 → 放大补帧 → 剪辑配音字幕
- 单镜 I2V 3–6s 最稳；约 1 分钟 ≈ 10–15 镜；对白镜勿与普通 I2V 混生成
- 同场连续：镜 N 末帧作镜 N+1 首帧；换场硬切勿强衔接
- 失败：脸 drift 降 motion/缩短；背景闪加 static background；崩手先修 keyframe 再 I2V
- 评审门：签字 keyframe 后再 I2V，勿对废分镜烧视频算力

## 来源
- URL: https://www.circler.cn/course_info/166/
- 日期: 2026-07-08
- 扫描日: 2026-09-11
