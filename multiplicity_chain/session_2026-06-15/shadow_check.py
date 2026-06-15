import importlib.util, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(123); A=[3,2,1,0]; B=[0,1,2,3]
def fold(base,k):
    c=[0]*(4*k)
    for i in range(4):
        for j in range(k): c[k*i+j]=base[i]*10**(4*(k-1-j))
    return c
def build_perm(perms,k):
    d=4*k; c=[0]*d
    for i in range(4):
        for s in range(k): sh=4*perms[i][s]; c[k*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
    return c
def fate(c,F,n,d,cap=400):
    cur=n; seen=[]
    while cur!=F:
        if cur==0: return ('ZERO',)
        if cur in seen:
            i=seen.index(cur); return ('CYC',)+tuple(seen[i:])
        seen.append(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return ('CAP',)
    return ('FP',)
def is_shadow(members):  # {4,5,9}-dominant signature
    for m in members:
        s=str(m); frac=sum(s.count(x) for x in '459')/len(s)
        if frac>=0.55 or s[:4] in ('4995','5355','5499','9955'): return True
    return False

# ---- (b) m=5,6 interleaved competing attractor ----
print("=== (b) shadow recurrence at m=5,6 (interleaved 6174xk rule) ===",flush=True)
for k in (5,6):
    d=4*k; R=fold([999,90,-90,-999],k); F=int("6174"*k)
    att=Counter(); ex={}
    G=25000
    for _ in range(G):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        if len(set(combo))==1: continue
        r=fate(R,F,int(''.join(map(str,combo))),d)
        if r[0]=='FP': continue
        if r[0]=='CYC':
            mem=tuple(sorted(r[1:])); att[mem]+=1; ex[mem]=r[1:]
        else: att[(r[0],)]+=1
    print(f"m={k}: {len(att)} distinct competitors among leaks",flush=True)
    for key,cnt in att.most_common(3):
        if isinstance(key[0],int) or (len(key)>1):
            mem=ex.get(key,key); sh=is_shadow(mem)
            print(f"   cycle (cnt {cnt}) SHADOW={sh}: " + " <-> ".join(str(m) for m in mem),flush=True)
        else:
            print(f"   {key} (cnt {cnt})",flush=True)

# ---- (a) m=4: across many rules, is the shadow the ONLY obstruction? ----
print("\n=== (a) m=4: distinct competing-attractor FAMILIES across 800 reorderings ===",flush=True)
k=4; d=16; F=int("6174"*4)
fams=Counter(); nonuniv=0; likelyuniv=0; checked=0
for t in range(40000):
    perms=[random.sample(range(k),k) for _ in range(4)]
    c=build_perm(perms,k)
    # monotone check
    s=0; mono=True
    for x in c:
        s+=x
        if s<0: mono=False; break
    if not mono: continue
    checked+=1
    # sample this rule
    leak_att=None
    for _ in range(3000):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        if len(set(combo))==1: continue
        r=fate(c,F,int(''.join(map(str,combo))),d)
        if r[0] in ('CYC',) :
            leak_att=tuple(sorted(r[1:])); break
        if r[0] in ('ZERO','CAP'):
            leak_att=(r[0],); break
    if leak_att is None: likelyuniv+=1
    else:
        nonuniv+=1
        if isinstance(leak_att[0],int) or len(leak_att)>1:
            fams[('shadow' if is_shadow(leak_att) else 'OTHER:'+str(leak_att[0]))]+=1
        else: fams[leak_att[0]]+=1
    if checked>=800: break
print(f"checked {checked} monotone reorderings: ~{likelyuniv} look universal, {nonuniv} non-universal",flush=True)
print(f"competing-attractor families seen: {dict(fams)}",flush=True)
print("DONE",flush=True)
