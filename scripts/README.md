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
| [`verify_60714_ladder.py`](verify_60714_ladder.py) | Explicit construction of 60714's lifting family at $`d = 5`$ to $`d = 100`$ | [§5.2, Appendix B](../sections/05_theorem_60714.md) | < 1 s |
| [`verify_lemma_5_2.py`](verify_lemma_5_2.py) | Finite-state reaching-time verification for Lemma 5.2 | [§5.5.1, Proposition 5.2](../sections/05_theorem_60714.md) | ~5 min |
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

Two verification steps:

```bash
python3 verify_60714_ladder.py 20     # explicit construction
python3 verify_lemma_5_2.py           # finite-state reaching-time bound
```

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

---

## Licensing

Code is released into the public domain for reproducibility purposes. Please cite the paper if this code contributes to derivative work.
