import csv,json,sys,re,os,statistics as st
from datetime import datetime
D='/workspace/agent-brain/x-ops/data/'
OUT=D+'creators_expand.csv'
ids=json.load(open(D+'expand_cache/ids.json'))
byid={v['id']:v for v in ids.values()}
rows={r['username'].lower():r for r in csv.DictReader(open(D+'creators.csv'))}
hdr=list(next(csv.reader(open(D+'creators.csv'))))
done=set()
if os.path.exists(OUT): done={r['username'].lower() for r in csv.DictReader(open(OUT))}
AI=re.compile(r'\b(ai|a\.i\.|llms?|gpt\S*|agi|agents?|agentic|models?|claude|gemini|openai|anthropic|grok|deepseek|qwen|llama|mistral|neural|transformers?|diffusion|inference|training|fine-?tun\w*|rag|prompt\w*|chatbots?|copilot|cursor|machine learning|ml|deep learning|benchmarks?|evals?|tokens?|gpus?|reasoning|multimodal|genai|robot\w*|sora|veo|midjourney|nvidia|alignment)\b',re.I)
def cat(bio):
    b=bio.lower()
    if re.search(r'newsletter|\bnews\b|journalist|reporter|podcast|writer|editor|substack|weekly|daily',b): return 'news/newsletter'
    if re.search(r'research|professor|phd|scientist|lab\b|university|prof\b|institute|paper',b): return 'research'
    if re.search(r'\b(art|artist|creative|film\w*|design\w*|music|video|image|generative|genai|creator|animation)\b',b): return 'creative/genAI'
    if re.search(r'founder|ceo|co-?founder|building|startup|builder|cto|company|platform|we build|investor|vc\b|partner',b): return 'founder/builder'
    if re.search(r'engineer|developer|dev\b|software|programmer|code|coding|hacker|open source|oss',b): return 'engineer'
    return 'other'
def hook(t):
    t=re.sub(r'^(@\w+\s*)+','',t).strip()
    if not t: return 'bare mention'
    if re.match(r'^https?://',t): return 'bare link/media'
    f=t.split('\n')[0]
    if '?' in f[:120]: return 'a question'
    if re.match(r'^\d',t): return 'a number/list'
    if re.match(r'^(new|introducing|announcing|today|just|we|excited|launch)',t,re.I): return 'an announcement ("%s...")'%' '.join(t.split()[:3])[:25]
    if re.match(r'^[^\w\s@#"\']',t): return 'an emoji/symbol lead'
    return 'a statement ("%s...")'%' '.join(t.split()[:3])[:25]
def proc(uid,path):
    t=open(path).read()
    u=byid[uid]; r=dict(rows[u['username'].lower()])
    if u['username'].lower() in done: return
    try:
        s=t.index('{');e=t.rindex('\nX reads')
        d=json.loads(t[s:e].strip().split('\n')[0] if t[s:e].strip().startswith('{"data"') else t[s:e])
    except Exception as ex: d={}
    P=d.get('data') or []
    r['category']=cat(r['bio'])
    if not P:
        r.update(sampled_posts=0,window_days='',posts_per_day='',reply_pct='',ai_share_orig='',median_impressions_orig='',median_engagement_rate='')
        err=(d.get('errors') or [{}])[0].get('detail') or (d.get('errors') or [{}])[0].get('title') or d.get('detail')
        r['quality_note']='No posts returned'+(f' ({err})' if err else ' (protected, suspended, or no recent posts)')+'.'
    else:
        ty=lambda p:{x['type'] for x in p.get('referenced_tweets',[])}
        reps=[p for p in P if 'replied_to' in ty(p)]
        rts=[p for p in P if 'retweeted' in ty(p)]
        orig=[p for p in P if not ({'replied_to','retweeted'}&ty(p))]
        ts=[datetime.fromisoformat(p['created_at'].replace('Z','+00:00')) for p in P]
        w=max(1,round((max(ts)-min(ts)).total_seconds()/86400,2))
        m=lambda p:p['public_metrics']
        ers=[(m(p)['like_count']+m(p)['retweet_count']+m(p)['reply_count']+m(p)['quote_count'])/m(p)['impression_count'] for p in P if m(p).get('impression_count')]
        n=len(P)
        r.update(sampled_posts=n,window_days=w,posts_per_day=round(n/w,3),reply_pct=round(len(reps)/n,3),
          ai_share_orig=round(sum(1 for p in orig if AI.search(p['text']))/len(orig),3) if orig else '',
          median_impressions_orig=round(st.median([m(p)['impression_count'] for p in orig])) if orig else '',
          median_engagement_rate=round(st.median(ers),3) if ers else '')
        fm={'replies':len(reps),'retweets':len(rts)}
        q=[p for p in orig if 'quoted' in ty(p)];fm['quote posts']=len(q)
        o2=[p for p in orig if 'quoted' not in ty(p)]
        fm['link/media posts']=sum(1 for p in o2 if 'http' in p['text']); fm['text-only posts']=len(o2)-fm['link/media posts']
        top=max(fm,key=fm.get)
        hs=[hook(p['text']) for p in orig] or [hook(p['text']) for p in P]
        hk=max(set(h.split(' (')[0] for h in hs),key=[h.split(' (')[0] for h in hs].count)
        ex=next(h for h in hs if h.startswith(hk))
        r['quality_note']=f'Mostly {top} ({fm[top]}/{n}); originals typically open with {ex}.'
    new=not os.path.exists(OUT)
    with open(OUT,'a',newline='') as f:
        wr=csv.DictWriter(f,hdr)
        if new: wr.writeheader()
        wr.writerow(r)
    done.add(u['username'].lower())
    print(u['username'],r['sampled_posts'],r['median_impressions_orig'],r['category'],r['quality_note'])
for a in sys.argv[1:]:
    uid,p=a.split(':',1); proc(uid,p)
print('done total',len(done))
