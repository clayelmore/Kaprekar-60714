import importlib.util, itertools
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
d=28; A=[3,2,1,0]; B=[0,1,2,3]; Fdesc=tuple([7]*7+[6]*7+[4]*7+[1]*7)
def build_uniform(tau):  # same place-value perm tau across all 4 blocks -> retains slice factorization
    c=[0]*28
    for i in range(4):
        for s in range(7): sh=4*tau[s]; c[7*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
    return c
def monotone(c):
    s=0
    for x in c:
        s+=x
        if s<0: return False
    return True
CYC=[4995599449955994599461744176,5355535553555175517581728172]
def cycle_killed(c,F):
    for n in CYC:
        cur=n; seen=set()
        while cur!=F:
            if cur==0 or cur in seen: return False
            seen.add(cur); cur=K_apply(c,sdd(cur,d))
            if len(seen)>400: return False
    return True
def alphabet():
    out=[]
    for a in range(29):
      for b in range(29-a):
        for cc in range(29-a-b):
          e=28-a-b-cc
          if e<0 or max(a,b,cc,e)==28: continue
          out.append(int(''.join(map(str,sorted([7]*a+[6]*b+[4]*cc+[1]*e,reverse=True)))))
    return out
alpha=alphabet()
def alpha_fails(c,F,cap=400):
    f=0
    for n in alpha:
        cur=n; seen=set()
        while cur!=F:
            if cur==0 or cur in seen: f+=1; break
            seen.add(cur); cur=K_apply(c,sdd(cur,d))
            if len(seen)>cap: f+=1; break
    return f
Fdesc_int=int("1"*7+"4"*7+"6"*7+"7"*7)
F=K_apply(build_uniform([6,5,4,3,2,1,0]),sdd(Fdesc_int,d))
mono=killed=clean=0; winners=[]
for tau in itertools.permutations(range(7)):
    c=build_uniform(tau)
    if not monotone(c): continue
    mono+=1
    if not cycle_killed(c,F): continue
    killed+=1
    af=alpha_fails(c,F)
    if af==0:
        clean+=1; winners.append(list(tau))
        print(f"UNIFORM cycle-killer + alphabet-clean: tau={list(tau)}",flush=True)
print(f"\nover 5040 uniform perms: monotone={mono}, killed 4995/5355={killed}, alphabet-clean={clean}",flush=True)
import json; json.dump(winners,open('/tmp/m7_uniform_winners.json','w'))
