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
def alpha_clean(c): return all(reaches(c,n) for n in alpha)
perms_all=list(itertools.permutations(range(k)))
mono=0; clean=0; cleanlist=[]; best=0
for combo in itertools.product(perms_all,repeat=4):
    c=build(list(combo))
    if not monotone(c): continue
    mono+=1
    # quick: count how many of a small sample reach F (cheap best-tracker)
    if alpha_clean(c):
        clean+=1; cleanlist.append(list(combo))
print(f"m=3: {mono} monotone reorderings (of 1296); ALPHABET-clean: {clean}",flush=True)
# full basin for any alphabet-clean ones
import itertools as it
def admissible():
    for cc in it.combinations_with_replacement(range(10),d):
        c=Counter(cc)
        if len(c)==1: continue
        yield int(''.join(map(str,sorted(cc,reverse=True))))
if cleanlist:
    ADM=list(admissible())
    for combo in cleanlist[:5]:
        c=build(combo); hit=sum(1 for n in ADM if reaches(c,n,300))
        print(f"  full basin {hit}/{len(ADM)} = {100*hit/len(ADM):.2f}%  perms={combo}  {'UNIVERSAL' if hit==len(ADM) else ''}",flush=True)
print("=> 6174x3 universal under a fold-reordering?", "YES" if clean else "NO (no alphabet-clean reordering exists)",flush=True)
print("DONE",flush=True)
