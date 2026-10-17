from load import load;import re,statistics as st,collections,json
T=load()
def body(t): return re.sub(r'^(@\w+\s*)+','',t['text']).strip()
R=[t for t in T if any(x['type']=='replied_to' for x in t.get('referenced_tweets',[])) and t.get('in_reply_to_user_id')!=t['author_id']]
S=[t for t in T if t.get('in_reply_to_user_id')==t['author_id']]
O=[t for t in T if not t.get('referenced_tweets')]
print('replies to others',len(R),'self-thread',len(S),'originals',len(O))
def feats(t):
    b=body(t);b2=re.sub(r'https?://\S+','',b).strip()
    w=len(b2.split())
    return dict(b=b2,w=w,ch=len(b2),q=b2.rstrip().endswith('?'),hasq='?' in b2,low=bool(re.match(r'[a-z]',b2)),
      noend=bool(b2) and b2[-1] not in '.!?)"\'',em='—' in b2,emoji=bool(re.search(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]',b2)),
      lol=bool(re.search(r'\b(lol|lmao|haha|lmfao|ngl|tbh|imo|fr|idk)\b',b2,re.I)),i=bool(re.search(r"\b(I|I'm|I've|my|me)\b",b2)),
      excl='!' in b2,nl='\n' in b2,link=bool(re.search(r'https?://',body(t))))
def summ(L,name):
    F=[feats(t) for t in L];F=[f for f in F if f['b']]
    n=len(F);ws=sorted(f['w'] for f in F)
    pct=lambda k:round(100*sum(f[k] for f in F)/n,1)
    print(f"\n== {name} n={n} words p10/25/50/75/90:",[ws[int(n*p)] for p in (.1,.25,.5,.75,.9)],'chars median',st.median(f['ch'] for f in F))
    print({k:pct(k) for k in ['q','hasq','low','noend','em','emoji','lol','i','excl','nl']})
    b=collections.Counter(min(f['w']//5*5,60) for f in F);print('word buckets',sorted(b.items()))
    return F
FR=summ(R,'replies');summ(S,'self-thread');summ(O,'originals')
# engagement correlation within replies
import math
def g(t,k):return t['public_metrics'][k]
rows=[(feats(t),t) for t in R if body(t)]
def eng(sel,lab):
    L=[t for f,t in rows if sel(f)]
    if not L:return
    print(f"{lab:25s} n={len(L):4d} medLikes={st.median(g(t,'like_count') for t in L):4} meanLikes={st.mean(g(t,'like_count') for t in L):6.1f} medViews={st.median(g(t,'impression_count') for t in L):6} gotReply%={100*sum(g(t,'reply_count')>0 for t in L)/len(L):.0f}")
print()
for lab,s in [('all',lambda f:1),('ends ?',lambda f:f['q']),('no ?',lambda f:not f['hasq']),('lowercase start',lambda f:f['low']),('cap start',lambda f:not f['low']),('no end punct',lambda f:f['noend']),('emoji',lambda f:f['emoji']),('lol/ngl/tbh',lambda f:f['lol']),('first person',lambda f:f['i']),('em dash',lambda f:f['em']),('<=8w',lambda f:f['w']<=8),('9-20w',lambda f:9<=f['w']<=20),('21-40w',lambda f:21<=f['w']<=40),('>40w',lambda f:f['w']>40),('!',lambda f:f['excl']),('link',lambda f:f['link'])]: eng(s,lab)
# openers
op=collections.Counter(' '.join(f['b'].split()[:1]).lower().strip(',.!') for f in FR);print('\ntop first words',op.most_common(40))
json.dump([dict(text=f['b'],w=f['w'],url=t['url'],likes=g(t,'like_count'),views=g(t,'impression_count'),rc=g(t,'reply_count')) for f,t in rows],open('/tmp/replies.json','w'))
