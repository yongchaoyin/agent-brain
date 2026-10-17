---
name: x-data-review
description: Use when reviewing @Gotwei performance (运营复盘's job) — which metrics, when to check, and the weekly report.
---
# X data review

## Metrics
1. Per post: impressions, likes, replies, reposts, bookmarks; relative impressions = post ÷ our median original (viral ≥3×); engagement rate; bookmarks/1k.
2. Per day: posts used vs ~160 budget (cap ~200+/rolling 24h), originals vs replies, median reply impressions, follower count.
3. Compare formats **within our own account** with ≥3 posts per arm before concluding (n=3 A/B tests are provisional).

## Checkpoints
4. Each original: check at ~1h and ~24h. Replies: sample daily; flag any reply >100 imp and note target, age of parent at reply time, length.
5. Baseline 2026-10-16: median original 7 imp (day 0), 10–29 after rebrand; best 23. 0–1k-stage peers: 25–700 — don't pivot on low numbers early.
5b. Baseline 2026-10-17 ~09:00 Beijing (API): followers **0**, 259 posts; originals median 10.5 imp (n=22), image originals 15 vs text 9 (n=5 vs 23); best 32 (BREAKING + image); replies median 2 imp, 0 likes (n=167, 2026-10-16 15:27–18:55), no difference by target size; peak pace ~60 replies/hour. Details: research/2026-10-17/gotwei-review.md.

## API recipe (≈10 X reads; shared 1000/day quota, resets 08:00 Beijing)
7. `get_users_by_username` Gotwei (user.fields public_metrics,description,most_recent_tweet_id) → followers + live bio (check it matches the Profile section in x-original-post).
8. `get_users_posts` id 2104754944545116160, exclude `retweets,replies`, post.fields `created_at,public_metrics,referenced_tweets,attachments,note_tweet` + expansions `attachments.media_keys` → all originals (1–2 pages).
9. Same with exclude `retweets` + expansions `in_reply_to_user_id`, user.fields `public_metrics` → replies with target follower counts; ~25 replies/page, stop after ~6 pages.
10. Judge originals only after ≥24h; compare within our account, ≥3 posts per arm.

## Weekly report (→ research/YYYY-MM-DD/weekly-review.md + CHANGELOG line)
6. Followers Δ, median original/reply impressions vs last week, top 5 posts (links), format scorecard, quota incidents, 1–3 rule changes proposed to X运营 (lead merges into skills).
