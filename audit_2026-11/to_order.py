#!/usr/bin/env python3
"""Try to build a rule with a requested endpoint F at length L, base 10 (2026-11-21).
1. Find all anagram pairs: W_hi - W_lo = F with W_hi, W_lo arrangements of F's digits.
2. Each pair gives many rules (which of several equal digits goes where).  Sample rules at random and keep
   those under which sampled starts all reach F.  Survivors are then checked by complete enumeration.
usage: to_order.py F L [samples]"""
import sys,random,itertools
from multiprocessing import Pool
F=int(sys.argv[1]); L=int(sys.argv[2]); NS=int(sys.argv[3]) if len(sys.argv)>3 else 200000
fd=sorted(str(F).zfill(L),reverse=True)
def perms(counts,n):
    if n==0: yield ''; return
    for d in sorted(counts):
        if counts[d]:
            counts[d]-=1
            for r in perms(counts,n-1): yield d+r
            counts[d]+=1
def pairs():
    cnt={}
    for ch in fd: cnt[ch]=cnt.get(ch,0)+1
    out=[]
    for w in perms(dict(cnt),L):
        hi=str(int(w)+F)
        if len(hi)<=L and sorted(hi.zfill(L),reverse=True)==fd: out.append((hi.zfill(L),w))
    return out
def make(hi,lo,rng):
    # letters 0..L-1 = sorted digits fd; place p (0 = units) of a word string is index L-1-p
    def assign(w):
        byd={}
        for p in range(L): byd.setdefault(w[L-1-p],[]).append(p)
        pl=[None]*L
        for d,ps in byd.items():
            letters=[i for i in range(L) if fd[i]==d]; rng.shuffle(ps)
            for i,p in zip(letters,ps): pl[i]=p
        return pl
    return assign(hi),assign(lo)
def reach(c,n,rng,cap=400):
    for _ in range(n):
        s=sorted((rng.randrange(10) for _ in range(L)),reverse=True)
        if s[0]==s[-1]: continue
        for k in range(cap):
            v=abs(sum(x*y for x,y in zip(c,s)))
            if v==F: break
            if v==0: return False
            s=sorted(((v//10**i)%10 for i in range(L)),reverse=True)
        else: return False
    return True
def work(args):
    seed,P,n=args; rng=random.Random(seed); good=[]
    for _ in range(n):
        hi,lo=rng.choice(P); a,b=make(hi,lo,rng); c=[10**x-10**y for x,y in zip(a,b)]
        if reach(c,3,rng,150) and reach(c,40,rng) and reach(c,600,rng): good.append((a,b,hi,lo))
    return good
if __name__=='__main__':
    P=pairs(); print('digits sorted:',''.join(fd),'; anagram pairs W_hi - W_lo = F:',len(P)); sys.stdout.flush()
    for hi,lo in P[:5]: print('  ',hi,'-',lo)
    if not P: sys.exit()
    with Pool(6) as p: res=p.map(work,[(s,P,NS//60) for s in range(60)])
    good=[g for r in res for g in r]; print('rules sampled:',NS,'; pass the 643-start screen:',len(good))
    for a,b,hi,lo in good[:20]: print('CAND a='+','.join(map(str,a)),'b='+','.join(map(str,b)),hi,lo)
