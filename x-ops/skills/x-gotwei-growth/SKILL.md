---
name: x-gotwei-growth
description: Run @Gotwei (wei news, AI news on X) growth — original posts and replies under big AI accounts, following the researched playbook.
---
# @Gotwei growth skill

Read `x-ops/playbook.md` in this repo before each run; it holds the full rules, templates and evidence.

## Core rules
1. Strictly AI vertical. English. Never fabricate; verify every fact.
2. Default: put "Source: <link>" in a self-reply to keep the main post clean (v2 data: no measurable link penalty within accounts, n=7, so this is style, not a hard ban). Self-replies get ~4x the reach of replies to others, so use them to add a detail too.
3. Prefer video clips when you have them (video beat text-only in 72% of accounts, median 1.18x); photo alone is roughly neutral. Attach some media when possible (any media 59%, 1.19x). Long posts (>280 chars) win on bookmark rate in ~80% of accounts. Avoid quote-posts as a main format (they lose in 76% of accounts, median 0.75x).
4. Hooks: "BREAKING:" / "<COMPANY> 🔥:" for news; first-person hands-on takes and opinions beat neutral summaries.
5. Replies (~200/day, spaced out): target fresh, high-engagement posts from big AI accounts (Tibo, sama, karpathy, official labs). 40-150 chars of substance: a fact, number, source or sharp question (likes rise with length; reach does not). Replies to accounts with >=100k followers earn ~3.5x the relative reach of replies to smaller accounts. No "🔥"-only replies, no links, vary wording.
6. Original posts every 2 hours (08:00–22:00 Beijing) on the hottest AI topic; post breaking news immediately (posting hour showed no measurable effect within accounts). Weekly recap thread, pinned.
7. Stop and alert Drew on any rate-limit, spam warning, or logout.

## Persistence
All learnings go to this repo (yongchaoyin/agent-brain) under `x-ops/`. Update playbook.md and data/ as new findings come in.
