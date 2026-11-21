#!/usr/bin/env python3
"""Odd-length family U_n at length 2n+1 in base b (2026-11-21).
Letters 0..2n = digits sorted descending.  Start from the even-length rule R'_n on places 0..n-1
(R'_n = R_n for n odd; for n even R_n with place 0 -> (n, n+1) and place 3 -> (n-1, n-2)), then
  * replace letter 2n-1 by letter 2n in its pair, and
  * replace the place-0 pair (n, n+1) by a 3-cycle: letter 2n-1 sits at place 2n in word 1 and place n in word 2,
    letter n at place n / place 0, letter n+1 at place 0 / place 2n.
K(s) = (b^n-1) |V|,  V = b^n (s[2n-1]-s[n+1]) + (s[n]-s[n+1]) + sum_{q>=1} b^q (s[P_q]-s[M_q])."""
import itertools, sys
from collections import Counter
from halfswap_family import pairs as po
from halfswap_even import pairs as pe
def rule(n):
    pl=dict(po(n) if n%2 else pe(n))
    if n%2==0: pl[3]=(n-1,n-2)
    rep=lambda x: 2*n if x==2*n-1 else x
    return {q:(rep(pl[q][0]),rep(pl[q][1])) for q in range(1,n)}
def V(s,n,b,pl): return b**n*(s[2*n-1]-s[n+1])+(s[n]-s[n+1])+sum(b**q*(s[P]-s[M]) for q,(P,M) in pl.items())
def K(s,n,b,pl): return (b**n-1)*abs(V(s,n,b,pl))
def digs(v,n,b): return sorted(((v//b**i)%b for i in range(2*n+1)),reverse=True)
if __name__=='__main__':
    for n,bases in ((3,(3,4,5,6,7,8)),(4,(3,4,5,6)),(5,(3,4,5)),(6,(3,4))):
        pl=rule(n)
        for b in bases:
            F=(b-1)*(b**n-1); worst=0; pat=Counter(); tpat=Counter()
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n+1):
                if s[0]==s[-1]: assert K(s,n,b,pl)==0; continue
                v=K(s,n,b,pl); assert v>0; st=1; ts=[]
                while v!=F:
                    ts.append(v//(b**n-1)//b**n)       # top digit t of m
                    v=K(digs(v,n,b),n,b,pl); assert v>0; st+=1; assert st<500
                worst=max(worst,st); tpat[tuple(min(t,1) for t in ts)]+=1
            print(f"n={n} b={b}: all reach F; max steps {worst}; patterns of (t>0?) along orbits: {tpat.most_common(6)}")
