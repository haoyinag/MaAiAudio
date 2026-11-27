# 2026-11-27 六维扫描账本

爬虫覆盖 general 0、platforms 0、types 0、pipeline 2、growth 0、compliance 0，国内 0、海外 2。Google News RSS 被 robots 拒绝，两个 Bing RSS 线索保留在管线账。六维都追加了中英文检索。先补搜技巧、制作工作流、失败返工、积分成本、拒审与取消变现、投放亏损，再打开拟采用原文，并以来源标识和主题词检索全库 Markdown（含历史摘要、原子、正式快照及 PLAYBOOK）。

表格记录 49 条进入裁决的线索，含一条同文镜像拒收记录。国内 30、海外 19（约 61:39），晋升 7、待核验 19、淘汰 23。待核验和淘汰项可依据检索摘要作线索筛选，未作为事实采用。11-25 的增长缺口于 11-26 已有晋升，未出现连续两次扫描无晋升的维度；本轮继续补搜完整 ROI 账。

## general

候选 8 条（晋升 1、待核验 4、淘汰 3）。

- 检索词 `AI短视频 可灵 官方 多镜头 运镜 一致性 失败 首尾帧` · `AI video shot continuity camera control failures official Runway` · `可灵 万相 官方 首尾帧 多镜头 提示词 失败` · `Runway image to video prompting guide limitations camera`
- 缺口 缺同镜头字幕发生率、裁切损失和可用率对照。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [Seedance 竖屏对白先验无字底片](https://docs.volcengine.com/docs/ark/seedance-2-0-prompt-guide?lang=zh) | 中 | 已晋升 | [原子稿](./general-seedance-clean-caption.md) |
| [可灵 O1 - 视频 O1 使用指南 - 轻雀文档](https://docs.qingque.cn/d/home/eZQCg5xHvxDaE-jP2GcnaNc6O?identityId=2E1MlYrrPk4) | 中 | 待核验 | 需同镜头连续性对照与失败日志 |
| [可灵-视频生成API文档 - 阿里云百炼](https://docs.bailian.console.aliyun.com/zh/model-studio/kling-video-generation-api-reference) | 中 | 待核验 | 需核对百炼接入与可灵原生版本的能力差异 |
| [Kling（可灵）AI 视频高级运镜与对口型实战：解决人物穿模、手指变形与多镜头衔接统一（2026-11 更新）- 贝果科技](https://bigolab.com/guides/5654-kling-ai-video-camera-lip-sync-clipping-hands-fix) | 中 | 淘汰 | 第三方教程无可复核的失败样本 |
| [可靈3.0系列模型全面上線 開啟「人人皆可當導演」的新時代](https://ir.kuaishou.com/zh-hant/node/11216/pdf) | 中 | 待核验 | 需核对功能上线地区及可用套餐 |
| [Autodesk's own AI film has a continuity error nobody could prompt aw](https://www.creativebloq.com/3d/autodesks-own-ai-film-has-a-continuity-error-nobody-could-prompt-away) | 外 | 待核验 | 缺原片时间码与重试日志 |
| [Image to Video Prompting Guide – Runway](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide?trk=article-ssr-frontend-pulse_little-text-block) | 外 | 淘汰 | 重复 11-12 清理冲突运动线索 |
| [Why doesn’t my generation match my prompt? – Runway](https://help.runwayml.com/hc/en-us/articles/56617505841939-Why-doesn-t-my-generation-match-my-prompt) | 外 | 淘汰 | 与 11-18 完成但不可用的重试边界重复 |

## platforms

候选 8 条（晋升 1、待核验 2、淘汰 5）。

- 检索词 `抖音 快手 B站 AI 短视频 低质 重复 限流 官方 创作者` · `YouTube TikTok Shorts inauthentic demonetization AI official` · `哔哩哔哩 快手 官方 AI 声明 投稿 低质 治理` · `TikTok For You unoriginal QR code monetization original official`
- 缺口 缺拒审到恢复的账号时间线与推荐系统实测。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [抖音小程序推广稿按挂载规则验收](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/platform-capabilities/video/video-creator-promote-mount-mgmt-spec) | 中 | 已晋升 | [原子稿](./platforms-douyin-anchor-review.md) |
| [短视频创作者管理规范_小程序_抖音开放平台](https://partner.open-douyin.com/docs/resource/zh-CN/mini-app/operation/platform-capabilities/video/video-creator-promote-mount-mgmt-spec) | 中 | 淘汰 | 与晋升规范同文镜像 |
| [抖音关于开展“治理AI技术滥用”专项的公告（一） - 抖音安全与信任中心](https://trust.douyin.com/article/15868) | 中 | 淘汰 | 主动声明已入手册 |
| [2026年7月8日抖音创作者新规核心围绕“内容精细化、创作真实性、经营合规化”，重点扶持优质原创、打击低质违规，具体要点如下： 1. 流](https://www.douyin.com/video/7662284318068191141) | 中 | 淘汰 | 账号视频未提供官方推荐权重 |
| [哔哩哔哩关于加强虚假摆拍内容治理的公告 - 哔哩哔哩](https://www.bilibili.com/opus/1162070497975861281) | 中 | 待核验 | 缺内容整改前后和处置通知 |
| [YouTube channel monetization policies - YouTube Help](https://support.google.com/youtube/answer/1311392?hl=en) | 外 | 淘汰 | YPP 模板及批量同质化已有覆盖 |
| [YouTube's Inauthentic Content Policy - Explained! - YouTube](https://www.youtube.com/watch?v=14Vm0CiyUVE) | 外 | 淘汰 | 模板化和敏感人设取消变现与手册重复 |
| [Community Guidelines · TikTok](https://archive.is/SLCPx) | 外 | 待核验 | 需当前 TikTok 原站版本及适用地区 |

## types

候选 8 条（晋升 2、待核验 4、淘汰 2）。

- 检索词 `中国 AI漫剧 短剧 数字人 带货 平台 官方 制作 案例 返工` · `AI series talking avatar short video production workflow failure official` · `快手 可灵 官方 AI短剧 漫剧 制作 工作流 失败` · `Runway AI film case study breakdown continuity production`
- 缺口 缺弃剧、付费或带货失败的逐集数据及同镜头返工成本。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [Act-Two 双人同框对白用同一底片分人驱动](https://help.runwayml.com/hc/en-us/articles/41748090660499-Creating-Multi-Character-Dialogues-with-Act-Two) | 外 | 已晋升 | [原子稿](./types-act-two-dialogue.md) |
| [循环数字人口播分开验画面与音频接缝](https://www.alibabacloud.com/help/zh/ims/developer-reference/api-ice-2020-11-09-submitavatarvideojob) | 中 | 已晋升 | [原子稿](./types-avatar-loop-seam.md) |
| [明略科技 MININ](https://oss.ibos.cn/53ai/bot/files/a734a874d1dff5bcd95c0ecbb3fac47a/2026AI%E7%9F%AD%E5%89%A7%E8%A1%8C%E4%B8%9A%E5%8F%91%E5%B1%95%E4%B8%8E%E5%8F%97%E4%BC%97%E6%B4%9E%E5%AF%9F%E6%8A%A5%E5%91%8A.pdf) | 中 | 待核验 | 缺数字人项目嘴型与销售效果对照 |
| [制作资源中心 - 专业漫剧制作团队 · 漫剧工场](https://www.manjugongchang.com/production?available=&cap=&fmt=3D%E5%8A%A8%E7%94%BB&genre=%E5%A5%87%E5%B9%BB%2F%E5%86%92%E9%99%A9&q=&scale=&sort=&tier=&tool=%E5%8D%B3%E6%A2%A6) | 中 | 淘汰 | 供应商资源招募，缺具体生产复盘 |
| [中国网络视听节目服务协会 视听动态 WAIC 2024快手分论坛举办，“星芒短剧×可灵大模型”创作者孵化计划正式发布](https://www.cnsa.cn/art/2024/7/11/art_1955_45208.html) | 中 | 淘汰 | 历史孵化公告，无返工或交付证据 |
| [快手AI的围城与重构 正观新闻](https://wap.zhengguannews.cn/html/zgh/377227.html) | 中 | 待核验 | 缺单剧镜头验收日志 |
| [Runway News · Project Luxo: Crossing the Uncanny Valley of AI Media](https://runway.com/news/company-news/project-luxo) | 外 | 待核验 | 缺未入选镜头及其生成成本 |
| [Runway Customers · How Obsidian Uses Runway to Power Campaigns for D](https://runway.com/customers/how-obsidian-uses-runway-to-power-campaigns-for-disney-nike-and-luxury-brands) | 外 | 待核验 | 缺可迁移到竖屏短剧的分镜和返工数据 |

## pipeline

候选 9 条（晋升 1、待核验 3、淘汰 5）。

- 检索词 `火山引擎 Seedance 视频 计费 失败 消耗 积分 工作流 腾讯 阿里` · `AI video generation credit burn failed generation retries cost Google Veo Runway official` · `site:help.aliyun.com 万相 视频 计费 失败` · `Runway API task failed retry billing official`
- 缺口 缺成功废片、任务失败、返工工时和实际扣费的同批记录。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [剧创重制工坊重新分析前先备份分集成果](https://docs.volcengine.com/docs/drama-creation/remake-workshop?lang=zh) | 中 | 已晋升 | [原子稿](./pipeline-remake-before-reanalysis.md) |
| [最近更新时间：2025-12-08 14](https://main.qcloudimg.com/raw/document/product/pdf/1616_82561_cn.pdf) | 中 | 待核验 | 需核对腾讯当前接入版本与实际扣费明细 |
| [阿里云百炼模型价格-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/model-pricing) | 中 | 待核验 | 需同一任务失败、重试和最终账单 |
| [如何调用万相Wan视频编辑模型-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/wan-video-editing-guide) | 中 | 待核验 | 需短剧同镜头编辑、重生的时长与可用率对照 |
| [如何调用万相wan3.0视频生成模型-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/wan3-video-generation-guide) | 中 | 淘汰 | 万相 3 主指南已见 10-30，仍需确认新限制与旧条目差异 |
| [Why do I see a charge and a refund for the same generation? – Runway](https://help.runwayml.com/hc/en-us/articles/55412733862675-Why-do-I-see-a-charge-and-a-refund-for-the-same-generation) | 外 | 淘汰 | 重复 11-23 Runway 预扣对账 |
| [Manage your Google Flow credits - Computer - Google Flow Help](https://support.google.com/flow/answer/16526234?co=GENIE.Platform%3DDesktop&hl=en) | 外 | 淘汰 | 重复 11-26 Flow 积分和迁移 |
| [广告生成工具榜单](https://note.com/rosy_shrew7689/n/n73446cbfe56c?hl=en) | 外 | 淘汰 | 爬虫候选，商业榜单线索，缺可复查的对照工作流 |
| [免费额度新闻稿](https://markets.chroniclejournal.com/chroniclejournal/article/marketersmedia-2026-11-26-what-is-the-best-free-ai-video-generator-for-2027-a-breakdown-of-what-free-credits-cover) | 外 | 淘汰 | 爬虫候选，营销分发，缺厂商原始权益条款及项目账单 |

## growth

候选 8 条（晋升 1、待核验 4、淘汰 3）。

- 检索词 `抖音 快手 漫剧 分账 激励 投流 ROI 亏损 官方` · `YouTube Shorts TikTok revenue qualified views demonetization ROI official` · `红果 漫剧 分账 官方 合作 结算 保底 投流` · `Shorts creator pool music revenue official TikTok qualified views` · `巨量引擎 短剧 投流 ROI 退款 归因` · `TikTok attribution time to conversion`
- 缺口 缺同部 AI 短剧的制作、退款、结算及到账全账。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [短剧投流按流水、结算与全成本分别复盘](https://static.cninfo.com.cn/finalpage/2026-06-30/1225397242.PDF) | 中 | 已晋升 | [原子稿](./growth-short-drama-roi-denominators.md) |
| [七大平台加码短剧，资金+流量持续拉满！·快手_新浪财经_新浪网](https://finance.sina.com.cn/wm/2026-05-25/doc-inhzcpii2783965.shtml) | 中 | 淘汰 | 泛扶持汇总，缺当前创作者合同 |
| [快手发布漫剧新政策：单部剧最高可获4%额外投流返点及2万元现金激励·快手_新浪财经_新浪网](https://finance.sina.com.cn/roll/2025-12-11/doc-inhakwan8058053.shtml) | 中 | 待核验 | 缺快手当前合作条款、返点计算和实际结算凭证 |
| [红果保底没了?多位制作方称合作仍在继续,项目正常推进中 · 流媒体网](https://lmtw.com/mzw/content/detail/id/252056) | 中 | 待核验 | 缺红果相应批次完整签约规则和结算单 |
| [红果短剧对AI真人剧本的保底分账政策具体怎么算？·实拍·生效·仿真_新浪财经_新浪新闻](https://k.sina.cn/article_7879995964_1d5af323c068019c12.html) | 中 | 待核验 | 缺红果原始公告及保底回收条款 |
| [YouTube Shorts monetization policies - YouTube Help](https://support.google.com/youtube/answer/12504220?no_head=1) | 外 | 淘汰 | Shorts 音乐池和合格播放已于 11-14 收录 |
| [With TikTok creator program, AI-sped misinformation pays](https://www.axios.com/2024/03/26/tik-tok-creator-program-ai-misinformation) | 外 | 待核验 | 缺涉事账号的实际回款、资格和处置明细 |
| [Tus vídeos de YouTube sumarán más visitas, pero tus ingresos no camb](https://cincodias.elpais.com/smartlife/lifestyle/2026-08-18/tus-videos-de-youtube-sumaran-mas-visitas-pero-tus-ingresos-no-cambiaran-esta-es-la-razon.html) | 外 | 淘汰 | 播放及收入定义已有 Shorts 条目 |

## compliance

候选 8 条（晋升 1、待核验 2、淘汰 5）。

- 检索词 `中国 AI生成短视频 标识 数字人 肖像 版权 判决 官方` · `AI short videos synthetic disclosure digital replica copyright official EU YouTube` · `site:cac.gov.cn 2026 11 AI 微短剧 盗脸 偷声 专项` · `EU AI Act article 50 deep fake artistic work transparency official`
- 缺口 缺个案补标恢复时限与完整通知。

| 候选 | 区域 | 裁决 | 依据或缺失证据 |
| --- | --- | --- | --- |
| [B 站稿件收到漏标补正时辨认处置阶段](https://www.bilibili.com/opus/1202507670848798745) | 中 | 已晋升 | [原子稿](./compliance-bilibili-label-return.md) |
| [法律适用丨周加海、司艳丽、秦元明、贾玉慧、张音：《最高人民法院关于依法审理涉人工智能纠纷案件的意见》的理解与适用 - 最高人民法院知识产](https://ipc.court.gov.cn/zh-cn/news/view-6039.html) | 中 | 淘汰 | 对应 11-13 肖像可识别性 |
| [赵丽颖起诉红果短剧 AI合成的脸谁来授权？ - 人民法治网](https://www.rmfzw.org.cn/article/0/335761) | 中 | 待核验 | 缺完整生效裁判和授权范围 |
| [中央网信办部署开展“清朗·整治短视频虚假人设乱象”专项行动_中央网络安全和信息化委员会办公室](https://www.cac.gov.cn/2026-09/30/c_1792520301987752.htm) | 中 | 淘汰 | 虚假人设治理在 11-09、11-11 已收录 |
| [中央网信办深入开展“清朗·整治AI应用乱象”专项行动第二阶段工作_中央网络安全和信息化委员会办公室](https://www.cac.gov.cn/2026-09/02/c_1790099041364574.htm) | 中 | 淘汰 | 通报案例类型与既有 AI 魔改、虚假带货和仿冒边界重叠，未给个案补救流程 |
| [Disclosing use of GenAI content - Computer - YouTube Help](https://support.google.com/youtube/answer/14328491?co=GENIE.Platform%3DDesktop&hlpl=) | 外 | 淘汰 | 通用披露入口与既有 YouTube 标识条目重复 |
| [Article 50: Transparency obligations for providers and deployers of ](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50?full=1) | 外 | 淘汰 | 欧盟透明度分工已有 10-28 及 11-26 |
| [Code of Practice on Transparency of AI-generated Content · Shaping E](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | 外 | 待核验 | 需发行商采纳证据与实际短片披露样本 |
