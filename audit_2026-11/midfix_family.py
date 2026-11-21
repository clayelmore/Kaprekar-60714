#!/usr/bin/env python3
"""Fixed-middle family M_n at odd length 2n+1 in base b (2026-11-21).
Letters 0..2n = digits sorted descending.  Letter 1 stays at the middle place n in both words.  The other 2n
letters carry the even rule R_n of PROOF_HALFSWAP.md under the relabeling 0 -> 0, i -> i+1, with swap distance
n+1:  K(s) = (b^(n+1) - 1) |V|,  V = sum_q b^q (s[P_q] - s[M_q]).   Endpoint (b-1)(b^(n+1) - 1)."""
import itertools, random, sys
from halfswap_family import pairs as po
from halfswap_even import pairs as pe
def rule(n):
    pl=dict(po(n) if n%2 else pe(n)); r=lambda i: 0 if i==0 else i+1
    return {q:(r(P),r(M)) for q,(P,M) in pl.items()}
def K(s,n,b,pl): return (b**(n+1)-1)*abs(sum(b**q*(s[P]-s[M]) for q,(P,M) in pl.items()))
def digs(v,n,b): return tuple(sorted(((v//b**i)%b for i in range(2*n+1)),reverse=True))
def deficits(v,n,b):
    x=v//(b**(n+1)-1)-1; out=[]
    for _ in range(n): t=x%b; x//=b; out.append(min(t,b-1-t))
    return tuple(sorted(out))
def string_of(rho,b): return tuple([b-1]+[b-1-x for x in rho]+list(reversed(rho)))
def T(rho,n,b):
    """reduced map on deficits (rho ascending)"""
    r=lambda x: min(x,b-1-x)
    if n%2:
        k=(n-1)//2; w=[rho[2*j]-rho[2*j-1] for j in range(1,k+1)]; extra=[rho[0]]
        act=[j for j in range(1,k+1) if w[j-1]]
        if not act: A=b-1-rho[0]; return tuple(sorted([0]*(n-1)+[r(A-1)]))
    else:
        k=(n-2)//2; w=[rho[2*j+1]-rho[2*j] for j in range(1,k+1)]; sig=b-1-rho[0]-rho[1]; extra=[r(sig),rho[1]]
        act=[j for j in range(1,k+1) if w[j-1]]
        if not act:
            s2=b-1-rho[1]
            return tuple(sorted([0]*(n-2)+[rho[1],r(sig-1)])) if sig else tuple(sorted([0]*(n-1)+[r(s2-1)]))
    J=max(act); out=extra+[w[J-1]-1,w[J-1]]
    for j in range(1,J): out+=[max(w[j-1]-1,0)]*2
    out+=[0]*(2*(k-J))
    return tuple(sorted(out))
if __name__=='__main__':
    for n,bases in ((3,range(3,10)),(4,range(3,8)),(5,(3,4,5)),(6,(3,4))):
        pl=rule(n)
        for b in bases:
            F=(b-1)*(b**(n+1)-1); tau=tuple([0]*(n-1)+[1]); worst=0
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n+1):
                if s[0]==s[-1]: assert K(s,n,b,pl)==0; continue
                v=K(s,n,b,pl); assert 0<v<b**(2*n+1); st=1
                while v!=F:
                    rho=deficits(v,n,b); assert digs(v,n,b)==string_of(rho,b)
                    v2=K(digs(v,n,b),n,b,pl); assert v2>0 and deficits(v2,n,b)==T(rho,n,b),(n,b,s,rho)
                    v=v2; st+=1; assert st<500
                worst=max(worst,st)
            assert deficits(F,n,b)==tau
            print(f"n={n} base={b}: every string reaches (b-1)(b^(n+1)-1); reduced map exact; max steps {worst}")
    random.seed(1)
    for n in (3,4,5,6,7,8,9,10):
        out=[]
        for b in (10,100,1000):
            H=(b-1)//2; tau=tuple([0]*(n-1)+[1]); worst=0
            for _ in range(30000):
                rho=tuple(sorted(random.randint(0,H) for _ in range(n))); st=0
                if random.random()<.3: rho=tuple(sorted(random.randint(H-3,H) if random.random()<.5 else random.randint(0,3) for _ in range(n)))
                while rho!=tau: rho=T(rho,n,b); st+=1; assert st<5000,(n,b)
                worst=max(worst,st)
            out.append(worst)
        print(f"reduced map n={n}: max steps to tau from sampled states, bases 10/100/1000: {out}")
