import importlib.util, random, itertools
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(11)
A=[3,2,1,0]; B=[0,1,2,3]

def build(perms,k):  # within-block reorder of the 6174 k-fold; fixes 6174xk regardless
    d=4*k; c=[0]*d
    for i in range(4):
        for s in range(k): sh=4*perms[i][s]; c[k*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
    return c
def monotone(c):
    s=0
    for x in c:
        s+=x
        if s<0: return False
    return True
def alphabet(k):
    d=4*k; out=[]
    for a in range(d+1):
      for b in range(d+1-a):
        for cc in range(d+1-a-b):
          e=d-a-b-cc
          if e<0 or max(a,b,cc,e)==d: continue
          out.append(int(''.join(map(str,sorted([7]*a+[6]*b+[4]*cc+[1]*e,reverse=True)))))
    return out
def alpha_fails(c,F,d,alpha,cap=400):
    f=0
    for n in alpha:
        cur=n; seen=set()
        while cur!=F:
            if cur==0 or cur in seen: f+=1; break
            seen.add(cur); cur=K_apply(c,sdd(cur,d))
            if len(seen)>cap: f+=1; break
    return f
def gen_clean(c,F,d,G=60000):
    bad=0
    for _ in range(G):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        cnt=Counter(combo)
        if len(cnt)==1 or max(cnt.values())>=d-1: continue
        cur=int(''.join(map(str,combo))); seen=set()
        while cur!=F:
            if cur==0 or cur in seen: bad+=1; break
            seen.add(cur); cur=K_apply(c,sdd(cur,d))
            if len(seen)>500: bad+=1; break
    return bad

for k in (5,6):
    d=4*k; F=int("6174"*k); alpha=alphabet(k)
    # canonical fold baseline
    canon=build([list(range(k-1,-1,-1))]*4,k)
    print(f"\n=== k={k} (d={d}), F=6174x{k}, alphabet size {len(alpha)} ===",flush=True)
    print(f"  canonical 6174 {k}-fold: monotone={monotone(canon)}, alphabet_fails={alpha_fails(canon,F,d,alpha)}",flush=True)
    # scramble search for an alphabet-clean monotone rule
    found=None; mono=0; N=120000
    for t in range(N):
        perms=[random.sample(range(k),k) for _ in range(4)]
        c=build(perms,k)
        if not monotone(c): continue
        mono+=1
        if alpha_fails(c,F,d,alpha)==0:
            found=perms; print(f"  alphabet-clean hit at t={t}: perms={perms}",flush=True); break
    if found:
        c=build(found,k); gb=gen_clean(c,F,d)
        print(f"  -> general sample (60k): {gb} failures  => 6174x{k} {'EVIDENCE-UNIVERSAL' if gb==0 else 'still leaks'}",flush=True)
    else:
        print(f"  -> NO alphabet-clean monotone scramble found in {mono} monotone tries (of {N})",flush=True)
print("\nDONE",flush=True)
