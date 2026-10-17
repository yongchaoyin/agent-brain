# Changelog (Beijing dates)

## 2026-10-17
- **Creator deep sample (v2.4)**: 234 more accounts deep-sampled (131 → 364 of 1000), 399 X reads; 158 verified, 80 flagged; **64 replaced** (46 inactive >60d, gwern protected, 4 RT-only/automation, grok bot, 12 off-topic/spam) with profile-verified AI accounts → library stays 1000. Notes: research/2026-10-17/creator-deep-sample.md, format-comparisons.csv, deep-sample-posts.csv, replaced.csv.
- Rules changed by the bigger sample: media vs text **reversed** (36% of 47 accounts, 0.86×; image 0.84×) → video when available, images only if informative; video > image 1.27×; long posts reach-neutral (0.96×) but bookmarks 1.68×; quotes lose more clearly (34% of 96, 0.84×); originals with a self-reply +1.28× (79% of 34); <120-char one-liners lose to 120–280 (33% of 55); emoji unresolved; hour irrelevant confirmed (93 accounts). Replies: ≥100k targets 3.77× (11 accts), self-replies 6.33× (62 accts), short replies not penalized.
- New templates T13–T18 (x-original-post), reply examples + T12b (x-reply).
- AI-keyword regex bug fixed (bare `AI` matched "said"); 2026-10-16 ai_share values may be inflated.
- @Gotwei check (~09:00): 0 followers, median original 10.5, replies median 2 (n=167); live bio missing "Sourced. Open discussion." → research/2026-10-17/gotwei-review.md; x-data-review gets the 10-read API recipe.
- README/x-original-post profile fixed to the final branding (photo avatar, "Wei AI · AI, with perspective." banner, 4-line bio).
- v2.3 (earlier today, ~08:58): merged overnight research (xyunying, lili, xiaoting, fupan, peitu) into research/2026-10-17/; x-reply: parent-type length rules replace "≥200 chars", freshness <15 min, no A/B/C endings, volume caps (≤60 replies/day at 09:01); x-original-post: new formats, red lines, compute & funding category; playbook.md stub.

## 2026-10-16
- **Restructure**: `playbook.md` (v2.2 + appended research) split into skills/; `x-gotwei-growth` skill merged into them; raw notes moved to `research/2026-10-16/`. Playbook deleted (full text in git history before this commit).
- Hot-news research: launches 09:00 PT = 00:00 Beijing; topic ranking; sources to watch.
- 0–1k stage research (11 accounts): growth comes from replies; keep one format; low early impressions normal.
- Creators library reaches **1000** (958 earlier today).
- Original-format research (丽丽): COMPANY: opener, screenshot + one line, ~10s recordings; drop A/B question posts; stay English.
- Reply research (小婷): reply only to posts <2h old (mega-posts <30 min); substance > praise.
- Free-tier cap: ~200+ per rolling 24h (hit 19:06 after ~217 posts). Budget ~160/day.
- Own A/B test (n=3): news + why-it-matters + image beat A/B question.
- v2.2: 621 creators, ~30-day windows; video 1.50×, image now +1.15×, emoji withdrawn, long replies 0.083.
- Profile rebrand: **Wei AI**, new bio/avatar/banner.
- Free-tier 280-char limit on originals.
- v2.1: 178 accounts / 5220 posts; video signal stronger.
- v2: within-account comparison (112 accounts); "body links kill reach" withdrawn; reply to big accounts first.
- x.com links in self-replies render as quote cards.
- v1: playbook, creator dataset, @Gotwei growth skill.

## 2026-10-15
- Initial commit.
