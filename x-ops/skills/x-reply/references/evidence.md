# Reply evidence (API study v1→v2.2 + browser research, 2026-10-16)

## API data (within-account, public_metrics)
| Finding | v1 | v2 | v2.1 | v2.2 (latest) |
|---|---|---|---|---|
| Reply to ≥100k vs <100k (rel. impressions) | mid-size first | 0.107 vs 0.031 (~3.5×) | 0.094 vs 0.031 | **0.090 vs 0.035 (~2.6×)** |
| Reply length | 40–150 chars | impressions flat (0.031–0.037); median likes <40:2, 40–100:3, 100–200:4, >200:6 | 200+ → 0.050 | **200+ → 0.083** (others 0.036–0.039) |
| Self-reply vs reply to others | for links | 0.142 vs 0.035 (4×); 12% have links | — | **0.140 vs 0.039 (~3.6×)** |

**v2.4 (2026-10-17, 231 new accounts, 979 aged replies + 1006 self-replies; within-account):** ≥100k vs <100k target 100% of 11 accts, 3.77× (stronger); ≥1M vs 100k–1M 2 accts, 2.06×; body ≥200 vs <200 70% of 10, 1.10× (weaker); <60 vs 60–200 43% of 28, 0.97× (new: short not penalized); self-reply vs others 98% of 62, 6.33× (stronger). Pooled rel by target: 0.020 / 0.041 / 0.056; by length <40 0.021, 40–100 0.021, 100–200 0.019, 200+ 0.039. @Gotwei 2026-10-16 15:27–18:55: 167 replies, median 2 imp, 0 likes, no difference by target size (research/2026-10-17/gotwei-review.md).
**2026-10-18 pooled (231 + 127 accounts):** ≥100k vs <100k target 100% of 17 accts, 3.57× (held); body ≥200 vs <200 57% of 14, 1.01× (weaker → neutral); <60 vs 60–200 45% of 40, 0.99× (held: short not penalized); self-reply vs others 99% of 78, 6.04× (held). Pooled rel by target 0.023 (n=1205) / 0.051 (147) / 0.056 (33); by length <40 0.025, 40–100 0.028, 100–200 0.022, 200+ 0.038 (n=94). Median reply to others 348 imp, 33.5 chars (n=2,014). research/2026-10-18/creator-deep-sample.md.
- Replies are 50–90% of top accounts' volume (levelsio 92%, rasbt 92%, AndrewCurran_ 88%, minchoi 84%). Replies to others: median 381 impressions ≈3.2% of the account's original median; median length 54 chars → replies build relationships / borrow distribution.
- v1 sample (kimmonismus "Source: https://..." style): all 142 self-replies median 1328 impressions.
- Only 520 replies had in_reply_to fields in early samples.

## Examples
- karpathy's full-thought reply to @omarsar0, 200K: https://x.com/i/status/2106806571321966793
- levelsio concrete advice reply, 22,481: https://x.com/i/status/2110783937001955629
- ylecun numbered (1/2) theory reply to @andrewgwils, 19,103: https://x.com/ylecun/status/2109184437535875275
- ns123abc "🫡" 13,250 (established account only): https://x.com/i/status/2110114683348721757
- shao__meng long opinion reply, 26 likes / 2.7K: https://x.com/shao__meng/status/1753720436381372440 (vs "LFG/Thanks sir" single digits)
- Browser reply research (~45 replies under OpenAI/Anthropic/karpathy/emollick/fchollet/kimmonismus + 4 Replies tabs): links in x-reply/SKILL.md rules 4–8.
