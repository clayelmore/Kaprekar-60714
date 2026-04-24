# Supplementary Code for "Dimension-Transcendent Attractors in Generalized Kaprekar Routines"

This directory contains reproducibility scripts for the exhaustive enumerations,
cross-dimensional verifications, and audit computations referenced in the paper.

All scripts are pure Python 3 (≥ 3.8) with no external dependencies beyond the
standard library. They run on commodity hardware with runtimes ranging from
seconds (small `d`) to a few hours (exhaustive `d = 6` classification).

## Scripts

| Script | Purpose | Paper reference | Runtime |
|---|---|---|---|
| `classify_at_d.py` | Exhaustive classification of universal full-variable fps at digit length $d$ | §3, Theorems 3.1–3.4 | seconds at $d \leq 5$; ~3 hours at $d = 6$ |
| `cross_check_d5_to_d6.py` | Theorem 4.1: the 33 $d=5$ fps tested at $d=6$ | §4 | ~30 minutes |
| `verify_60714_ladder.py` | Explicit construction of 60714's lifting family at $d = 5$ to $d = 100$ | §5.2, Appendix B | <1 second |
| `verify_lemma_5_2.py` | Finite-state reaching-time verification for Lemma 5.2 | §5.5.1, Proposition 5.2 | ~5 minutes total |
| `audit_6174_d8_d9.py` | 6174 coefficient-preserving lifting audit at $d=8, 9$ | §6.2, Theorem 6.1, Appendix E | 3 min (d=8); 60 min (d=9) |

## Reproducing the paper's main claims

### Theorem 3.1 (d=3: 0 fps)
```
python3 classify_at_d.py 3
```

### Theorem 3.2 (d=4: 4 fps)
```
python3 classify_at_d.py 4
```

### Theorem 3.3 (d=5: 33 fps)
```
python3 classify_at_d.py 5 --save
```

### Theorem 3.4 (d=6: 507 fps)
```
python3 classify_at_d.py 6 --save
```
**Warning:** runtime is approximately 3 hours.

### Theorem 4.1 (exactly one d=5 fp extends to d=6)
```
python3 cross_check_d5_to_d6.py
```

### Theorem 5.2 (60714 universal at every d ≥ 5)
Two verification steps:
```
python3 verify_60714_ladder.py 20     # explicit construction
python3 verify_lemma_5_2.py           # finite-state reaching-time bound
```

### Theorem 6.1 (6174 fingerprint)
```
python3 audit_6174_d8_d9.py 8   # verifies best basin = 0.998141, 45 escapes
python3 audit_6174_d8_d9.py 9   # verifies best basin = 0.999073
```

## Input/output conventions

- All scripts take digit length `d` as a command-line argument when relevant.
- Save flags (e.g., `--save`) write JSON files with full classification data.
- Stdout output is human-readable; stderr is reserved for progress messages.

## Licensing

Code is released into the public domain for reproducibility purposes. Please
cite the paper if this code contributes to derivative work.

## Notes on near-repdigit exclusion

All scripts use the paper's admissibility convention: a $d$-digit multiset is
**admissible** if it is neither a repdigit (all digits equal) nor a near-repdigit
(one digit appearing $d - 1$ or $d$ times). This follows standard practice in
Kaprekar-routine analysis and is explained in §2.1 and §5.6 of the paper.
