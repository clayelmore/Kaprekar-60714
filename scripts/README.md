# Reproducibility scripts

Reproducibility scripts for the exhaustive enumerations, cross-dimensional verifications, and audits referenced in [the paper](../paper.md).

Pure Python 3 (≥ 3.8), no external dependencies. Runs on commodity hardware.

[← Back to repo root](..)

---

## Scripts at a glance

| Script | Purpose | Paper reference | Runtime |
|---|---|---|---|
| [`classify_at_d.py`](classify_at_d.py) | Classification of universal full-variable fps at digit length $`d`$ | [§3, Theorems 3.1–3.4](../sections/03_classifications.md) | $`d \leq 5`$: seconds; $`d = 6`$: ~5–10 min |
| [`cross_check_d5_to_d6.py`](cross_check_d5_to_d6.py) | Theorem 4.1: the 33 $`d=5`$ fps tested at $`d=6`$ | [§4](../sections/04_cross_check.md) | ~30 min |
| [`verify_60714_ladder.py`](verify_60714_ladder.py) | Explicit construction of 60714's lifting family at $`d = 5`$ to $`d = 100`$. Verifies the **fixed-point equation** $`K(60714) = 60714`$ at each $`d`$. | [§5.2, Appendix B](../sections/05_theorem_60714.md) | < 1 s |
| [`verify_60714_basin.py`](verify_60714_basin.py) | **Basin verifier** for the 60714 ladder: iterates every admissible multiset at $`d`$ and reports basin coverage, escape class size, and verifies the block-aligned characterization. Distinct from `verify_lemma_5_2.py`. | [§5.2, Theorem 5.2](../sections/05_theorem_60714.md) | $`d = 7`$: ~3 s; $`d = 8`$: ~30 s; $`d = 9`$: ~5 min |
| [`verify_lemma_5_2.py`](verify_lemma_5_2.py) | Finite-state reaching-time bound for entry into the tail-2-zeros set $`T_d`$ (NOT basin universality — see `verify_60714_basin.py` for that). Covers the low-d cases. | [§5.5.1, Proposition 5.2](../sections/05_theorem_60714.md) | ~5 min |
| [`verify_even_ladder_closure.py`](verify_even_ladder_closure.py) | One-step $`T_d`$ closure on the even ladder at $`d \geq 18`$. Confirms the algebraic argument of Lemma C.4. | [§C.5, Lemma C.4](../sections/C_support_lemmas.md) | $`d = 18`$: ~30 s; $`d = 20`$: ~3 min |
| [`verify_case2_recovery.py`](verify_case2_recovery.py) | Lemma C.10 (admissibility recovery for Case 2 inputs): every Case 2 input at $`d \in [7, 30]`$ reaches $`60714`$, with admissible-projection recovery in $`\leq 2`$ iterations. | [§C.6, Lemma C.5 / C.10](../sections/C_support_lemmas.md) | $`d \leq 20`$: ~30 s; full $`d \leq 30`$: ~2 min |
| [`audit_6174_d8_d9.py`](audit_6174_d8_d9.py) | 6174 coefficient-preserving lifting audit at $`d = 8, 9`$ | [§6.2, Theorem 6.1, Appendix E](../sections/06_thread_7641.md) | $`d = 8`$: ~3 min; $`d = 9`$: ~60 min |

---

## Reproducing the paper's main theorems

### Theorem 3.1 ($`d = 3`$: 0 universal fps)

```bash
python3 classify_at_d.py 3
```

### Theorem 3.2 ($`d = 4`$: 4 universal fps)

```bash
python3 classify_at_d.py 4
```

### Theorem 3.3 ($`d = 5`$: 33 universal fps)

```bash
python3 classify_at_d.py 5 --save
```

### Theorem 3.4 ($`d = 6`$: 506 universal fps)

```bash
python3 classify_at_d.py 6 --save-txt
```

This produces `d6_fps.txt` (the supplementary file already in the repo at [`../d6_fps.txt`](../d6_fps.txt)). Runtime: ~5–10 minutes. The 506 count excludes the trivial fixed point $`F = 0`$ (cf. paper §2 convention).

The `--save` and `--save-txt` flags can be combined to produce both JSON and text output.

### Theorem 4.1 (exactly one $`d = 5`$ fp extends to $`d = 6`$)

```bash
python3 cross_check_d5_to_d6.py
```

### Theorem 5.2 (60714 universal at every $`d \geq 5`$)

The corrected Theorem 5.2 has three parts (algebraic at all d, strict-universal at d = 5, 6, near-universal at d ≥ 7 with characterized escape class). Four verification steps:

```bash
python3 verify_60714_ladder.py 20             # algebraic part: K(60714) = 60714 at each d
python3 verify_lemma_5_2.py                   # bounded reaching time to T_d (low d)
python3 verify_even_ladder_closure.py 18      # one-step T_d closure on even ladder, d=18 (~30 s)
python3 verify_even_ladder_closure.py 20      # exhaustive at d=20 (~3 min)
python3 verify_case2_recovery.py              # Lemma C.10: Case 2 admissibility recovery (~30 s)
python3 verify_60714_basin.py 7               # basin universality + escape class characterization
python3 verify_60714_basin.py 8               # repeat at higher d
```

`verify_60714_ladder.py` covers the algebraic claim (part 1). `verify_lemma_5_2.py` covers the low-d finite-state reaching-time bound. `verify_even_ladder_closure.py` confirms the high-d Lemma C.4 algebraic argument empirically. `verify_60714_basin.py` is the **basin verifier**: it directly iterates every admissible multiset at the given d, reports the basin fraction (1.0 at d = 5, 6; below 1 at d ≥ 7), and confirms that all step-1 escape inputs are exactly the block-aligned multisets characterized by Definition 5.2.

### Theorem 6.1 (6174 cross-dimensional pattern)

```bash
python3 audit_6174_d8_d9.py 8   # verifies best basin = 0.998141, 45 escapes
python3 audit_6174_d8_d9.py 9   # verifies best basin = 0.999073, 45 escapes
```

---

## Input/output conventions

- All scripts take digit length `d` as a command-line argument when relevant.
- Save flags (e.g., `--save`, `--save-txt`) write files to the current directory.
- Stdout output is human-readable; stderr is reserved for progress messages.

## Notes on near-repdigit exclusion

All scripts use the paper's admissibility convention: a $`d`$-digit multiset is **admissible** if it is neither a repdigit (all digits equal) nor a near-repdigit (one digit appearing $`d - 1`$ or $`d`$ times). This follows standard practice in Kaprekar-routine analysis and is explained in [§2.1](../sections/02_framework.md) and §5.6 of the paper.

## Notes on `classify_at_d.py` methodology

The classification script combines two phases:

1. **Candidate-filtering phase.** For each digit multiset, the script tests whether at least one rule fixes it. This phase uses a sampling heuristic that scales tractably to $`d = 6`$ (which has 5,005 multisets and 190,800 full-variable rules).
2. **Full-basin verification phase.** For each candidate fixed point identified in phase 1, the script tests every full-variable rule for universality (basin = 1) by iterating every admissible input.

For $`d \leq 5`$, the classification was independently cross-verified against a sound enumeration that does not use the candidate-filtering heuristic (every multiset is exhaustively tested). The results agree exactly.

For $`d = 6`$, the count of 506 universal fixed points was independently verified against three sources: (i) a 3-day exhaustive enumeration on consumer hardware, (ii) the supplementary file `d6_fps.txt`, and (iii) a no-shortcut sound enumeration. All three sources agree.

---

## Licensing

Code is released into the public domain for reproducibility purposes. Please cite the paper if this code contributes to derivative work.
