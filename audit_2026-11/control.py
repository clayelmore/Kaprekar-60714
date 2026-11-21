#!/usr/bin/env python3
"""Control experiment: do RANDOM eligible digit sets (digit sum divisible by 9, not (near-)repdigit) also carry
universal fixed points?  usage: control.py d nsets seed"""
import sys, random, subprocess, itertools
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
d, n, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); random.seed(seed)
el = [t for t in itertools.combinations_with_replacement(range(9,-1,-1), d) if sum(t) % 9 == 0 and sum(t) > 0 and max(Counter(t).values()) < d-1]
pick = random.sample(el, n)
def run(t):
    s = ''.join(map(str, t)); tot = 0; fps = set(); rules = 0
    outs = [subprocess.Popen(['./chain', str(d), s, str(i), '3'], stdout=subprocess.PIPE, text=True) for i in range(3)]
    for p in outs:
        for l in p.stdout:
            if l.startswith('UNIV'): tot += 1; fps.add(l.split()[2])
            elif l.startswith('SUMMARY'): rules += int(l.split('rules=')[1].split()[0])
    return s, rules, tot, len(fps)
hit = 0
with ThreadPoolExecutor(6) as ex:
    for s, rules, tot, nf in ex.map(run, pick):
        hit += tot > 0; print(f"  {s}: fixing rules={rules:>10d} universal rules={tot:>8d} distinct universal fixed points={nf}", flush=True)
print(f"d={d}: {hit} of {n} random eligible digit sets carry a universal fixed point ({len(el)} eligible sets in all)")
