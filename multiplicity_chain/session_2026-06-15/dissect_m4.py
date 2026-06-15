import importlib.util, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(4); d=16
def fold(base,k):
    c=[0]*(4*k)
    for i in range(4):
        for j in range(k): c[k*i+j]=base[i]*10**(4*(k-1-j))
    return c
R=fold([999,90,-90,-999],4)   # interleaved m=4 rule (basin 99.69%, NOT universal)
F=6174617461746174
def fate(c,n,cap=400):
    cur=n; seen=[]
    while cur!=F:
        if cur==0: return ('ZERO',None)
        if cur in seen:
            i=seen.index(cur); return ('CYCLE',tuple(seen[i:]))
        seen.append(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return ('CAP',None)
    return ('FP',None)
# sample to find the competing attractor(s)
attractors=Counter(); examples={}
G=400000; leaks=0
for _ in range(G):
    combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
    cnt=Counter(combo)
    if len(cnt)==1: continue
    f,info=fate(R,int(''.join(map(str,combo))))
    if f=='FP': continue
    leaks+=1
    key=('CYCLE',info) if f=='CYCLE' else (f,)
    attractors[key]+=1
    if f=='CYCLE': 
        for m in info: examples.setdefault(m, dict(sorted(Counter(str(m).zfill(d)).items())))
print(f"interleaved 6174x4 rule: {leaks} leaks in {G} samples ({100*leaks/G:.3f}%)")
print(f"distinct competing attractors: {len(attractors)}")
for k,cnt in attractors.most_common(8):
    if k[0]=='CYCLE':
        cyc=k[1]; print(f"  CYCLE period {len(cyc)} (count {cnt}):")
        for m in cyc: print(f"     {m}   digits {dict(sorted(Counter(str(m).zfill(d)).items()))}")
    else:
        print(f"  {k[0]} (count {cnt})")
