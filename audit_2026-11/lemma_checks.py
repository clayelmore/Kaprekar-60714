#!/usr/bin/env python3
"""Numerical checks of the three lemmas in the all-lengths argument for 146070 (exact big integers)."""
import random, itertools
from collections import Counter
def K(s):
    d=len(s); low=990*s[0]+90000*s[1]-99990*s[2]-900*s[3]-99*s[4]-s[5]+10**4*s[d-1]
    return abs(sum(10**k*(s[k-1]-s[k]) for k in range(6,d) if s[k-1]!=s[k])+low)
def img(s): d=len(s); return sorted((int(x) for x in str(K(s)).zfill(d)),reverse=True)
random.seed(7)
# Lemma 0: K(s)=0 only for repdigits. H=0 forces s5=...=s_{d-1}=m, so it is a 6-variable check.
bad0=[t for t in itertools.combinations_with_replacement(range(9,-1,-1),6) if len(set(t))>1 and 990*t[0]+90000*t[1]-99990*t[2]-900*t[3]-99*t[4]-t[5]+10**4*t[5]==0]
print("Lemma 0 (only repdigits map to 0): counterexamples =",len(bad0))
# Lemma 1: after one step, at most 15 nonzero digits other than 9.
worst=0
for d in (21,25,40,77):
    for _ in range(40000):
        k=random.choice([2,3,4,5,7,10]); ds=random.sample(range(10),k); s=sorted((random.choice(ds) for _ in range(d)),reverse=True)
        if len(set(s))==1: continue
        c=Counter(img(s)); worst=max(worst,sum(v for g,v in c.items() if g not in (0,9)))
print("Lemma 1 (non-9 nonzero digits after one step <= 15): worst seen =",worst)
# Lemma 2: regime step. State 9^t + R (digits 1..8) + zeros, t>=6  ->  9^(t-5) + (partition of 9) + zeros;
#          zero-free variant: same, except R all 8s gives 9^(t-4) and nothing else.
bad=0; n=0
Rs=[r for u in range(0,5) for r in itertools.combinations_with_replacement(range(8,0,-1),u)]+[tuple(sorted((random.randint(1,8) for _ in range(random.randint(5,15))),reverse=True)) for _ in range(3000)]
for R in Rs:
    for t in (6,7,8,11,12,30):
        for z in (0,1,2,9):
            if z==0 and not R: continue
            s=[9]*t+list(R)+[0]*z
            if len(s)<21: s=s+[0]*(21-len(s)) if z else None
            if s is None: continue
            c=Counter(img(s)); n+=1; nines=c.pop(9,0); c.pop(0,None); rest=sum(g*v for g,v in c.items())
            ok = (nines==t-5 and rest==9) or (z==0 and set(R)=={8} and nines==t-4 and rest==0)
            if not ok: bad+=1; print("  counterexample",t,R,z,img(s)[:20])
print(f"Lemma 2 (nine-drain: t -> t-5, remainder a partition of 9): {n} cases, counterexamples = {bad}")
