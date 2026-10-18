# Creator deep sample — 2026-10-18 (Beijing)

Run: X API v2 via MCP, 08:35–08:45 Beijing, **142 calls** by this run (130 A + 10 O1 + 1 profile lookup + 1 wasted on a wrong user id). Daily reads left after the last call: **833 / 1000** (shared with ops; resets 08:00 Beijing). No browser used.

## Method
Same as research/2026-10-17/creator-deep-sample.md, with a smaller budget (≤150 reads):
- Queue = profile-only rows of `data/creators.csv` active ≤30 days (by yesterday's `most_recent_tweet_id`): 615 of 632. Order: benchmarks (10 Japanese benchmark accounts, ranks 25–35 in research/2026-10-16/benchmark-candidates.csv) → English accounts by followers (604k → 51k) → rest. First 130 sampled.
- **A** for every account (latest 25 non-RT posts, last 30 days). The A call also expanded `author_id`, which returned a fresh profile (followers/listed/tweets/most_recent) for free, so no up-front profile call was needed. **O1** (latest 25 originals, `exclude=retweets,replies`) for 10 high-value accounts with <12 originals in A (3 benchmarks + accounts ≥60k followers). No OB.
- Note: `exclude=replies` keeps self-replies (thread parts), so O1 adds little for thread-heavy accounts (keitowebai: 24 of 25 O1 posts were already in A; ai_news_x 19 of 21).
- One `get_users_by_usernames` call re-checked the 17 profile-only rows that looked inactive yesterday plus 69 replacement candidates.
- Pooled analysis: yesterday's 231 accounts (r1017 posts, same exclusions) + today's 127 accounts (3 replaced accounts excluded). The two sets don't overlap, and each post's age is measured against its own run time. Same within-account method: ≥3 posts per arm (≥2 for rare openers and threads), rel = impressions ÷ the account's median aged original, only posts ≥24h old, viral = rel ≥3.

## Coverage
- Deep-sampled today: **127 rows kept** (130 sampled, 3 replaced). Library: **495 deep-sampled / 505 profile-only**, still **1000** rows.
- Today's rows: **62 verified, 65 flagged.** Flags (a row can carry several): 32 low keyword AI share, 19 <3 originals, 4 reply-only, 10 all originals <24h old (medians not captured), 5 likely promoted impressions (cerebras, milichab, togethercompute, warpdotdev, LeonardoAi), 1 reply-farming volume (deepfates), 1 automation-like lifetime volume (izutorishima). Manual notes on regex misses: AI_CLIPs_Daily (AI-generated clips), sarahookr, thegautamkamath, shi3z.
- 17 profile-only rows re-flagged as inactive 31–58d (e.g. CadeMetz 58d, bitsCrunch 55d, trychroma 51d, TheGregYang 50d). None is >60d yet, so none was replaced; CadeMetz and bitsCrunch will pass 60d within the week.
- **Replaced 3** (replaced.csv): Awesome_O_AI (~188 posts/day, 100% generic "ngl…" replies, median reply 7 imp), bernirov (~71/day, 92% generic Spanish replies, Bolt promos, AI share 0), liambraus (96% generic replies, Bolt promo; same reply cluster as bernirov and the @aiscwork group dropped on 2026-10-17). Replacements (profile-checked: followers ≥10k, listed ≥50, tweets ≥300, AI in bio, posted ≤14d, not protected): **zephyr_z9** (174k, "AI & Chips"), **burkov** (60k, "PhD in AI", LLM/ML books), **DavidSKrueger** (25.5k, "AI prof at Mila"). They are profile-only for now.
- Today's 127 accounts: median 2.4 posts/day, 64% replies, keyword AI share 0.50 (lower than yesterday's 0.64: more personal accounts in the 50–80k tier). 32 of them have A windows <3 days.
- Today's originals (621): 31% text, 37% image, 31% video; 8% long; 5% with a non-X link. 57% of originals+quotes posted 21:00–06:00 Beijing (yesterday 62%).

