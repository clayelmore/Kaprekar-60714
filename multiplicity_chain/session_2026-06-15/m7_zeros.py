import importlib.util, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(30)
def fold_coeffs(base,k):
    c=[0]*(4*k)
    for i in range(4):
        for j in range(k): c[k*i+j]=base[i]*10**(4*(k-1-j))
    return c
c28=fold_coeffs([999,90,-90,-999],7)

def add_pairs(c,npairs):  # 60714-style absorbing zero-sum pairs
    c=list(c); d=len(c)
    for _ in range(npairs):
        c=c+[9*10**d,-9*10**d]; d+=2
    return c
def add_passive(c,nz):    # passive zero coefficients
    return list(c)+[0]*nz

def classify(c,F,start,d,cap=900):
    cur=start; seen=set()
    while cur!=F:
        if cur==0: return 'ZERO'
        if cur in seen: return 'CYCLE'
        seen.add(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return 'CAP'
    return 'FP'

# the d=28 obstruction-cycle member
cyc28=4995599449955994599461744176

for d,(kind,c) in {
    29:('+1 passive zero', add_passive(c28,1)),
    30:('+1 absorbing pair (z=2)', add_pairs(c28,1)),
    31:('+1 pair +1 passive (z=3)', add_passive(add_pairs(c28,1),1)),
    32:('+2 absorbing pairs (z=4)', add_pairs(c28,2)),
}.items():
    z=d-28
    F=K_apply(c, tuple([7]*7+[6]*7+[4]*7+[1]*7+[0]*z))
    # (1) the d=28 cycle multiset, padded with z zeros
    padded=int(str(cyc28)+'0'*z)  # appends z zeros -> multiset gains z zeros
    out_cyc=classify(c,F,padded,d)
    # (2) general sample
    G=60000; res=Counter()
    for _ in range(G):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        cnt=Counter(combo)
        if len(cnt)==1 or max(cnt.values())>=d-1: continue
        res[classify(c,F,int(''.join(map(str,combo))),d)]+=1
    print(f"d={d} ({kind}): F={F}")
    print(f"   the d=28 cycle multiset +{z} zeros -> {out_cyc}")
    print(f"   general ~{G}: {dict(res)}",flush=True)
