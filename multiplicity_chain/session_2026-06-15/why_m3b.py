import importlib.util, itertools, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(3); A=[3,2,1,0]; B=[0,1,2,3]; k=3; d=12; F=int("6174"*3)
def build(perms):
    c=[0]*d
    for i in range(4):
        for s in range(k): sh=4*perms[i][s]; c[k*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
    return c
def monotone(c):
    s=0
    for x in c:
        s+=x
        if s<0: return False
    return True
def alphabet():
    out=[]
    for a in range(d+1):
      for b in range(d+1-a):
        for cc in range(d+1-a-b):
          e=d-a-b-cc
          if e<0 or max(a,b,cc,e)==d: continue
          out.append(int(''.join(map(str,sorted([7]*a+[6]*b+[4]*cc+[1]*e,reverse=True)))))
    return out
alpha=alphabet()
def reaches(c,n,cap=300):
    cur=n; seen=set()
    while cur!=F:
        if cur==0 or cur in seen: return False
        seen.add(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return False
    return True
def terminal(c,n,cap=300):
    cur=n; seen=[]
    while cur!=F:
        if cur==0: return ('ZERO',)
        if cur in seen:
            i=seen.index(cur); return ('CYC',)+tuple(sorted(seen[i:]))
        seen.append(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return ('CAP',)
    return ('FP',)
perms_all=list(itertools.permutations(range(k)))
near=[build(list(combo)) for combo in itertools.product(perms_all,repeat=4)
      if monotone(build(list(combo))) and all(reaches(build(list(combo)),n) for n in alpha)]
print(f"near-universal reorderings: {len(near)}",flush=True)
P=535549955994
fixedP=sum(1 for c in near if K_apply(c,sdd(P,d))==P)
print(f"535549955994 is a FIXED POINT in {fixedP}/{len(near)} of them",flush=True)
# sampled competing attractor per rule
comp=Counter()
for c in near:
    found=None
    for _ in range(8000):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        if len(set(combo))==1: continue
        t=terminal(c,int(''.join(map(str,combo))))
        if t[0]!='FP': found=t; break
    if found: comp[found]+=1
    else: comp[('none_found',)]+=1
print("competing attractor (first leak found) across the rules:",flush=True)
for att,cnt in comp.most_common():
    if att[0]=='CYC': desc=f"CYCLE p{len(att)-1}: {att[1:]}"
    else: desc=att[0] if att[0] in ('ZERO','none_found','CAP') else str(att)
    print(f"   {cnt} rules -> {desc}",flush=True)
# is the m=3 obstruction always period-1 (fixed point)?
periods=Counter()
for att,cnt in comp.items():
    if att[0]=='CYC': periods[len(att)-1]+=cnt
print("competing-attractor periods:", dict(periods),flush=True)
print("DONE",flush=True)