## Pooled within-account results (full table: format-comparisons.csv)
| Comparison | 10-17 (accts, win, ratio) | 10-18 only | **Pooled** (accts, win, ratio, viral A vs B) | Verdict |
|---|---|---|---|---|
| any media vs text | 47, 36%, 0.86 | 9, 44%, 0.95 | **56, 38%, 0.86** (9.9 vs 11.7) | held |
| image vs text | 33, 36%, 0.84 | 9, 33%, 0.71 | **42, 36%, 0.78** | held, a bit stronger |
| video vs text | 18, 56%, 1.19 | 1 | **19, 53%, 1.17** | held (weak +, today adds ~nothing) |
| video vs image | 32, 62%, 1.27 | 8, 50%, 1.11 | **40, 60%, 1.25** (14.7 vs 8.1) | held |
| long >280 vs short (reach) | 33, 45%, 0.96 | 2 | **35, 46%, 0.96** | held neutral |
| long vs short (bookmarks/1k) | 33, 82%, 1.68 | 2 | **35, 83%, 1.68** | held |
| media vs text (bookmarks/1k) | 47, 55%, 1.39 | 9, 67%, 1.08 | **56, 57%, 1.12** | weaker |
| video vs image (bookmarks/1k) | 32, 72%, 1.49 | 8, 50%, 1.12 | **40, 68%, 1.29** | new pooled + |
| <120 vs 120–280 chars | 55, 33%, 0.84 | 10, 40%, 0.94 | **65, 34%, 0.84** | held |
| body link vs none | 14, 50%, 0.99 | 1 | **15, 53%, 1.03** | held neutral |
| quote vs original | 96, 34%, 0.84 | **34, 53%, 1.02** | **130, 39%, 0.86** | **weaker** (today's new accounts: neutral) |
| original + own self-reply vs none | 34, 79%, 1.28 | 9, 78%, 1.49 | **43, 79%, 1.39** (22.3 vs 10.5) | held, stronger ratio |
| launch opener vs statement | 14, 86%, 2.11 | 1 | **15, 87%, 2.01** | held (launch-confounded) |
| `Company:` opener | 7, 71%, 1.16 | 1 | 8, 62%, 1.11 | weak, small n |
| question opener | 16, 50%, 0.94 | 2 | 18, 50%, 1.00 | neutral |
| first-person opener | 7, 29%, 0.80 | 0 | 7, 29%, 0.80 | unchanged (no new data) |
| emoji in first 60 chars | 18, 67%, 1.34 | 6, 50%, 0.98 | **24, 62%, 1.21** | still unresolved (today flat) |
| hour 21–02 Beijing vs other | 93, 47%, 0.98 | 17, 47%, 0.99 | **110, 47%, 0.98** | held: irrelevant |
| hour 06–12 vs rest | 42, 62%, 1.09 | 14, 57%, 1.11 | **56, 61%, 1.11** | held slight + |
| hour 12–18 vs rest | 25, 36%, 0.89 | 5, 20%, 0.77 | **30, 33%, 0.86** | slight −, a bit stronger |
| hour 18–24 vs rest | 66, 50%, 1.01 | 13, 8%, 0.77 | **79, 43%, 0.97** | slight − (driven by 13 accounts today) |

## Replies
| Comparison | 10-17 | 10-18 only | **Pooled** | Verdict |
|---|---|---|---|---|
| reply to ≥100k vs <100k target | 11, 100%, 3.77 | 6, 100%, 3.03 | **17, 100%, 3.57** | held |
| reply to ≥1M vs 100k–1M | 2, 100%, 2.06 | 0 | 2 | untestable |
| reply body ≥200 vs <200 chars | 10, 70%, 1.10 | 4, 25%, 0.91 | **14, 57%, 1.01** | **weaker → neutral** |
| reply body <60 vs 60–200 | 28, 43%, 0.97 | 12, 50%, 1.11 | **40, 45%, 0.99** | held: short replies are not penalized |
| self-reply vs reply to others | 62, 98%, 6.33 | 16, 100%, 3.36 | **78, 99%, 6.04** | held |
Pooled rel (1,385 aged replies with a known target): target <100k 0.023 (n=1205), 100k–1M 0.051 (147), ≥1M 0.056 (33). By body length: <40 0.025 (771), 40–100 0.028 (323), 100–200 0.022 (203), 200+ 0.038 (94). Self-replies pooled 0.130 (1,310). Median reply to others: 348 impressions, 33.5 chars (n=2,014).

## Example posts (today's sample, ≥24h old, rel = × account median original)
| Account | Link | Imp | Likes | Bookmarks | rel | Format |
|---|---|---|---|---|---|---|
| ComfyUI | https://x.com/ComfyUI/status/2110870071933645103 | 505,012 | 4,483 | 3,199 | 42× | call-out of a competitor's broken promise + offer, video, 278 chars |
| theworldlabs | https://x.com/theworldlabs/status/2104665621120311465 | 1,453,140 | 5,459 | 697 | 31× | "We are excited to announce … joining @AMD" + video |
| kajikent | https://x.com/kajikent/status/2110513402535940278 | 110,890 | 461 | 706 | 21× | JP: practical "Claude Code as a 24h AI worker" how-to, text |
| thegautamkamath | https://x.com/thegautamkamath/status/2110707102390108496 | 87,050 | 4,451 | 218 | 19× | 24-char joke "argon doesn't trust me 😭" + screenshot |
| MLBear2 | https://x.com/MLBear2/status/2111028941972804073 | 189,620 | 967 | 1,058 | 16× | JP long post: which model I use for what (Opus 5.5 etc.) |
| stitchbygoogle | https://x.com/stitchbygoogle/status/2105695155164741984 | 373,193 | 1,405 | 829 | 16× | "We have an MCP, an SDK… not a CLI. Until now. Introducing…" + video |
| minilek | https://x.com/minilek/status/2109706940020596840 | 325,249 | 1,969 | 1,327 | 12.5× | quote + personal anecdote about a skeptical colleague, 273 chars |
| deanwball | https://x.com/deanwball/status/2110794674587746764 | 84,830 | 1,051 | 246 | 12× | quote: "There is so much to say about this, and I will, but WOW…" |
| FlowbyGoogle | https://x.com/FlowbyGoogle/status/2107920605420949723 | 128,612 | 1,038 | 254 | 18× | "People are already putting <model> to the test! Take a look ⤵️" |
Reply: steipete → @thsottiaux "🤫 we'll let the work do the talking" (35 chars) 140,212 imp / 1,010 likes (https://x.com/steipete/status/2111340668190965818).
Off-topic outlier, not used for rules: CharaspowerAI Tesla Roadster video 7.09M imp (2,900× the account median).

## Notes and limits
- With A only, many of today's accounts are reply-heavy and only 69 of 127 had ≥3 aged originals for a baseline. So today adds few accounts to most original-format arms (often 1–10). The pooled numbers are mostly yesterday's, nudged. The big additions are quote vs original (+34 accounts), hours (+13–18), self-reply thread (+9), replies to ≥100k (+6), self-replies (+16) and reply length (+4/+12).
- Quote vs original is the one result that moved: today's 34 accounts show no quote penalty (53%, 1.02×). Pooled, quotes still lose (39% of 130, 0.86×), but less clearly than "34% of 96".
- The 18–24 Beijing dip comes from 13 accounts and is probably noise. Hour stays "barely matters".
- Keyword AI share undercounts Japanese/AI-media accounts and researchers' personal posts. Treat low-AI flags as review hints, not verdicts.
- Topic skew this week: Tesla Roadster, Gemini 4 Argon, DeepSeek V4.1, Opus 5.5.
- Post text isn't stored in deep-sample-posts.csv (links + metrics only), same as 2026-10-17.
- Next run: ~488 active profile-only rows remain. At ~130 accounts per 150 reads that's ~4 more runs, or ~2 runs at yesterday's ~400-read budget.
