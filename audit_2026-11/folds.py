#!/usr/bin/env python3
"""Audit 2026-11: rebuild every fold / tower rule from Definition 5.1 and classify the complete
multiset space with the independent C engine (./kap). Usage: folds.py [maxd]"""
import subprocess, sys
maxd = int(sys.argv[1]) if len(sys.argv) > 1 else 24
def fold(c, k):
    d0 = len(c); out = [0]*(k*d0)
    for i in range(d0):
        for j in range(k):
            out[k*i+j] = c[i]*10**(d0*(k-1-j))
    return out
def run(name, c):
    d = len(c)
    if d > maxd: return
    r = subprocess.run(['./kap', str(d)] + [str(x) for x in c], capture_output=True, text=True).stdout
    lines = r.strip().split('\n'); head = lines[0]
    nonrep = int(head.split('nonrep=')[1].split()[0])
    terms = [l.split() for l in lines[1:] if l.strip().startswith(('FIX','CYC'))]
    fx = [(t[2][4:], int(t[3][6:])) for t in terms if t[0]=='FIX' and int(t[3][6:])>0 or (t[0]=='FIX' and t[2]!='val=0')]
    best = max(terms, key=lambda t:int(t[3][6:]))
    nfix = sum(1 for t in terms if t[0]=='FIX' and t[2]!='val=0'); ncyc = sum(1 for t in terms if t[0]=='CYC')
    b = int(best[3][6:])
    print(f"{name:34s} d={d:2d} nonrep={nonrep:>10d} top={best[0]} {best[2][4:]} basin={b} ({100*b/nonrep:.4f}%) maxsteps={best[4][9:]} nonzero_fixed={nfix} cycles={ncyc}" + ("  UNIVERSAL" if b==nonrep else ""), flush=True)
    if nfix > 1 and nfix < 6:
        for t in terms:
            if t[0]=='FIX' and t[2]!='val=0': print("      fixed", t[2][4:], t[3])
R = {'6174':[999,90,-90,-999], '1746':[9,-900,900,-9], '2538':[90,999,-999,-90], '5382':[900,-9,9,-900]}
for n,c in R.items(): run(f"{n} base", c)
for n,c in R.items(): run(f"{n} 2-fold", fold(c,2))
for m in (3,4,5): run(f"interleaved 6174 {m}-fold", fold(R['6174'],m))
for k in (3,4,5,6): run(f"1746 {k}-fold", fold(R['1746'],k))
for n,c in R.items(): run(f"{n} double-double", fold(fold(c,2),2))
for n in ('2538','5382'):
    for k in (3,5): run(f"{n} {k}-fold", fold(R[n],k))
run("60714 native 2-fold", fold([9900,9,90,-9000,-999],2))
m3 = [99999999999,9990000000,999900000,99999000,999900,9990,-99999000,-999900,-9990,-99999999999,-9990000000,-999900000]
run("m=3 rule (666141417774)", m3); run("m=3 rule 2-fold", fold(m3,2))
run("1746 2-fold then 3-fold", fold(fold(R['1746'],2),3))
run("1746 7-fold", fold(R['1746'],7))
run("1746 8-fold (direct)", fold(R['1746'],8))
run("1746 tower level 3", fold(fold(fold(R['1746'],2),2),2))
