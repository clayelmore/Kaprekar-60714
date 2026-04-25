# Dimension-Transcendent Attractors in Generalized Kaprekar Routines

Paper draft and reproducibility code for the result that **60714 is a universal full-variable fixed point at every digit length $d \geq 5$** — the first rigorously dimension-transcendent attractor in the generalized Kaprekar family.

---

## Quick links

📄 **[Read the full paper →](paper.md)**

📊 **[Browse the 506 fixed points at $d = 6$ →](d6_fps.txt)**

⚙️ **[Run the reproducibility scripts →](scripts/)**

---

## Table of contents

The full paper is in [`paper.md`](paper.md). For easier navigation, individual sections are also linked below.

### Main text

| Section | Link | Topic |
|---|---|---|
| §1 | [Introduction](sections/01_introduction.md) | Kaprekar's routine, middle-digit cancellation at odd $d$, and the organizing question |
| §2 | [Framework](sections/02_framework.md) | Permutation-pair rules, algebraic rank, universal fixed points, native digit length |
| §3 | [Classifications at $d \leq 6$](sections/03_classifications.md) | Theorems 3.1–3.4: exhaustive classification yielding 0, 4, 33, 506 universal fps |
| §4 | [Cross-check $d = 5 \to d = 6$](sections/04_cross_check.md) | Theorem 4.1: of the 33 fps at $d = 5$, only 60714 transcends |
| §5 | [The 60714 theorem](sections/05_theorem_60714.md) | Theorem 5.2: 60714 is universal at every $d \geq 5$ |
| §6 | [The {7,6,4,1} thread](sections/06_thread_7641.md) | 60714 vs 6174 vs 60417 vs 1746; the `sum_locked_spans` invariant |
| §7 | [Open questions](sections/07_open_questions.md) | Conjectures and directions for further work |

### Appendices

| Appendix | Link | Topic |
|---|---|---|
| A | [Classification tables](sections/A_classification_tables.md) | Per-$d$ enumeration data, fixed-point catalogues |
| B | [60714 ladder construction](sections/B_60714_ladder.md) | Coefficient-preserving liftings through $d = 20$ |
| C | [Support lemmas for Theorem 5.2](sections/C_support_lemmas.md) | Core non-negativity, $T_d$ closure, $d = 15$ algebraic hinge |
| D | [Transcendent fps at $d = 7$](sections/D_dF7_observations.md) | 22-fp audit (10 Case 1 + 11 Case 2 + 1 NEAR-edge) |
| E | [6174 audit at $d = 8, 9$](sections/E_6174_audit.md) | The 45-input escape class characterized |

---

## The main result

**Theorem (60714 is dimension-transcendent).** *The integer $F = 60714$ is a universal full-variable fixed point at every digit length $d \geq 5$ under an explicit family of permutation-pair rules connected by a coefficient-preserving lifting recipe.*

The paper establishes four theorems:

| | Statement |
|---|---|
| **Theorems 3.1–3.4** | Exhaustive classification of universal full-variable fixed points at $d = 3, 4, 5, 6$ — yielding $0, 4, 33, 506$ fps respectively |
| **Theorem 4.1** | Of the $33$ universal fps at $d = 5$, exactly one ($60714$) also universalizes at $d = 6$ |
| **Theorem 5.2** | $60714$ is universal at every $d \geq 5$ via the explicit lifting family of §5 |
| **Theorem 6.1** | The classical Kaprekar fp $6174$ has a characterized cross-dimensional pattern: strict at $d = 4$, algebraic obstruction at $d = 5$, dynamic obstruction at $d = 6$, near-universal with monotonically improving basin at $d = 7, 8, 9$ |

---

## Reproducibility

All exhaustive claims in the paper have corresponding Python scripts in [`scripts/`](scripts/). Pure Python 3 (≥ 3.8), no external dependencies.

| Script | Reproduces | Runtime |
|---|---|---|
| [`classify_at_d.py`](scripts/classify_at_d.py) | Theorems 3.1–3.4 (classification) | $d = 5$: ~5 s · $d = 6$: ~5–10 min |
| [`cross_check_d5_to_d6.py`](scripts/cross_check_d5_to_d6.py) | Theorem 4.1 ($d = 5 \to d = 6$) | ~30 min |
| [`verify_60714_ladder.py`](scripts/verify_60714_ladder.py) | Theorem 5.2 (60714 lifting through $d = 20$) | < 1 s |
| [`verify_lemma_5_2.py`](scripts/verify_lemma_5_2.py) | Proposition 5.2 (finite-state $T_d$ verification) | ~5 min |
| [`audit_6174_d8_d9.py`](scripts/audit_6174_d8_d9.py) | Theorem 6.1, parts 5 & 6 | $d = 8$: ~3 min · $d = 9$: ~60 min |

Run any script with `python3 scripts/<script>.py` and `--help` for options.

To regenerate the [`d6_fps.txt`](d6_fps.txt) supplementary file (already in the repo):

```bash
python3 scripts/classify_at_d.py 6 --save-txt
```

This produces `d6_fps.txt` with one line per fixed point, including zero-digit count, multiset, and rule count. The `--save` flag additionally produces a richer JSON file (`d6_classification.json`).

---

## The d6_fps.txt supplementary file

[`d6_fps.txt`](d6_fps.txt) lists all $506$ universal full-variable fixed points at $d = 6$, with metadata per fp:

```
# d6_fps.txt — Universal full-variable fixed points at d=6
# Total: 506 fps, 1174 universal rules
#
# Zero-digit stratification:
#   0 zeros: 205 fps
#   1 zeros: 240 fps
#   2 zeros:  53 fps
#   3 zeros:   8 fps
#
# Format: <F> zeros=<count> multiset=<sorted-asc-string>
#
    252  zeros=3  multiset=000225  n_rules=2
   2520  zeros=3  multiset=000225  n_rules=2
   4545  zeros=2  multiset=004455  n_rules=2
   ...
```

The $506$ count excludes the trivial fixed point $F = 0$ (cf. [§2 convention](sections/02_framework.md)).

---

## Status

Pre-submission revision complete. All five pre-submission items resolved:

1. ✓ §4 Tables 4.1 & 4.2 filled with all 32 dimension-locked fps at $d = 5$ ([§4](sections/04_cross_check.md))
2. ✓ $d = 15$ odd-ladder hinge argument strengthened ([Appendix C](sections/C_support_lemmas.md))
3. ✓ All 22 TRANS fps at $d_F = 7$ documented ([Appendix D](sections/D_dF7_observations.md))
4. ✓ `sum_locked_spans` invariant honestly characterized — within-thread only ([§6](sections/06_thread_7641.md))
5. ✓ `d6_fps.txt` generated ([here](d6_fps.txt))

---

## Citation

*(To be filled in upon submission.)*
