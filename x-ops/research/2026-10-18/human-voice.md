# Human voice research — 2026-10-18 (phase 1, offline)

Source: `data/expand_cache/raw/*.txt` (146 creator timelines, read-only), parsed with `load.py`, stats by `an.py` / `mv.py` (copied here, rerunnable).
3,624 unique posts → **1,316 replies to others** (1,289 with text after stripping @mentions/links), 381 self-thread replies, 706 originals.

Caveats: these are the creators' *own* replies (many in their own threads / to friends), so likes are low (median 1, median 97 views). "gotReply" = the reply itself received ≥1 reply — a proxy for "someone (often the author) answered". No per-reply author identity, so it is not exact author-reply-back. Move-type regexes are rough; small n for some groups. Correlation, not causation.

## Headline numbers (replies to others, n=1,289)
| metric | real creators | @Gotwei (pre-10-18) |
|---|---|---|
| ends with "?" | **6.1%** (any "?" 9.0%) | 63% |
| lowercase first letter | **24.0%** | 0% |
| no final punctuation | **60.6%** | ~0% |
| em dash "—" | **0.3%** (4 of 1,289) | frequent |
| emoji | 16.4% | — |
| lol/ngl/tbh/imo/idk | 2.7% | 0 |
| first person (I/my/me) | 17.6% | rare |
| "!" | 21.3% | — |
| line breaks | 8.2% | — |
| words p10/25/50/75/90 | **1 / 2 / 6 / 14 / 32** (median 32 chars) | ~25 every time |

Word-count buckets (0–4, 5–9, …): 551, 269, 149, 84, 53, 43, 21, 35, 26, 35, 21, 2 → a long-tail: 43% under 5 words, 6% over 40 words. Length follows content, not a target.

Self-thread replies (n=366): median 28 words, 38% multi-line, "?" endings 1.1%. Originals (n=697): median 35 words, 69% multi-line, em dash 5.2%, "?" endings 2.4%, lowercase starts 6.9%.

## What correlates with engagement (replies)
| group | n | mean likes | median views | got a reply |
|---|---|---|---|---|
| all | 1315 | 3.7 | 97 | 39% |
| ends "?" | 79 | 5.4 | 147 | **72%** |
| lowercase start | 310 | 3.7 | 98 | 45% |
| first person | 227 | 4.9 | 93 | 43% |
| ≤8 words | 809 | 2.3 | 94 | 34% |
| 9–20 words | 287 | 5.3 | 101 | 44% |
| 21–40 words | 139 | 4.1 | 122 | 50% |
| >40 words | 80 | **11.9** | 93 | 49% |
| contains link | 132 | 5.9 | 120 | 55% |
| emoji | 212 | 2.5 | 69 | 27% |

Move types: pushback n=25 (mean 8.6 likes, 52% got reply); skeptic/doubt n=19 (7.1, 42%); personal experience n=14 (2.9, 50%); agree+add n=90 (5.3, 34%); humor n=78 (7.0, 40%); quote-a-line-and-respond (">") n=5 (12.2, 80%); question n=79 (5.4, 72%); congrats/thanks n=150 (2.5, 32%).

Read: (1) Real people almost never end on a question, but when they do it is a *specific* question born of curiosity, and it gets answered 72% of the time — so the problem was never questions, it was a question stapled to every reply. (2) Longer replies carry an argument (counter-evidence, analogy, own experience) and earn the most likes; length comes from having more to say. (3) Disagreement and quoting a specific line earn replies; emoji/congrats don't. (4) Humor posts are the top-liked singles (234, 173 likes).

Openers (top first words): i 60, congrats 43, thanks 31, this 27, you 22, yes 22, the 20, yeah 16, what 14, no 12, if 11, so 10, haha 9, oh 9, true 9, maybe 7, wait 5 … — no single opener above 5%. Nobody opens with a label like "BREAKING:" in replies.

