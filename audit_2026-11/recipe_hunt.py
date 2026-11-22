#!/usr/bin/env python3
"""Recipe hunt (2026-11-21): for targets where a rule exists, sample many rules that keep the target fixed and
compare the ones under which everything reaches the target (winners) with the rest.
usage: recipe_hunt.py L NTARGETS SAMPLES  -> writes to_order/hunt_L{L}.tsv  (one row per sampled rule: all winners,
plus every 25th loser)."""
import sys,random,subprocess,math
from multiprocessing import Pool
sys.argv=[sys.argv[0]]+sys.argv[1:]
L=int(sys.argv[1]); NT=int(sys.argv[2]); NS=int(sys.argv[3])
import importlib
sys_argv_backup=sys.argv[:]; sys.argv=['x',str(L),'1']; tb=importlib.import_module('to_order_big'); sys.argv=sys_argv_backup
P10=[10**i for i in range(L)]
def feats(a,b):
    c=[P10[x]-P10[y] for x,y in zip(a,b)]; C=[]; s=0
    for x in c[:-1]: s+=x; C.append(s)
    mags=[len(str(abs(x))) if x else 0 for x in C]
    return c,dict(nneg=sum(1 for x in C if x<0),nzero=sum(1 for x in C if x==0),distinct_mag=len(set(mags)),minmag=min(mags),maxmag=max(mags),
                  a0=a[0],b0=b[0],aL=a[-1],bL=b[-1],fixed=sum(1 for x,y in zip(a,b) if x==y),
                  topdiff=abs(a[0]-b[0]),mags=''.join(format(m,'x') for m in mags),signs=''.join('-' if x<0 else ('0' if x==0 else '+') for x in C))
def one(k):
    rng=random.Random(1*1000003+k)
    while True:
        ds=[rng.randrange(10) for _ in range(L)]
        if sum(ds)%9==0 and len(set(ds))>1: break
    F=int(''.join(map(str,ds))); fs=str(F).zfill(L); fd=sorted(fs,reverse=True)
    P,exh=tb.pairs([int(ch) for ch in reversed(fs)],rng)
    if not P: return []
    def rs():
        s=[rng.randrange(10) for _ in range(L)]
        while len(set(s))==1: s=[rng.randrange(10) for _ in range(L)]
        return tuple(sorted(s,reverse=True))
    starts=[rs() for _ in range(40)]
    G=[(tb.groups(hi,fd),tb.groups(lo,fd)) for hi,lo in P]; rows=[]; seen=set()
    for i in range(NS):
        gi=rng.randrange(len(G)); gh,gl=G[gi]; a=tb.rand_assign(gh,rng); b=tb.rand_assign(gl,rng)
        key=(tuple(a),tuple(b))
        if key in seen: continue
        seen.add(key); c,f=feats(a,b); win=0
        if tb.quick(c,F,starts[:3]) and tb.quick(c,F,starts):
            o=subprocess.run(['./univcheck',str(L),str(F),','.join(map(str,a)),','.join(map(str,b))],capture_output=True,text=True).stdout
            win=1 if 'PASS' in o else 0
        if win or i%25==0:
            rows.append('\t'.join(map(str,[fs,len(P),gi,win,25 if not win else 1,','.join(map(str,a)),','.join(map(str,b))]+[f[k] for k in ('nneg','nzero','distinct_mag','minmag','maxmag','a0','b0','aL','bL','fixed','topdiff','mags','signs')])))
    return rows
if __name__=='__main__':
    with Pool(6) as p, open(f'to_order/hunt_L{L}.tsv','w') as out:
        out.write('target\tpairs\tpair_index\twin\tweight\ta\tb\tnneg\tnzero\tdistinct_mag\tminmag\tmaxmag\ta0\tb0\taL\tbL\tfixed\ttopdiff\tmags\tsigns\n')
        for rows in p.imap(one,range(NT)):
            for r in rows: out.write(r+'\n')
            out.flush()
