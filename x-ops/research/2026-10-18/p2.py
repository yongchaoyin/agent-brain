import sys,glob,json,re,statistics as st,collections,os
sys.path.insert(0,'/tmp');from px import P
from datetime import datetime as D
TH={'2111131677351432197':('sama','2026-10-16T16:26:29'),'2109361546505966046':('karpathy','2026-10-11T19:12:37'),'2110047081414987957':('AnthropicAI','2026-10-13T16:36:41'),'2111192259073094035':('OpenAI','2026-10-16T20:27:13'),'2111374692028158023':('kimmonismus','2026-10-17T08:32:08'),'2111422471799013809':('kimmonismus','2026-10-17T11:42:00'),'2111518455216394680':('scaling01','2026-10-17T18:03:24'),'2111510402140197252':('Yuchenj_UW','2026-10-17T17:31:24'),'2111380259295653976':('testingcatalog','2026-10-17T08:54:16'),'2111525476292341861':('kimmonismus','2026-10-17T18:31:18')}
R={};U={};AR=[];INC={}
for f in [g for g in glob.glob('*.txt') if os.path.getmtime(g)>D(2026,10,18,8,0).timestamp()]:
    t=open(f).read()
    if 'conversation_id:' not in t and 'is:reply' not in t: pass
    try:d,_=P(f)
    except Exception:continue
    for u in d.get('includes',{}).get('users',[]):U[u['id']]=u
    for x in d.get('includes',{}).get('tweets',[]):INC[x['id']]=x
    for p in d.get('data',[]):R[p['id']]=p
def body(s):return re.sub(r'https?://\S+','',re.sub(r'^(@\w+\s*)+','',s)).strip()
rows=[]
for p in R.values():
    c=p.get('conversation_id')
    # conversation search results lack conversation_id field; infer via replied_to chain
    rows.append(p)
# thread replies: those whose in our thread windows -> identify by referenced replied_to == thread id (direct) 
th=[]
for p in R.values():
    rt=[x['id'] for x in p.get('referenced_tweets',[]) if x['type']=='replied_to']
    if rt and rt[0] in TH:
        a,t0=TH[rt[0]];mins=(D.fromisoformat(p['created_at'][:19])-D.fromisoformat(t0)).total_seconds()/60
        u=U.get(p['author_id'],{});b=body(p['text'])
        th.append(dict(thread=rt[0],acct=a,mins=mins,likes=p['public_metrics']['like_count'],views=p['public_metrics'].get('impression_count',0),rc=p['public_metrics']['reply_count'],fol=u.get('public_metrics',{}).get('followers_count',0),user=u.get('username'),text=b,w=len(b.split()),url=f"https://x.com/{u.get('username')}/status/{p['id']}",id=p['id']))
print('direct replies',len(th))
json.dump(th,open('/tmp/th.json','w'))
def s(L,lab):
    if not L:return
    print(f"{lab:22s} n={len(L):3d} medViews={st.median([x['views'] for x in L]):7.0f} meanViews={st.mean([x['views'] for x in L]):8.0f} medLikes={st.median([x['likes'] for x in L])} gotReply={100*sum(x['rc']>0 for x in L)/len(L):.0f}%")
for lo,hi in [(0,5),(5,20),(20,60),(60,120)]: s([x for x in th if lo<=x['mins']<hi],f'{lo}-{hi} min')
for lo,hi in [(0,1000),(1000,10000),(10000,1e9)]: s([x for x in th if lo<=x['fol']<hi],f'followers {lo}-{hi}')
for lab,f in [('ends ?',lambda x:x['text'].endswith('?')),('lowercase',lambda x:bool(re.match('[a-z]',x['text']))),('<=8w',lambda x:x['w']<=8),('9-25w',lambda x:9<=x['w']<=25),('>25w',lambda x:x['w']>25),('media/link only',lambda x:x['w']==0),('humor',lambda x:bool(re.search(r'lol|lmao|😂|🤣|💀|haha',x['text'],re.I)))]: s([x for x in th if f(x)],lab)
F=[x for x in th if x['w']>0]
print('stats: ?end %.1f lower %.1f emdash %.1f median words %s'%(100*sum(x['text'].endswith('?') for x in F)/len(F),100*sum(bool(re.match('[a-z]',x['text'])) for x in F)/len(F),100*sum('—' in x['text'] for x in F)/len(F),st.median(x['w'] for x in F)))
print('\nTOP by views')
for x in sorted(th,key=lambda x:-x['views'])[:30]: print(f"{x['views']:6d} {x['likes']:4d} rc{x['rc']} {x['mins']:5.0f}m fol{x['fol']:7d} @{x['acct']} {x['url']} | {x['text'][:150]}".replace('\n',' / '))
# author replies to commenters
print('\nAUTHOR REPLIES')
ac=[]
for p in R.values():
    au=U.get(p['author_id'],{}).get('username','?')
    rt=[x['id'] for x in p.get('referenced_tweets',[]) if x['type']=='replied_to']
    if au in ('kimmonismus','scaling01','Yuchenj_UW','testingcatalog','btibor91','karpathy','sama') and rt and rt[0] in INC:
        par=INC[rt[0]];pu=U.get(par['author_id'],{})
        if pu.get('username')==au: continue
        ac.append((au,pu.get('username'),pu.get('public_metrics',{}).get('followers_count'),body(par['text'])[:200],body(p['text'])[:160],p['public_metrics'].get('impression_count'),p['public_metrics']['like_count'],f"https://x.com/{au}/status/{p['id']}"))
print(len(ac))
for a in ac: print(' | '.join(map(str,a)).replace('\n',' / '))
