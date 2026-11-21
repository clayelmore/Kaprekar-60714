# Referee check of Steps 3-7 on the reduced (A,w) map, written independently.
import sys
from fractions import Fraction as Fr
def fold(t,b): return max(t,b-1-t)
def state_of_m(m,b):
    n=m-1; x,y,z=n//(b*b),(n//b)%b,n%b
    mu=sorted([fold(x,b),fold(y,b),fold(z,b)],reverse=True)
    return (2*mu[0]-(b-1), mu[1]-mu[2])
def step(s,b):
    A,w=s; m=abs(b*A-(b*b-1)*w)
    return state_of_m(m,b), m
def typ(s,b):
    A,w=s
    if w==0: return 'w0'
    return 'i' if fold(A,b)>=b-w else 'ii'
worst=[]
for b in range(3,int(sys.argv[1])+1):
    # all states arising from some M
    states={state_of_m(m,b) for m in range(1,b**3)}
    assert all(0<=A<=b-1 and 0<=w<=(b-1)//2 and (A-(b-1))%2==0 and 2*w<=A for A,w in states)
    T=(b-1,1)
    maxrun=0; maxtot=0
    for s in states:
        if s==(0,0): continue
        # run of type-(ii) steps from s, verify identity
        seq=[s]; cur=s; run=0
        while typ(cur,b)=='ii':
            cur,_=step(cur,b); seq.append(cur); run+=1
        c=Fr(b+3,4)
        for k in range(1,run):  # triples seq[k-1],seq[k],seq[k+1] with both steps (ii)
            o=lambda t: t[1]-c
            assert o(seq[k+1])+o(seq[k])==-2-2*abs(o(seq[k-1])),(b,seq)
        maxrun=max(maxrun,run)
        # steps from state s to T
        cur=s; t=0
        while cur!=T: cur,_=step(cur,b); t+=1; assert t<10*b
        maxtot=max(maxtot,t)
    bound_doc=Fr(b+3,2)+3
    worst.append((b,maxrun,float(bound_doc),maxtot))
    assert maxrun<=bound_doc
print("b maxrun docbound(b+3)/2+3 max_state_steps_to_T")
for r in worst:
    if r[0]<=40 or r[0]%20==0: print(*r)
print("max run over all b:",max(r[1] for r in worst), "at", [r[0] for r in worst if r[1]==max(x[1] for x in worst)][:5])
