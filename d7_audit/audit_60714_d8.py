#!/usr/bin/env python3
"""
audit_60714_d8.py
=================
Quick exhaustive audit of 60714's coefficient-preserving lifting at d=8
(EVEN ladder).

For the constructed even-ladder rule K_60714^(8) at d=8:
  coefs = (9900, 9, 90, -9000, 99000, -99999, 90000000, -90000000)

The d=8 rule is built by appending one zero-sum pair to the d=6 split-lifted
root (positions 4,5 hold the split coefs 99000 / -99999; the new pair at
positions 6,7 holds 9*10^7 / -9*10^7). All trailing-zero positions of F=60714
absorb the appended coefficients without affecting K(F)=F.

The script exhaustively iterates all 24,210 admissible (non-repdigit,
non-near-repdigit) digit multisets at d=8 and records:

  - fate of each: reaches 60714, reaches 0 (escape class), enters cycle, timeout
  - basin density (fraction reaching 60714)
  - step-1 escape class size: predicted |E_8^(1)| = 45 by Lemma 5.5
    (same as d=7 because k = 1 + (8-6)/2 = 2 = k at d=7)
  - max reaching time among successes
  - reaching-time histogram
  - sample trajectories

This is a complementary "Run A2" to audit_60714_d7.py — same fast scope
(~6-10 seconds) but along the even ladder instead of the odd ladder. Useful
data point: d=6, d=8, d=10... basin decay is what Theorem 5.2 predicts
along the even ladder; this audit gives the d=8 number.

Output:
  - audit_60714_d8.json — structured results
  - prints summary to stdout

Usage:
  python3 audit_60714_d8.py
"""

import sys
import json
import time
from collections import Counter
from math import comb

import kaprekar_core as kc


D = 8


def is_block_aligned_d8(ms_desc):
    """Block-aligned multiset at d=8 on the even ladder (Definition 5.2).

    At d=8 (even ladder), d_0 = 6; one base block of size 6 plus one
    appended pair of size 2.
      Base block: positions 0..5, all equal
      Appended pair: positions 6,7 equal
    So ms = (a,a,a,a,a,a, b,b) for some a, b in 0..9.
    """
    return (
        ms_desc[0] == ms_desc[1] == ms_desc[2] == ms_desc[3]
        == ms_desc[4] == ms_desc[5]
        and ms_desc[6] == ms_desc[7]
    )


