# Dimension-Transcendent Attractors in Generalized Kaprekar Routines

Paper draft and reproducibility code.

## Layout

- **`paper.md`** — the complete paper, stitched from all sections (1,679 lines, ~155 KB). This is the primary deliverable.
- **`sections/`** — individual section and appendix files, useful for editing. Concatenating these in order (01 → 07, A → E) reproduces `paper.md`.
- **`scripts/`** — Python reproducibility scripts for every exhaustive claim in the paper.

## Paper summary

The paper establishes that the integer **60714** is a dimension-transcendent attractor: it is a universal full-variable fixed point at every digit length $d \geq 5$ under an explicit family of lifted rules. Four theorems are proven:

- **Theorem 3.1–3.4** — exhaustive classification of universal full-variable fixed points at $d = 3, 4, 5, 6$ (0, 4, 33, 507 fps respectively).
- **Theorem 4.1** — of the 33 universal fps at $d = 5$, exactly one (60714) also universalizes at $d = 6$.
- **Theorem 5.2** — 60714 is universal at every $d \geq 5$, proven via a block-structure decomposition and finite-state enumeration at $d \leq 16$.
- **Theorem 6.1** — the classical Kaprekar fixed point 6174 has a characterized cross-dimensional fingerprint at $d = 4, \ldots, 9$.

## Reproducing the main claims

All claims in the paper that rely on exhaustive enumeration have corresponding Python scripts in `scripts/`. From the `scripts/` directory:

```
python3 classify_at_d.py 5              # Theorem 3.3 — runs in ~5 seconds
python3 classify_at_d.py 6 --save       # Theorem 3.4 — runs in ~3 hours
python3 cross_check_d5_to_d6.py         # Theorem 4.1 — runs in ~30 minutes
python3 verify_60714_ladder.py 20       # Theorem 5.2 construction — <1 second
python3 verify_lemma_5_2.py             # Proposition 5.2 — runs in ~5 minutes
python3 audit_6174_d8_d9.py 8           # Theorem 6.1, part 5 — runs in ~3 minutes
python3 audit_6174_d8_d9.py 9           # Theorem 6.1, part 6 — runs in ~60 minutes
```

Scripts are pure Python 3 (≥ 3.8) with no external dependencies.

## Paper status

Draft complete. Pre-submission items remaining:

1. Complete the lists in §3 Table 3.1 and §4 Tables 4.1/4.2 (data exists; mechanical).
2. Strengthen the d=15 odd-ladder hinge argument in §5.5.2 / Appendix C.4 from "direct computation confirms" to a clean algebraic statement.
3. Audit the remaining 12 of 22 TRANS fps at $d_F = 7$ referenced in Appendix D.
4. Test the `sum_locked_spans` invariant (§6 Observation 6.2) beyond the {7, 6, 4, 1}-thread on multisets 2538, 5382, 1746.
5. Generate the `d6_fps.txt` supplementary file listing all 507 universal fps at $d = 6$.

## Citation

*(To be filled in upon submission.)*
