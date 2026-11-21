from ref import *
random.seed(5)
# Lemma 1: exhaustive d=6..12 + random: image non9-nonzero count <=15; record max, also record nines beyond borrow
worst=0
for d in range(6,13):
    for s in itertools.combinations_with_replacement(range(9,-1,-1),d):
        c=Counter(img(s)); worst=max(worst,sum(v for g,v in c.items() if g not in(0,9)))
w2=0; ex=None
def adv(d):
    r=random.random()
    if r<0.3:
        k=random.choice([2,3,4,5,7,10]); ds=random.sample(range(10),k); return tuple(sorted((random.choice(ds) for _ in range(d)),reverse=True))
    # many distinct descents: random cut points so that all 9 gaps appear at places >=6 and low digits are messy
    cuts=sorted(random.sample(range(1,d),9)); s=[]; g=9; prev=0
    for cpt in cuts+[d]: s+= [g]*(cpt-prev); prev=cpt; g-=1
    return tuple(s)
for d in (16,21,22,25,30,40,60):
    for _ in range(40000):
        s=adv(d)
        if len(set(s))==1: continue
        c=Counter(img(s)); v=sum(v for g,v in c.items() if g not in(0,9))
        if v>w2: w2=v; ex=(s,img(s))
print("Lemma1 worst non9 nonzero: exhaustive d<=12:",worst," random/adversarial:",w2,ex)
# Lemma 2 exhaustive: all R multisets of digits 1..8 with |R|<=7, plus random bigger, t in 6..13 & 30, z in 0..6
n=0;bad=0; variants=Counter()
def chk(t,R,z):
    global n,bad
    s=tuple([9]*t+list(R)+[0]*z); d=len(s)
    if len(set(s))==1: return
    im=img(s); c=Counter(im); n+=1
    nines=c.get(9,0); zeros=c.get(0,0); rest=sorted((g for g in im if g not in(0,9)),reverse=True)
    if z==0 and R and set(R)=={8}:
        ok=(nines==t-4 and not rest and zeros==d-(t-4)); variants['all8 zero-free']+=1
    else:
        if z>0:
            exp=[8-(R[0] if R else 0)]+[R[i]-R[i+1] for i in range(len(R)-1)]+([R[-1]] if R else [])+[1]
        else:
            exp=[8-R[0]]+[R[i]-R[i+1] for i in range(len(R)-1)]+[1+R[-1]]
        exp=sorted((e for e in exp if e),reverse=True)
        ok=(nines==t-5 and rest==exp and sum(rest)==9 and zeros>=4 and len(rest)<=9)
    if not ok: bad+=1; print("CEX",t,R,z,im)
for u in range(0,8):
    for R in itertools.combinations_with_replacement(range(8,0,-1),u):
        for t in (6,7,8,9,10,11,12,13,30):
            for z in range(0,7): chk(t,R,z)
for _ in range(60000):
    R=tuple(sorted((random.randint(1,8) for _ in range(random.randint(8,40))),reverse=True))
    chk(random.choice([6,7,8,9,10,11,16,50,333]),R,random.choice([0,0,1,2,5,40]))
print("Lemma 2 cases",n,"counterexamples",bad,dict(variants))
# drain iteration: from any t>=6 state, follow until t<=5; check t strictly decreases by 5 (or 4 once), ends 1..5, state has zero, |R|<=9
m=0
for _ in range(20000):
    t=random.randint(6,80); R=tuple(sorted((random.randint(1,8) for _ in range(random.randint(0,20))),reverse=True)); z=random.choice([0,0,1,3])
    s=tuple([9]*t+list(R)+[0]*z)
    if len(set(s))==1: continue
    first=True
    while s.count(9)>=6:
        t0=s.count(9); s2=img(s); t1=s2.count(9)
        assert t1 in (t0-5,t0-4) and (t1==t0-5 or (first and 0 not in s)),(s,s2)
        assert 0 in s2 and s2.count(0)>=4
        s=s2; first=False
    assert 1<=s.count(9)<=5 and sum(1 for g in s if g not in(0,9))<=9 and 0 in s; m+=1
print("drain runs ok:",m)
