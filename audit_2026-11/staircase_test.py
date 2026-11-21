#!/usr/bin/env python3
"""Are 'staircase' digit sets (neighboring sorted digits at most 1 or 2 apart, counting the step down to 0)
over-represented among surviving endpoint digit sets?  Baseline: every multiset of nonzero digits with the same
number of digits and digit sum a multiple of 9 (required of any endpoint).  2026-11-21"""
import csv, itertools, random
from collections import Counter, defaultdict
cnt=Counter(r['nonzero_digits'] for r in csv.DictReader(open('catalog_n7_to14.tsv'),delimiter='\t'))
def maxgap(t):
    d=[int(x) for x in t]+[0]; return max(d[i]-d[i+1] for i in range(len(d)-1))
allsets=defaultdict(list)
for k in range(2,10):
    for c in itertools.combinations_with_replacement(range(1,10),k):
        if sum(c)%9==0: allsets[k].append(''.join(map(str,sorted(c,reverse=True))))
surv=defaultdict(list)
for t in cnt: surv[len(t)].append(t)
random.seed(7)
for thr in (1,2,3):
    print(f"\n== staircase = largest step <= {thr}")
    obs=exp=0
    print('  size  survivors: staircase/total   all possible: staircase/total')
    for k in sorted(allsets):
        s=sum(maxgap(t)<=thr for t in surv[k]); a=sum(maxgap(t)<=thr for t in allsets[k])
        obs+=s; exp+=len(surv[k])*a/len(allsets[k])
        print(f"   {k}      {s:3d}/{len(surv[k]):3d} ({100*s/max(len(surv[k]),1):3.0f}%)        {a:4d}/{len(allsets[k]):4d} ({100*a/len(allsets[k]):3.0f}%)")
    ge=0; T=20000
    for _ in range(T):
        x=sum(sum(maxgap(t)<=thr for t in random.sample(allsets[k],len(surv[k]))) for k in allsets)
        ge+= x>=obs
    rules=sum(cnt[t] for t in cnt if maxgap(t)<=thr)
    print(f"  digit sets: observed {obs} of 436, expected by chance {exp:.1f}, ratio {obs/exp:.2f}, chance of this many or more: {ge}/{T}")
    print(f"  rules on staircase sets: {rules} of {sum(cnt.values())} ({100*rules/sum(cnt.values()):.0f}%)")
# average largest step, survivors vs all, per size
print('\nmean largest step by size (survivors / all):',[(k,round(sum(map(maxgap,surv[k]))/max(len(surv[k]),1),2),round(sum(map(maxgap,allsets[k]))/len(allsets[k]),2)) for k in sorted(allsets)])
# rules per set: do staircase sets carry more rules each?
import statistics
for thr in (2,):
    a=[cnt[t] for t in cnt if maxgap(t)<=thr]; b=[cnt[t] for t in cnt if maxgap(t)>thr]
    print(f'rules per set: staircase median {statistics.median(a)}, mean {statistics.mean(a):.0f};  others median {statistics.median(b)}, mean {statistics.mean(b):.0f}')
