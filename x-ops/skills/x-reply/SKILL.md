---
name: x-reply
description: Use when writing replies for @Gotwei (运营小婷's job) — choosing targets, timing, wording, self-replies and replying under our own posts.
---
# X replies

## Whom
1. Prefer fresh posts from big AI accounts (≥100k followers) — **stronger** 2026-10-17: replies to ≥100k beat replies to <100k in 100% of 11 accounts (3.77×; pooled rel 0.020 <100k → 0.041 100k–1M → 0.056 ≥1M; v2.2 ~2.6×). Caveat: at 0 followers @Gotwei saw no lift yet (median 2 imp for every target tier, n=167) — freshness/position under the parent is what we lack.
2. But big accounts' replies are ranked first, so a small account is also visible under **mid-size** AI posts — mix both (reply research, 2026-10-16).
3. Target list: testingcatalog, btibor91, kimmonismus, ai_for_success, AILeaksAndNews, chetaslua, scaling01, iScienceLuvr, sama, karpathy, official labs, bcherny, OfficialLoganK; more in `data/creators.csv`. Track done IDs in `data/replied_ids.txt` (never reply twice).

## When (most important)
4. Only reply to posts **<2h old**; on mega-posts only in the first **30 min**. Top replies land 1–3h after the parent; our 1–7h-late replies got 1–5 impressions (https://x.com/NFiniT7777/status/2109372159923757516 vs ours https://x.com/Gotwei/status/2111015685044281673). *Supersedes v1 "within 15 min of notification" as the core rule; earlier is still better.*

## What
5. Add substance: a concrete fact, number, source, or reasoned pushback (https://x.com/Sophty_/status/2110896402251514276, https://x.com/m_adams/status/2110053908748148783). Plain agreement doesn't travel.
6. Length (v2.3, supersedes the old "≥200 chars" rule, which came from late replies on small threads): length depends on parent type — see "v2.3 rules" below.
7. Early image/GIF + short caption wins on mega-posts; late copycats get nothing (https://x.com/igor_pesin/status/2109627274773590076).
8. A specific "how does X work" question gets author replies (https://x.com/fchollet/status/2109100717596381405) but few likes — use for relationships.
9. Never: "🔥"/"Congrats"/"woah"/"LFG"/"thanks" only, snark, piling on, links, @-ing for traffic. One-word replies work only for established accounts (ns123abc "🫡" 13,250 imp https://x.com/i/status/2110114683348721757) — not us. Vary wording.
10. Tone: peer, professional, relaxed; humor ok, no arguing.
11. Template T12: `@{bigaccount} Worth adding: {fact/number/source they didn't mention}. {short implication or sharp question}?`

## Self-replies & own threads
12. Every original gets a self-reply (source and/or extra detail). Self-replies beat replies to others in 98% of 62 accounts (6.33×, 2026-10-17; v2.2 ~3.6× → **stronger**), and originals with a self-reply out-reach those without (79% of 34 accounts, 1.28×). Only 12% of top accounts' self-replies carry links — add content, not just links.
13. Reply to every comment under our posts within 1h.

Note: some top accounts' high reply counts are community management under their own posts with tiny views (ai_for_success), vs. minchoi's quick reactions under big accounts (150–8.8K views) — see research/2026-10-16/creator-top-posts-batch1-raw.md.
More examples & data: references/evidence.md.


## v2.3 rules (2026-10-17, from overnight research; pending validation by data review)
- Only reply to AI posts < 15 min old whose views are already climbing (thousands+). Late replies got 2–13 views.
- No "A, B, or C?" endings. Lead with a stance; vary sentence shape.
- Length evidence (2026-10-17, within-account): <60-char replies ≈ 60–200-char ones (43% of 28 accounts, 0.97×) → short replies are not penalized; ≥200 chars 70% of 10 accounts, 1.10× (v2.2 0.083 vs ~0.037 → weaker). Median creator reply: 36 chars, 342 imp.
- By parent type:
  - Big account, life/chit-chat post: deadpan joke or rhetorical question, ≤ 60 chars (top replies median 20–40 chars).
  - Big account, AI launch/model post: one-line judgement, ≤ 80 chars.
  - Technical post / mid-size account: 120–250 chars, a concrete number + one pointed follow-up; or a jargon quip (30–60 chars, e.g. "4k tokens context window btw"); or congrats + a usable resource.
- Red lines: no swearing, insults, or attacks on specific people.
- Volume: ≤ 1 reply per 5 min, ≤ 60 replies/day until the account gains trust (2026-10-16 data: 204 replies, median 2.5 views, 0 likes); posts+replies ≤ 170 per rolling 24h (free-account cap ~200 was hit on 2026-10-16).
- Browser: one tab, ≤ 2 page loads/min, only one agent on the @Gotwei login at a time; stop on 429/splash.
- Examples (2026-10-17 sample): insider answer "Hi! I work on Cowork…" → @GergelyOrosz 185,248 imp (https://x.com/felixrieseberg/status/2107206431376334975); friendly pushback "you really need to learn to get to the point" → @nickcammarata 62,040 / 713 likes (https://x.com/giffmana/status/2110814420553322983); 53-char quip → @liron 43,316 (https://x.com/robertskmiles/status/2110625716765389090); numbers-based pushback 72,520 (https://x.com/dylan522p/status/2108948086626369842).
- Template T12b (quip, big account, ≤60 chars): `@{bigaccount} {deadpan observation tied to a specific detail in their post}` — no emoji-only, no "congrats".
