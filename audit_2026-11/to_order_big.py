#!/usr/bin/env python3
"""Build-to-order survey for longer targets (2026-11-21).  Same targets and outcomes as to_order_survey.py, but
pairs W_lo + F = W_hi are found by a digit-by-digit search with carries (randomized, capped at PAIRCAP), and the
complete check is done by ./univcheck (C).  'none' is reported only when every pair and every rule was tried.
usage: to_order_big.py L NTARGETS [BUDGET] [SEED]"""
import sys,random,itertools,math,subprocess
from multiprocessing import Pool
L=int(sys.argv[1]); NT=int(sys.argv[2]); BUDGET=int(sys.argv[3]) if len(sys.argv)>3 else 20000; SEED=int(sys.argv[4]) if len(sys.argv)>4 else 1
PAIRCAP=3000; NODECAP=400000; VERIFYCAP=60
P10=[10**i for i in range(L)]
def pairs(fdig,rng):
    """fdig[p] = digit of F at place p.  returns (list of (hi,lo) strings), exhaustive?"""
    cnt=[0]*10
    for d in fdig: cnt[d]+=1
    lo=[0]*L; hi=[0]*L; out=[]; nodes=[0]; full=[True]
    cl=cnt[:]; ch=cnt[:]
    def rec(p,carry):
        if len(out)>=PAIRCAP or nodes[0]>NODECAP: full[0]=False; return
        if p==L:
            if carry==0: out.append((''.join(map(str,reversed(hi))),''.join(map(str,reversed(lo)))))
            return
        ds=[x for x in range(10) if cl[x]]; rng.shuffle(ds)
        for x in ds:
            y=x+fdig[p]+carry; yd=y%10
            if not ch[yd]: continue
            nodes[0]+=1; cl[x]-=1; ch[yd]-=1; lo[p]=x; hi[p]=yd
            rec(p+1,y//10)
            cl[x]+=1; ch[yd]+=1
    rec(0,0); return out,full[0]
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
def quick(c,F,starts):
    for s in starts:
        seen=set()
        while True:
            v=abs(sum(x*y for x,y in zip(c,s)))
            if v==F: break
            t=tuple(sorted(((v//P10[i])%10 for i in range(L)),reverse=True))
            if v==0 or t in seen: return False
            seen.add(t); s=t
    return True
def target(k):
    rng=random.Random(SEED*1000003+k)
    while True:
        ds=[rng.randrange(10) for _ in range(L)]
        if sum(ds)%9==0 and len(set(ds))>1: break
    F=int(''.join(map(str,ds))); fs=str(F).zfill(L); fd=sorted(fs,reverse=True)
    P,exh=pairs([int(ch) for ch in reversed(fs)],rng)
    mult=1
    for d in set(fd): mult*=math.factorial(fd.count(d))
    nrules=len(P)*mult*mult
    info=dict(F=fs,pairs=len(P),exh=exh,rules=nrules,distinct=len(set(fd)),zeros=fd.count('0'))
    if not P: info['out']='no pair' if exh else 'not found'; return info
    def rs():
        s=[rng.randrange(10) for _ in range(L)]
        while len(set(s))==1: s=[rng.randrange(10) for _ in range(L)]
        return tuple(sorted(s,reverse=True))
    starts=[rs() for _ in range(40)]
    exact=exh and nrules<=BUDGET
    def cands():
        if exact:
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
        if not exact and screened>VERIFYCAP: break
        o=subprocess.run(['./univcheck',str(L),str(F),','.join(map(str,a)),','.join(map(str,b))],capture_output=True,text=True).stdout
        if 'PASS' in o:
            w1=[None]*L; w2=[None]*L
            for i in range(L): w1[a[i]]=i; w2[b[i]]=i
            AB='ABCDEFGHIJKLMNOP'
            info.update(out='found',tested=tested,screened=screened,rule=''.join(AB[w1[p]] for p in range(L-1,-1,-1))+' - '+''.join(AB[w2[p]] for p in range(L-1,-1,-1)),moves=all(x!=y for x,y in zip(a,b)))
            return info
    info.update(out='none' if exact else 'not found',tested=tested,screened=screened); return info
if __name__=='__main__':
    with Pool(6) as p:
        print("target\tpairs\tpairs_exhaustive\trules\tdistinct\tzeros\toutcome\ttested\tscreened\trule\tevery_letter_moves")
        for r in p.imap(target,range(NT)):
            print(f"{r['F']}\t{r['pairs']}\t{r['exh']}\t{r['rules']}\t{r['distinct']}\t{r['zeros']}\t{r['out']}\t{r.get('tested','')}\t{r.get('screened','')}\t{r.get('rule','')}\t{r.get('moves','')}"); sys.stdout.flush()
