# 2026-11-12 primary-source sweep

> 采集日期：2026-11-12（Asia/Shanghai）。供当日 `SCAN.md`、atom 与 `DIGEST.md` 复核整合；候选不是事实，晋升建议仍须由主流程最终去重。

## 起点与范围

- 爬虫起点：`general=0 / platforms=4 / types=4 / pipeline=3 / growth=1 / compliance=3`，国内 4、海外 0；优先补扫 `general`、`growth` 和海外来源，同时不把其余四维视为已覆盖。
- 中文检索覆盖 AI 视频提示词、万相 / Seedance 官方文档、AI 微短剧类型、创作者收益、AI 视频标识与直播电商；海外检索覆盖 prompting、vertical microdrama、Reels AI translation、creator monetization、workflow 与 synthetic-media disclosure。
- 打开并核验 13 个一手页面，另审查 4 条爬虫线索。可靠候选按主维度归档后为国内 7、海外 4，约 64:36；没有为比例采用低质量来源。

## general｜通用技巧

### 晋升建议：图生视频先检查输入图的隐含运动线索

- **来源：** [Runway Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)
- **机构 / 日期：** Runway；页面未标发布日期，2026-11-12 核验当前版本
- **来源等级 / 状态：** 模型厂商官方文档 / `已核验`
- **来源明确事实：** 输入图中的运动模糊、动作中姿势、方向线等会形成隐含运动线索；文字要求与这些线索冲突时可能需要更多迭代。官方示例移除静止车辆周围的尘土和运动模糊后，用同一提示获得预期运动。
- **可执行含义：** 把“输入图运动线索检查”放在提示词调试之前；目标为静止主体时先清理运动模糊、扬尘和中途动作姿态。
- **去重 / 边界：** 全库只有“图生视频主要写运动 + 运镜”和“末帧续接”，未见该冲突检查。厂商示例仅验证 Runway 当前行为，不能宣称跨模型成功率。

### 合并 / 淘汰

