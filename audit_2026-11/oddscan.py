#!/usr/bin/env python3
"""True orbit depths for odd-length rules (2026-11-21).  Rule string as printed by oddswap.c: XYZ,P-M(place n-1),...,P-M(place 1).
V = b^n (s_X - s_Z) + (s_Y - s_Z) + sum_q b^q (s_P - s_M);  K = (b^n - 1)|V|."""
import itertools,sys,glob,re,collections
def parse(r):
    parts=r.split(','); X,Y,Z=(ord(c)-65 for c in parts[0]); n=len(parts)
    prs={n-1-i:(ord(p[0])-65,ord(p[2])-65) for i,p in enumerate(parts[1:])}
    return n,X,Y,Z,prs
def mk(r,b):
    n,X,Y,Z,prs=parse(r); L=2*n+1
    def V(s): return b**n*(s[X]-s[Z])+(s[Y]-s[Z])+sum(b**q*(s[P]-s[M]) for q,(P,M) in prs.items())
    def step(s):
        v=(b**n-1)*abs(V(s)); return tuple(sorted(((v//b**i)%b for i in range(L)),reverse=True))
    return n,L,V,step
def depth(r,b):
    n,L,V,step=mk(r,b); memo={}
    worst=0; tmax=0
    for s in itertools.combinations_with_replacement(range(b-1,-1,-1),L):
        if s[0]==s[-1]: continue
        path=[]; c=s
        while c not in memo:
            if c in path:
                if path[-1]!=c: return None
                memo[c]=0; break
            path.append(c); c=step(c)
            if c[0]==c[-1]: return None
        base=memo[c]
        for i,p in enumerate(reversed(path)):
            if p not in memo: memo[p]=base+i+ (0 if memo.get(path[-1],None)==0 and False else 1)
        worst=max(worst,memo[s])
    return worst
if __name__=='__main__':
    n=int(sys.argv[1]); bases=[int(x) for x in sys.argv[2].split(',')]
    fs=glob.glob(f'oddswap/out_b*_n{n}.txt'); d=collections.defaultdict(set)
    for f in fs:
        b=int(re.search(r'_b(\d+)_',f).group(1))
        for l in open(f):
            if l.startswith('UNIV'): d[l.split()[3].split('=')[1]].add(b)
    rules=[r for r,v in d.items() if len(v)==len(fs)]
    if len(sys.argv)>3: rules=rules[:int(sys.argv[3])]
    out=[]
    for r in rules: out.append(([depth(r,b) for b in bases],r))
    for x in sorted(out,key=lambda t:(t[0][-1] or 99,t[1])): print(x[1],x[0])
