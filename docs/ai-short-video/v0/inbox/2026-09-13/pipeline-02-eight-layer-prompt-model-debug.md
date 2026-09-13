# 八层提示词 + 按模型调试层

- 维度：制作管线
- 日期：2026-09-13

## 一句话

先写一套模型无关的八层 brief；失败只改一层。再按最难点叠各模型自己的调试层，不要按排行榜选模。

## 要点

- 通用八层：Reference / Shot label / Subject / Action / Camera / Scene+lighting / Audio|timing / Constraints。一层只答一个问题，避免同一句里塞互斥机位。
- 失败只改一层：主体漂先改 Subject/Reference，动作空先改 Action，机位乱先改 Camera。禁止整段重写。
- 模型调试层（相对 09-11/09-12 的戏型路由与 Binding 专条，本条只记提示词控制面）：
  - Runway Gen-4.5：force-reaction（因果物理链）+ Motion Sketch
  - Kling 3.0：Elements / Bind Subject；对白须写 face + camera，只写台词表情会随机
  - Veo 3.1：`says:` / `SFX:` / `Ambient:` 当作控制面，不是装饰标签
  - Seedance 2.0：`@character` / `@product` / `@scene` / `@style` 标签锚定用途
- 选型按最难点：物理→Runway；脸一致/对白→Kling；伪真+原生音频→Veo；品牌资产锚定→Seedance。

## 可执行

- 每镜先填八层骨架；生成失败时只改被证伪的那一层，其余层冻结。
- 物理接触/动量镜：把动作改写成力→阻力→形变→下一步，并用 Motion Sketch 画路径。
- 对白镜：Kling 写「谁说 + face + camera」；Veo 用 `says:` / `SFX:` / `Ambient:`，勿把音效写进动作层当画面指令。
- 有品牌图/产品/场景/风格参考时，Seedance 用 `@` 标签逐项绑定，禁止无标签堆参考。
- 选模只看本镜最难点，不按「哪个模型更好」一刀切。

## 来源

- URL: https://aiworkflowpro.com/ai-video-prompt-framework/
- 日期: 2026-09-15（文标 Sep 15, 2026；日期晚于扫描日，仍按页面标注）
- 扫描日: 2026-09-13
- 备注: 页面日期异常（扫描日 09-13、文标 09-15），不另推日期；模型层为来源作者归纳，待核
