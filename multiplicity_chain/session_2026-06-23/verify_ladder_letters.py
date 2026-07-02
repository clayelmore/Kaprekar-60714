"""Expands every row of Appendix F's letter table to coefficients and checks it equals
the Section-4 ladder exactly (the check that would have caught the crossed even rungs)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def ladder_c(d):
    if d%2: c=[9900,9,90,-9000,-999]; L=5
    else:   c=[9900,9,90,-9000,99000,-99999]; L=6
    while L<d: L+=2; c += [9*10**(L-2), -9*10**(L-2)]
    return c

TABLE = {
 5:("adcbe","deacb"), 6:("eadcbf","fdeacb"), 7:("fgadcbe","gfdeacb"),
 8:("gheadcbf","hgfdeacb"), 9:("hifgadcbe","ihgfdeacb"), 10:("ijgheadcbf","jihgfdeacb"),
 11:("jkhifgadcbe","kjihgfdeacb"), 12:("klijgheadcbf","lkjihgfdeacb"),
 13:("lmjkhifgadcbe","mlkjihgfdeacb"), 14:("mnklijgheadcbf","nmlkjihgfdeacb"),
 15:("nolmjkhifgadcbe","onmlkjihgfdeacb"), 16:("opmnklijgheadcbf","ponmlkjihgfdeacb"),
 17:("pqnolmjkhifgadcbe","qponmlkjihgfdeacb"), 18:("qropmnklijgheadcbf","rqponmlkjihgfdeacb"),
 19:("rspqnolmjkhifgadcbe","srqponmlkjihgfdeacb"), 20:("stqropmnklijgheadcbf","tsrqponmlkjihgfdeacb"),
}
ok=True
for d,(pi,sg) in sorted(TABLE.items()):
    ppos={ch:k for k,ch in enumerate(pi)}; spos={ch:k for k,ch in enumerate(sg)}
    c=[10**(d-1-ppos[chr(97+i)])-10**(d-1-spos[chr(97+i)]) for i in range(d)]
    good = c==ladder_c(d)
    # fixed-point evaluation: a=7,b=6,c=4,d=1, rest 0
    s=[7,6,4,1]+[0]*(d-4)
    pv=sum(10**(d-1-k)*s[ord(pi[k])-97] for k in range(d))
    sv=sum(10**(d-1-k)*s[ord(sg[k])-97] for k in range(d))
    fp = (pv==71460 and sv==10746 and abs(pv-sv)==60714)
    print(f"d={d:2d}: coefficients match ladder: {good}   pi.s={pv} sg.s={sv} K={abs(pv-sv)} fixed: {fp}")
    ok &= good and fp
print("ALL ROWS CORRECT" if ok else "MISMATCH FOUND"); sys.exit(0 if ok else 1)
