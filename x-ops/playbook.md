# @Gotwei（wei news）X 运营手册 v2（2026-10-16 更新）

数据来源：2026-10-16 通过 X API 拉取 51 个头部 AI 账号的最近帖子（1287 条，其中原创 445 条、回复 817 条），外加 @Gotwei 自己的最近 25 条。下面所有数字都来自 API 返回的 public_metrics。“相对曝光”是指一条帖子的曝光除以该账号原创帖曝光的中位数，用来抵消粉丝量差距。爆款定义为相对曝光 ≥3 倍。
候选账号库：x-creators.csv（v2：431 个通过质量门槛的账号，其中 77 个做了深度抽样）。


## ★ v2 更新摘要（相对 v1 的变化）
样本扩大到 **112 个 AI 账号、3362 条帖子（原创 1239 条、回复 2123 条）**，其中 40 个核心账号往前多翻了一页。每个账号的时间窗中位数是 3.9 天。
方法改进：v1 是把所有帖子混在一起比，粉丝多的大号会把结果带偏。v2 改为**账号内配对比较**：在同一个账号里，用 A 类帖子的相对曝光中位数和 B 类比，只有 A、B 各有至少 3 条的账号才计入（样本少的项目放宽到 2 条），然后统计"A 胜出的账号占比"和"A/B 中位比值"。

| 结论 | v1 | v2（账号内对照） | 变化 |
|---|---|---|---|
| 正文放外链 | 爆款率 0%，强烈减分 | 只有 7 个账号能比较，其中 5 个带链接的反而更高，中位比值 1.09 | **v1 结论撤回**，证据不足。仍然建议把来源放在自回复里，理由是让正文更干净，而不是数据证明外链降权 |
| 带媒体 vs 纯文字 | 视频爆款率最高 | 带媒体胜出 23/38 个账号（61%），比值 1.19。视频对纯文字 12/19（63%），比值 1.03；图片对纯文字 12/24（50%），比值 0.98 | 带媒体有小幅优势，单看图片几乎没差别。收藏率上带媒体胜出 27/38（71%） |
| 引用转发（quote） | 没测 | 胜出只有 12/49（24%），比值 **0.75** | **新增**：引用帖明显不如原创帖，少用 |
| 长帖（>280 字） | 收藏多 | 曝光胜出 23/40（57%），比值 1.12；**收藏率胜出 34/40（85%）** | 加强：长帖最稳的收益是收藏 |
| 第一人称 | 互动高 | 曝光胜出 24/43（56%），比值 1.03 | 减弱：对曝光几乎没影响 |
| BREAKING/NEW 开头 | 1.69 倍 | 胜出 4/5，比值 1.67，但只有 5 个账号 | 方向不变，样本很小 |
| emoji | 没明确结论 | 胜出 10/15，比值 2.02 | 新增，但样本小，当作弱信号 |
| 发帖时段（北京时间 21:00–02:00） | 建议主发 | 胜出 23/53（43%），比值 0.98 | **时段几乎没影响**，不用卡时间 |
| 回复谁 | 中腰部账号优先 | 回复粉丝 ≥10 万账号的相对曝光是 0.107，回复 <10 万账号的是 0.031，差约 **3.5 倍** | **改为优先回大号**（发帖后尽早回） |
| 回复长度 | 40–150 字 | 曝光和长度无关（各档都在 0.031–0.037），赞数中位数随长度上升：<40 字 2、40–100 字 3、100–200 字 4、>200 字 6 | 写有内容的长回复多拿赞，不多拿曝光 |
| 自回复 | 用来放链接 | 自回复相对曝光 0.142，是给别人回复（0.035）的 4 倍；只有 12% 的自回复带链接 | 自回复主要用来补充内容，放链接是次要用途 |

### 账号质量核验
- CSV 收录门槛：粉丝 ≥1 万、被列入列表次数 ≥50（防机器人和刷粉）、发帖 ≥300、bio 跟 AI 相关。v1 的 AI 关键词正则有 bug，会误收 "said" 这类词，已修复并重筛。
- 深度抽样的账号在 CSV 里额外有这些字段：posts_per_day、reply_pct、ai_share_orig（原创里提到 AI 相关词的比例）、median_impressions_orig、median_engagement_rate。
- ai_share_orig 低于 0.4 的账号标为"low AI share"，比如 JeffDean、paulg、GaryMarcus、ylecun。其中一些是回复为主、原创太少，造成比例失真。挑对标账号时优先选 ai_share 高的。

