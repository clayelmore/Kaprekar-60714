# 60714

A five-digit number that's a universal attractor at every digit length d ≥ 5.

Pick any number with five or more digits. Apply the right rule. Watch it converge to **60714** (with a structurally characterized small class of exceptions at d ≥ 7). The rule depends on the input's digit length, but the destination is almost always the same.

This is a generalization of Kaprekar's classical 1949 result, extended in a direction the literature has not explored: instead of fixing the rule and asking which digit lengths work, we let the rule vary with the digit length, and find a single fixed point — 60714 — whose universality holds across infinitely many dimensions simultaneously.

The integer 60714 is one consequence of a more general structural framework. The paper's underlying contributions are the **classification of universal full-variable fixed points at digit length d** (yielding the catalog 0, 4, 33, 506 fps at d ∈ {3, 4, 5, 6}), the **coefficient-preserving lifting recipe** that connects rules across digit lengths, and the **block-aligned escape class** (Definition 5.2) that exactly characterizes when the lifted dynamics fail. 60714 is the unique integer for which this framework produces a cross-dimensional attractor with universally large basin.

---

## ⚡ Try it

**👉 [Open the interactive calculator](60714_calculator.html)**

Type any number 5–20 digits long. The calculator shows the full trajectory, step by step, until convergence.

---

## What's here

| | |
|---|---|
| **[60714_calculator.html](60714_calculator.html)** | Single-file interactive calculator. Open it in any browser. No setup. |
| **[paper.md](paper.md)** | The complete paper: classifications, theorems, proofs, appendices. ~170 KB; if GitHub's math renderer struggles with the size, browse the [section files](#-the-paper-section-by-section) below. |
| **[d6_fps.txt](d6_fps.txt)** | All 506 universal fixed points at d = 6, with metadata. |
| **[scripts/](scripts/)** | Reproducibility scripts for every exhaustive claim in the paper. |

---

## What 60714 actually is

In Kaprekar's classical routine at d = 4, you sort the digits descending, sort them ascending, subtract, and repeat. From every non-repdigit input, you reach **6174** within seven steps.

The trick "stops working" at d = 5 — Kaprekar's specific rule cycles instead of converging. The standard story for 77 years has been: 5-digit Kaprekar doesn't work.

The story changes if you let the rule itself vary. For each digit length d there are many ways to combine sorted-descending and sorted-ascending digits — d! · (d! − 1) ordered permutation pairs, each defining its own iteration rule. Most produce cycles. A small subset converge universally. At d = 6 the count is exactly **506**.

The natural follow-up question: which of these cross-dimensional fixed points persist? If F is universal at d, is it also universal at d + 1, under some related rule?

The answer is mostly no. Of the 33 universal fixed points at d = 5, only one extends to d = 6. That one is **60714**.

What makes 60714 special isn't just that it extends once. It extends to every higher d, with an explicit recipe: each rule is built from the d = 5 rule by appending pairs of coefficients summing to zero at the new digit positions. Theorem 5.2 proves this construction is universal — every admissible input converges — at every d ≥ 5.

The paper proves it through finite-state verification at d ≤ 16 plus a d-independent algebraic argument extending it to all higher d.

---

## 🔗 The four main results

| Theorem | Statement |
|---|---|
| **3.1–3.4** | Exhaustive classification: 0, 4, 33, and 506 universal full-variable fixed points at d = 3, 4, 5, 6 respectively |
| **4.1** | Of the 33 fixed points at d = 5, exactly one (60714) also universalizes at d = 6 |
| **5.2** | 60714 is universal at every d ≥ 5, via an explicit lifting recipe |
| **6.1** | The classical Kaprekar constant 6174 has a characterized cross-dimensional pattern: strict-universal at d = 4 and d = 7, near-universal with bounded basin at d = 8, 9; obstructed at d = 5, 6 |

---

## 📖 The paper, section by section

For in-browser viewing — sections render cleanly on GitHub.

### Main text

