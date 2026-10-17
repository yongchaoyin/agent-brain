# Peitu research (Oct 2-16, 2026) - partial
| URL | handle | date | views | media | orientation | imgs | overlays | notes |
|---|---|---|---|---|---|---|---|---|
| (sama: no own-media originals in window) | sama | - | - | - | - | - | - | all Oct 2-16 posts text-only or quote-media |
| x.com/OpenAI/status/2110797830361436604 | OpenAI | Oct 15 | 1.3M | video (GPT-Live voice demo) | landscape 16:9 | 1 | not verified | video thumbnail |
| x.com/OpenAI/status/2110442001749659890 | OpenAI | Oct 14 | 413K | image/graphic (business AI adoption) | landscape ~3:2 | 1 | not verified | |
| x.com/OpenAI/status/2110841898076418336 | OpenAI | Oct 15 | 272K | video (GPT-Rosalind research access) | landscape | 1 | not verified | |
| x.com/GoogleDeepMind/status/2110039274922131792 | GoogleDeepMind | Oct 14 | 2.4M | video (Gemini 4 Argon launch) | landscape 16:9 | 1 | not verified | |
| x.com/GoogleDeepMind/status/2110078384617464201 | GoogleDeepMind | Oct 14 | 256K | video (Argon robot plays chess) | landscape | 1 | not verified | |
| x.com/GoogleDeepMind/status/2110034327111131168 | GoogleDeepMind | Oct 13 | 232K | video (square) | square | 1 | not verified | |
| x.com/GoogleDeepMind/status/2107834249680499136 | GoogleDeepMind | Oct 7 | 199K | video (SynthID Detector) | square | 1 | not verified | |
| x.com/GoogleDeepMind/status/2110421861435879476 | GoogleDeepMind | Oct 15 | 155K | video (Argon) | square | 1 | not verified | |

## 配图师 10/16 夜间进度（浏览器因负载和 429 中止，调研移交 X运营）
- karpathy（Oct 2–16）没有自带媒体的高曝光原创：
  - https://x.com/karpathy/status/2109361546505966046 约 6.53M，引用帖，无媒体
  - https://x.com/karpathy/status/2105819303471976479 约 7.87M，带 1 个媒体（约 516×258），类型未确认
  - https://x.com/karpathy/status/2105909609487872075 约 1.41M，引用帖，图属于被引用的帖子
- 初步信号：头部个人号的高曝光帖不靠配图，靠观点和引用。配图对新闻类原创更重要（丽丽第 5 条：图表、录屏好于纯文字，纯链接卡最差）。
- 可用模板：templates/news_card.py、data_card.py、annotate.py（截图标注，教程 thread 用）

## X运营 中号配图观察（10/16 23:04）
- 演示类帖子用录屏效果最好：chetaslua 的 Gemini 演示录屏 17.6 万曝光 https://x.com/chetaslua/status/2110050110784798950
- 新闻和泄露帖多半配一张截图：chetaslua 的 Azure 泄露截图 5.6 万 https://x.com/chetaslua/status/2110032565927329992
- 信息卡很少见；高曝光帖几乎都带图
- 出图规则：演示类帖子优先 10 秒左右的录屏，新闻和泄露帖用一张真实截图，信息卡只在实在没有素材时兜底

## 红线（X运营 10/16 23:05）
- 泄露类帖子的配图只截原始出处（比如 Azure 模型列表页），图片来源要告诉丽丽，方便她在自回复里附上出处
- 传闻类消息不做「仿截图」，也不转用别人帖子里来源不明的截图；没有原始出处就用信息卡并标 Reportedly，或者不配图

## X运营 第2批配图相关（10/16 23:11）
- 带截图出处的泄露或 BREAKING 帖起量：koltregaskes 140K https://x.com/koltregaskes/status/2109288430857507154 ；blankspeaker 的 BREAKING 配 6 张图，97K
- 两个模型同题对比的录屏：notjazii 65–69K https://x.com/notjazii/status/2110059198230970782
- 限制：我没有模型账号，也不能在网页上提交提示词，所以自己录不了同题对比。可用的替代：官方发布页或文档里的演示视频、官方的对比图和基准测试表，用 data_card.py 做左右对比卡，数据必须有出处

## X运营 第5、6批配图相关（10/16 23:41）
- 抢先发的发布帖配一张数据图效果好：synthwavedd 配 Artificial Analysis 智能指数图，26.5 万曝光 https://x.com/synthwavedd/status/2109688487372898480
- 出图规则：数据图优先直接截官方或 Artificial Analysis 的原图并标出处；用 data_card.py 重画时数字必须照原图抄，出处写在卡片底部
- 「AI 作品演示」类帖子用录屏：BenjaminDEKR https://x.com/BenjaminDEKR/status/2109819804358259029 ，没有现成素材时可以剪作者公开的演示片段
