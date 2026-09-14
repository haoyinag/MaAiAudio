# Seedance 行为型提示词 vs Kling 电影语言

- 维度：制作管线
- 日期：2026-09-13

## 一句话

Kling 吃 cinematic 词库；同一套滤镜词搬到 Seedance 常变差。Seedance 更吃「主体在做什么、表情如何变」。

## 要点

- 社区经验：Kling 常用 cinematic 词库（景深 / 胶片颗粒 / golden hour）有效；原样搬到 Seedance 常得到平庸结果。
- Seedance 更吃 behavioral prompts：写主体动作与表情变化，例如「年轻女性缓缓转向镜头，表情从走神变为惊讶」，优于堆滤镜词。
- 角色一致：正脸中性头像 + 45° 侧脸双锚，项目开始就锁定，中途不换「更好看」的参考。
- 单镜约 4–6s 防漂移；约 60s 成片拆 12–15 短镜再剪（作者经验，待核）。本条不重开 09-12「即梦+可灵 2–4s」组合。

## 可执行

- Seedance 提示词库按行为重写：主体动作 + 表情变化优先，滤镜词降级或删除。
- 每个项目先产出并锁定两张锚图：正脸中性头像、45° 侧脸；后续镜只复用，不中途换参考。
- 角色向成片按 4–6s 单镜生成；约 60s 目标先拆 12–15 短镜再剪（作者经验，待核）。
- 禁止把 Kling 的 cinematic 词库整段粘到 Seedance 当「电影感补丁」。

## 来源

- URL: https://www.reddit.com/r/aitubers/comments/1sser4x/how_seedance_20_restructured_my_ai_tuber_content/
- 日期: 见扫描日（社区帖，无稳定文内日期）
- 扫描日: 2026-09-13
- 备注: 作者自报工作流；4–6s / 12–15 镜为作者经验，待核
