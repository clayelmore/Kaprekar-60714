import importlib.util, itertools, json
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
d=12; A=[3,2,1,0]; B=[0,1,2,3]
def build_clean(perms):
    c=[0]*d
    for i in range(4):
        for s in range(3): sh=4*perms[i][s]; c[3*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
    return c
# best clean-6174x3 rule (99.98%), fixes 617461746174
R_clean=build_clean([(0,1,2),(2,1,0),(2,1,0),(1,2,0)])
F_clean=617461746174
# the universal scramble rule, fixes 666141417774 (100%)
e=json.load(open('/Users/clayelmore/Downloads/d16_1467_test/m3_verified_universals.json'))[0]
R_scr=eng.coefs_from_invs(e['pi_inv'],e['sigma_inv'],d)
F_scr=K_apply(R_scr,sdd(int('111444666777'),d))

def admissible():
    for combo in itertools.combinations_with_replacement(range(10),d):
        c=Counter(combo)
        if len(c)==1: continue
        yield int(''.join(map(str,sorted(combo,reverse=True))))
ADM=list(admissible())

def fate(c,F,n,cap=300):
    cur=n; seen=[]
    while cur!=F:
        if cur==0: return ('ZERO',None)
        if cur in seen: 
            i=seen.index(cur); return ('CYCLE', tuple(seen[i:]))
        seen.append(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return ('CAP',None)
    return ('FP',None)

# 1) leaks under R_clean
leaks=[]; cycles=Counter()
for n in ADM:
    f,info=fate(R_clean,F_clean,n)
    if f!='FP':
        leaks.append((n,f,info))
        if f=='CYCLE': cycles[info]+=1
print(f"R_clean (fixes {F_clean}): {len(ADM)-len(leaks)}/{len(ADM)} reach F; {len(leaks)} leak")
print(f"  distinct terminal cycles: {len(cycles)}")
for cyc,cnt in cycles.most_common():
    print(f"   cycle period {len(cyc)} (basin {cnt}): {cyc}")
    for m in cyc: print(f"      member {m}  digits {dict(sorted(Counter(str(m).zfill(d)).items()))}")
# the leaking start multisets
print(f"  sample leaking inputs: {[x[0] for x in leaks[:10]]}")

# 2) how does R_scr handle those same leaking inputs?
print(f"\nR_scr (fixes {F_scr}): does it have ANY cycle over all admissible?")
scr_leaks=0; scr_cyc=Counter()
for n in ADM:
    f,info=fate(R_scr,F_scr,n)
    if f!='FP':
        scr_leaks+=1
        if f=='CYCLE': scr_cyc[info]+=1
print(f"  R_scr leaks: {scr_leaks}  (cycles: {len(scr_cyc)})  -> {'UNIVERSAL (no cycles)' if scr_leaks==0 else 'has leaks'}")
print(f"  the {len(leaks)} R_clean-leaking inputs under R_scr all reach F_scr?",
      all(fate(R_scr,F_scr,x[0])[0]=='FP' for x in leaks))
