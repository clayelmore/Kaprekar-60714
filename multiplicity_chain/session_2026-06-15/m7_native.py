import importlib.util, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(0)
d=28
Fdesc=tuple([7]*7+[6]*7+[4]*7+[1]*7)
A=[3,2,1,0]; B=[0,1,2,3]   # 6174 base: c_i = 10^{A_i}-10^{B_i}, blocks ordered 7,6,4,1

def build(perms):  # perms[i]=permutation of 0..6 (place-value slots) for block i; pair-symmetric, fixes M7
    c=[0]*28
    for i in range(4):
        for s in range(7):
            sh=4*perms[i][s]
            c[7*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
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

Fcanon=K_apply(build([[6,5,4,3,2,1,0]]*4),Fdesc)
print(f"target fixed point (6174x7) = {Fcanon}",flush=True)
print(f"canonical: monotone={monotone(build([[6,5,4,3,2,1,0]]*4))}, cycle_killed={cycle_killed(build([[6,5,4,3,2,1,0]]*4),Fcanon)}",flush=True)

N=400000; mono=0; killed=0; hits=[]
for t in range(1,N+1):
    perms=[random.sample(range(7),7) for _ in range(4)]
    c=build(perms)
    if not monotone(c): continue
    mono+=1
    F=K_apply(c,Fdesc)
    if F!=Fcanon: continue
    if not cycle_killed(c,F): continue
    killed+=1
    af=alpha_fails(c,F)
    if af==0:
        hits.append(perms)
        print(f"*** CANDIDATE t={t}: alpha_fails=0  perms={perms}",flush=True)
    elif af<=20:
        print(f"  near t={t}: alpha_fails={af} (cycle killed)  perms={perms}",flush=True)
    if t%50000==0:
        print(f"t={t}: monotone={mono}, cycle-killed-among-mono={killed}, clean-hits={len(hits)}",flush=True)
print(f"DONE: {mono} monotone, {killed} killed the 4995/5355 cycle, {len(hits)} clean alphabet hits",flush=True)
import json
json.dump(hits,open('/tmp/m7_native_hits.json','w'))
