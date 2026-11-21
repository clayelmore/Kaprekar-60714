#!/usr/bin/env python3
"""Six-digit rule EABDFC - DFCEAB in base b, reduced form (2026-11-21).
K(s) = (b^3-1) * m,  m = |b p + u - b^2 v|,  p = s0-s5, u = s1-s2, v = s3-s4.
(b^3-1) m has digits (x,y,z) of n = m-1 followed by their complements, so the state after one step is the
multiset M = {max(t, b-1-t) : t in x,y,z}.  With M = {mu1>=mu2>=mu3}: A = 2 mu1-(b-1), w = mu2-mu3 and
   w = 0 :  next M = {b-1, b-1, max(A-1, b-A)}
   w >= 1:  next M = {max(w-1,b-w), max(A,b-1-A), max(w,b-1-w)}
This script (1) checks the reduction against the direct rule, (2) follows the reduced map for many bases."""
import itertools, sys
def direct(s,b):
    a=[4,3,0,2,5,1]; bb=[1,0,3,5,2,4]; return abs(sum((b**x-b**y)*v for x,y,v in zip(a,bb,s)))
def M_of_value(K,b):
    m=K//(b**3-1); assert K==m*(b**3-1); n=m-1; x,y,z=n//(b*b),(n//b)%b,n%b
    return tuple(sorted((max(t,b-1-t) for t in (x,y,z)),reverse=True))
def nxt(M,b):
    A=2*M[0]-(b-1); w=M[1]-M[2]
    if w==0:
        if A==0: return None
        return tuple(sorted((b-1,b-1,max(A-1,b-A)),reverse=True))
    return tuple(sorted((max(w-1,b-w),max(A,b-1-A),max(w,b-1-w)),reverse=True))
def check_reduction(b):
    for s in itertools.combinations_with_replacement(range(b-1,-1,-1),6):
        if s[0]==s[5]: continue
        K=direct(s,b); M=M_of_value(K,b)
        s2=sorted([M[0],M[1],M[2],b-1-M[0],b-1-M[1],b-1-M[2]],reverse=True)
        K2=direct(s2,b); assert M_of_value(K2,b)==nxt(M,b),(b,s,M)
for b in range(3,13): check_reduction(b)
print('reduction verified against the direct rule, bases 3..12, every six-digit string')
res=[]
for b in range(3,int(sys.argv[1])+1):
    tgt=tuple(sorted((b-1,b-1,max(b-2,1)),reverse=True)); lo=(b-1+1)//2  # ceil((b-1)/2)
    memo={tgt:0}; worst=0; bad=0; profile={}
    for M in itertools.combinations_with_replacement(range(b-1,lo-1,-1),3):
        if b%2==1 and M==((b-1)//2,)*3: continue
        path=[]; x=M
        while x not in memo:
            if x is None or x in path: bad+=1; break
            path.append(x); x=nxt(x,b)
        else:
            base=memo[x]
            for y in reversed(path): base+=1; memo[y]=base
            worst=max(worst,memo[M])
    res.append((b,worst,bad))
print('bases with any failure:',[r for r in res if r[2]])
print('max steps (after the first) by base:',[(b,w) for b,w,_ in res if b<=40 or b%25==0])
