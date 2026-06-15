import importlib.util, itertools
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
A=[3,2,1,0]; B=[0,1,2,3]; k=3; d=12; F=int("6174"*3)
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
def admissible():
    for cc in itertools.combinations_with_replacement(range(10),d):
        c=Counter(cc)
        if len(c)==1: continue
        yield int(''.join(map(str,sorted(cc,reverse=True))))
ADM=list(admissible())

# all near-universal (alphabet-clean) reorderings, their competing attractors
perms_all=list(itertools.permutations(range(k)))
near=[]
for combo in itertools.product(perms_all,repeat=4):
    c=build(list(combo))
    if not monotone(c): continue
    if all(reaches(c,n) for n in alpha):  # alphabet-clean = near-universal
        near.append((list(combo),c))
print(f"near-universal (alphabet-clean) clean-6174x3 reorderings: {len(near)}",flush=True)
# for each, full basin + competing attractor
comp_counter=Counter()
for combo,c in near:
    atts=Counter()
    for n in ADM:
        t=terminal(c,n)
        if t[0]!='FP': atts[t]+=1
    # the dominant competitor
    if atts:
        top=atts.most_common(1)[0]
        comp_counter[top[0]]+=1
print(f"\nDistinct competing attractors across the {len(near)} near-universal rules:",flush=True)
for att,cnt in comp_counter.most_common():
    if att[0]=='FP': desc='FP (=F, shouldn\'t happen)'
    elif att[0]=='CYC': desc=f'CYCLE period {len(att)-1}: {att[1:]}'
    elif att[0]=='ZERO': desc='ZERO'
    else: desc=str(att)
    print(f"   in {cnt} rules: {desc}",flush=True)
# is 535549955994 a fixed point in ALL of them?
P=535549955994
fixedinall=sum(1 for combo,c in near if K_apply(c,sdd(P,d))==P)
print(f"\n535549955994 is a FIXED POINT in {fixedinall}/{len(near)} of the near-universal rules",flush=True)
print("DONE",flush=True)
