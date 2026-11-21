#!/usr/bin/env python3
"""Even half-length family G_n (n even >= 4), length 2n, base b: reduced deficit dynamics (2026-11-21).
k = (n-2)/2.  Pairs by place:  0: (n-2, n-1)   1: (1, 2n-1)   2: (0, 2n-2)   3: (n+1, n)
  for j = 1..k-1:  place n+1-2j: (2j+1, 2j)     place n-2j: (2n-2-2j, 2n-1-2j)
Reduced: deficits rho_1<=...<=rho_n; w_j = rho_{2j+2}-rho_{2j+1} (j=1..k); sigma = b-1-rho_1-rho_2;
h(t) = min(t, b-1-t).
  some w_j >= 1, J = largest:  next = {(w_j-1)^+ twice: j<J} + {w_J-1, w_J} + {0 twice: j>J} + {h(sigma), h(sigma)}
  all w = 0:                   next = {0 (n-2 times), h(sigma), h(sigma-1)}        (sigma >= 1)"""
import itertools, random
from halfswap_family import K, deficits
def pairs(n):
    k=(n-2)//2; pl={0:(n-2,n-1),1:(1,2*n-1),2:(0,2*n-2),3:(n+1,n)}
    for j in range(1,k): pl[n+1-2*j]=(2*j+1,2*j); pl[n-2*j]=(2*n-2-2*j,2*n-1-2*j)
    return pl
def T(rho,n,b):
    k=(n-2)//2; w=[rho[2*j+1]-rho[2*j] for j in range(1,k+1)]; sg=b-1-rho[0]-rho[1]; h=lambda t:min(t,b-1-t)
    act=[j for j in range(1,k+1) if w[j-1]>=1]
    if not act:
        if sg==0: return None
        return tuple(sorted([0]*(n-2)+[h(sg),h(sg-1)]))
    J=max(act); out=[h(sg),h(sg),w[J-1]-1,w[J-1]]
    for j in range(1,J): out+=[max(w[j-1]-1,0)]*2
    out+=[0]*(2*(k-J))
    return tuple(sorted(out))
if __name__=='__main__':
    for n,bases in ((4,range(3,10)),(6,range(3,6)),(8,(3,))):
        pl=pairs(n)
        for b in bases:
            F=(b-1)*(b**n-1); worst=0
            for s in itertools.combinations_with_replacement(range(b-1,-1,-1),2*n):
                if s[0]==s[-1]: assert K(s,n,b,pl)==0; continue
                v=K(s,n,b,pl); assert 0<v<b**(2*n); st=1
                while v!=F:
                    rho=deficits(v,n,b); dg=sorted(((v//b**i)%b for i in range(2*n)),reverse=True)
                    v2=K(dg,n,b,pl); assert v2>0 and deficits(v2,n,b)==T(rho,n,b),(n,b,s,rho); v=v2; st+=1; assert st<500
                worst=max(worst,st)
            print(f"even n={n} base={b}: all strings reach (b-1)(b^n-1); reduction exact; max steps {worst}")
    random.seed(2)
    for n in (4,6,8,10,14):
        out=[]
        for b in (3,4,5,6,7,8,10,13,16,20,33,50,101,300,1001):
            H=(b-1)//2; tot=1
            for i in range(n): tot=tot*(H+1+i)//(i+1)
            states=itertools.combinations_with_replacement(range(H+1),n) if tot<=150000 else [tuple(sorted(min(H,max(0,random.choice((0,1,2,H//4,H//3,H//2,H,random.randint(0,H)))+random.randint(-3,3))) for _ in range(n))) for _ in range(100000)]
            tgt=tuple([0]*(n-1)+[1]); worst=0; fail=0; maxbad=0
            for rho in states:
                if b%2==1 and all(x==H for x in rho): continue
                x=rho; st=0; run=0; bad=0
                while x!=tgt:
                    y=T(x,n,b)
                    if y is None or st>3000: fail+=1; break
                    run=run+1 if y[1]>=1 else 0; bad=max(bad,run); x=y; st+=1
                worst=max(worst,st); maxbad=max(maxbad,bad)
            out.append((b,worst,maxbad,fail))
        print(f"even n={n}: (base, max steps, longest bad run, failures)",out)
