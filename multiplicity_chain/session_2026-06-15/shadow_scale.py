import importlib.util, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(55); A=[3,2,1,0]; B=[0,1,2,3]
def build(perms,k):
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
def terminal(c,F,n,d,cap=400):
    cur=n; seen=[]
    while cur!=F:
        if cur==0: return ('ZERO',)
        if cur in seen:
            i=seen.index(cur); return ('CYC',)+tuple(seen[i:])
        seen.append(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return ('CAP',)
    return ('FP',)
def blocks(n,d): s=str(n).zfill(d); return [s[i:i+4] for i in range(0,len(s),4)]

SHADOW_ALPHABET={'5355','5175','8172','4995','5994','4176','6174'}
for k in (5,6):
    d=4*k; F=int("6174"*k); alpha=alphabet(k)
    best=None  # (failcount, c)
    for t in range(6000):
        perms=[random.sample(range(k),k) for _ in range(4)]
        c=build(perms,k)
        if not monotone(c): continue
        # count alphabet fails (early-exit if clearly bad)
        fails=[]
        for n in alpha:
            if terminal(c,F,n,d)[0]!='FP':
                fails.append(n)
                if len(fails)>60: break   # not near-universal, abandon
        if 0<len(fails)<=60 and (best is None or len(fails)<best[0]):
            best=(len(fails),c,fails)
            if len(fails)<=10: break
    if best is None:
        print(f"\nm={k}: no near-universal scramble (1..60 fails) found in sample",flush=True); continue
    fc,c,fails=best
    print(f"\n=== m={k} (d={d}): near-universal scramble with {fc} alphabet failures ===",flush=True)
    # residual attractors + block decomposition
    atts=Counter(); ex={}
    for n in fails:
        t=terminal(c,F,n,d)
        key=('CYC',tuple(sorted(t[1:]))) if t[0]=='CYC' else (t[0],)
        atts[key]+=1
        if t[0]=='CYC': ex[key]=t[1:]
    for key,cnt in atts.most_common(3):
        if key[0]=='CYC':
            mem=ex[key]
            print(f"  residual CYCLE period {len(mem)} (catches {cnt}):",flush=True)
            for m_ in mem:
                bl=blocks(m_,d); inshadow=all(b in SHADOW_ALPHABET for b in bl)
                print(f"     {m_}  blocks={bl}  multiset={dict(Counter(bl))}  ALL-shadow-blocks={inshadow}",flush=True)
        else:
            print(f"  residual {key[0]} (catches {cnt})",flush=True)
print("\nDONE",flush=True)
