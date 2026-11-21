#!/usr/bin/env python3
"""Find every fixed point of an extended rule, at every length at once, with no iteration (2026-11-21).

Fixed-point equation.  With sorted digits s_0 >= s_1 >= ... and gaps g_j = s_j - s_{j+1}, the rule is
K = | sum_j C_j g_j |, C_j = partial sums of the coefficients.  F is a fixed point iff the gaps of F's own
sorted digits, put back into that sum, give F:        F = | sum_j C_j * gap_j(F) |.
Gaps are digits that add up to the largest digit (<= 9), and beyond the core each gap is written straight into
its own place, so a fixed point has at most N + 9 nonzero digits whatever the length.  So: list the digit
multisets with at most N + 9 nonzero digits, apply the rule ONCE to each, keep those that return their own digits.
usage: fixed_points.py a0,a1,.. b0,b1,..      e.g.  fixed_points.py 3,5,1,2,0,4 1,4,5,3,2,0"""
import sys, itertools, time
a=[int(x) for x in sys.argv[1].split(',')]; b=[int(x) for x in sys.argv[2].split(',')]; N=len(a)
def K(s):                                   # s: nonzero digits sorted descending; one zero appended
    d=max(len(s)+1,N); s=list(s)+[0]*(d-len(s))
    aa=a if d==N else a[:N-1]+list(range(N,d))+[a[N-1]]; bb=b if d==N else b[:N-1]+[b[N-1]]+list(range(N,d))
    return abs(sum((10**x-10**y)*v for x,y,v in zip(aa,bb,s)))
t=time.time(); found=[]; tested=0
for k in range(1,N+10):
    for s in itertools.combinations_with_replacement(range(9,0,-1),k):
        tested+=1; F=K(s)
        if tuple(sorted((int(c) for c in str(F) if c!='0'),reverse=True))==s: found.append((F,s))
print(f"{tested:,} candidates, one rule application each, {time.time()-t:.0f}s")
for F,s in found: print('fixed point',F,' nonzero digits',''.join(map(str,s)),' gaps',[s[i]-(s[i+1] if i+1<len(s) else 0) for i in range(len(s))])
