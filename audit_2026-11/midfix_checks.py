#!/usr/bin/env python3
"""Checks of the lemmas in PROOF_FIXEDMIDDLE.md on the reduced map T (2026-11-21)."""
import itertools, random
from midfix_family import T
def parts(r,n,b):
    if n%2: k=(n-1)//2; w=[r[2*j]-r[2*j-1] for j in range(1,k+1)]
    else: k=(n-2)//2; w=[r[2*j+1]-r[2*j] for j in range(1,k+1)]
    return k,w
def bad(r,n,b):
    k,w=parts(r,n,b)
    if n%2: return r[0]>=1 and all(x>=2 for x in w)
    h=min(r[0]+r[1],b-1-r[0]-r[1])
    return r[1]>=1 and all(x>=2 for x in w[:-1]) and w[-1]>=1 and not (w[-1]==1 and h==0)
def check(r,n,b,stats):
    tau=tuple([0]*(n-1)+[1]); H=(b-1)//2; run=0; steps=0; hist=[]
    while r!=tau:
        assert all(0<=x<=H for x in r)
        r1=T(r,n,b); B=bad(r,n,b); lead=r[0] if n%2 else r[1]
        if lead==0:                                   # at most 2 steps to tau
            assert T(r1,n,b)==tau or r1==tau,(n,b,r)
        elif not B: assert (r1[0] if n%2 else r1[1])==0,(n,b,r)
        if B:
            run+=1; hist.append(r)
            if n%2: assert r1[-1]<=r[-1]-1,(n,b,r)
            elif len(hist)>=2 and bad(r1,n,b) or (not n%2 and len(hist)>=1):
                pass
        else:
            stats['run']=max(stats['run'],run); run=0; hist=[]
        if not n%2 and B and bad(r1,n,b):
            r2=T(r1,n,b)
            if n==4: assert r2[-1]<=r[-1]-1,(n,b,r)
            else: assert r2[-1]<=max(r[-1],r1[-1])-2,(n,b,r)
        r=r1; steps+=1; assert steps<10**5
    stats['run']=max(stats['run'],run); stats['steps']=max(stats['steps'],steps)
random.seed(5)
for n in range(3,12):
    for b in (3,4,5,6,7,8,9,10,11,16,17,40,41,200,1001):
        H=(b-1)//2; stats={'run':0,'steps':0}
        tot=1
        for i in range(n): tot=tot*(H+1+i)//(i+1)
        if tot<=150000:
            for r in itertools.combinations_with_replacement(range(H+1),n): check(r,n,b,stats)
            mode='all'
        else:
            for _ in range(60000):
                if random.random()<.5: r=tuple(sorted(random.randint(0,H) for _ in range(n)))
                else:
                    x=random.randint(0,H); r=tuple(sorted(min(H,max(0,x+random.randint(-3,3)*random.randint(0,1)*(1+(i%2)*random.randint(0,H//3+1)))) for i in range(n)))
                check(r,n,b,stats)
            mode='sampled'
        print(f"n={n} b={b} ({mode}): lemmas hold; longest bad run {stats['run']}; max reduced steps {stats['steps']}")