def main():
    print("=" * 60)
    print("audit_60714_d8.py — Run A2 (even ladder)")
    print("60714 even-ladder lifted rule at d=8")
    print("=" * 60)
    print()

    coefs = kc.coefs_60714_odd_ladder(D)
    print(f"Coefficient vector at d=8: {coefs}")
    print()

    # Direct K(60714) = 60714 verification
    F_padded = (7, 6, 4, 1, 0, 0, 0, 0)
    val, nxt = kc.step_python(F_padded, D, coefs)
    if val != 60714 or nxt != F_padded:
        print(f"FATAL: K(60714 padded) = {val}, sorted-desc {nxt}")
        print(f"       expected 60714 fixed at {F_padded}")
        sys.exit(1)
    print(f"K({''.join(str(x) for x in F_padded)}) = {val}  [fixed point confirmed]")
    print()

    # Build admissibles
    print("Enumerating admissibles at d=8...")
    admissibles = kc.build_admissible_multisets(D)
    print(f"  {len(admissibles):,} admissible multisets")
    print()

    # Iterate all
    print("Iterating K on every admissible (max 80 steps)...")
    t0 = time.time()
    fate_counts = Counter()
    step_hist = Counter()
    reaches_60714 = []
    reaches_0 = []
    other = []
    for ms in admissibles:
        val, n, fate = kc.trace_python(ms, D, coefs, max_steps=80)
        fate_counts[fate] += 1
        if fate == 'fixed_60714':
            reaches_60714.append((ms, n))
            step_hist[n] += 1
        elif fate == 'fixed_0':
            reaches_0.append((ms, n))
        else:
            other.append((ms, n, fate))
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.2f}s")
    print()

    n_total = len(admissibles)
    n_60714 = fate_counts['fixed_60714']
    n_0 = fate_counts['fixed_0']
    basin = n_60714 / n_total
    print(f"Basin: {n_60714:,} / {n_total:,} = {basin:.6f}")
    print(f"  reach 60714 : {n_60714:,}")
    print(f"  reach 0     : {n_0:,}")
    if other:
        print(f"  other       : {len(other):,}")
        for ms, n, fate in other[:5]:
            print(f"      {ms}  fate={fate}  steps={n}")
    print()

    # Step-1 escape class — predicted by Lemma 5.5
    # |E_d^(1)| = C(10 + k - 1, k) - 10 with k = 1 + (d - d0)/2
    # d=8, d_0=6 => k = 1 + 1 = 2
    # |E_8^(1)| = C(11, 2) - 10 = 55 - 10 = 45 (same as d=7 by coincidence of k)
    pred_E1 = comb(11, 2) - 10
    step_1_inputs = [(ms, n) for ms, n in reaches_0 if n == 1]
    # Some "reaches_0" might be admissible block-aligned multisets that collapse in step 1
    # We measure |E_8^(1)| as: admissibles that map to 0 in exactly one step under K.
    actual_E1 = sum(1 for ms in admissibles
                    if kc.step_python(ms, D, coefs)[0] == 0)
    print(f"Step-1 escape class |E_8^(1)|:")
    print(f"  predicted (Lemma 5.5):  {pred_E1}")
    print(f"  observed (exhaustive):  {actual_E1}")
    if pred_E1 == actual_E1:
        print("  MATCH ✓")
    else:
        print(f"  MISMATCH — investigate")
    print()

    # All inputs reaching 0 (full escape class E_8) - those reaching 0 in any number of steps
    print(f"Full escape class |E_8| at d=8 (admissibles reaching 0 in any # steps): {n_0}")
    if n_0 > 0:
        max_e_steps = max(n for _, n in reaches_0)
        print(f"  max steps to 0: {max_e_steps}")
        # Show distribution of steps-to-0
        e_step_hist = Counter(n for _, n in reaches_0)
        print(f"  steps-to-0 histogram: {dict(sorted(e_step_hist.items()))}")
    print()

    # Reaching-time histogram for successes
    if step_hist:
        max_t = max(step_hist.keys())
        min_t = min(step_hist.keys())
        print(f"Reaching-time histogram (60714 successes): max steps = {max_t}")
        for n in sorted(step_hist.keys()):
            bar = '#' * min(60, step_hist[n] // max(1, max(step_hist.values()) // 60))
            print(f"  {n:>3}: {step_hist[n]:>6} {bar}")
    print()

    # Sample trajectories
    print("Sample trajectories (first 5 admissibles):")
    for ms in admissibles[:5]:
        traj = [ms]
        cur = ms
        for _ in range(40):
            val, nxt = kc.step_python(cur, D, coefs)
            traj.append(nxt)
            if nxt == cur:
                break
            cur = nxt
        as_int = lambda t: int(''.join(str(x) for x in t))
        print(f"  {as_int(traj[0]):>7} -> " +
              " -> ".join(str(as_int(t)) for t in traj[1:]))
    print()

    # Block-aligned check
    block_aligned_admissibles = [ms for ms in admissibles if is_block_aligned_d8(ms)]
    print(f"Block-aligned admissibles at d=8: {len(block_aligned_admissibles)}")
    print(f"  (predicted to be the step-1 escape class)")
    # Verify all block-aligned admissibles reach 0 in 1 step
    n_match = sum(1 for ms in block_aligned_admissibles
                  if kc.step_python(ms, D, coefs)[0] == 0)
    print(f"  block-aligned admissibles that map to 0 in 1 step: {n_match}/{len(block_aligned_admissibles)}")
    print()

    # Save results
    # Build proper sample-trajectory data
    def build_traj(ms):
        traj = [list(ms)]
        cur = ms
        for _ in range(60):
            val, nxt = kc.step_python(cur, D, coefs)
            traj.append(list(nxt))
            if nxt == cur:
                break
            cur = nxt
        as_int = lambda t: int(''.join(str(x) for x in t))
        return {
            'start_int': as_int(ms),
            'start_multiset': list(ms),
            'steps_taken': len(traj) - 1,
            'final_int': as_int(traj[-1]),
            'trajectory_ints': [as_int(t) for t in traj],
        }
    sample_traj = [build_traj(ms) for ms in admissibles[:5]]

    out = {
        'meta': {
            'script': 'audit_60714_d8.py',
            'd': D,
            'coefs': list(coefs),
            'pi': [4, 1, 2, 3, 5, 0, 6, 7],
            'sigma': [2, 0, 1, 4, 3, 5, 7, 6],
            'fixed_point': 60714,
            'F_sorted_desc': list(F_padded),
            'wall_time_seconds': round(elapsed, 3),
        },
        'admissibles_total': n_total,
        'fate_counts': dict(fate_counts),
        'basin_60714': basin,
        'n_reach_60714': n_60714,
        'n_reach_0': n_0,
        'step1_escape_predicted': pred_E1,
        'step1_escape_observed': actual_E1,
        'step1_escape_match': pred_E1 == actual_E1,
        'reaching_time_max': max(step_hist.keys()) if step_hist else 0,
        'reaching_time_histogram': {str(k): v for k, v in sorted(step_hist.items())},
        'escape_steps_histogram': {
            str(k): v for k, v in
            sorted(Counter(n for _, n in reaches_0).items())
        },
        'block_aligned_admissibles': len(block_aligned_admissibles),
        'block_aligned_collapse_to_0_in_1_step': n_match,
        'sample_trajectories': sample_traj,
    }

    out_path = 'audit_60714_d8.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")
    print()

    # Final summary
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  basin density at d=8         : {basin:.6f}  ({n_60714:,}/{n_total:,})")
    print(f"  step-1 escape class match    : {pred_E1 == actual_E1}  ({pred_E1} predicted, {actual_E1} observed)")
    print(f"  full escape class size |E_8| : {n_0}")
    print(f"  max reaching time            : {max(step_hist.keys()) if step_hist else 0}")
    print(f"  cycles / timeouts            : {len(other)}")
    print()


if __name__ == '__main__':
    main()