## Verbatim examples by move type (likes / views / replies-to-it)
### Jokes / jabs
- "I wonder how many folks will pretend to work at OpenAI on dating apps to try to get seduced 😂" — 234 / 18,525 / 7 https://x.com/BlackHC/status/2110660140756263014
- "Zucc paid this dude lol" — 173 / 15,737 / 2 https://x.com/intheworldofai/status/2109736440326406515
- "Lmao wait is it actually down I assumed it was my shitty plane WiFi just not working" — 27 / 6,946 / 2 https://x.com/_aidan_clark_/status/2103622857930723617
- "BuzzFeed News... back when it still existed RIP" — 16 / 2,829 https://x.com/ParkerOrtolani/status/2111094801219063887
- "in the arena. but the arena is the cage you built for others, only to discover you live there too." — 101 / 7,736 https://x.com/nickfrosst/status/2108322403516285273
- "Gabriel, powered by Codex" — 15 / 3,629 https://x.com/gabrielchua/status/2110921049038897195
- "My eardrums are a small price to pay for a rocket car" — 14 / 612 https://x.com/viemccoy/status/2110936417673392580
- "This stage of progress is like: "We're gonna pry the panel off this machine and look inside. Whoops, our screwdriver just broke off in our hand. (Years later.) AWESOME NEWS THE SCREWDRIVER IS REPAIRED NOW."" — 23 / 879 https://x.com/allTheYud/status/2110853001749594363
### Pushback / disagreement
- "this seems to be for both closed and open models, and open models actually get the license almost automatically? (+ this is a proposal not in place yet) / i think your post is quite misleading…" — 116 / 7,566 / 4 https://x.com/eliebakouch/status/2111101966483063044
- "The thing is: from the beginning we always would have continued to call what we have now LLMs…" — 137 / 10,192 / 4 https://x.com/_aidan_clark_/status/2103907372964159855
- "afaict this is slightly misleading as the numerator counts the people served who are no longer homeless, and the denominator only counts those still homeless. (but it's still a lot)" — 11 / 463 https://x.com/catherineols/status/2095294802044883329
- "I am yet to see someone who doesn't work at OpenAI or Goodfire think that this is a big deal. I personally think it's both a) obviously false and b) presents little evidence worth engaging with." — 15 / 462 https://x.com/BlancheMinerva/status/2111148476830564750
- "I have and they don't" — 13 / 506 / 3 https://x.com/JeffLadish/status/2109899929103815151
- "Depends on what the harness is doing. If it tries to dictate how the model works, it fights the model and you get brittleness…" — 24 / 15,572 https://x.com/jiayq/status/2082559440922783854
- "This only makes sense if they reviewing process works…" (typo kept) — 16 / 1,115 https://x.com/yoavartzi/status/2110744184797737261
### Skeptic / doubt (short)
- "Wait what? How is this new?" — 82 / 21,229 / 3 https://x.com/koltregaskes/status/2110828172128444597
- "Not super sure about this" — 25 / 3,567 https://x.com/xiaolonw/status/2105683450292515149
- "Maybe this video is fake though" — 10 / 763 https://x.com/catherineols/status/2090699851000586680
- "seems like we did not expect it to be false???" — 24 / 5,730 / 4 https://x.com/catherineols/status/2079144281000845607
- "tbh i'm disappointed" — 17 / 18,097 https://x.com/minimaxir/status/2025975317211537486
- "where's the CI." — 25 / 2,212 https://x.com/kalomaze/status/2110493200687481247
### Personal experience
- "which ones? i've tried them all and landed back with claude code / codex" — 13 / 1,378 / 4 https://x.com/skeptrune/status/2110789098449584405
- "Echoing this... this morning we had a similar experience, quoting my cofounder: "I compared opus 5 vs 4.6 … Zero improvement…"" — 13 / 2,170 https://x.com/jiayq/status/2088062375467569195
- "This makes logical sense, but in my experience bosses that don't make a habit of doing the core thing … gradually become very ineffective" — 5 / 965
- "This is really cool! I've been doing a lot of CAD experiments in other domains. … LLMs are terrible at generating it directly but can generate python code to generate good CAD files" — 2 / 300 / 2
- "same for me when i tell the kids i used to (a) code in tensorflow 1 and (b) write everything by hand. we're dinosaurs 🦖" — https://x.com/_lewtun/status/2110449485143040204
### Agree + add something
- "yeah I'd love the "it's just hype"sters to explain why OpenAI fired the ppl who worked with the independent third party evaluator…" — 79 / 2,816 / 4 https://x.com/So8res/status/2108356890681909472
- "Yes, this is about transfer between models that derive from the same base model. AFAIK, this is part of frontier post-training…" — 44 / 2,265 https://x.com/OwainEvans_UK/status/2108605301163499933
- "In some sense, the labs cooperated nicely at the model level. Less so at the human level" — 33 / 3,101 https://x.com/jack_w_rae/status/2097356863193182639
- ""Missing mood" is exactly the right frame here" — 15 / 747 https://x.com/catherineols/status/2086857145967169936
- "Agreed." — 22 / 451 https://x.com/JeffLadish/status/2110144471522509272
- "both sides too" — 25 / 24,324 / 4 https://x.com/ParkerOrtolani/status/2111168342526443596
### Specific, curious questions (the 6%)
- "What does RL add here compared to doing IK?" — 39 / 10,916 / **8** https://x.com/xiaolonw/status/2105330449497395529
- "How do I get one?" — 26 / 2,307 / 3 https://x.com/sualehasif996/status/2090559251207037158
- "Sam, are you buying more compute from Elon?" — 12 / 1,525 https://x.com/1littlecoder/status/2111134810181980350
- "> lack of open debate / what is this referring to?" — 18 / 2,731 / 2 https://x.com/catherineols/status/2086906911992205507
### Practical additions
- "Congrats on the release and thank you for the open weights! You will be able to run Muse Spark open on two Mac Studios with 256GB or one with 512GB Using MLX-VLM…" — 77 / 6,631 / 3 (Prince_Canuma)
- "You can just do IK for this" — 15 / 910 https://x.com/xiaolonw/status/2105163892360089894
- "have you tried reinstalling the driver" — 18 / 697 https://x.com/VoidAsuka/status/2107233397483655351
- "forget conda" — 11 / 271 / 2 https://x.com/kalomaze/status/2111254491819655453
### Continuing an argument (multi-turn, same person in one thread)
- allTheYud ran 5+ replies in one thread, each a different shape: a question ("Which particular problem of superalignment had…"), an analogy ("No, I'm saying that this is like putting money into a Coke machine…"), a concession+condition ("If I thought interpretability had a realistic chance…"), a joke (screwdriver). https://x.com/allTheYud/status/2110838232988721463 , …/2110833841996972424 , …/2110851890292650179
- catherineols quotes the exact line she answers ("> altered the weights … again as I said elsewhere I think this is wrong… WDYT?") https://x.com/catherineols/status/2081074333825286506
- togelius clarifies instead of repeating: "If you read the post, I'm very much not arguing for ignoring the developments, rather…" — 47 / 1,632 / 3 https://x.com/togelius/status/2109062926657310873
- togelius concedes: "This is actually a very good counterargument, and also rhyme with what I see…" https://x.com/togelius/status/2109480405447463161

