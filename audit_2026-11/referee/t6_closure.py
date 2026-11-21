# Independent closure: Phi computed via RAW K_d on (nonzero digits + zeros), d = max(n+1,7). Seeds: <=5 nines, <=15 other nonzero digits.
from ref import *
import sys
def phi(N):   # N: descending tuple of nonzero digits
    d=max(len(N)+1,7); s=N+(0,)*(d-len(N)); v=K(s)
    return tuple(sorted((int(ch) for ch in str(v) if ch!='0'),reverse=True))
T=(7,6,4,1); assert phi(T)==T
memo={T:0}; seeds=0; mxs=0; mxsize=0; mxex=None; fails=0
def run(N):
    global mxs,mxsize,mxex,fails
    path=[]; onpath=set(); x=N
    while x not in memo:
        if x in onpath or len(x)==0: fails+=1; print("FAIL",N,x); return
        path.append(x); onpath.add(x)
        if len(x)>mxsize: mxsize=len(x); mxex=x
        x=phi(x)
    b=memo[x]
    for p in reversed(path): b+=1; memo[p]=b
    if memo[N]>mxs: mxs=memo[N]
for u in range(0,16):
    for R in itertools.combinations_with_replacement(range(8,0,-1),u):
        for t in range(0,6):
            if t+u==0: continue
            seeds+=1; run((9,)*t+R)
print(f"seeds={seeds} fails={fails} states={len(memo)} maxsteps={mxs} maxsize={mxsize} ex={mxex}")
# length-independence spot check (Lemma 3): same nonzero digits, different zero padding
random.seed(3); keys=random.sample(list(memo),20000); bad=0
for N in keys:
    for pad in (1,2,5,17):
        d=len(N)+pad
        if d<7: continue
        s=N+(0,)*pad; v=K(s)
        if tuple(sorted((int(ch) for ch in str(v) if ch!='0'),reverse=True))!=phi(N): bad+=1
print("Lemma 3 padding-independence mismatches:",bad)
# states of size 20 visited that are NOT seeds
print("visited states with size 20:",sum(1 for k in memo if len(k)==20), " visited non-seed states:",len(memo)-seeds)
