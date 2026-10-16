# Reply evidence (API study v1→v2.2 + browser research, 2026-10-16)

## API data (within-account, public_metrics)
| Finding | v1 | v2 | v2.1 | v2.2 (latest) |
|---|---|---|---|---|
| Reply to ≥100k vs <100k (rel. impressions) | mid-size first | 0.107 vs 0.031 (~3.5×) | 0.094 vs 0.031 | **0.090 vs 0.035 (~2.6×)** |
| Reply length | 40–150 chars | impressions flat (0.031–0.037); median likes <40:2, 40–100:3, 100–200:4, >200:6 | 200+ → 0.050 | **200+ → 0.083** (others 0.036–0.039) |
| Self-reply vs reply to others | for links | 0.142 vs 0.035 (4×); 12% have links | — | **0.140 vs 0.039 (~3.6×)** |
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
