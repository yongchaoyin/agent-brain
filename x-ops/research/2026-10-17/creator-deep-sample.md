# Creator deep sample — 2026-10-17 (Beijing)

Run: X API v2 via MCP, 08:3x–09:1x Beijing, **411 calls** used by this run (sampling 399, replacement lookups 2, @Gotwei 10). Daily reads left after the last call: **518 / 1000** (shared with ops; resets 08:00 Beijing).

## Method
- Queue = profile-only rows of `data/creators.csv`, active ≤30 days (by `most_recent_tweet_id`), order: benchmarks (research/2026-10-16/benchmark-candidates.csv) → English accounts by followers → CJK.
- Per account: **A** = latest 25 non-retweet posts in the last 30 days (originals, quotes, replies, self-replies). If A held <12 originals and had more pages, **O1** = latest 25 originals/quotes (replies excluded). High-frequency English benchmarks got **OB** = a second originals slice ending 2026-10-02. Average ≈1.6 calls/account.
- Medians use posts **≥24h old** only (young posts under-count). "Relative impressions" (rel) = post impressions ÷ the account's median original. Within-account comparison: accounts with ≥3 posts in each arm (≥2 for rare openers / threads); report % accounts where arm A's median rel beats B, and the median of A/B ratios. Viral = rel ≥3.
- Excluded from format stats: 16 accounts later replaced (spam/off-topic/RT-only) + 3 accounts whose impressions look promoted (AlibabaGroup, abacusai, digitalocean: median ER ≤0.0002). Result: 231 accounts, 6296 posts (2061 originals, 1163 quotes, 1847 replies, 1225 self-replies); 178 accounts had ≥3 aged originals for a baseline.
- **Regex fix:** the AI-keyword regex used in 2026-10-16 tooling (`v2.py`) ended with a bare `AI` under case-insensitive matching, so "said", "again", "email" counted as AI. Fixed here (case-sensitive standalone `AI`). 2026-10-16 `ai_share_orig` values may be inflated — re-check when those rows are re-sampled.
- Keyword AI share undercounts AI-product accounts whose posts are AI-generated media with no keywords (higgsfield_ai, suno, Kling_ai, Hailuo_AI). Those were kept and flagged, not replaced.

## Coverage
- Deep-sampled rows: **131 → 364** (+234 new with ≥1 post; 1 old deep row, heyBarsee, replaced as inactive 240d). 4 more were sampled but returned 0 non-RT posts (pmarca, janleike, katecrawford, ch402) → flagged, not counted as deep.
- New deep rows: **158 verified**, **80 flagged** (38 low AI share by keywords, 13 <3 originals, 11 promoted-looking impressions, 6 reply-only, 5 low reach vs followers, 4 reply-farming volume, 4 all-originals-too-young, 4 zero posts, 2 automation-like lifetime volume; one row can carry several flags).
- 19 non-sampled rows flagged inactive 31–60 days (e.g. ilyasut 45d, woj_zaremba 37d).
- **Replaced 64** (list + reasons: replaced.csv): 46 inactive >60d, 1 protected (gwern), 4 RT-only/automation (Arxiv_Daily, Krishnaik06, ipfconline1, Nicochan33), 1 bot (grok), 12 off-topic/spam (DrEliDavid, ijustine, gigadgets_, JordanSchachtel, TrungTPhan, ozansihay, javilop, 0xgaut, maxifirtman, MPhuong609, davidshor, TerenceLeungSF). Replacements: profile-checked (followers ≥10k, listed ≥50, tweets ≥300, AI in name/bio, posted ≤14d, not protected), sourced from reply targets in today's samples + /workspace/gotwei/new-creators.txt. Dropped from candidates: an "@aiscwork" growth cluster (xiathis, aresotik, maarcoofdezz, gelorria), PromptSin, yoshi0320 (automation volume), JoannaStern/andrewmccalip/autonolas (bio matched but not AI). Library stays at **1000**.