Typos/informality occur and are left in ("they reviewing process", "also rhyme with", "Ukranian", "dont join academia"). We should not fake typos, but should stop polishing everything.

## Own-data reference
Best-ever @Gotwei reply: short casual jab under @dtzy_88's DeepSeek test post, 1.5h late, 2.9K views / 15 likes; the author answered and that lifted it. Worst pattern: 63% of replies ended in "?", ~25 words each, all "X is the real story / the number that matters" + follow-up question; someone replied "Bot".

## Phase 2 (pending)
X API reads of top replies under big AI posts (sama, karpathy, OpenAI, AnthropicAI, kimmonismus, btibor91, scaling01, testingcatalog, Yuchenj_UW) and author-reply-back threads — scheduled after the 08:00 quota reset; appended in a later commit if done.

## Raw stat output
```
replies to others 1316 self-thread 381 originals 706

== replies n=1289 words p10/25/50/75/90: [1, 2, 6, 14, 32] chars median 32
{'q': 6.1, 'hasq': 9.0, 'low': 24.0, 'noend': 60.6, 'em': 0.3, 'emoji': 16.4, 'lol': 2.7, 'i': 17.6, 'excl': 21.3, 'nl': 8.2}
word buckets [(0, 551), (5, 269), (10, 149), (15, 84), (20, 53), (25, 43), (30, 21), (35, 35), (40, 26), (45, 35), (50, 21), (55, 2)]

== self-thread n=366 words p10/25/50/75/90: [4, 9, 28, 40, 45] chars median 177.0
{'q': 1.1, 'hasq': 3.8, 'low': 8.5, 'noend': 64.2, 'em': 1.1, 'emoji': 15.3, 'lol': 0.3, 'i': 13.7, 'excl': 10.4, 'nl': 38.0}
word buckets [(0, 45), (5, 56), (10, 20), (15, 19), (20, 22), (25, 27), (30, 38), (35, 45), (40, 51), (45, 30), (50, 13)]

== originals n=697 words p10/25/50/75/90: [4, 13, 35, 43, 47] chars median 219
{'q': 2.4, 'hasq': 10.8, 'low': 6.9, 'noend': 75.5, 'em': 5.2, 'emoji': 19.7, 'lol': 0.6, 'i': 13.2, 'excl': 15.1, 'nl': 68.6}
word buckets [(0, 71), (5, 52), (10, 62), (15, 36), (20, 29), (25, 39), (30, 46), (35, 89), (40, 142), (45, 104), (50, 26), (60, 1)]

all                       n=1315 medLikes=   1 meanLikes=   3.7 medViews=    97 gotReply%=39
ends ?                    n=  79 medLikes=   1 meanLikes=   5.4 medViews=   147 gotReply%=72
no ?                      n=1199 medLikes=   1 meanLikes=   3.5 medViews=    94 gotReply%=36
lowercase start           n= 310 medLikes= 1.0 meanLikes=   3.7 medViews=  98.5 gotReply%=45
cap start                 n=1005 medLikes=   1 meanLikes=   3.7 medViews=    97 gotReply%=37
no end punct              n= 781 medLikes=   1 meanLikes=   3.1 medViews=    92 gotReply%=35
emoji                     n= 212 medLikes= 1.0 meanLikes=   2.5 medViews=  69.0 gotReply%=27
lol/ngl/tbh               n=  35 medLikes=   1 meanLikes=   7.5 medViews=    63 gotReply%=40
first person              n= 227 medLikes=   1 meanLikes=   4.9 medViews=    93 gotReply%=43
em dash                   n=   4 medLikes= 1.0 meanLikes=   1.0 medViews= 103.5 gotReply%=0
<=8w                      n= 809 medLikes=   1 meanLikes=   2.3 medViews=    94 gotReply%=34
9-20w                     n= 287 medLikes=   1 meanLikes=   5.3 medViews=   101 gotReply%=44
21-40w                    n= 139 medLikes=   1 meanLikes=   4.1 medViews=   122 gotReply%=50
>40w                      n=  80 medLikes= 1.0 meanLikes=  11.9 medViews=  92.5 gotReply%=49
!                         n= 275 medLikes=   1 meanLikes=   2.1 medViews=   104 gotReply%=40
link                      n= 132 medLikes= 2.0 meanLikes=   5.9 medViews= 119.5 gotReply%=55

top first words [('i', 60), ('congrats', 43), ('thanks', 31), ('this', 27), ('you', 22), ('yes', 22), ('the', 20), ('thank', 17), ('yeah', 16), ('happy', 16), ('what', 14), ('no', 12), ('if', 11), ('so', 10), ('congratulations', 9), ('can', 9), ("it's", 9), ('we', 9), ('how', 9), ('haha', 9), ('oh', 9), ('true', 9), ('love', 8), ('awesome', 8), ('maybe', 7), ('hi', 7), ('very', 7), ("i'm", 7), ('it’s', 6), ('it', 6), ('nice', 6), ('really', 6), ('🤣', 6), ('and', 6), ('welcome', 5), ('just', 5), ('do', 5), ('that', 5), ('a', 5), ('wow', 5)]

pushback         n=  25 share= 1.9% medLikes=2 meanLikes=8.6 medViews=68 gotReply=52%
skeptic/doubt    n=  19 share= 1.4% medLikes=1 meanLikes=7.1 medViews=89 gotReply=42%
personal exp     n=  14 share= 1.1% medLikes=1.0 meanLikes=2.9 medViews=123.0 gotReply=50%
agree+add        n=  90 share= 6.8% medLikes=1.0 meanLikes=5.3 medViews=85.0 gotReply=34%
humor            n=  78 share= 5.9% medLikes=1.0 meanLikes=7.0 medViews=54.0 gotReply=40%
quote-respond    n=   5 share= 0.4% medLikes=16 meanLikes=12.2 medViews=579 gotReply=80%
question         n=  79 share= 6.0% medLikes=1 meanLikes=5.4 medViews=147 gotReply=72%
congrats/thanks  n= 150 share=11.4% medLikes=1.0 meanLikes=2.5 medViews=165.5 gotReply=32%

## pushback
- "this seems to be for both closed and open models, and open models actually get the license almost automatically? (+ this is a proposal not in place yet) /  / i think your post is quite misleading as most people will read "it" — 116 likes, 7566 views, 4 replies, https://x.com/eliebakouch/status/2111101966483063044
- "Not super sure about this" — 25 likes, 3567 views, 0 replies, https://x.com/xiaolonw/status/2105683450292515149
- "No, I'm saying that this is like putting money into a Coke machine and having a Coke come out, and you've still got no idea how the Coke gets made or where it comes from or the recipe that produces it, but you built an X" — 17 likes, 773 views, 3 replies, https://x.com/allTheYud/status/2110833841996972424
- "&gt; 3. It is very rare, even via egg freezing and IVF, that a woman is able get pregnant after 40. /  / This is not true. Eggs extracted from &gt;40yo women work less well, but the uterus is totally fine. See donor egg stat" — 16 likes, 579 views, 0 replies, https://x.com/catherineols/status/2086930927742222701
- "afaict this is slightly misleading as the numerator counts the people served who are no longer homeless, and the denominator only counts those still homeless. (but it's still a lot)" — 11 likes, 463 views, 1 replies, https://x.com/catherineols/status/2095294802044883329
- "haha, yeah, I don't think anyone does really, but it's basically this:" — 4 likes, 93 views, 2 replies, https://x.com/sqs/status/2111122080188219548
- "I don't think it's AI" — 3 likes, 48 views, 1 replies, https://x.com/k1rallik/status/2111170546159227303

## skeptic/doubt
- "Wait what? How is this new?" — 82 likes, 21229 views, 3 replies, https://x.com/koltregaskes/status/2110828172128444597
- "Not super sure about this" — 25 likes, 3567 views, 0 replies, https://x.com/xiaolonw/status/2105683450292515149
- "Maybe this video is fake though" — 10 likes, 763 views, 0 replies, https://x.com/catherineols/status/2090699851000586680
- "Really cool!" — 4 likes, 269 views, 0 replies, https://x.com/LeRobotHF/status/2105911328401719398
- "Wait, your phone creating files, running code and all 🔥🙌🏽" — 3 likes, 1053 views, 1 replies, https://x.com/Prince_Canuma/status/2107957135095058728
- "Wait, I'm not the foreman?" — 3 likes, 172 views, 0 replies, https://x.com/zachlloydtweets/status/2110818953346076791
- "Really enjoy the art in your talk! And the ideas are 👌" — 2 likes, 302 views, 1 replies, https://x.com/clintgibler/status/2100458776537215471

## personal exp
- "Echoing this... this morning we had a similar experience, quoting my cofounder: "I compared opus 5 vs 4.6 on a small but a bit hard hobby project i tried back in Jan. Zero improvement, both took almost 1.5 days. Opus5 ac" — 13 likes, 2170 views, 1 replies, https://x.com/jiayq/status/2088062375467569195
- "which ones? i've tried them all and landed back with claude code / codex" — 13 likes, 1378 views, 4 replies, https://x.com/skeptrune/status/2110789098449584405
- "This makes logical sense, but in my experience bosses that don’t make a habit of doing the core thing that their organization does gradually become very ineffective, even though the manager job is totally different" — 5 likes, 965 views, 1 replies, https://x.com/l2k/status/2107599582779859121
- "I use branches and merges. You can rollback merges, right?" — 3 likes, 1210 views, 3 replies, https://x.com/kieranklaassen/status/2111149477780480107
- "This is really cool! I’ve been doing a lot of CAD experiments in other domains. My experience sounds similar that the LLMs are terrible at generating it directly but can generate python code to generate good CAD files" — 2 likes, 300 views, 2 replies, https://x.com/l2k/status/2051704128963801174
- "same for me when i tell the kids i used to (a) code in tensorflow 1 and (b) write everything by hand. /  / we're dinosaurs 🦖" — 1 likes, 64 views, 0 replies, https://x.com/_lewtun/status/2110449485143040204
- "i tried not many face fat left" — 1 likes, 243 views, 0 replies, https://x.com/VoidAsuka/status/2106994306187952588

## agree+add
- "this seems to be for both closed and open models, and open models actually get the license almost automatically? (+ this is a proposal not in place yet) /  / i think your post is quite misleading as most people will read "it" — 116 likes, 7566 views, 4 replies, https://x.com/eliebakouch/status/2111101966483063044
- "yeah I'd love the "it's just hype"sters to explain why OpenAI fired the ppl who worked with the independent third party evaluator that exposed how bad things got" — 79 likes, 2816 views, 4 replies, https://x.com/So8res/status/2108356890681909472
- "Yeah if you're gonna do a giant victory dance and tell me what I'm gonna think about it, then there's no victory, I get annoyed. /  / It sounds like you don't believe in any of the problems of superalignment that are unlike " — 46 likes, 3360 views, 4 replies, https://x.com/allTheYud/status/2110838752008659168
- "Yes, this is about transfer between models that derive from the same base model. AFAIK, this is part of frontier post-training. Labs create many copies of the same base model, RL them on specific skills (math, code, law," — 44 likes, 2265 views, 1 replies, https://x.com/OwainEvans_UK/status/2108605301163499933
- "This stage of progress is like:  "We're gonna pry the panel off this machine and look inside.  Whoops, our screwdriver just broke off in our hand.  (Years later.)  AWESOME NEWS THE SCREWDRIVER IS REPAIRED NOW."" — 23 likes, 879 views, 2 replies, https://x.com/allTheYud/status/2110853001749594363
- "Agreed." — 22 likes, 451 views, 0 replies, https://x.com/JeffLadish/status/2110144471522509272
- "This only makes sense if they reviewing process works. The process is under a lot of stress. 10% random chance or 20% random chance... both are meaningless, because the quality of the accepted pool remains random /  / Loweri" — 16 likes, 1115 views, 2 replies, https://x.com/yoavartzi/status/2110744184797737261

## humor
- "I wonder how many folks will pretend to work at OpenAI on dating apps to try to get seduced 😂" — 234 likes, 18525 views, 7 replies, https://x.com/BlackHC/status/2110660140756263014
- "Zucc paid this dude lol" — 173 likes, 15737 views, 2 replies, https://x.com/intheworldofai/status/2109736440326406515
- "Lmao wait is it actually down I assumed it was my shitty plane WiFi just not working" — 27 likes, 6946 views, 2 replies, https://x.com/_aidan_clark_/status/2103622857930723617
- "BuzzFeed News... back when it still existed RIP" — 16 likes, 2829 views, 1 replies, https://x.com/ParkerOrtolani/status/2111094801219063887
- "The Booster head is rock solid 😅" — 13 likes, 381 views, 1 replies, https://x.com/RemiCadene/status/2107841376649900214
- "😂😂😂" — 6 likes, 1062 views, 0 replies, https://x.com/eliebakouch/status/2110846697999852017
- "lol thank you Siamak" — 5 likes, 420 views, 1 replies, https://x.com/nickfrosst/status/2097846791186116621

## quote-respond
- "&gt; very strongly implying they altered the weights to dampen the model's normal tendency /  / Reasonable guess, but later it says they removed "production classifiers", where the classifier is external to (and subsequent t" — 19 likes, 585 views, 1 replies, https://x.com/catherineols/status/2081074005520290221
- "&gt; lack of open debate / what is this referring to?" — 18 likes, 2731 views, 2 replies, https://x.com/catherineols/status/2086906911992205507
- "&gt; 3. It is very rare, even via egg freezing and IVF, that a woman is able get pregnant after 40. /  / This is not true. Eggs extracted from &gt;40yo women work less well, but the uterus is totally fine. See donor egg stat" — 16 likes, 579 views, 0 replies, https://x.com/catherineols/status/2086930927742222701
- "&gt; altered the weights /  / again as I said elsewhere I think this is wrong, I think they removed a *classifier*, but left the *generative model* fully alone, WDYT?" — 8 likes, 141 views, 1 replies, https://x.com/catherineols/status/2081074333825286506
- "&gt; if anything "submitting" will probably give you more control over your fate. /  / Really confusing conclusion! I'm proposing methodology for increasing human oversight, agency, and control before we decide if we've buil" — 0 likes, 46 views, 1 replies, https://x.com/viemccoy/status/2110935994891678083

## question
- "Why is never time for Putin to go? How can you consistently blame Ukraine for fighting for its existence?" — 89 likes, 1303 views, 2 replies, https://x.com/BlackHC/status/2110632966431117433
- "Wait what? How is this new?" — 82 likes, 21229 views, 3 replies, https://x.com/koltregaskes/status/2110828172128444597
- "What does RL add here compared to doing IK?" — 39 likes, 10916 views, 8 replies, https://x.com/xiaolonw/status/2105330449497395529
- "How do I get one?" — 26 likes, 2307 views, 3 replies, https://x.com/sualehasif996/status/2090559251207037158
- "seems like we did not expect it to be false???" — 24 likes, 5730 views, 4 replies, https://x.com/catherineols/status/2079144281000845607
- "Which particular problem of superalignment had the critical subproblem that we don't know which neurons often fire when an LLM thinks about a related concept?" — 23 likes, 1060 views, 3 replies, https://x.com/allTheYud/status/2110838232988721463
- "&gt; lack of open debate / what is this referring to?" — 18 likes, 2731 views, 2 replies, https://x.com/catherineols/status/2086906911992205507

## congrats/thanks
- "Congrats on the release and thank you for the open weights!  /  / You will be able to run Muse Spark open on two Mac Studios with 256GB or one with 512GB  /  / Using MLX-VLM and @Nativ_AI" — 77 likes, 6631 views, 3 replies, https://x.com/Prince_Canuma/status/2110789703414784094
- "Congrats, looks like very nice science went into this run" — 29 likes, 5069 views, 0 replies, https://x.com/jack_w_rae/status/2110807121352901036
- "Congrats Jiahui! Looking forward to what you'll build next!" — 24 likes, 5482 views, 0 replies, https://x.com/jiayq/status/2087943919376142560
- "congrats on the release 🔥 /  / can't wait to try it :)" — 22 likes, 3886 views, 1 replies, https://x.com/atomic_chat_hq/status/2110752032655393147
- "welcome back :) :) :)" — 13 likes, 1405 views, 2 replies, https://x.com/nickfrosst/status/2102078544910151812
- "congrats!! looking forward to the tech report 🫡" — 9 likes, 1076 views, 0 replies, https://x.com/eliebakouch/status/2111087325669458011
- "Congrats! Big day for American OSS, and proud to be a day 0 launch partner!" — 9 likes, 384 views, 1 replies, https://x.com/baseten/status/2110753227537076710
```
