---
name: x-gotwei-growth
description: Run @Gotwei (wei news, AI news on X) growth — original posts and replies under big AI accounts, following the researched playbook.
---
# @Gotwei growth skill

Read `x-ops/playbook.md` in this repo before each run; it holds the full rules, templates and evidence.

## Core rules
1. Strictly AI vertical. English. Never fabricate; verify every fact.
2. Default: put "Source: <link>" in a self-reply to keep the main post clean (v2.2 data: no measurable link penalty within accounts, n=11, so this is style, not a hard ban). Self-replies get ~3.6x the reach of replies to others, so use them to add a detail too.
3. Prefer video clips when you have them (v2.2: video beat text-only in 67% of accounts, median 1.50x). Photos now show a mild lift (58%, 1.15x). Attach some media when possible (any media 66%, 1.28x). Long posts (>280 chars) win on reach in 64% (1.27x) and on bookmark rate in ~74%. Avoid quote-posts as a main format (they win in only 29% of accounts, median 0.81x). Do not add emoji just for engagement (v2.2: ~neutral/slightly negative).
4. Hooks: "BREAKING:" / "<COMPANY> 🔥:" for news; first-person hands-on takes and opinions beat neutral summaries.
5. Replies (~200/day, spaced out): target fresh, high-engagement posts from big AI accounts (Tibo, sama, karpathy, official labs, bcherny, OfficialLoganK). Prefer 40–200+ chars of substance: a fact, number, source or sharp question. v2.2: replies ≥200 chars get ~2× the relative reach of shorter ones (0.083 vs ~0.037); replies to accounts with ≥100k followers still earn ~2.6× vs smaller accounts. No "🔥"-only replies, no links, vary wording.
6. Original posts every 2 hours (08:00–22:00 Beijing) on the hottest AI topic; post breaking news immediately (posting hour showed no measurable effect within accounts). Weekly recap thread, pinned.
7. Stop and alert Drew on any rate-limit, spam warning, or logout.

## Persistence
All learnings go to this repo (yongchaoyin/agent-brain) under `x-ops/`. Update playbook.md and data/ as new findings come in.

## Creator study
Keep growing `x-ops/data/creators.csv` toward 1000 (followers≥10k, listed≥50, tweets≥300, real AI bio). Prefer curated lists over keyword search. Widen deep-sample windows when quota allows; leave ~50 public-read spare for ops. Current target progress: see playbook v2.2 (621/1000, 131 deep-sampled).
