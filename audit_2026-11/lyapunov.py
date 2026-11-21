#!/usr/bin/env python3
"""Audit 2026-11: Theorem 7.1 from scratch. Gap system of the classical 4-digit map,
exact Farkas certificates for degree <= 6, exact degree-7 Lyapunov function."""
import numpy as np, sympy as sp
from fractions import Fraction
from scipy.optimize import linprog
def G(p,q):
    v=999*p+90*q; s=sorted(f"{v:04d}",reverse=True); a,b,c,e=map(int,s); return (a-e,b-c)
S=[(p,q) for p in range(1,10) for q in range(p+1)]; fixed=[s for s in S if G(*s)==s]
# acyclic / reaching time / image sizes
def rt(s):
    n=0
    while s!=(6,2): s=G(*s); n+=1; assert n<60
    return n
img=set(S); sizes=[len(img)]
while len(img)>1: img={G(*s) for s in img}; sizes.append(len(img))
print("states",len(S),"fixed",fixed,"max reaching time",max(rt(s) for s in S),"image sizes",sizes)
NF=[s for s in S if s!=(6,2)]
for D in range(2,8):
    mon=[(i,j) for i in range(D+1) for j in range(D+1-i)]
    M=[[G(*s)[0]**i*G(*s)[1]**j - s[0]**i*s[1]**j for (i,j) in mon] for s in NF]   # 53 x nmon integer matrix
    Mf=np.array(M,dtype=float)
    # infeasibility certificate: y>=0, sum y=1, M^T y = 0
    r=linprog(np.zeros(len(NF)),A_eq=np.vstack([(Mf/np.abs(Mf).max(axis=0).clip(1)).T,np.ones(len(NF))]),b_eq=np.r_[np.zeros(len(mon)),1],bounds=(0,None),method='highs-ds')
    if r.status==0:
        sup=[k for k in range(len(NF)) if r.x[k]>1e-9]
        ns=sp.Matrix([[M[k][c] for k in sup] for c in range(len(mon))]).nullspace()
        ok=False
        for v in ns:
            v=v*(1 if v[0]>0 else -1)
            if all(x>0 for x in v): ok=True
        # general exact check when nullspace dim>1: solve exact LP on support via sympy
        print(f"D={D}: monomials={len(mon)} dual LP feasible, support={len(sup)}, exact nullspace dim={len(ns)}, exact positive certificate={ok}")
    else:
        # look for Lyapunov function: maximize margin t with |w|<=1 (scaled columns)
        sc=np.abs(Mf).max(axis=0).clip(1)
        A=np.hstack([Mf/sc,np.ones((len(NF),1))]); c=np.zeros(len(mon)+1); c[-1]=-1
        r2=linprog(c,A_ub=A,b_ub=np.zeros(len(NF)),bounds=[(-1,1)]*len(mon)+[(0,None)],method='highs')
        w=[Fraction(float(x)/float(s)).limit_denominator(10**18) for x,s in zip(r2.x[:-1],sc)]
        dec=[sum(wi*mi for wi,mi in zip(w,row)) for row in M]
        print(f"D={D}: monomials={len(mon)} dual infeasible; Lyapunov LP margin={r2.x[-1]:.3e}; exact rational check: all 53 strict decreases = {all(x<0 for x in dec)} (worst {float(max(dec)):.3e})")
