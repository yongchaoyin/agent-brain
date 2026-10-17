import json,glob,re
def load():
    out={}
    dec=json.JSONDecoder()
    for p in glob.glob('/workspace/agent-brain/x-ops/data/expand_cache/raw/*.txt'):
        t=open(p).read()
        for m in re.finditer(r'\{"data"',t):
            try: d,_=dec.raw_decode(t[m.start():])
            except Exception: continue
            for tw in d.get('data',[]):
                if isinstance(tw,dict) and 'text' in tw: out[tw['id']]=tw
    return list(out.values())
