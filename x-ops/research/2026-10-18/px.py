import json,sys
def P(f):
    t=open(f).read();s=t.index('{');d,_=json.JSONDecoder().raw_decode(t[s:]);return d,t