| § | Section | Topic |
|---|---|---|
| 1 | [Introduction](sections/01_introduction.md) | Kaprekar's routine, the cross-dimensional question, the 54 → 60714 discovery arc |
| 2 | [Framework](sections/02_framework.md) | Permutation-pair rules, algebraic rank, native digit length |
| 3 | [Classifications at d ≤ 6](sections/03_classifications.md) | Exhaustive enumeration, Theorems 3.1–3.4 |
| 4 | [Cross-check d = 5 → d = 6](sections/04_cross_check.md) | Theorem 4.1, the 32 dimension-locked fps |
| 5 | [The 60714 theorem](sections/05_theorem_60714.md) | The lifting construction, Theorem 5.2 and its proof |
| 6 | [The {7,6,4,1} thread](sections/06_thread_7641.md) | 60714 vs 6174 vs 60417 vs 1746 |
| 7 | [Open questions](sections/07_open_questions.md) | Conjectures and directions |

### Appendices

| | Appendix | Topic |
|---|---|---|
| A | [Classification tables](sections/A_classification_tables.md) | Per-d enumeration data, fixed-point catalogues |
| B | [60714 ladder construction](sections/B_60714_ladder.md) | Explicit coefficient vectors through d = 20 |
| C | [Support lemmas for Theorem 5.2](sections/C_support_lemmas.md) | Core non-negativity, Td closure, the d = 15 algebraic hinge |
| D | [Transcendent fps at d = 7](sections/D_dF7_observations.md) | 22-fp audit |
| E | [6174 audit at d = 8, 9](sections/E_6174_audit.md) | The 45-input escape class |

---

## ⚙️ Reproducibility

All exhaustive claims in the paper have corresponding Python scripts in [`scripts/`](scripts/). Pure Python 3 (≥ 3.8), no external dependencies.

| Script | Reproduces | Runtime |
|---|---|---|
| [`classify_at_d.py`](scripts/classify_at_d.py) | Theorems 3.1–3.4 | d = 5: ~5 s · d = 6: ~5–10 min |
| [`cross_check_d5_to_d6.py`](scripts/cross_check_d5_to_d6.py) | Theorem 4.1 | ~30 min |
| [`verify_60714_ladder.py`](scripts/verify_60714_ladder.py) | Theorem 5.2 algebraic part: K(60714) = 60714 at each d | < 1 s |
| [`verify_60714_basin.py`](scripts/verify_60714_basin.py) | Theorem 5.2 dynamic part: basin universality + escape class characterization | d = 7: ~3 s · d = 8: ~30 s · d = 9: ~5 min |
| [`verify_lemma_5_2.py`](scripts/verify_lemma_5_2.py) | Proposition 5.2: bounded reaching time at low d | ~5 min |
| [`verify_even_ladder_closure.py`](scripts/verify_even_ladder_closure.py) | Lemma C.4: one-step T_d closure on the even ladder at d ≥ 18 | d = 18: ~30 s · d = 20: ~3 min |
| [`verify_case2_recovery.py`](scripts/verify_case2_recovery.py) | Lemma C.10: Case 2 admissibility recovery for d ∈ [7, 30] | ~30 s |
| [`audit_6174_d8_d9.py`](scripts/audit_6174_d8_d9.py) | Theorem 6.1, parts 5 & 6 | d = 8: ~3 min · d = 9: ~60 min |

Run any script with `python3 scripts/<script>.py` and `--help` for options.

To regenerate the [`d6_fps.txt`](d6_fps.txt) supplementary file:

```bash
python3 scripts/classify_at_d.py 6 --save-txt
```

---

## How this paper was written

The discovery arc, the classification errors and self-corrections, the proof gaps and their resolution, and the methodological pattern are documented in §1.4 of the paper. In short: brute-force enumeration produced the empirical landscape, an early candidate (54) revealed itself as algebraically degenerate on closer inspection, and the search refined toward fixed points with no zero digits in their native form. The unique answer was 60714.

The full collaboration story — including the wrong-answer detour through 45000, the 54-vs-60714 distinction, the proof saga that closed at 1 a.m. — is in the LinkedIn companion article *(link forthcoming)*.

---

## Citation

*(To be filled in upon submission.)*

---

*The repository is private during pre-submission review. If you arrived here from a link and the calculator or paper isn't loading, contact the author.*
