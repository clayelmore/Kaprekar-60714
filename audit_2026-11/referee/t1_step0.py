# Step 0: digit description vs raw definition
from ref import *
def predicted(s):
    d=len(s)
    L=990*s[0]+90000*s[1]-99990*s[2]-900*s[3]-99*s[4]-s[5]+10**4*s[d-1]
    assert abs(L)<10**6
    g={k:s[k-1]-s[k] for k in range(6,d)}
    H=sum(10**k*v for k,v in g.items())
    assert sum(g.values())<=9
    dig=[0]*d
    for k,v in g.items(): dig[k]=v
    if H==0: low=abs(L)
    elif L>=0: low=L
    else:
        assert H+L>0
        low=10**6+L; j=6
        while dig[j]==0: dig[j]=9; j+=1
        dig[j]-=1
    assert 0<=low<10**6
    for j in range(6): dig[j]=low%10; low//=10
    return sum(x*10**i for i,x in enumerate(dig)), H, L
cnt=Counter(); n=0; mnL=0; mxL=0
for d in range(6,13):
    for s in itertools.combinations_with_replacement(range(9,-1,-1),d):
        p,H,L=predicted(s); assert p==K(s),(s,p,K(s)); n+=1
        mnL=min(mnL,L); mxL=max(mxL,L)
        cnt[(H>0,(L>0)-(L<0))]+=1
        if K(s)==0: assert len(set(s))==1,s
        if H>0: assert H+L>0
print("exhaustive d=6..12 states",n,"case counts (H>0, sign L):",dict(cnt),"L range",mnL,mxL)
random.seed(11)
for d in (13,17,21,22,30,60,200):
    for _ in range(30000):
        k=random.choice([1,2,3,4,5,7,10]); ds=random.sample(range(10),k)
        s=tuple(sorted((random.choice(ds) for _ in range(d)),reverse=True))
        p,H,L=predicted(s); assert p==K(s); n+=1
print("total incl random",n,"all match")
