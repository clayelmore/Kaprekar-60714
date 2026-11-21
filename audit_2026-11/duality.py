#!/usr/bin/env python3
"""Duality test (2026-11-21).  A fixed point is an addition of three arrangements of one digit multiset:
W_hi - W_lo = F  <=>  W_hi - F = W_lo.  So the rule (hi, lo) with fixed point F has a dual rule (hi, f)
(f = how F arranges the sorted digits) with fixed point W_lo.  Is the dual of a universal rule universal?
Tested at d=6 on the 1,174 universal full-variable 6-digit rules."""
import subprocess, itertools
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
d=6
U=[]
for l in open('univ_rules_d6.txt'):
    p=l.split(); U.append((int(p[1][2:]),tuple(int(x) for x in p[2][2:].split(',')),tuple(int(x) for x in p[3][2:].split(','))))
Uset={(a,b) for F,a,b in U}|{(b,a) for F,a,b in U}
def universal(a,b):
    c=[10**x-10**y for x,y in zip(a,b)]
    o=subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.split('\n'); nonrep=o[0].split('nonrep=')[1].split()[0]
    full=[l for l in o if f'basin={nonrep} ' in l and 'FIX' in l and 'val=0 ' not in l]
    return full[0].split('val=')[1].split()[0] if full else None
def duals(F,a,b):
    s=sorted((int(x) for x in str(F).zfill(d)),reverse=True)
    w=lambda p: sum(10**p[i]*s[i] for i in range(d))
    h,l=(a,b) if w(a)>w(b) else (b,a); assert w(h)-w(l)==F
    Fd=[int(x) for x in str(F).zfill(d)][::-1]            # Fd[p] = digit at place p
    out=set()
    groups={}
    for i,v in enumerate(s): groups.setdefault(v,[]).append(i)
    places={v:[p for p in range(d) if Fd[p]==v] for v in groups}
    for combo in itertools.product(*[itertools.permutations(places[v]) for v in groups]):
        f=[0]*d
        for v,perm in zip(groups,combo):
            for i,p in zip(groups[v],perm): f[i]=p
        out.add((h,tuple(f)))
    return out,w(l)
def job(u):
    F,a,b=u; ds,lo=duals(F,a,b); res=[]
    for h,f in ds:
        fv=all(x!=y for x,y in zip(h,f)); r=universal(h,f); res.append((fv,r,lo,(h,f) in Uset))
    return res
with ThreadPoolExecutor(6) as ex: R=list(ex.map(job,U))
nd=sum(len(r) for r in R); un=sum(1 for r in R for x in r if x[1]); fv=sum(1 for r in R for x in r if x[0]); fvun=sum(1 for r in R for x in r if x[0] and x[1])
right=sum(1 for r in R for x in r if x[1] and int(x[1])==x[2])
print(f"universal 6-digit rules: {len(U)}; dual rules (all digit-tie choices): {nd}; dual universal: {un} ({100*un/nd:.1f}%); full-variable duals: {fv}, of which universal: {fvun} ({100*fvun/max(fv,1):.1f}%)")
print(f"rules with at least one universal dual: {sum(1 for r in R if any(x[1] for x in r))} of {len(U)};  dual endpoint equals the subtracted word: {right}/{un}")
print('base rate: 1174/190800 = 0.6% of full-variable rules are universal at d=6')
