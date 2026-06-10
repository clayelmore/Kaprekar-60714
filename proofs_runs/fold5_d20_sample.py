import random, time, json
from collections import Counter
random.seed(60714)
def V(t): return 9*t[0]-900*t[1]+900*t[2]-9*t[3]
def slices(s,k): return [(s[j],s[k+j],s[2*k+j],s[3*k+j]) for j in range(k)]
def fold_K(s,k): return abs(sum(V(sl)*10**(4*(k-1-j)) for j,sl in enumerate(slices(s,k))))
def coherent(s,k):
    sg=[V(sl) for sl in slices(s,k) if V(sl)!=0]
    return all(x>0 for x in sg) or all(x<0 for x in sg)
def sd(n,d): return tuple(sorted((int(c) for c in str(n).zfill(d)),reverse=True))
k,d=5,20
N=300000; mx=0; never=0; t0=time.time(); tested=0
while tested<N:
    s=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
    c=Counter(s)
    if len(c)==1 or max(c.values())>=d-1: continue
    tested+=1; cur=s; st=0
    while not coherent(cur,k):
        v=fold_K(cur,k)
        if v==0: break
        cur=sd(v,d); st+=1
        if st>100: never+=1; break
    mx=max(mx,st)
res={'k':5,'d':20,'sampled':tested,'max_entry':mx,'never':never,'sec':round(time.time()-t0)}
json.dump(res,open('/tmp/kap60714/proofs_runs/fold5_sample_results.json','w'))
print(res)
