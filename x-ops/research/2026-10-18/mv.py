import json,re,statistics as st
R=json.load(open('replies.json'))
M={'pushback':r"^(no\b|not\b|nah|this is not|i disagree|disagree|that's not|wrong|misleading)|misleading|\bnot true\b|i don'?t think",
'skeptic/doubt':r"^(wait|hmm|really\??|doubt|not sure|not super sure|source\?)|\b(maybe .* fake|i doubt|skeptical|citation)",
'personal exp':r"\b(i tried|i've tried|i've been|we had|in my experience|i use|i ran|i tested|my experience|i compared|landed back)",
'agree+add':r"^(yes|yeah|yep|true|exactly|agreed|this\b|100%|same)",
'humor':r"(lol|lmao|haha|😂|🤣|😅|💀|rip\b)",
'quote-respond':r"^&gt;",
'question':r"\?\s*$",
'congrats/thanks':r"^(congrat|thank|happy|welcome|love|awesome|nice|great)"}
out={}
for k,p in M.items():
    L=[r for r in R if re.search(p,r['text'],re.I)]
    out[k]=L
    print(f"{k:16s} n={len(L):4d} share={100*len(L)/len(R):4.1f}% medLikes={st.median([r['likes'] for r in L])} meanLikes={st.mean([r['likes'] for r in L]):.1f} medViews={st.median([r['views'] for r in L])} gotReply={100*sum(r['rc']>0 for r in L)/len(L):.0f}%")
for k,L in out.items():
    print('\n##',k)
    for r in sorted(L,key=lambda r:-r['likes'])[:7]: print(f"- \"{r['text'][:220].replace(chr(10),' / ')}\" — {r['likes']} likes, {r['views']} views, {r['rc']} replies, {r['url']}")
