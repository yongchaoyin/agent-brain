# @Gotwei（wei news）X 运营手册 v1

数据来源：2026-10-16 通过 X API 拉取 51 个头部 AI 账号的最近帖子（1287 条，其中原创 445 条、回复 817 条），外加 @Gotwei 自己的最近 25 条。下面所有数字都来自 API 返回的 public_metrics。“相对曝光”是指一条帖子的曝光除以该账号原创帖曝光的中位数，用来抵消粉丝量差距。爆款定义为相对曝光 ≥3 倍。
候选账号库：/workspace/x-creators.csv（截至今日 350 个合格 AI 账号）。

## 0. 现状诊断（@Gotwei）
- 0 粉丝，最近 25 条帖子覆盖约 1.3 天（约 19 条/天），原创帖曝光中位数是 **7**。
- 18 条原创全部纯文字、没有配图；其中 13 条正文带外链。bio 写得很泛（"Global AI news & insights..."），没有置顶帖。
- 曝光最高的一条才 23（https://x.com/i/status/2110550427070791759）。
- 结论：一边在高频发，一边内容没有差异化，外加纯文字和外链，等于在一个没有分发的账号上自我限流。

## 1. 核心发现（附数据）
1. **外链放在正文里是最大的减分项**：正文带外链的原创有 32 条，爆款率 **0%**，互动率中位数 0.61%；不带外链的有 413 条，爆款率 11%，互动率 1.21%。头部账号普遍把来源放在自回复里，例如 kimmonismus 的 "Source: https://..."。全部 142 条自回复的曝光中位数是 1328。
2. **视频的爆款率最高**：视频 16%，图片 9%，纯文字 9%。收藏率（每千次曝光）：视频 2.83，图片 2.06，纯文字 1.39。示例：AiBreakfast 的 Opus 视频 54 万曝光（https://x.com/i/status/2108532134696903162），haider1 发的 Terence Tao 访谈片段 20 万（https://x.com/i/status/2110797855879471162）。
3. **"BREAKING / 机构名 🔥:" 这类开头有效**：用这类开头的 10 条帖子，相对曝光中位数 1.69，是全样本里最高的一组。testingcatalog 几乎每条都这么写，例如 "GOOGLE 🔥: Gemini 4 Argon is rolling out…"，19,613 曝光，526 赞（https://x.com/i/status/2110872881261601280）。
4. **第一人称观点和亲测体验互动最好**：第一人称帖子互动率 1.49%，非第一人称 1.04%；爆款率 13% 对 10%。示例：rowancheung 写 "I'm GrokBot pilled… My 4 favorite routines (copy/paste these prompts)"，64.5 万曝光、3175 收藏（https://x.com/i/status/2108328114552000842）；mattshumer_ 写 "Clear AI trend I'm seeing…"，56 万曝光（https://x.com/i/status/2107533403142619384）。
5. **清单和长帖收藏多，短句容易爆**：带清单的帖子收藏率 3.00/千，长于 280 字的 2.47/千。短于 120 字的帖子爆款率 16%，但互动率只有 0.70%。可行的组合是：一句强钩子，加上要点清单，或者一句话配视频。
6. **回复占了头部账号大部分发帖量**：多数账号的回复占比在 50%–90%，比如 levelsio 92%、rasbt 92%、AndrewCurran_ 88%、minchoi 84%。给别人的回复，曝光中位数只有 381，大约是本账号原创中位数的 3.2%，中位长度 54 字。所以回复的作用是建立关系、蹭进别人的分发，不是直接冲曝光。
7. **发帖频率差异很大，频率本身不决定结果**：rowancheung 每天约 0.5 条，原创中位曝光 40k；karpathy 每天约 0.3 条；_akhaliq 每天 1.6 条、而且从不回复。另一头，kimmonismus 每天约 47 条（含回复），minchoi 约 51 条。对 0 粉账号来说，**质量和差异化 > 频率**。
8. **时间段**：样本主要集中在北京时间 22:00–03:00，对应美东早上到下午，这也是头部账号发帖最多的时段。各时段的相对曝光差别不大（多数在 0.85–1.05 之间）。北京时间 13:00 前后样本少，数值偏低。建议主发时段放在 **北京时间 21:00–02:00**（美东 9:00–14:00）。

## 2. 规则清单
### 文字格式
- 第一行就是全部：先写"谁 + 做了什么 + 为什么重要"，可以用 `BREAKING:`、`OpenAI 🔥:`、`NEW:` 开头，每条最多 1–2 个 emoji。
- 正文分三段：钩子 → 3–5 条要点（用 `-` 或 `→`）→ 一句自己的判断（"My take:" / "Why it matters:"）。
- 正文不放外链，链接放在第一条自回复里："Source: <link>"。
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
- **回谁**：从 x-creators.csv 里挑 30–50 个账号，按粉丝 1 万–30 万的中腰部优先，比如 testingcatalog、btibor91、kimmonismus、ai_for_success、AILeaksAndNews、chetaslua、scaling01、iScienceLuvr。打开通知，争取在他们发帖后 **15 分钟内**回复。
- **怎么回**：一般 40–150 字，补充一个对方没提的事实、数字或来源（"Worth noting: pricing is $X, same as v2"），或者给出一个有依据的反问。不要只回 "🔥" 或 "Huge"。这种短附和只在已经有一定关系的大号身上偶尔有效，例如 ns123abc 回 "🫡" 拿到 13,250 曝光（https://x.com/i/status/2110114683348721757），新号别学。
- **语气**：同行、专业、轻松。可以用幽默，但别抬杠，别 @ 对方去导流。
- **有价值的回复的例子**：karpathy 回 @omarsar0 的那条是一段完整的思考，20 万曝光（https://x.com/i/status/2106806571321966793）；levelsio 给出具体建议的回复拿到 22,481 曝光（https://x.com/i/status/2110783937001955629）。
- **自回复**：每条原创都配 1 条自回复，写 "Source:" 加链接，或者补一个细节、给出下一步。这是放链接的地方，也能延长对话。
- 自己帖子下的每一条评论都在 1 小时内回复。

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
- 每个账号只取了最近约 25 条帖子，样本时间窗很短（高频账号只覆盖不到 1 天），数据受当天热点影响（Muse Spark、Tesla Roadster）。
- 部分早期样本缺少 in_reply_to 字段，所以回复分析只基于 520 条有回复对象的回复。
- 后续：每天新增约 300–500 个账号到 CSV，同时对 Top 100 做第二轮采样（用 pagination 往前翻），并按周跟踪 @Gotwei 执行前后的曝光中位数变化。
