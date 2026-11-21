#!/usr/bin/env python3
"""Passenger-digit rule G_n at odd length 2n+1 (n odd), base b (2026-11-21).
Letters s_0 >= ... >= s_2n.  g = s_{2n-1} - s_{2n} (bottom gap), p = s_0 - s_{2n-1}, e_q = s_{2q-1} - s_{2q} (q = 1..n-1).
  V = p - b^n g - sum_q b^q e_q,   K = (b^n - 1)|V|.
Checks, on every sorted string:
  (1) image formula: digits of K = {t, p', b-1-t-p'} + complementary pairs, as stated in NOTES_ODD_LENGTHS.md;
  (2) strings with g = 0 agree with the even rule on the top 2n letters;
  (3) every string with two 0s and a b-1 reaches the endpoint within a few steps (prints the maximum);
  (4) every non-repdigit reaches one endpoint (prints it and the maximum number of steps)."""
import itertools,sys
from collections import Counter
def parts(s,n): return s[2*n-1]-s[2*n], s[0]-s[2*n-1], [s[2*q-1]-s[2*q] for q in range(1,n)]
def K(s,n,b):
    g,p,e=parts(s,n); return (b**n-1)*abs(p-b**n*g-sum(b**(q+1)*x for q,x in enumerate(e)))
def digs(v,n,b): return tuple(sorted(((v//b**i)%b for i in range(2*n+1)),reverse=True))
def predicted(s,n,b):
    g,p,e=parts(s,n); pair=lambda y:[y,b-1-y]
    if g==0 and not any(e): return sorted([0]+pair(p-1)+[0,b-1]*(n-1)) if p else None
    qs=[q for q in range(n-1) if e[q]]
    if not qs: return sorted([g-1,p,b-g-p]+[0,b-1]*(n-1))          # all e = 0, g >= 1
    q0=qs[0]; out=[g,p,b-1-g-p]
    if p==0: return None
    for q in range(n-1): out+=pair(b-1) if q<q0 else (pair(e[q]-1) if q==q0 else pair(e[q]))
    return sorted(out)
if __name__=='__main__':
    for n,bases in ((3,range(3,13)),(5,(3,4,5,6))):
        for b in bases:
            memo={}; F=None; worst=0; end=0
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n+1):
                if s[0]==s[-1]: assert K(s,n,b)==0; continue
                v=K(s,n,b); assert v>0
                pr=predicted(s,n,b)
                if pr is not None: assert pr==sorted(digs(v,n,b)),(n,b,s)
                g,p,e=parts(s,n)
                if g==0: assert v==(b**n-1)*abs(p-sum(b**(q+1)*x for q,x in enumerate(e)))
            def depth(s):
                path=[]
                while s not in memo:
                    t=digs(K(s,n,b),n,b)
                    if t==s: memo[s]=0; break
                    assert s not in path; path.append(s); s=t
                d=memo[s]
                for x in reversed(path): d+=1; memo[x]=d
                return memo[path[0]] if path else memo[s]
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n+1):
                if s[0]==s[-1]: continue
                d=depth(s); worst=max(worst,d)
                if s[-1]==0 and s[-2]==0 and s[0]==b-1: end=max(end,d)
            fx=[s for s,d in memo.items() if d==0]; assert len(fx)==1
            m=K(fx[0],n,b)//(b**n-1)
            print(f"n={n} b={b}: formula ok; one endpoint, m={m} (b^(n-1)+1={b**(n-1)+1}); max steps {worst}; from two 0s and a b-1: {end}")
