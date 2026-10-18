---
name: x-creator-research
description: Use when growing or analysing the creator library (data/creators.csv) or sampling benchmark accounts' posts for format/reply research.
---
# X creator research

## Inclusion bar (creators.csv)
1. followers ≥10k, listed_count ≥50 (anti-bot/bought followers), tweet_count ≥300, clearly AI (bio/name; institutional `*AI*` handles ok). Library: **1000** rows (2026-10-17: 64 replaced; 2026-10-18: 3 spam/reply-farming replaced — Awesome_O_AI, bernirov, liambraus; lists in research/2026-10-1{7,8}/replaced.csv). **495 deep-sampled** (131 on 2026-10-16 + 234 on 2026-10-17 + 127 on 2026-10-18, minus replacements); 505 profile-only (~488 of them active ≤30d).
2. AI-keyword regex must match whole words (v1 bug matched "said"; fixed and re-screened).
3. Deep-sampled rows add: sampled_posts, window_days, posts_per_day, reply_pct, ai_share_orig, median_impressions_orig, median_engagement_rate. ai_share_orig <0.4 → "low AI share" (JeffDean, paulg, GaryMarcus, ylecun — sometimes reply-heavy distortion). Prefer high ai_share benchmarks.
3b. Column definitions (2026-10-17 run): sampled_posts = unique non-RT posts fetched; window_days = 30 if the 30-day A call was exhausted, else days back to its oldest post; posts_per_day = A posts ÷ window; reply_pct = % replies (incl. self-replies) in A; ai_share_orig = share of originals+quotes matching the AI regex; median_impressions_orig / median_engagement_rate = originals+quotes ≥24h old. quality_note = `deep-sampled YYYY-MM-DD (phases); verified` or `…; flagged: reasons`.
3c. Verification: **replace** if protected, last post >60d, 0 non-RT posts in 30d with automation-like volume, bot, or clearly off-topic (keyword AI share <0.2 on ≥10 originals + manual check) / spam; **flag, keep** if inactive 31–60d, AI share 0.2–0.4 or AI-media accounts the regex misses, <3 originals, reply-only, median impressions <0.5% of followers, likely promoted (median ER <0.001 or ≥30% of 100k+ posts with engagement <0.15%), reply-farming (≥40/day, ≥90% replies). Replacement bar = inclusion bar + AI in bio + posted ≤14d.
3d. AI regex: match a standalone, case-sensitive `AI` only (the 2026-10-16 `v2.py` regex matched "said"/"again" — those ai_share values may be inflated).

## Sourcing & sampling
4. Grow via curated lists (Fireply, Downstream, Visionik, AI-TLDR, awesome-ai-on-x) + handles seen in API results; keyword search is noisy with few authors.
5. Use wide windows (~30 days) — ~25 latest posts covers <1 day for high-frequency accounts. Compare **within account** (see x-original-post/references/evidence.md method).
6. Browser research: `from:user since:YYYY-MM-DD`, Top tab; record link, format, media, length, opener, replies/reposts/likes/views; don't invent missing numbers (mark "not captured"). Search index may be stale (tsarnick: nothing after Feb 2025 → treat inactive).

## Quota & box etiquette
7. X API: **1000 reads/day, resets 08:00 Beijing**, 30/min, 25 posts per call; `get_users_by_usernames` = 100 profiles per read. Shared with @Gotwei ops (~71 reads by ops in parallel during the 2026-10-17 research run) — keep ≥100 spare. Prefer the browser for reading.
7a. Free profile refresh: add `author_id` to the A call's expansions (user.fields public_metrics,protected,most_recent_tweet_id) — every account with ≥1 post returns its fresh profile, so no up-front profile call is needed (2026-10-18). Save `get_users_by_usernames` for rows with 0 posts, inactive re-checks and replacement candidates (one call for all). `exclude=retweets,replies` still returns **self-replies**, so O1 adds little for thread-heavy accounts (keitowebai 24/25 overlap with A).
7b. Budget per account ≈1.6 reads: A (25 latest non-RT, 30d) → O1 (25 originals) only if A had <12 originals → OB (second originals slice) only for high-frequency English benchmarks. 2026-10-17: 399 reads → 254 accounts. 2026-10-18 (hard cap 150 reads): 142 reads → 130 accounts (130 A + 10 O1 + 1 profile + 1 wasted) — ~1.1 reads/account when OB is skipped. With A only, ~45% of accounts are too reply-heavy for an originals baseline (69 of 127 had ≥3 aged originals), so A-only runs add mostly reply/quote/hour data; spend O1 on high-follower English accounts when format arms matter. ~488 active profile-only rows remain: ~4 runs at 150 reads or ~2 at ~400.
8. **One browser at a time** on the shared box; heavy video profiles crash tabs, and memory pressure (load ~300) killed all x.com tabs — kill stray chrome/playwright first, one query per tab.

Raw: research/2026-10-16/creator-top-posts-batch1-raw.md, 0-1k-stage-batch1.md, benchmark-candidates.csv (82 ranked benchmarks).
