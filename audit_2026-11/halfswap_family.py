#!/usr/bin/env python3
"""Half-swap family F_n (n odd >= 3) at length 2n in base b, and its reduced 'deficit' dynamics (2026-11-21).

Letters 0..2n-1 = digits sorted descending.  k = (n-1)/2.  Signed pairs by place q (value b^q (s[P]-s[M])):
  place 0: (n, n+1)      place 1: (0, 2n-1)      place 2: (n-1, n-2)
  for j = 1..k-1:  place n+1-2j: (2j, 2j-1)      place n-2j: (2n-1-2j, 2n-2j)
K(s) = (b^n - 1) * | sum_q b^q (s[P_q] - s[M_q]) |.   Claimed endpoint: (b-1)(b^n-1).

Reduced form.  An image is n digits x plus complements; deficits rho_i = b-1-max(x, b-1-x), sorted ascending
rho_1 <= ... <= rho_n.  w_j = rho_{2j+1} - rho_{2j} (j=1..k), g = min(2 rho_1, b-1-2 rho_1).
  if some w_j >= 1, let J = the largest such j:
      next = { (w_j-1)^+ twice : j < J } + { w_J - 1, w_J } + { 0 twice : j > J } + { g }
  else: next = { 0 (n-1 times), min(A-1, b-A) } with A = b-1-2 rho_1 >= 1.
Target: (0,...,0,1)."""
import itertools, random, sys
def pairs(n):
    k=(n-1)//2; pl={0:(n,n+1),1:(0,2*n-1),2:(n-1,n-2)}
    for j in range(1,k): pl[n+1-2*j]=(2*j,2*j-1); pl[n-2*j]=(2*n-1-2*j,2*n-2*j)
    return pl
def K(s,n,b,pl): return (b**n-1)*abs(sum(b**q*(s[P]-s[M]) for q,(P,M) in pl.items()))
def deficits(Kv,n,b):
    m=Kv//(b**n-1); x=m-1; out=[]
    for _ in range(n): t=x%b; x//=b; out.append(b-1-max(t,b-1-t))
    return tuple(sorted(out))
def T(rho,n,b):
    k=(n-1)//2; w=[rho[2*j]-rho[2*j-1] for j in range(1,k+1)]   # rho is 0-indexed: rho_{2j+1}-rho_{2j}
    r1=rho[0]; g=min(2*r1,b-1-2*r1)
    act=[j for j in range(1,k+1) if w[j-1]>=1]
    if not act:
        A=b-1-2*r1
        if A==0: return None
        return tuple(sorted([0]*(n-1)+[min(A-1,b-A)]))
    J=max(act); out=[g, w[J-1]-1, w[J-1]]
    for j in range(1,J): out+=[max(w[j-1]-1,0)]*2
    out+=[0]*(2*(k-J))
    return tuple(sorted(out))
if __name__=='__main__':
    # 1) reduction vs direct rule: every digit string, small cases
    for n,bases in ((3,range(3,9)),(5,range(3,7)),(7,(3,4))):
        pl=pairs(n)
        for b in bases:
            tgt=tuple([0]*(n-1)+[1]); F=(b-1)*(b**n-1); worst=0
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n):
                if s[0]==s[-1]: assert K(s,n,b,pl)==0; continue
                v=K(s,n,b,pl); assert v>0 and v<b**(2*n); st=1
                while v!=F:
                    rho=deficits(v,n,b); dg=sorted(((v//b**i)%b for i in range(2*n)),reverse=True)
                    v2=K(dg,n,b,pl); assert v2>0; assert deficits(v2,n,b)==T(rho,n,b),(n,b,s,rho)
                    v=v2; st+=1; assert st<500
                worst=max(worst,st)
            print(f"n={n} base={b}: every string reaches (b-1)(b^n-1); reduction exact; max steps {worst}")