### v2 新增高表现例子（相对曝光 = 该帖曝光 ÷ 该账号原创中位数）
- ai_for_success，Grok Voice 3.0 测评视频：97.7 倍，280,424 曝光（https://x.com/ai_for_success/status/2110457504182509911）。形式是"产品 🔥"开头、一段说明、配实测视频。
- EHuanglu，"AI now knows physics very well"：53.6 倍，2,103,373 曝光（https://x.com/EHuanglu/status/2108695694005649863）。一句话配视频。
- btibor91，"OpenAI is preparing a new higher-tier ChatGPT Pro plan"：36.9 倍，518,869 曝光（https://x.com/btibor91/status/2103222629171908937）。78 字的独家前瞻配截图。
- ns123abc，"🚨 Elon Musk agrees with…"：40.2 倍，1,009,456 曝光（https://x.com/ns123abc/status/2109448545904586837）。🚨 开头配视频。
- Yuchenj_UW，Claude Code "digital whip"：28.9 倍，892,169 曝光、22,033 赞（https://x.com/Yuchenj_UW/status/2108394698482368527）。幽默梗配视频。
- emollick，Gemini 4 观察：21.5 倍，617,569 曝光（https://x.com/emollick/status/2110060618258497764）。168 字的纯文字观点。
- AndrewYNg，"New: A map of the most important skills in AI Engineering"：6,944,460 曝光、52,550 收藏（https://x.com/AndrewYNg/status/2088302050706686198）。信息图配 "New:" 开头，收藏极高。
- 回复例子：ylecun 回 @andrewgwils 的一条带 1/2 编号的理论要点，19,103 曝光（https://x.com/ylecun/status/2109184437535875275）。说明用实质内容回大号能拿到曝光。

### v2 新增模板
**T9 独家/前瞻一句话（对标 btibor91）**
```
{Company} is preparing {specific thing} 👀
```
配图：代码字符串、界面或 changelog 截图，用红框标出重点。自回复写 "Spotted in: {where}. Not official yet."

**T10 名人/专家引语（对标 haider1、Hesamation）**
```
{Expert, title}:

"{the most striking 1–2 sentence quote}"

{one line: why this matters for AI builders}
```
配图：采访片段（≤60 秒）或带出处的截图。

**T11 信息图/地图（对标 AndrewYNg）**
```
New: {a map/cheatsheet} of {topic}.

{1 line on how to use it}
```
配图：自制信息图。这类帖收藏率最高，适合置顶。

**T12 回复大号的模板（40–150 字）**
```
@{bigaccount} Worth adding: {concrete fact/number/source they didn't mention}. {Short implication or sharp question}?
```

## 0. 现状诊断（@Gotwei）
- 0 粉丝，最近 25 条帖子覆盖约 1.3 天（约 19 条/天），原创帖曝光中位数是 **7**。
- 18 条原创全部纯文字、没有配图；其中 13 条正文带外链。bio 写得很泛（"Global AI news & insights..."），没有置顶帖。
- 曝光最高的一条才 23（https://x.com/i/status/2110550427070791759）。
- 结论：一边在高频发，一边内容没有差异化，外加纯文字和外链，等于在一个没有分发的账号上自我限流。

## 1. 核心发现（附数据）
1. **（v2 已撤回，见上方摘要）外链放在正文里是最大的减分项**：正文带外链的原创有 32 条，爆款率 **0%**，互动率中位数 0.61%；不带外链的有 413 条，爆款率 11%，互动率 1.21%。头部账号普遍把来源放在自回复里，例如 kimmonismus 的 "Source: https://..."。全部 142 条自回复的曝光中位数是 1328。
2. **视频的爆款率最高**：视频 16%，图片 9%，纯文字 9%。收藏率（每千次曝光）：视频 2.83，图片 2.06，纯文字 1.39。示例：AiBreakfast 的 Opus 视频 54 万曝光（https://x.com/i/status/2108532134696903162），haider1 发的 Terence Tao 访谈片段 20 万（https://x.com/i/status/2110797855879471162）。
3. **"BREAKING / 机构名 🔥:" 这类开头有效**：用这类开头的 10 条帖子，相对曝光中位数 1.69，是全样本里最高的一组。testingcatalog 几乎每条都这么写，例如 "GOOGLE 🔥: Gemini 4 Argon is rolling out…"，19,613 曝光，526 赞（https://x.com/i/status/2110872881261601280）。
4. **第一人称观点和亲测体验互动最好**：第一人称帖子互动率 1.49%，非第一人称 1.04%；爆款率 13% 对 10%。示例：rowancheung 写 "I'm GrokBot pilled… My 4 favorite routines (copy/paste these prompts)"，64.5 万曝光、3175 收藏（https://x.com/i/status/2108328114552000842）；mattshumer_ 写 "Clear AI trend I'm seeing…"，56 万曝光（https://x.com/i/status/2107533403142619384）。
5. **清单和长帖收藏多，短句容易爆**：带清单的帖子收藏率 3.00/千，长于 280 字的 2.47/千。短于 120 字的帖子爆款率 16%，但互动率只有 0.70%。可行的组合是：一句强钩子，加上要点清单，或者一句话配视频。
6. **回复占了头部账号大部分发帖量**：多数账号的回复占比在 50%–90%，比如 levelsio 92%、rasbt 92%、AndrewCurran_ 88%、minchoi 84%。给别人的回复，曝光中位数只有 381，大约是本账号原创中位数的 3.2%，中位长度 54 字。所以回复的作用是建立关系、蹭进别人的分发，不是直接冲曝光。
7. **发帖频率差异很大，频率本身不决定结果**：rowancheung 每天约 0.5 条，原创中位曝光 40k；karpathy 每天约 0.3 条；_akhaliq 每天 1.6 条、而且从不回复。另一头，kimmonismus 每天约 47 条（含回复），minchoi 约 51 条。对 0 粉账号来说，**质量和差异化 > 频率**。
8. **时间段**：样本主要集中在北京时间 22:00–03:00，对应美东早上到下午，这也是头部账号发帖最多的时段。各时段的相对曝光差别不大（多数在 0.85–1.05 之间）。北京时间 13:00 前后样本少，数值偏低。建议主发时段放在 **北京时间 21:00–02:00**（美东 9:00–14:00）。**v2 修正**：账号内对照显示时段几乎没影响，按新闻时效发就行。

