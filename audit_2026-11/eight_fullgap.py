#!/usr/bin/env python3
"""Eight-letter cores (base-10 census so far) that see every gap: do any survive base 50?  (2026-11-21)
Stage 1: gaps seen = 7 of 7.  Stage 2: base 50, lengths 8, 9, 10, 40 sampled starts each (cycle / zero / two endpoints = fail).
Stage 3: survivors: bases 50, 7, 13, 21, 30, 37, 45, 60, 97, lengths 8-11, 400 starts each."""
import glob,random,sys,collections
from multiprocessing import Pool
from usage_score import coeffs,extend
def gaps(pc):
    out=[]
    for b in (7,10,13):
        c=coeffs(pc,b); s=0; C=[]
        for x in c[:-1]: s+=x; C.append(s)
        out.append(len({abs(x) for x in C if x}))
    return min(out)
def sample(pc,b,d,n,seed):
    random.seed(seed); c=coeffs(extend(pc,d),b); F=None
    for _ in range(n):
        s=tuple(sorted((random.randrange(b) for _ in range(d)),reverse=True))
        if s[0]==s[-1]: continue
        seen=set()
        while True:
            if s in seen: return 'cycle'
            seen.add(s); v=abs(sum(x*y for x,y in zip(c,s)))
            if v==0: return 'zero'
            t=tuple(sorted(((v//b**i)%b for i in range(d)),reverse=True))
            if t==s: break
            s=t
        if F is None: F=v
        elif F!=v: return 'two endpoints'
    return None
def stage2(pc):
    for d in (8,9,10):
        r=sample(pc,50,d,40,d)
        if r: return pc,(d,r)
    return pc,None
def stage3(pc):
    for b in (50,7,13,21,30,37,45,60,97):
        for d in (8,9,10,11):
            r=sample(pc,b,d,400,b*31+d)
            if r: return pc,(b,d,r)
    return pc,None
if __name__=='__main__':
    cores=[]
    for f in glob.glob('census_out/n8_*.txt'):
        for l in open(f):
            if l.startswith('CORE') and ' A=1 B=1 ' in l:
                p=l.split()
                try: cores.append(list(zip(map(int,p[2][2:].split(',')),map(int,p[3][2:].split(',')))))
                except Exception: pass
    hist=collections.Counter(gaps(pc) for pc in cores); print('cores so far:',len(cores),'gaps seen:',dict(sorted(hist.items())))
    full=[pc for pc in cores if gaps(pc)==7]
    with Pool(6) as p: r2=p.map(stage2,full,chunksize=50)
    s2=[pc for pc,f in r2 if f is None]; print('full-gap:',len(full),'; pass base 50 quick test:',len(s2),'; fail reasons:',dict(collections.Counter(f[1] for pc,f in r2 if f)))
    with Pool(6) as p: r3=p.map(stage3,s2,chunksize=1)
    s3=[pc for pc,f in r3 if f is None]; print('pass nine-base scan:',len(s3))
    print('first failures:',dict(collections.Counter((f[0],f[1]) for pc,f in r3 if f).most_common(12)))
    for pc in s3: print('SURVIVOR a='+','.join(str(x) for x,_ in pc)+' b='+','.join(str(y) for _,y in pc))