## Posting behaviour (231 accounts)
- Median posts/day 2.2 (non-RT), median reply share 56%, median keyword AI share 0.64.
- When originals are posted (Beijing): 00–03 26%, 03–06 16%, 21–24 20% → **62% between 21:00 and 06:00** (US daytime); 06–21 only 38%.
- Originals: 36% text, 34% image, 29% video; 19% long (>280); 10% carry a non-X link.

## Within-account format results (full table: format-comparisons.csv)
| Comparison | accounts | A wins | median A/B | posts A/B | viral A vs B | vs v2.2 |
|---|---|---|---|---|---|---|
| any media vs text | 47 | 36% | 0.86 | 316/291 | 10.4% vs 10.7% | **reversed** (v2.2 66%, 1.28) |
| image vs text | 33 | 36% | 0.84 | 188/200 | 9.0 vs 9.0 | **reversed** (58%, 1.15) |
| video vs text | 18 | 56% | 1.19 | 92/100 | 10.9 vs 8.0 | weaker (67%, 1.50) |
| video vs image | 32 | 62% | 1.27 | 182/212 | 15.4 vs 8.5 | new |
| long >280 vs short (reach) | 33 | 45% | 0.96 | 185/253 | 9.2 vs 10.3 | weaker → neutral (64%, 1.27) |
| long vs short (bookmarks/1k) | 33 | 82% | 1.68 | | | **stronger** (74%) |
| media vs text (bookmarks/1k) | 47 | 55% | 1.39 | | | ≈ (70%) |
| <120 vs 120–280 chars | 55 | 33% | 0.84 | 297/331 | 11.1 vs 11.8 | new: one-liners lose on median |
| body link vs none | 14 | 50% | 0.99 | 86/105 | 8.1 vs 4.8 | confirmed neutral (73%, 1.12) |
| quote vs original | 96 | 34% | 0.84 | 775/841 | 12.1 vs 12.7 | **stronger** (29%, 0.81; n now 96) |
| original + own self-reply vs none | 34 | 79% | 1.28 | 118/247 | 22.0 vs 8.9 | new |
| "Introducing/NEW/Today/We're…" opener vs statement | 14 | 86% | 2.11 | 57/91 | 29.8 vs 11.0 | new (confounded: these are launches) |
| `Company:` opener vs statement | 7 | 71% | 1.16 | 16/55 | 12.5 vs 3.6 | weak +, small n |
| BREAKING/🚨 opener vs statement | 1 | — | 2.62 | 2/10 | | not testable (1 account) |
| question opener vs statement | 16 | 50% | 0.94 | 70/167 | 7.1 vs 8.4 | neutral |
| first-person opener vs statement | 7 | 29% | 0.80 | 31/50 | 19.4 vs 14.0 | weaker (v2 56%, 1.03) |
| emoji in first 60 chars vs none | 18 | 67% | 1.34 | 88/190 | 12.5 vs 9.5 | reversed again (48%, 0.87) → unresolved |
| hour 21–02 Beijing vs other | 93 | 47% | 0.98 | 557/580 | | confirmed irrelevant (45%, 0.98) |
| hour 06–12 Beijing vs rest | 42 | 62% | 1.09 | 178/368 | | slight + |
| hour 12–18 Beijing vs rest | 25 | 36% | 0.89 | 135/223 | | slight − |

Robustness of the media reversal: same direction when text posts with link cards are removed (41 accts, 41%, 0.84) and in each follower tier (<100k 40%/0.84; 100–500k 39%/0.91). Video beats text only in the 100–500k tier (11 accts, 82%, 1.79).

## Replies (within account unless "pooled")
| Comparison | accounts | A wins | median A/B | vs v2.2 |
|---|---|---|---|---|
| reply to ≥100k vs <100k target | 11 | 100% | 3.77 | **stronger** (0.090 vs 0.035, ~2.6×) |
| reply to ≥1M vs 100k–1M | 2 | 100% | 2.06 | tiny n |
| reply body ≥200 vs <200 chars | 10 | 70% | 1.10 | weaker (0.083 vs ~0.037) |
| reply body <60 vs 60–200 | 28 | 43% | 0.97 | new: short replies not penalized |
| self-reply vs reply to others | 62 | 98% | 6.33 | **stronger** (~3.6×) |
Pooled rel (979 aged replies): target <100k 0.020 (n=846), 100k–1M 0.041 (101), ≥1M 0.056 (28); body <40 0.021, 40–100 0.021, 100–200 0.019, 200+ 0.039 (64). Self-replies pooled 0.130 (1006). Median reply to others: 342 impressions, 36 chars.

