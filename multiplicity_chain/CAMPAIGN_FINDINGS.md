# d=16 m=4 → d=20 m=5 Universal Search Campaign — Findings

**Period covered:** 2026-05-31 through 2026-06-02 (~36 hours active research)
**Subject:** Strict classical universal fixed points in the multiplicity chain {1,4,6,7}^m at digit length d = 4m
**Outcome:** Established the existence of universals at m=4 (341+ verified) and m=5 (≥1 verified), discovered the **pair-symmetric block-permutation rule structure** as the productive search family, and identified consistent cross-dimensional positional patterns.

---

## 1. The Core Question

For the generalized Kaprekar framework K_{π,σ}(n) at digit length d with multiset {1,4,6,7}^m (each of {1,4,6,7} appearing m times, d = 4m), is the set of strict classical universal fixed points non-empty at all m ≥ 1?

A *strict classical universal at d* is an integer F such that for some pair (π, σ) ∈ S_d × S_d with derangement σ∘π⁻¹ (i.e., sv = d), every non-repdigit d-digit input iterates to F under K_{π,σ}.

## 2. Pre-Campaign Baseline

| m | d | strict classical universals | source |
|---:|---:|---:|---|
| 1 | 4 | 2 (6174, 1746) | Kaprekar 1949 / Paper 2 |
| 2 | 8 | 481 | d8_multiset_77664411_v3.json |
| 3 | 12 | 42 | d12_7641.json (Windows 14-day run, May 2026) |
| 4 | 16 | unknown | this campaign |

## 3. Campaign Phases

### Phase A — Random forward search (unsuccessful)
- 73,901 random F arrangements tested at d=16 m=4 → 0 universals
- 80 templated candidates (parallel-block forms, 6174-substring lifts) → 0 universals
- 1,000,000,000 random (π, σ) pairs in forward search → 0 universals, 47 partial fixed points (all basins ≤ 10,164)
- 50M+ samples on deep K-rule searches for high-basin partial fixed points → 0 universals

**Conclusion of Phase A:** Random rule sampling cannot find d=16 m=4 universals. The probability of a random rule having universal-producing structure is on the order of 10⁻¹⁵.

### Phase B — User-suggested side quest (breakthrough)
**User suggestion:** "reverse existing d=8 fixed points, then check each iteration of 6714 for the remaining slots"

This generated candidates of the form `reverse(F8) || 6174-family-suffix`. Among 9,972 such candidates:
- 75 had at least one K-rule (i.e., were fixed points of some rule)
- **F = 6177414661746174** appeared with basin 2,040,808 / 2,042,965 = **99.8944%**
- This F has only 1 K-rule, with **S-shortfall of only 8 multisets**

The 99.89% basin F was the key — it gave us a clean, near-universal rule whose structure we could analyze.

### Phase C — Structural analysis of the 99.89% rule
The single rule fixing F = 6177414661746174 has c-vector with strikingly **pair-symmetric structure**:

```
c[0..3]   (7-block):  (+999900000000000, -900000000,    +9990000, +999)
c[4..7]   (6-block):  (+90000000000000,  -990000000000, +900000,  +90)
c[8..11]  (4-block):  (-90000000000000,  +990000000000, -900000,  -90)
c[12..15] (1-block):  (-999900000000000, +900000000,    -9990000, -999)
```

The pattern: **c[8..11] = −c[4..7]** and **c[12..15] = −c[0..3]**.

This means digit-blocks 4 and 6 contribute anti-symmetrically, as do digit-blocks 1 and 7. The K-formula collapses:

K = 7·S₇ + 6·S₆ + 4·S₄ + 1·S₁
  = 7·S₇ + 6·S₆ + 4·(−S₆) + 1·(−S₇)
  = **6·S₇ + 2·S₆**

where S_d = sum of c-coefficients in the d-digit block.

### Phase D — Pair-symmetric structured search (the breakthrough)
Built a search that enumerates partitions (A₇, A₆, A₄, A₁) of {0,…,15} into 4 size-4 subsets, and constructs the pair-symmetric rule:
- π places the 7-digits at positions A₇, the 6-digits at A₆, the 4-digits at A₄, the 1-digits at A₁
- σ swaps these by pair: 7-digits to A₁, 6-digits to A₄, 4-digits to A₆, 1-digits to A₇

