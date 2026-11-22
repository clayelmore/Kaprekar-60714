#!/usr/bin/env python3
"""Survey: for random target numbers, can a rule be built to order?  (2026-11-21)
Targets: random L-digit strings (leading zeros allowed), not repdigits, digit sum divisible by 9, base 10.
For each target F:
  pairs  = arrangements W_lo of F's digits with W_lo + F also an arrangement (needed for F to be a fixed point);
  rules  = all assignments of equal digits to places, for all pairs (enumerated if <= BUDGET, else sampled);
  a rule is kept if EVERY non-repdigit L-digit multiset reaches F (exact: cycle detection, complete enumeration).
Outcome: 'no pair' (impossible), 'none' (all rules enumerated, none works: impossible at this length),
         'not found' (sampled only), 'found' (rule printed).
usage: to_order_survey.py L NTARGETS [BUDGET] [SEED]"""
import sys,random,itertools,math
from multiprocessing import Pool
L=int(sys.argv[1]); NT=int(sys.argv[2]); BUDGET=int(sys.argv[3]) if len(sys.argv)>3 else 20000; SEED=int(sys.argv[4]) if len(sys.argv)>4 else 1
P10=[10**i for i in range(L)]
ALL=[t for t in itertools.combinations_with_replacement(range(9,-1,-1),L) if t[0]!=t[-1]]
def perms(cnt,n):
    if n==0: yield ''; return
    for d in sorted(cnt):
        if cnt[d]:
            cnt[d]-=1
            for r in perms(cnt,n-1): yield d+r
            cnt[d]+=1
def pairs(F,fd):
    cnt={}
    for ch in fd: cnt[ch]=cnt.get(ch,0)+1
    out=[]
    for w in perms(dict(cnt),L):
        hi=str(int(w)+F)
        if len(hi)<=L and sorted(hi.zfill(L),reverse=True)==fd: out.append((hi.zfill(L),w))
    return out
def groups(w,fd):
    byd={}
    for p in range(L): byd.setdefault(w[L-1-p],[]).append(p)
    return [([i for i in range(L) if fd[i]==d],ps) for d,ps in sorted(byd.items())]
def all_assign(g):
    for combo in itertools.product(*[itertools.permutations(ps) for _,ps in g]):
        pl=[None]*L
        for (letters,_),ps in zip(g,combo):
            for i,p in zip(letters,ps): pl[i]=p
        yield pl
def rand_assign(g,rng):
    pl=[None]*L
    for letters,ps in g:
        ps=ps[:]; rng.shuffle(ps)
        for i,p in zip(letters,ps): pl[i]=p
    return pl
def step(c,s):
    v=abs(sum(x*y for x,y in zip(c,s))); return v,tuple(sorted(((v//P10[i])%10 for i in range(L)),reverse=True))
def quick(c,F,starts):
    for s in starts:
        seen=set()
        while True:
            v,t=step(c,s)
            if v==F: break
            if v==0 or t in seen: return False
            seen.add(t); s=t
    return True
def full(c,F):
    good=set()
    for s in ALL:
        path=[]; cur=s
        while cur not in good:
            v,t=step(c,cur)
            if v==0 or t in path: 
                if v==F and t==cur: break
                return False
            path.append(cur)
            if v==F: path.append(t); break
            cur=t
        good.update(path)
    return True
def target(k):
    rng=random.Random(SEED*1000003+k)
    while True:
        ds=[rng.randrange(10) for _ in range(L)]
        if sum(ds)%9==0 and len(set(ds))>1: break
    F=int(''.join(map(str,ds))); fd=sorted(str(F).zfill(L),reverse=True)
    P=pairs(F,fd)
    mult=1
    for d in set(fd): mult*=math.factorial(fd.count(d))
    nrules=len(P)*mult*mult
    info=dict(F=str(F).zfill(L),pairs=len(P),rules=nrules,distinct=len(set(fd)),zeros=fd.count('0'))
    if not P: info['out']='no pair'; return info
    starts=[ALL[rng.randrange(len(ALL))] for _ in range(25)]
    def cands():
        if nrules<=BUDGET:
            for hi,lo in P:
                gh,gl=groups(hi,fd),groups(lo,fd)
                for a in all_assign(gh):
                    for b in all_assign(gl): yield a,b
        else:
            G=[(groups(hi,fd),groups(lo,fd)) for hi,lo in P]
            for _ in range(BUDGET):
                gh,gl=G[rng.randrange(len(G))]; yield rand_assign(gh,rng),rand_assign(gl,rng)
    tested=0; screened=0
    for a,b in cands():
        tested+=1; c=[P10[x]-P10[y] for x,y in zip(a,b)]
        if not quick(c,F,starts[:3]) or not quick(c,F,starts): continue
        screened+=1
        if full(c,F):
            w1=[None]*L; w2=[None]*L
            for i in range(L): w1[a[i]]=i; w2[b[i]]=i
            AB='ABCDEFGHIJKLMNOP'
            info.update(out='found',tested=tested,screened=screened,rule=''.join(AB[w1[p]] for p in range(L-1,-1,-1))+' - '+''.join(AB[w2[p]] for p in range(L-1,-1,-1)),moves=all(x!=y for x,y in zip(a,b)))
            return info
    info.update(out='none' if nrules<=BUDGET else 'not found',tested=tested,screened=screened); return info
if __name__=='__main__':
    with Pool(6) as p:
        print("target\tpairs\trules\tdistinct\tzeros\toutcome\ttested\tscreened\trule\tevery_letter_moves")
        for r in p.imap(target,range(NT)):
            print(f"{r['F']}\t{r['pairs']}\t{r['rules']}\t{r['distinct']}\t{r['zeros']}\t{r['out']}\t{r.get('tested','')}\t{r.get('screened','')}\t{r.get('rule','')}\t{r.get('moves','')}"); sys.stdout.flush()