- [阿里云万相官方 Prompt 指南](https://help.aliyun.com/zh/model-studio/text-to-video-prompt)明确总体描述、镜头序号、时间戳、分镜内容及“图 n / 视频 n”参考指代，但 2026-10-22 已有万相结构化提示 atom，合并更新来源，不另立条目。
- Runway 最小运动描述、正向措辞和逐项迭代已由 2026-11-03 atom 覆盖，重复。

## platforms｜平台技巧

### 晋升建议：Instagram Reels AI 翻译先预览，再决定是否锁定发布

- **来源：** [Instagram、リール動画のAI翻訳に日本語が対応](https://about.fb.com/ja/news/2026/07/meta-ai-translation/amp/)
- **机构 / 日期：** Meta 日本官方；2026-07-14
- **来源等级 / 状态：** 平台官方 / `已核验`
- **来源明确事实：** 日本官方页称功能向 Instagram 全部公开账号免费提供；发布前可选翻译语言、口型同步，并开启“翻译批准”先预览。发布后可以关闭该视频翻译，但关闭后不能对同一视频重新开启。译制版本显示 AI 翻译标签。页面列出此次新增日、韩、法、德、意及此前支持语言。
- **可执行含义：** 把翻译语言、口型同步和译文预览列为发布前验收项；关闭不可逆，不能把它当临时 A/B 开关。
- **去重 / 边界：** 2026-11-10 `SCAN.md` 曾因缺国家、账户和语言清单而待核；本页补足 Instagram 日本范围、公开账号、语言、预览及关闭边界。不得外推 Facebook 全球，也无翻译准确率或推荐权重证据。

### 待核验 / 重复

- [Facebook Creator Assistant 官方公告](https://about.fb.com/news/2026/06/creator-assistant-more-languages-for-ai-translations-on-facebook/)确认美国、加拿大、印度逐步开放，但缺 2026-11 当前帮助页、账户资格清单和错误率，保留待核。
- YouTube Shorts seasons / episodes 已在 2026-11-09、11-10 记录，重复。

## types｜类型技巧

### 待核验：AI 微短剧供给规模不能推出类型打法

- **来源：** [曹淑敏在 2026 中国广播电视精品创作大会开幕式上的致辞](https://www.nrta.gov.cn/art/2026/11/5/art_3901_74407.html)
- **机构 / 日期：** 国家广播电视总局；2026-11-05
- **来源等级 / 状态：** 监管部门官方讲话 / `单一来源`
- **来源明确事实：** 致辞称 2026 年前 10 个月上线微短剧近 55 万部，约为 2025 年全年的 17 倍；其中 AI 剧超过 94%，并强调精品化、大众化、国际化和人的创作主体性。
- **精确缺口：** 未公开“上线”“AI 剧”的统计口径、去重规则、平台范围或题材分布，不能推导某题材更受欢迎、AI 提升完播或类型 ROI。
- **去重：** 上位评价方向已在 2026-11-10 types atom 晋升；只建议账本记录新规模数字，不拆新 atom。

### 重复淘汰

- [YouTube 竖屏微短剧官方页](https://blog.youtube/culture-and-trends/the-evolution-of-web-series-on-youtube-microdramas/)的 15 秒钩子、竖屏构图、日更、普适主题、评论参与剧情、季集与会员路径已由 2026-11-09 和 11-10 atom 覆盖。
- TikTok 品牌连载两种结构已在 2026-11-09 types atom 晋升。

## pipeline｜制作管线

### 待核验：YouTube 对话式剪辑连接自动初稿与人工时间线

- **来源：** [New tools to power your creation journey from start to finish](https://blog.youtube/news-and-events/made-on-youtube-new-tools-power-creation-journey/)
- **机构 / 日期：** YouTube；2026-09-23
- **来源等级 / 状态：** 平台官方公告 / `待核验`
- **来源明确事实：** YouTube 宣布为 Shorts 和 YouTube Create 集成对话式剪辑助手，可从建议或自写提示生成初稿，继续对话获得重排画面、裁切、按节拍同步音乐等建议，并可在对话编辑和手动时间线间切换。
- **精确缺口：** 公告为“正在集成”口径，未给 2026-11 当前地区、账号、系统版本、导出边界和失败恢复规则；需要当前帮助页或实际账户证据。
- **去重：** 全库未见“对话编辑—手动时间线往返”条目，补齐可用性后有独立增量。

### 重复淘汰 / 合并

- [火山引擎官方文档](https://docs.volcengine.com/docs/large-model-of-image-generation/smart-video?lang=zh)确认 Seedance 2.5 单片段最长 30 秒、50 个全模态资产参考和更可控编辑，但 2026-09-17、10-23、11-09 已覆盖，重复；只可替换旧二手来源。
- 万相 3.0 时间戳多镜头与参考素材指代和现有结构化提示、资产职责条目重叠，合并。

## growth｜增长变现

### 晋升建议：TikTok One 将旧视频授权、品牌 brief 新制和代理邀约分账

- **来源：** [Unlocking New Ways for South African Creators to Earn through TikTok One](https://newsroom.tiktok.com/unlocking-new-ways-for-south-african-creators-to-earn-through-tiktok-one?lang=en-ZA)
- **机构 / 日期：** TikTok South Africa；2026-09-28
- **来源等级 / 状态：** 平台官方 / `已核验`
- **来源明确事实：** TikTok One Creator Marketplace 内置于 TikTok Studio。南非官方页区分：`Spark Opportunity` 授权品牌把既有视频作为 Spark Ads 投放并在实际投放时获报酬（至少 500 粉且注册 TikTok One）；`Creative Challenge` 按品牌 brief 制作并按表现与媒体投入变现（至少 1,000 粉且注册）；`Creator Led Package` 由获批代理按项目邀请。单项活动仍受各自要求约束。
- **可执行含义：** 收益账本分开记录“旧素材授权投放”“按 brief 新制”“代理邀约”，不要混算成稳定平台分成；记录实际投放、媒体投入和邀请是否发生。
- **去重 / 边界：** 全库未见 TikTok One 三路径。门槛仅为南非口径，不可外推其他地区，也不能由平台全球同比数据推导单个创作者收入。

### 待核验 / 重复

- YouTube Shorts Series 会员剧集属“未来几周”口径且已在 2026-11-09 记录；缺当前帮助页、地区与分成细则。
- TikTok / Amplify 品牌资助连载已在 2026-11-09 晋升，重复。

## compliance｜合规与风控

### 晋升建议：AI 数字人直播电商必须持续提示，未履行可触发罚则

- **来源：** [《直播电商监督管理办法》官方 PDF](https://www.samr.gov.cn/cms_files/filemanager/1647978232/attach/20261/c7ac0df71be943fc9fd99d68aa7fa6d5.pdf)
- **机构 / 日期：** 国家市场监督管理总局、国家互联网信息办公室；2025-12-18 公布，2026-02-01 施行
- **来源等级 / 状态：** 部门规章 / `已核验`
- **来源明确事实：** 第三十七条要求直播间运营者使用 AI 等技术生成的人物图像、视频从事直播电商时依法标识，并“持续向消费者提示”；违法由管理或使用该人物图像、视频的直播间运营者依法担责。第五十九条将不履行标识义务列入责令限期改正、拒不改正或情节严重时一万至十万元罚款的情形；第六十五条另规定网信职责内处置。
- **可执行含义：** 数字人直播不能只在开场短暂显示一次 AI 标签；全过程验收持续提示、运营主体责任，以及回放 / 剪辑成广告后的广告法义务。
- **去重 / 边界：** 全库未见该规章或持续提示罚则。适用中国大陆直播电商；普通非带货短视频不能直接套用该罚则。

### 待核验：赵丽颖 AI 换脸诉讼线索

- **线索：** 爬虫两篇搜狐稿和新浪评论称赵丽颖就红果平台内 AI 换脸短剧起诉相关主体。
- **精确缺口：** 未找到法院公告、庭审直播回放、裁判文书、案号、起诉状原文或原被告官方声明。只能确认媒体报道“开庭 / 原告主张”，不能把侵权成立、平台责任或赔偿请求写成事实。
- **建议：** 留 `SCAN.md` 待核验，不建普通 atom；取得法院一手文书后再处理。

## 爬虫 4 条线索处置

1. **国盛证券：AI 微短剧合规门槛抬升（搜狐转载）**：淘汰。二手券商观点；下架数量、专项治理时间和“头部受益”缺监管原文 / 完整研报方法，且与既有政策 atom 重叠。
2. **赵丽颖起诉 AI 换脸短剧（搜狐）**：待核验。缺法院一手文书、案号与当事人官方材料。
3. **马上评｜明星起诉短剧“偷脸”（新浪评论）**：待核验 / 不作事实来源。评论不足以证明案情与责任；缺同上证据。
4. **AI 短剧竞争升级（新浪转载 / 滚动稿）**：淘汰。成本、效率和趋势为无样本 / 口径的行业估算；模型能力可由火山、阿里、快手官方资料替代，且多项已有 atom。

## 推荐最小发布集与剩余缺口

- `general`：Runway 输入图隐含运动线索检查（海外）。
- `platforms`：Instagram Reels AI 翻译发布前预览与关闭不可逆（海外，日本口径）。
- `types`：不建议新建；规模数据缺统计口径，结论重复。
- `pipeline`：不建议直接晋升；YouTube 对话式剪辑缺当前 rollout，Seedance / 万相重复。
- `growth`：TikTok One 三种品牌合作收入路径（海外，限定南非）。
- `compliance`：AI 数字人直播电商持续提示与运营者责任（国内）。

最小晋升集为国内 1、海外 3，不符合 65:35；主流程应继续优先补扫国内 `general / platforms / types / pipeline / growth`，但不应为比例采用二手行业稿。国内广电总局规模讲话和火山 / 阿里官方文档可作为账本覆盖，因重复或证据边界不宜强行晋升。