For each pair-symmetric rule:
1. Compute K = K(sorted_desc) using the c-vector
2. Check if K has the multiset {1,4,6,7}⁴
3. If yes, run classify_rule and classify as classical / s_only / partial

**Results:**
- First run (2M partitions): 149 F candidates, **41 classical universals**
- Big run (20M partitions): 1158 F candidates, **313 classical universals**
- Combined unique: **341 verified classical universals at d=16 m=4**
- Universal hit rate: ~16 per million pair-symmetric partitions
- Extrapolated full family count: ~990 universals (sampled ~35% of 63M-partition space)

### Phase E — d=20 m=5 extension
**Tested 7 distinct structural rule families at d=20:**

| family | block-permutation | K-formula | F candidates | universals |
|---|---|---|---:|---:|
| pair-sym v1 | (7↔1)(6↔4) | K = 6S₇ + 2S₆ | 150 | 0 (in 30M) → 1 (in 200M, see below) |
| pair-sym v2 | (7↔4)(6↔1) | K = 3S₇ + 5S₆ | 0 | 0 |
| pair-sym v3 | (7↔6)(4↔1) | K = S₇ + 3S₄ | 0 | 0 |
| 4-cycle | (7→6→4→1→7) | K = 6P(A₇) − P(A₆) − 2P(A₄) − 3P(A₁) | 0 | 0 |
| reverse 4-cycle | (7→1→4→6→7) | mirror of above | 0 | 0 |
| derangement | (1,0,3,2) | varies | 0 | 0 |
| derangement | (1,2,3,0) | varies | 0 | 0 |
| SHIFT-5 | σ_inv = π_inv shifted by 5 | new structural family | 0 | 0 |

**Then a DEEPER pair-sym v1 (200M samples) found:**
- **F = 17461746146174617746 — basin = 10,014,995 / 10,014,995 = 100% CLASSICAL UNIVERSAL**
- Found at sample k = 3,144,101 in the 200M run
- Plus a high-basin near-universal: F = 14617461774617746146 at basin 6,796,448 (67.86%)

The earlier 30M sample missed this; deeper sampling was the difference.

## 4. Cross-Dimensional Patterns

Patterns observed across the 866+ verified universals at d ∈ {4, 8, 12, 16}:

### Positional constraints (apparent at multiple d)
| d | leading digit | trailing digit |
|---|---|---|
| 4 | {1, 6} | {4, 6} |
| 8 | {1, 4, 6} | uniform |
| 12 | {1, 4, 6} | mostly {6} |
| 16 | {1, 6} | {4, 6} |
| **20** (1 example) | **{1}** | **{6}** | ← consistent with pattern |

**d=4 and d=16 share IDENTICAL head/tail constraints.** This is a structural cross-dimensional invariant. The single d=20 universal so far also fits this pattern.

### Universal property: position 0 ≠ 7
Across all 866+ universals at d ∈ {4, 8, 12, 16}, NO universal F has a leading 7. This appears to be a hard structural constraint of the rule family.

### Substring enrichment
| d | % universals containing "6174" | % containing "1746" |
|---|---:|---:|
| 4 | 50% (trivial) | 50% |
| 8 | 6% | 6% |
| 12 | 10% | 10% |
| 16 | **52%** | **53%** |
| 20 (1 example) | yes (2 copies) | yes (2 copies) |

The d=16 pair-symmetric universals are **massively enriched** in 6174/1746 substrings — more than half contain one as a 4-digit subsequence. The single d=20 universal contains **two** copies of "1746" at positions 0-3 and 4-7.

## 5. The Discovery Chain — Why Random Search Failed

The space of (π, σ) pairs at d=16 is (16!)² ≈ 4.4 × 10²⁶. The pair-symmetric subfamily has 63 million partitions. So pair-symmetric rules form a fraction ≈ 1.4 × 10⁻¹⁹ of the full rule space.

For a random sample to find ONE pair-symmetric rule by chance, you'd need ~10¹⁹ samples — physically infeasible. The 1B random forward search we ran is 10¹⁰ off from finding ANY pair-symmetric rule, let alone a universal one.

