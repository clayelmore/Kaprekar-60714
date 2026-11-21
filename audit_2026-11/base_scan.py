#!/usr/bin/env python3
"""Base-by-base scan (every base 21..120) of the candidate cores that survived bigbase_stress.py (2026-11-21).
Lengths N, N+1, N+2; 800 random starts each; reports the first (length, base) with a cycle or a second endpoint."""
import random,sys
from multiprocessing import Pool
from usage_score import coeffs,extend,from_words
def test(args):
    name,pc=args; N=len(pc)
    for b in range(21,121):
        for d in (N,N+1,N+2):
            random.seed(d*7919+b); c=coeffs(extend(pc,d),b); F=None
            for _ in range(800):
                s=tuple(sorted((random.randrange(b) for _ in range(d)),reverse=True))
                if s[0]==s[-1]: continue
                seen=set()
                while True:
                    if s in seen: return name,(d,b,'cycle')
                    seen.add(s); v=abs(sum(x*y for x,y in zip(c,s)))
                    if v==0: return name,(d,b,'zero')
                    t=tuple(sorted(((v//b**i)%b for i in range(d)),reverse=True))
                    if t==s: break
                    s=t
                if F is None: F=v
                elif F!=v: return name,(d,b,'two endpoints')
    return name,None
if __name__=='__main__':
    jobs=[]
    for l in open('bases7/stress.txt'):
        if ' OK ' in l and (l.strip().startswith('6:') or l.strip().startswith('7:')):
            nm=l.strip().split(' OK')[0]
            if nm.startswith('6:'): w1,w2=nm[2:].split(' - '); jobs.append((nm,from_words(w1,w2)))
            else: a,bb=nm[2:].split(); jobs.append((nm,list(zip(map(int,a.split(',')),map(int,bb.split(','))))))
    with Pool(6) as p: res=p.map(test,jobs,chunksize=1)
    ok=[r for r in res if r[1] is None]
    print(len(res),'rules scanned;',len(ok),'with no failure in bases 21-120')
    for nm,r in res: print('  ',nm,'no failure' if r is None else f'FAILS first at length {r[0]}, base {r[1]} ({r[2]})')
