---
name: x-creator-research
description: Use when growing or analysing the creator library (data/creators.csv) or sampling benchmark accounts' posts for format/reply research.
---
# X creator research

## Inclusion bar (creators.csv)
1. followers ≥10k, listed_count ≥50 (anti-bot/bought followers), tweet_count ≥300, clearly AI (bio/name; institutional `*AI*` handles ok). Library: **1000** rows as of 2026-10-16.
2. AI-keyword regex must match whole words (v1 bug matched "said"; fixed and re-screened).
3. Deep-sampled rows add: sampled_posts, window_days, posts_per_day, reply_pct, ai_share_orig, median_impressions_orig, median_engagement_rate. ai_share_orig <0.4 → "low AI share" (JeffDean, paulg, GaryMarcus, ylecun — sometimes reply-heavy distortion). Prefer high ai_share benchmarks.

## Sourcing & sampling
4. Grow via curated lists (Fireply, Downstream, Visionik, AI-TLDR, awesome-ai-on-x) + handles seen in API results; keyword search is noisy with few authors.
5. Use wide windows (~30 days) — ~25 latest posts covers <1 day for high-frequency accounts. Compare **within account** (see x-original-post/references/evidence.md method).
6. Browser research: `from:user since:YYYY-MM-DD`, Top tab; record link, format, media, length, opener, replies/reposts/likes/views; don't invent missing numbers (mark "not captured"). Search index may be stale (tsarnick: nothing after Feb 2025 → treat inactive).

## Quota & box etiquette
7. X API: **1000 reads/day, resets 08:00 Beijing**. Keep ~50 spare for ops. Prefer the browser for reading.
8. **One browser at a time** on the shared box; heavy video profiles crash tabs, and memory pressure (load ~300) killed all x.com tabs — kill stray chrome/playwright first, one query per tab.

Raw: research/2026-10-16/creator-top-posts-batch1-raw.md, 0-1k-stage-batch1.md, benchmark-candidates.csv (82 ranked benchmarks).