## 2. 规则清单
### 文字格式
- 第一行就是全部：先写"谁 + 做了什么 + 为什么重要"，可以用 `BREAKING:`、`OpenAI 🔥:`、`NEW:` 开头，每条最多 1–2 个 emoji。
- 正文分三段：钩子 → 3–5 条要点（用 `-` 或 `→`）→ 一句自己的判断（"My take:" / "Why it matters:"）。
- 默认把链接放在第一条自回复里（"Source: <link>"），让正文干净。v2 数据没有证明外链会降权，所以不必绝对禁止。
- 数字要具体（价格、参数、基准分），写清楚日期，不确定的就直接写"rumor / unconfirmed"。
- 每天至少 1 条第一人称内容：亲测、对比、"I tried X so you don't have to"。

### 视觉
- 每条原创都必须带视觉素材。优先级：官方演示视频剪成 15–40 秒 > 官方页面、changelog、价格表截图（用红框标出重点）> 自制对比卡（统一模板）。
- 自制图模板：深色背景、左上角放 "wei news" 小 logo、标题 ≤8 个词、最多 3 个数字。尺寸 1600×900 或 1080×1350。
- 图里的文字和正文要互补，不要重复。截图要裁掉多余的界面元素。

### 节奏
- 第 1–4 周：每天 3–5 条原创（1 条深度长帖或清单、2–3 条快讯、可选 1 条观点），外加 20–40 条有质量的回复。
- 一小时内最多发 1 条原创；如果大新闻正在发酵，先抢 1 条快讯，30–60 分钟后再补一条解读。
- 每周 1 次 "This week in AI" 汇总，用清单 + 拼图形式，适合放进置顶。

### 回复策略（重点）
- **回谁（v2 修正）**：回复粉丝 ≥10 万的账号，相对曝光是回复小号的约 3.5 倍，所以优先回大号的新帖，再搭配一部分中腰部账号建立关系。从 x-creators.csv 里挑 30–50 个账号，比如 testingcatalog、btibor91、kimmonismus、ai_for_success、AILeaksAndNews、chetaslua、scaling01、iScienceLuvr。打开通知，争取在他们发帖后 **15 分钟内**回复。
- **怎么回**：一般 40–150 字，补充一个对方没提的事实、数字或来源（"Worth noting: pricing is $X, same as v2"），或者给出一个有依据的反问。不要只回 "🔥" 或 "Huge"。这种短附和只在已经有一定关系的大号身上偶尔有效，例如 ns123abc 回 "🫡" 拿到 13,250 曝光（https://x.com/i/status/2110114683348721757），新号别学。
- **语气**：同行、专业、轻松。可以用幽默，但别抬杠，别 @ 对方去导流。
- **有价值的回复的例子**：karpathy 回 @omarsar0 的那条是一段完整的思考，20 万曝光（https://x.com/i/status/2106806571321966793）；levelsio 给出具体建议的回复拿到 22,481 曝光（https://x.com/i/status/2110783937001955629）。
- **自回复**：每条原创都配 1 条自回复，写 "Source:" 加链接，或者补一个细节、给出下一步。这是放链接的地方，也能延长对话。
- 自己帖子下的每一条评论都在 1 小时内回复。
- 自回复里如果放 x.com 帖子链接，X 会自动渲染成引用卡片（2026-10-16 实测）。想借原帖的截图和热度时可以这样做；只想放来源时，用官方网页链接。

