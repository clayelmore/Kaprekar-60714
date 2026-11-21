#!/usr/bin/env python3
"""How much of the number does a rule really use?  (2026-11-21)
A rule at length L in base b is a coefficient vector c on the sorted letters s_0 >= ... >= s_{L-1}:
K(s) = |sum c_i s_i|, sum c_i = 0.  With gaps g_j = s_j - s_{j+1} and partial sums C_j = c_0 + ... + c_j,
K = |sum_j C_j g_j|  (j = 0..L-2).  Measures, all exact for the given (L, b):
  letters   number of letters with c_i != 0, out of L
  gaps      number of DISTINCT nonzero C_j, out of L-1: how many separate quantities step one can see
            (the L-1 gaps are all the information a difference rule can use; equal C_j merge two gaps into one)
  kept      log(#distinct first images) / log(#non-repdigit inputs): share of the input information surviving step one
  mean, max steps to the endpoint
  rich      digits of the endpoint (written with L digits) that are neither 0 nor b-1, out of L
  distinct  number of distinct digits in the endpoint
Prints 'not universal' if the rule does not have a single endpoint at that (L, b)."""
import itertools, math, sys
def from_words(w1,w2):
    L=len(w1); a={ch:L-1-i for i,ch in enumerate(w1)}; b={ch:L-1-i for i,ch in enumerate(w2)}
    return [(a[chr(65+i)],b[chr(65+i)]) for i in range(L)]
def extend(core,d):
    N=len(core); a=[x for x,_ in core]; b=[y for _,y in core]
    if d==N: return core
    a2=a[:N-1]+list(range(N,d))+[a[N-1]]; b2=b[:N-1]+[b[N-1]]+list(range(N,d))
    return list(zip(a2,b2))
def coeffs(places,b): return [b**x-b**y for x,y in places]
def score(c,b):
    L=len(c); C=[]; s=0
    for x in c[:-1]: s+=x; C.append(s)
    letters=sum(1 for x in c if x); gaps=len({abs(x) for x in C if x})
    def step(t):
        v=abs(sum(x*y for x,y in zip(c,t))); return tuple(sorted(((v//b**i)%b for i in range(L)),reverse=True)),v
    memo={}; imgs=set(); n=0; tot=0; mx=0; F=None
    for t in itertools.combinations_with_replacement(range(b-1,-1,-1),L):
        if t[0]==t[-1]: continue
        n+=1; u,v=step(t); imgs.add(u)
        path=[t]; cur=u
        while cur not in memo:
            if cur[0]==cur[-1] or cur in path[:-1] and cur!=path[-1]: return None
            if cur==path[-1]:
                memo[cur]=0; F=step(cur)[1] if F is None else F
                if step(cur)[1]!=F: return None
                break
            path.append(cur); cur=step(cur)[0]
            if len(path)>5000: return None
        d=memo[cur]
        for x in reversed(path):
            if x==cur and d==0: continue
            d+=1; memo[x]=d
        tot+=memo[t]; mx=max(mx,memo[t])
    fx=[k for k,v in memo.items() if v==0]
    if len(fx)!=1: return None
    fd=[(F//b**i)%b for i in range(L)]
    return dict(L=L,b=b,letters=letters,gaps=gaps,kept=math.log(len(imgs))/math.log(n),mean=tot/n,max=mx,
                rich=sum(1 for x in fd if x not in (0,b-1)),distinct=len(set(fd)),F=F)
def classical(L): return [(L-1-i,i) for i in range(L)]
def extreme(L): return [(L-1,0)]+[(L-1-i,L-1-i) for i in range(1,L-1)]+[(0,L-1)]
def halfswap(n):
    from halfswap_family import pairs as po
    from halfswap_even import pairs as pe
    pl=dict(po(n) if n%2 else pe(n)); pc=[None]*(2*n)
    for q,(P,M) in pl.items(): pc[P]=(q+n,q); pc[M]=(q,q+n)
    return pc
def midfix(n):
    from midfix_family import rule
    pc=[None]*(2*n+1); pc[1]=(n,n)
    for q,(P,M) in rule(n).items(): pc[P]=(q+n+1,q); pc[M]=(q,q+n+1)
    return pc
def rotation(n):
    pc=[None]*(2*n+1); pc[2*n]=(2*n,n); pc[0]=(n,0); pc[2*n-1]=(0,2*n)
    for q in range(1,n): pc[2*q-1]=(q,q+n); pc[2*q]=(q+n,q)
    return pc
RULES=[
 ("Kaprekar 495 (ABC - CBA)",classical(3)),
 ("Kaprekar 6174 (ABCD - DCBA)",classical(4)),
 ("Extreme swap, 4 digits",extreme(4)),
 ("Extreme swap, 7 digits",extreme(7)),
 ("60714 (ADCBE - DEACB)",from_words("ADCBE","DEACB")),
 ("146070 (BFADCE - CBDEAF)",from_words("BFADCE","CBDEAF")),
 ("146070 rule at 7 digits",extend(from_words("BFADCE","CBDEAF"),7)),
 ("146070 rule at 8 digits",extend(from_words("BFADCE","CBDEAF"),8)),
 ("All-base six-digit (EABDFC - DFCEAB)",from_words("EABDFC","DFCEAB")),
 ("Half-swap, 6 digits",halfswap(3)),
 ("Half-swap, 8 digits",halfswap(4)),
 ("Half-swap, 10 digits",halfswap(5)),
 ("Fixed-middle, 7 digits",midfix(3)),
 ("Fixed-middle, 9 digits",midfix(4)),
 ("Rotation (passenger), 7 digits",rotation(3)),
 ("Pandigital rule at 10 digits",extend(list(zip([0,1,2,3,6,4,7,5],[2,3,4,5,0,7,1,6])),10)),
 ("Pandigital rule at 12 digits",extend(list(zip([0,1,2,3,6,4,7,5],[2,3,4,5,0,7,1,6])),12)),
]
if __name__=='__main__':
    b=int(sys.argv[1]) if len(sys.argv)>1 else 10
    print("rule\tL\tletters\tgaps\tkept\tmean_steps\tmax_steps\trich\tdistinct\tendpoint")
    for name,pc in RULES:
        r=score(coeffs(pc,b),b)
        if r is None: print(f"{name}\t{len(pc)}\tnot universal"); continue
        print(f"{name}\t{r['L']}\t{r['letters']}/{r['L']}\t{r['gaps']}/{r['L']-1}\t{r['kept']:.2f}\t{r['mean']:.1f}\t{r['max']}\t{r['rich']}/{r['L']}\t{r['distinct']}\t{r['F']}")
        sys.stdout.flush()