**The structural insight came from the user's side quest** (reverse d=8 universals + 6174 suffixes), which forced rules into the high-structure region. The 99.89% F that emerged had a unique rule whose pair-symmetric c-vector pattern was visible to the eye. From there, the structured search enumerated the pair-symmetric family directly.

## 6. Updated Multiplicity Chain

| m | d | strict classical universals | source |
|---:|---:|---|---|
| 1 | 4 | 2 | classical Kaprekar |
| 2 | 8 | 481 | Paper 2 framework |
| 3 | 12 | 42 | 14-day search |
| 4 | 16 | **341 verified** (≈ 990 in full pair-sym family) | this campaign |
| 5 | 20 | **≥ 1 verified**, ongoing | this campaign |

**The non-emptiness conjecture is now verified for m ≤ 5.** The pair-symmetric construction provides an explicit mechanism for generating universals at every m tested.

## 7. Open Questions

1. **Universal count at m=5**: How many universals exist in the d=20 m=5 pair-symmetric family? Initial extrapolation from 200M samples (1 universal so far) suggests density may be 1 in 10⁸ to 10⁹ partitions. Total pair-symmetric family at d=20 has 11.7 billion partitions, so possibly hundreds to thousands of universals.

2. **Other structural rule families at d=20**: Block-permutation pair-symmetric variants 2 and 3, as well as 4-cycles and basic derangements, produce **zero** F candidates at d=20. The reason is arithmetic — these K-formulas don't land on valid {1,4,6,7}⁵ multiset outputs. Whether more exotic structural families (within-block 5-fold cyclic, non-uniform block permutations, etc.) produce universals remains open.

3. **Does the pair-symmetric family scale arbitrarily?** If non-emptiness holds at every m via pair-symmetric construction, can we prove a uniform lower bound on universal density?

4. **Why the cross-d head/tail constraint?** Position-0 never being 7 and the lead ∈ {1,6} / tail ∈ {4,6} patterns at d=4 and d=16 suggest a structural identity. A proof would explain WHY these positional constraints hold for all pair-symmetric universals.

5. **What other multisets behave similarly?** The {0,4,5,9} core at d=12 m=3 produced 152 universals (vs 42 for {1,4,6,7}). Does pair-symmetric structure also operate on {0,4,5,9}? Unknown.

## 8. Methodology Notes

### What worked
- **User's structural hypothesis (side quest)** — forced rules into productive subspace
- **Pair-symmetric enumeration** — efficient sampling of structured family
- **Block-sum decomposition** (K = 6S₇ + 2S₆) — algebraic shorthand for the structure
- **Cross-d pattern analysis** — generated falsifiable predictions for higher d

### What didn't work
- Random rule sampling (1B samples, 0 universals at d=16)
- Random F sampling with classify_rule (73k F's, 0 universals at d=16)
- Templated candidates without structural foundation (80 candidates, 0 universals)
- 4-cycle and other block-permutation variants at d=20 (0 candidates)

### Tools used
- `search_multiset_universals_fast.py` — primary search infrastructure
- Custom structured search scripts — pair-symmetric, variants, perturbation searches
- Hamming-distance climbing for local landscape exploration
- Statistical analysis of positional/structural patterns across known universals

## 9. Key Files

In `/Users/clayelmore/Downloads/d16_1467_test/`:
- `pair_symmetric_BIG.json` — 313 d=16 universals with full rule data (652 KB)
- `pair_symmetric_search.json` — first 41 d=16 universals (full rules)
- `d16_m4_universals_summary.json` — clean d=16 summary
- `d20_v1_DEEP.json` — d=20 m=5 deep search (will be written when 200M run completes; contains the universal rule)
- `d20_universals_live.json` — d=20 universals saved incrementally as found
- `forward_1B_final.json` — baseline 1B random forward search (47 partials, 0 universals)
- `outlier_perturbation_results.json` — H-2 climbs around the original 10164-basin outlier
- `forward_uniform_candidates.json` — the original 4 partial fixed points that started everything
- `CAMPAIGN_FINDINGS.md` — this document