## Example posts (rel = × the account's median original; all metrics from API, ≥24h old)
| Account | Link | Imp | Likes | Bookmarks | rel | Format |
|---|---|---|---|---|---|---|
| felixrieseberg | https://x.com/felixrieseberg/status/2110023283169247623 | 4,637,480 | 21,499 | 46,517 | 251× | first-person insider intro, 246-char text |
| nickcammarata | https://x.com/nickcammarata/status/2110757819427574056 | 3,475,644 | 18,342 | 18,726 | 194× | 276-char text take (interpretability) |
| opencode | https://x.com/opencode/status/2110635747648909472 | 3,533,731 | 25,677 | 8,664 | 16.5× | 43-char "X is now free in Y" |
| GoogleDeepMind | https://x.com/GoogleDeepMind/status/2105388084154056939 | 8,992,396 | 42,951 | 6,216 | 38.5× | "Introducing <model>" + image, long |
| OpenAIDevs | https://x.com/OpenAIDevs/status/2108624138369929725 | 1,807,494 | 6,937 | 1,420 | 16.5× | "Now in beta: …" + video |
| shiri_shh | https://x.com/shiri_shh/status/2105717583794274346 | 560,449 | 1,285 | 550 | 76.7× | quote + image, casual hook |
| krea_ai | https://x.com/krea_ai/status/2110760037128012146 | 451,966 | 2,073 | 999 | 21× | launch line + spec bullets + video |
| btaylor | https://x.com/btaylor/status/2107535182119244176 | 358,155 | 2,945 | 2,353 | 28.7× | "Today we're announcing…" + image |
| SemiAnalysis_ | https://x.com/SemiAnalysis_/status/2105055045959995719 | 927,438 | 1,841 | 336 | 23× | "ALERT 🚨🚨" scoop + image |
| ai_for_success | https://x.com/ai_for_success/status/2110457504182509911 | 284,398 | 1,159 | 167 | 28× | "Product is 🔥" + own test video |
| nathanbenaich | https://x.com/nathanbenaich/status/2108096754365419873 | 140,366 | 683 | 759 | 57.5× | report launch + video |
| yoavgo | https://x.com/yoavgo/status/2106503106833817918 | 128,914 | 1,581 | 369 | 14× | "wait what??" quote with a number |
| Sentdex | https://x.com/Sentdex/status/2106904650125640152 | 102,447 | 1,695 | 521 | 15× | "In my opinion, the best model … is X" |
| mdancho84 | https://x.com/mdancho84/status/2105259648001376474 | 40,335 | 606 | 1,067 | 12× | "Some guy built a free AI university on GitHub." list |
Replies: felixrieseberg → @GergelyOrosz "Hi! I work on Cowork…" 185,248 imp (https://x.com/felixrieseberg/status/2107206431376334975); giffmana → @nickcammarata banter 62,040 / 713 likes (https://x.com/giffmana/status/2110814420553322983); dylan522p substantive pushback 72,520 (https://x.com/dylan522p/status/2108948086626369842); robertskmiles 53-char quip to @liron 43,316 (https://x.com/robertskmiles/status/2110625716765389090).
Excluded as likely promoted (imp ≥100k, engagement <0.15%): boltdotnew 2.46M/256 likes, ericzakariasson 6.68M/1,987, Kimi_Moonshot 982k/964.

## Limits
- 25 posts per call; 56 of 231 accounts' A windows cover <3 days (high-frequency accounts), so their reply/self-reply stats are short-window. Originals windows are wider (O1/OB).
- Within-account arms are small for openers/links (7–16 accounts); treat as provisional.
- Topic skew: Gemini 4 Argon, Muse Spark, Tesla Roadster week.
- Post text is not stored in deep-sample-posts.csv (links + metrics only).
