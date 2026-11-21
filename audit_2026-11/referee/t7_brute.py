from ref import *
import sys
for d in range(6,13):
    tgt=tuple(sorted(map(int,str(146070).zfill(d)),reverse=True)); assert K(tgt)==146070
    memo={tgt:0}; n=0; mx=0
    for s in itertools.combinations_with_replacement(range(9,-1,-1),d):
        if len(set(s))==1: assert K(s)==0; continue
        n+=1; path=[]; x=s
        while x not in memo:
            assert x not in path and len(set(x))>1,(d,s,x)
            path.append(x); x=img(x)
        b=memo[x]
        for p in reversed(path): b+=1; memo[p]=b
        mx=max(mx,memo[s])
    print(f"d={d} nonrep={n} all reach 146070, max steps={mx}",flush=True)
