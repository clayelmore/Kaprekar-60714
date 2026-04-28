# d7 Outcome Verifier

Purpose: determine the exact d=7 transcendence outcome (TRANS / NEAR / LOCK) for every two-zero d=6 universal sv=6 fixed point.

## What it does

For each of the 52 two-zero d=6 universal fps, the script:

1. **Enumerates every valid sv=7 rule** — all (pi, sigma) permutation pairs at d=7 such that K(F_padded) = F and the coefficient vector has no zero entries. Uses an optimized backtracking enumerator that finds all valid rules in well under a second per fp (vs. minutes for brute-force enumeration).

2. **Computes the exact basin fraction** for every valid rule — no sampling. Uses multiset-memoization: trace every non-repdigit multiset (~11,430 of them at d=7) to its fate, then weight-aggregate. This gives the true basin fraction to full precision, across all 9,999,990 non-repdigit 7-digit inputs.

3. **Classifies the fp** based on the best basin observed:
   - **TRANS**: at least one rule achieves basin ≥ 0.99 (universal modulo quasi-repdigit escapes)
   - **NEAR**: best basin in [0.95, 0.99) — near-universal with a small competing attractor
   - **LOCK**: best basin < 0.95 — substantially sub-universal, dimension-locked

These thresholds match the paper's empirical groupings.

## Validated against known cases

The script was tested against four fps with known verified outcomes:
- F = 60714: best basin 0.998617, 4 rules ≥ 0.99 → TRANS ✓
- F = 146070: best basin 1.000000, 4 rules ≥ 0.99 → TRANS ✓
- F = 170460: best basin 0.917912, 0 rules ≥ 0.99 → LOCK ✓
- F = 607140: best basin 0.999370, 2 rules ≥ 0.99 → TRANS ✓

All four match Clay's earlier memory notes.

## Expected runtime

- Infrastructure setup: ~10 seconds (builds sort-desc table for 10 million integers)
- Per fp runtime: 1-30 seconds depending on rule count (36 to 1632 valid rules per fp)
- Total for all 52 fps: estimated **1-3 hours** on a modern laptop

The script saves progress incrementally to `d7_verified_partial.json` after every fp, so an interruption does not lose work. If restarted, it resumes from the saved checkpoint.

## Outputs

- **`d7_verified_outcomes.json`** — complete per-fp data (best basin, best rule coefs, all statistics)
- **`d7_summary.txt`** — one-line-per-fp summary
- **`d7_classifier_analysis.txt`** — cross-tab of cycle-length signatures vs verified outcomes, testing the partial classifier we identified

## Pre-check

The script optionally reads `d6_graph_data.pkl` (the pickle file from our earlier work) to produce the cycle-classifier cross-tab. If that file isn't in the current directory, the script still produces the full verified-outcome data; it just skips the cross-tab analysis step.

To place `d6_graph_data.pkl` in the script's working directory, copy it from wherever it lives in your Mac's filesystem.

## How to run

```bash
python3 d7_outcome_verifier.py
```

No arguments, no flags. Writes everything to the current directory. Progress prints to stdout.

## What we'll learn

After the run completes, we'll have:

1. **Verified outcomes for all 52 two-zero d=6 fps** — eliminating the current gap where only 27 are individually confirmed and 25 are inferred from paper totals.

2. **Full picture of the long-cycle bucket.** The partial classifier says "cycle signature with all lengths ≤ 3 at d=6 ⇒ LOCK" (verified 12-for-12). The remaining 40 fps (four signatures: (2,4), (6,), (3,4), plus any surprise others) split TRANS/LOCK. We'll see the exact split and can then hunt within it for second-order discriminators that weren't visible in the noisy 27-fp sample.

3. **Confirmation or refutation of the partial classifier.** If any of the 40 currently-unverified fps with all-short-cycle signature turns out to transcend, that's a violation of the classifier and we need to revisit. If none does, the classifier is confirmed on a larger sample.

Once Clay sends back `d7_verified_outcomes.json`, I'll pick up the analysis.
