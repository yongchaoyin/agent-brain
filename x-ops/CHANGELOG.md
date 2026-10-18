# Changelog (Beijing dates)

## 2026-10-18
- **x-human-voice phase 2** (25 X API reads, 08:05–08:15): 401 live replies under 10 big AI threads + 24 author→commenter replies. Big-thread replies 33% lowercase, 11.6% "?", median 15 words; ≤8w median 144 views vs >25w 62; early helps (0–5 min 367 vs 60–120 min 86) but the top reply (274K) was a 101-follower joke 18 min in. Authors answer challenges (10/24) and excited specific agreement (6/24), not summaries. Raw: research/2026-10-18/phase2_raw/.
- **New skill x-human-voice** (Drew: "Bot" reply, "AI flavor", "X is for discussion and opinions"). Offline analysis of 1,289 real replies / 697 originals from 146 creators (research/2026-10-18/human-voice.md): real replies end in "?" 6.1% (ours 63%), start lowercase 24% (ours 0), 61% no final punctuation, em dash 0.3%, median 6 words (p90 32, no cap; >40w replies most liked). Questions rare but answered 72%; pushback/quote-a-line replies get answered most. Banned-phrase list, ~1-in-20 question rate, no length cap, never answer bot accusations, timing jitter, pre-post check vs last 10 posts, 17 before/after rewrites.
- x-reply: T12/T12b templates, per-parent char caps and "fact + question" pattern removed; points to x-human-voice. x-original-post: BREAKING:/NEW:/`<Company> 🔥:` openers, "Why it matters", hook→bullets→take structure and 120–280 char target retired; formats are references only.
- **Creator deep sample, day 3** (142 X reads, 08:35–08:45; hard cap 150): 127 more accounts deep-sampled (A-only + 10 O1; library **495 deep / 505 profile-only**, still 1000 rows); 62 verified, 65 flagged, 17 inactive rows re-flagged (31–58d, none >60d); **3 replaced** (Awesome_O_AI, bernirov, liambraus: spam/reply-farming cluster) with zephyr_z9, burkov, DavidSKrueger. Notes: research/2026-10-18/creator-deep-sample.md, deep-sample-posts.csv, format-comparisons.csv (pooled 10-17+18), replaced.csv.
- Pooled results (358 accounts): held: media vs text (38% of 56, 0.86×), image 0.78×, video > image (60% of 40, 1.25×), long = bookmarks not reach, <120 chars lose (34% of 65), self-reply on originals (79% of 43, 1.39×), hour irrelevant (110 accts), replies to ≥100k (100% of 17, 3.57×), self-replies (99% of 78, 6.04×). **Weaker**: quotes vs originals (39% of 130, 0.86×; new accounts neutral), reply ≥200 chars → neutral (57% of 14, 1.01×), media bookmark edge 1.39× → 1.12×. Emoji still unresolved. x-original-post rules 8–13/16, x-reply rules 1/6/12 and both evidence files updated with the pooled numbers; no new templates.
- x-creator-research: coverage counts; `author_id` expansion on the A call gives free fresh profiles; `exclude=replies` keeps self-replies (O1 weak for thread-heavy accounts); 150-read budget math (~1.1 reads/account A-only).

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