### 主页
- 名称：`wei news | AI daily` 这类写法，让人一眼看出赛道。
- Bio 示例："AI news without the noise. Model launches, pricing changes & what they mean for builders. Daily, sourced, with my take." 别写成泛泛的 "Global AI news & insights"。
- 置顶帖：一条代表作（深度清单或对比图），或者每周汇总，每周更新。
- 头像用清晰的 logo，横幅写一句价值主张，再加一句发布节奏，比如 "Daily AI briefings, 9am ET"。

## 3. 可复用模板（英文）
**T1 快讯（截图/视频）**
```
BREAKING 🔥: {Company} just {launched/rolled out} {Product}.

- {Key spec / number}
- {Pricing / availability}
- {What's different vs {competitor}}

Why it matters: {one-line take}.
```
自回复：`Source: {link}`

**T2 第一人称亲测**
```
I tested {Product} for {time/task} so you don't have to.

What worked:
- {…}
What broke:
- {…}

Verdict: {use it for X, skip it for Y}.
```
配图：前后对比截图或录屏。

**T3 对比卡**
```
{Model A} vs {Model B}, the numbers that matter:

→ Price: {a} vs {b}
→ Context: {a} vs {b}
→ {Benchmark}: {a} vs {b}

My pick for builders: {…}
```
配图：自制对比卡。

**T4 一句话 + 视频**
```
{Surprising one-liner about what the AI just did}. {Short reaction} 🤯
```
配图：15–40 秒剪辑，对标 AiBreakfast 和 minchoi 的写法。

**T5 趋势观点**
```
Clear AI trend I'm seeing:

{Observation 1}
{Observation 2}

{Punchline / implication}.
```
可以不配媒体，靠观点本身。对标 mattshumer_ 那条 56 万曝光的帖子。

**T6 每周汇总（置顶用）**
```
This week in AI, the 7 things that actually matter 🧵

1. {…}
2. {…}
…
7. {…}

Bookmark this. Follow @Gotwei for one of these every week.
```

**T7 传闻/前瞻**
```
👀 {Company} appears to be preparing {feature} (unconfirmed).

Spotted: {where: code strings / changelog / leak}.
If true: {implication}.

Will update when it's official.
```
对标 testingcatalog、btibor91。

**T8 价格/政策变化**
```
{Company} quietly changed {pricing/limits}:

Before: {…}
Now: {…}

Who this hurts: {…}
Who this helps: {…}
```

## 4. 典型高表现帖（API 实测数据）
| 账号 | 链接 | 曝光 | 赞 | 收藏 | 形式 |
|---|---|---|---|---|---|
| karpathy | https://x.com/i/status/2105819303471976479 | 7,866,101 | 55,562 | 81,713 | 长文 + 图 |
| rowancheung | https://x.com/i/status/2108328114552000842 | 644,615 | 2,596 | 3,175 | 第一人称 + 提示词清单 |
| mattshumer_ | https://x.com/i/status/2107533403142619384 | 562,254 | 6,296 | 803 | 短观点 |
| AiBreakfast | https://x.com/i/status/2108532134696903162 | 540,938 | 3,238 | 3,187 | 一句话 + 视频 |
| ns123abc | https://x.com/i/status/2110106771356532891 | 332,710 | 2,151 | 583 | BREAKING + 图 |
| Hesamation | https://x.com/i/status/2110675668161659043 | 277,186 | 5,296 | 1,159 | 名人引语 + 图 |
| haider1 | https://x.com/i/status/2110797855879471162 | 200,624 | 2,477 | 908 | 引语 + 视频 |
| btibor91 | https://x.com/i/status/2107127767951388938 | 124,271 | 311 | 93 | 政策快讯 + 截图 |
| akshay_pachaar | https://x.com/i/status/2108497955049345102 | 80,914 | 1,127 | 1,650 | 亲测教程 + 视频 |
| testingcatalog | https://x.com/i/status/2110872881261601280 | 19,613 | 526 | 43 | "GOOGLE 🔥:" + 截图 |

## 5. 局限与后续
- v2：账号内配对比较里，有些项目能比较的账号很少（外链 7 个、BREAKING 5 个、emoji 15 个），只能当作方向参考。时间窗中位数 3.9 天，仍然偏短。
- 每个账号只取了最近约 25 条帖子，样本时间窗很短（高频账号只覆盖不到 1 天），数据受当天热点影响（Muse Spark、Tesla Roadster）。
- 部分早期样本缺少 in_reply_to 字段，所以回复分析只基于 520 条有回复对象的回复。
- 后续：每天新增约 300–500 个账号到 CSV，同时对 Top 100 做第二轮采样（用 pagination 往前翻），并按周跟踪 @Gotwei 执行前后的曝光中位数变化。
