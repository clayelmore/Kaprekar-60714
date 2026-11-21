# Referee: everything from the raw definition. Exact ints.
import itertools, random
from collections import Counter
def coef(d):
    if d==6: return [990,90000,-99990,-900,-99,9999]
    return [990,90000,-99990,-900,-99,999999]+[9*10**k for k in range(6,d-1)]+[-(10**(d-1)-10**4)]
_C={}
def K(s):  # s sorted descending tuple/list
    d=len(s)
    c=_C.get(d)
    if c is None: c=_C[d]=coef(d)
    return abs(sum(x*y for x,y in zip(c,s)))
def img(s):
    d=len(s); v=K(s); t=sorted(map(int,str(v).zfill(d)),reverse=True)
    assert len(t)==d
    return tuple(t)
def coef_core(a6,b6,d):
    a=list(a6[:5])+list(range(6,d))+[a6[5]]; b=list(b6[:5])+[b6[5]]+list(range(6,d))
    assert len(a)==d==len(b) and sorted(a)==list(range(d)) and sorted(b)==list(range(d))
    return [10**x-10**y for x,y in zip(a,b)]
def orbit_end(s,f=img,cap=100000):
    seen=set(); n=0
    while True:
        t=f(s)
        if t==s: return ('fix',s,n)
        if t in seen: return ('cyc',t,n)
        seen.add(t); s=t; n+=1
        if n>cap: return ('cap',s,n)
