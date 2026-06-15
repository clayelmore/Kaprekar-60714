import importlib.util, random, sys
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(606); A=[3,2,1,0]; B=[0,1,2,3]; k=6; d=24; F=int("6174"*6)
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
def reaches(c,n,cap=300):
    cur=n; seen=set()
    while cur!=F:
        if cur==0 or cur in seen: return False
        seen.add(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return False
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
alpha=alphabet(); random.shuffle(alpha)
prefilter=alpha[:200]   # cheap subset
print(f"k=6 d=24 alphabet={len(alpha)}, prefilter=200",flush=True)
found=None; mono=0; passed_pre=0; N=150000
for t in range(N):
    perms=[random.sample(range(k),k) for _ in range(4)]
    c=build(perms)
    if not monotone(c): continue
    mono+=1
    if not all(reaches(c,n) for n in prefilter): 
        if mono%5000==0: print(f"  {mono} monotone, {passed_pre} passed prefilter, no hit",flush=True)
        continue
    passed_pre+=1
    if all(reaches(c,n) for n in alpha):
        found=perms; print(f"ALPHABET-CLEAN hit t={t} mono={mono}: {perms}",flush=True); break
    if mono%5000==0: print(f"  {mono} monotone, {passed_pre} passed prefilter, no clean hit",flush=True)
if found:
    c=build(found); bad=0; G=40000
    for _ in range(G):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        cnt=Counter(combo)
        if len(cnt)==1 or max(cnt.values())>=d-1: continue
        if not reaches(c,int(''.join(map(str,combo))),500): bad+=1
    print(f"RESULT 6174x6: general {G} -> {bad} fails => {'EVIDENCE-UNIVERSAL' if bad==0 else 'leaks'}",flush=True)
else:
    print(f"RESULT 6174x6: NO clean hit in {mono} monotone tries ({passed_pre} passed prefilter)",flush=True)
print("DONE",flush=True)
