"""
classify_at_d.py
================
Exhaustively classifies universal full-variable fixed points at a given digit length d.

Reproduces the classification theorems (Theorems 3.1-3.4) of the paper:
    d=3: 0 universal full-variable fps (12 rules tested)
    d=4: 4 universal fps, 8 rules (216 rules tested)
    d=5: 33 universal fps, 66 rules (5,280 rules tested)
    d=6: 507 universal fps, 1,288 rules (190,800 rules tested)

Runtime:
    d=3: <1 second
    d=4: ~1 second
    d=5: ~3 seconds
    d=6: ~3 hours (commodity hardware)

Usage:
    python3 classify_at_d.py 5        # runs d=5 classification
    python3 classify_at_d.py 6 --save # runs d=6 and saves results to d6_fps.json
"""

import sys
import json
import time
from itertools import permutations, combinations_with_replacement
from collections import defaultdict, Counter


def build_admissible_multisets(d):
    """Return sorted-descending tuples of admissible multisets at length d.
    Admissible = not a repdigit and not a near-repdigit.
    A multiset is near-repdigit if one digit appears d-1 or d times."""
    multisets = []
    for ms in combinations_with_replacement(range(10), d):
        ms_desc = tuple(sorted(ms, reverse=True))
        cnt = Counter(ms_desc)
        if len(cnt) == 1:
            continue  # repdigit
        if max(cnt.values()) >= d - 1:
            continue  # near-repdigit
        multisets.append(ms_desc)
    return multisets


def apply_rule_multiset(ms_desc, coefs, d):
    """Apply K_{pi,sigma} to a sorted-descending multiset; return new sorted-desc tuple."""
    val = abs(sum(c * x for c, x in zip(coefs, ms_desc)))
    return tuple(sorted((int(c) for c in str(val).zfill(d)), reverse=True))


def iterate_to_fp(ms_desc, coefs, d, budget=80):
    """Iterate K starting from ms_desc; return the fixed-point value or None if cycling."""
    cur = ms_desc
    seen = set()
    for _ in range(budget):
        if cur in seen:
            return None
        seen.add(cur)
        val = abs(sum(c * x for c, x in zip(coefs, cur)))
        nxt = tuple(sorted((int(c) for c in str(val).zfill(d)), reverse=True))
        if nxt == cur:
            return val
        cur = nxt
    return None


def classify(d):
    """Exhaustively classify universal full-variable fps at digit length d.
    Returns dict: {fp: [(pi, sigma, coefs), ...]}"""
    print(f"Classifying at d={d}...", flush=True)
    print(f"Building admissible multisets...", flush=True)
    multisets = build_admissible_multisets(d)
    print(f"  {len(multisets)} admissible multisets", flush=True)
    
    fp_to_rules = defaultdict(list)
    t0 = time.time()
    count = 0
    # Report every ~10% of the total, minimum 100 to avoid spam at small d
    if d <= 4:
        report_interval = 10 ** 9  # never report for small d
    else:
        report_interval = max(100, 10 ** (d - 3) // 10)
    
    for pi in permutations(range(d)):
        for sigma in permutations(range(d)):
            # Full-variable check: pi and sigma must disagree at every position (derangement condition)
            if any(pi[i] == sigma[i] for i in range(d)):
                continue
            count += 1
            if count % report_interval == 0:
                print(f"  {count} rules tested, {time.time()-t0:.0f}s elapsed", flush=True)
            
            coefs = tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))
            
            # Fast filter: iterate from a few scattered inputs to find candidate fp(s)
            step = max(1, len(multisets) // 20)
            candidate_fps = set()
            for i in range(0, len(multisets), step):
                r = iterate_to_fp(multisets[i], coefs, d, budget=30)
                if r is not None and r != 0:
                    candidate_fps.add(r)
            
            # For each candidate, test full basin
            for fp in candidate_fps:
                universal = True
                for ms in multisets:
                    r = iterate_to_fp(ms, coefs, d)
                    if r != fp:
                        universal = False
                        break
                if universal:
                    fp_to_rules[fp].append((pi, sigma, coefs))
    
    elapsed = time.time() - t0
    print(f"\nDone at d={d} in {elapsed:.1f}s", flush=True)
    print(f"  Full-variable rules tested: {count}")
    print(f"  Universal full-variable fps: {len(fp_to_rules)}")
    print(f"  Total universal rules: {sum(len(r) for r in fp_to_rules.values())}")
    
    return fp_to_rules


def main():
    if len(sys.argv) < 2:
        print("Usage: classify_at_d.py <d> [--save]")
        sys.exit(1)
    
    d = int(sys.argv[1])
    save = '--save' in sys.argv
    
    results = classify(d)
    
    # Group by multiset
    by_multiset = defaultdict(list)
    for fp in results.keys():
        ms = ''.join(sorted(str(fp).zfill(d)))
        by_multiset[ms].append(fp)
    
    print("\nFixed points grouped by digit multiset:")
    for ms, fps in sorted(by_multiset.items()):
        print(f"  {ms}: {sorted(fps)}")
    
    if save:
        out_path = f"d{d}_classification.json"
        data = {
            'd': d,
            'total_fps': len(results),
            'total_rules': sum(len(r) for r in results.values()),
            'fps_sorted': sorted(results.keys()),
            'by_multiset': {k: sorted(v) for k, v in by_multiset.items()},
            'per_fp': {
                str(fp): {
                    'n_rules': len(rules),
                    'sample_pi': list(rules[0][0]),
                    'sample_sigma': list(rules[0][1]),
                    'sample_coefs': list(rules[0][2]),
                } for fp, rules in results.items()
            }
        }
        with open(out_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nSaved to {out_path}")


if __name__ == '__main__':
    main()
