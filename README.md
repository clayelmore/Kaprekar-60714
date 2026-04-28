# 60714

A five-digit number that's a universal attractor at every digit length d ≥ 5.

Pick any number with five or more digits. Apply the right rule. Watch it converge to **60714** at every digit length $d \geq 5$, modulo a small structurally characterized escape class that's continuous with the classical Kaprekar escape phenomenon at $d = 3, 4$ (the ten repdigits at $d = 3$, the ten multiples of 1111 at $d = 4$). The rule depends on the input's digit length, but the destination is almost always the same.

This is a generalization of Kaprekar's classical 1949 result, extended in a direction the literature has not explored: instead of fixing the rule and asking which digit lengths work, we let the rule vary with the digit length, and find a single fixed point — 60714 — whose universality holds across infinitely many dimensions simultaneously.

The integer 60714 is one consequence of a more general structural framework. The paper's underlying contributions are the **classification of universal full-variable fixed points at digit length d** (yielding the catalog 0, 4, 33, 506 fixed points at d ∈ {3, 4, 5, 6}), the **coefficient-preserving lifting recipe** that connects rules across digit lengths, and the **block-aligned escape class** (Definition 5.2) that exactly characterizes when the lifted dynamics fail. 60714 is the unique integer for which this framework produces a cross-dimensional attractor with universally large basin.

---

## ⚡ Try it

**👉 [Open the interactive calculator](60714_calculator.html)**

Type any number 5–20 digits long. The calculator shows the full trajectory, step by step, until convergence.

---

## What's here

| | |
|---|---|
| **[paper.pdf](paper.pdf)** | The complete paper, compiled (71 pages, 629 KB). The canonical reading version. |
| **[60714_calculator.html](60714_calculator.html)** | Single-file interactive calculator. Open it in any browser. No setup. |
| **[paper.md](paper.md)** | Markdown source of the paper, identical content to the PDF. ~225 KB; if GitHub's math renderer struggles with the size, browse the [section files](#-the-paper-section-by-section) below. |
| **[paper.tex](paper.tex)** | LaTeX source. Compiles to `paper.pdf` with `pdflatex`. |
| **[d6_fps.txt](d6_fps.txt)** | All 506 universal fixed points at d = 6, with metadata. |
| **[d7_fps.txt](d7_fps.txt)** | All 18,004 universal full-variable fixed points at d = 7, from the exhaustive Run B classification (Appendix D). |
| **[d7_summary.txt](d7_summary.txt)** | Human-readable summary of the d=7 classification: per-zero-stratum counts, rule totals, and reproducibility metadata. |
| **[d7_classification.json](d7_classification.json)** | Run B output: full machine-readable d=7 classification (10 MB). |
| **[d7_verified_outcomes.json](d7_verified_outcomes.json)** | Run C output: cross-dimensional outcomes for the two-zero d=6 stratum verified at d=7 (42 MB). |
| **[audit_60714_d7.json](audit_60714_d7.json)**, **[audit_60714_d8.json](audit_60714_d8.json)** | Empirical confirmation of Lemma 5.5 at d=7 and d=8 (cf. §5 Remark). |
| **[README_d7_verifier.md](README_d7_verifier.md)** | Documentation for the d=7 outcome verifier methodology. |
| **[scripts/](scripts/)** | Reproducibility scripts for every exhaustive claim in the paper at $d \leq 6$. |
| **[d7_audit/](d7_audit/)** | Self-contained $d = 7$ verification package: Run B (exhaustive classification), Run C (cross-dimensional outcomes), Run A/A2 (60714 lifting audits at $d = 7, 8$). See `d7_audit/README.md`. |

---

## What 60714 actually is

In Kaprekar's classical routine at d = 4, you sort the digits descending, sort them ascending, subtract, and repeat. From every non-repdigit input, you reach **6174** within seven steps.

The routine "stops working" at d = 5 — Kaprekar's specific rule cycles instead of converging. The standard story for 77 years has been: 5-digit Kaprekar doesn't work.

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
| 4 | [Cross-check d = 5 → d = 6](sections/04_cross_check.md) | Theorem 4.1, the 32 dimension-locked fixed points |
| 5 | [The 60714 theorem](sections/05_theorem_60714.md) | The lifting construction, Theorem 5.2 and its proof |
| 6 | [The {7,6,4,1} thread](sections/06_thread_7641.md) | 60714 vs 6174 vs 60417 vs 1746 |
| 7 | [Open questions](sections/07_open_questions.md) | Conjectures and directions |

### Appendices

| | Appendix | Topic |
|---|---|---|
| A | [Classification tables](sections/A_classification_tables.md) | Per-d enumeration data, fixed-point catalogues |
| B | [60714 ladder construction](sections/B_60714_ladder.md) | Explicit coefficient vectors through d = 20 |
| C | [Support lemmas for Theorem 5.2](sections/C_support_lemmas.md) | Core non-negativity, Td closure, the d = 15 algebraic hinge |
| D | [Universal full-variable fps at d = 7](sections/D_dF7_observations.md) | Exhaustive d = 7 classification (18,004 fps) and cross-dimensional outcomes for the two-zero d = 6 stratum |
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

### d = 7 verification

For the d = 7 work in Appendix D — the exhaustive classification, the cross-dimensional outcome verification, and the empirical confirmation of Lemma 5.5 — see the self-contained [`d7_audit/`](d7_audit/) package. It uses Numba parallel acceleration and supports crash-resume on the longer enumerations.

| Script | Reproduces | Runtime |
|---|---|---|
| [`d7_audit/audit_60714_d7.py`](d7_audit/audit_60714_d7.py) | §5 Remark: Lemma 5.5 confirmation at d = 7 | ~3 s |
| [`d7_audit/audit_60714_d8.py`](d7_audit/audit_60714_d8.py) | §5 Remark: Lemma 5.5 confirmation at d = 8 | ~3 s |
| [`d7_audit/classify_d7_full.py`](d7_audit/classify_d7_full.py) | Run B: exhaustive d=7 classification (18,004 universal fps) | ~5–30 min |
| [`d7_audit/d7_outcome_verifier.py`](d7_audit/d7_outcome_verifier.py) | Run C: cross-dimensional outcomes for the 53-fp two-zero d=6 stratum | ~1–3 hours |
| [`d7_audit/typeA_validator.py`](d7_audit/typeA_validator.py) | §6.6 Observation 6.3: held-out validation of the Type A LOCK characterization | ~5 min |

---

## How this paper was written

The discovery arc, the classification errors and self-corrections, the proof gaps and their resolution, and the methodological pattern are documented in §1.4 of the paper. In short: brute-force enumeration produced the empirical landscape, an early candidate (54) revealed itself as algebraically degenerate on closer inspection, and the search refined toward fixed points with no zero digits in their native form. The unique answer was 60714.

The full collaboration story — including the wrong-answer detour through 45000, the 54-vs-60714 distinction, the proof saga that closed at 1 a.m. — is in the LinkedIn companion article *(link forthcoming)*.

---

## Citation

*(To be filled in upon submission.)*

---

*The repository is private during pre-submission review. If you arrived here from a link and the calculator or paper isn't loading, contact the author.*
