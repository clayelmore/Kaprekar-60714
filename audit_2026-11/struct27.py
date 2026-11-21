import math,random,sys
from usage_score import coeffs,extend
def words(pc):
    L=len(pc); return ''.join(chr(65+i) for p in range(L-1,-1,-1) for i in range(L) if pc[i][0]==p)+' - '+''.join(chr(65+i) for p in range(L-1,-1,-1) for i in range(L) if pc[i][1]==p)
def depth(pc,b,N=4000,seed=1):
    random.seed(seed); c=coeffs(pc,b); L=len(c); worst=0; tot=0
    for _ in range(N):
        s=sorted((random.randrange(b) for _ in range(L)),reverse=True); k=0; seen=None
        while True:
            v=abs(sum(x*y for x,y in zip(c,s))); t=sorted(((v//b**i)%b for i in range(L)),reverse=True)
            if t==s: break
            s=t; k+=1
            if k>3000: return None
        worst=max(worst,k); tot+=k
    return worst,round(tot/N,1)
rules=[]
for f in ('bases7/survivors_5gap.txt',):
    for l in open(f):
        if l.strip():
            a,bb=l.split(); rules.append(list(zip(map(int,a.split(',')),map(int,bb.split(',')))))
out=[]
for pc in rules:
    fac=[]
    for d in (7,8,9):
        e=extend(pc,d); gs=[]
        for b in (7,10,13):
            g=0
            for x in coeffs(e,b): g=math.gcd(g,abs(x))
            gs.append(g)
        # express gcd as product of (b^k-1)
        desc=[]
        for k in (6,5,4,3,2,1):
            if all(g%(b**k-1)==0 for g,b in zip(gs,(7,10,13))): desc.append(f"b^{k}-1"); break
        fac.append(desc[0] if desc else '?')
    ds=[depth(pc,b) for b in (10,40,160,640)]
    d9=[depth(extend(pc,9),b,2000) for b in (10,40,160)]
    out.append((ds[-1][0] if ds[-1] else 9999,words(pc),fac,ds,d9))
for o in sorted(out,key=lambda t:t[0]): print(o[1],o[2],'L7 (max,mean) b=10,40,160,640:',o[3],'| L9 b=10,40,160:',o[4])
