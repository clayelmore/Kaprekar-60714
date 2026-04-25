# Dimension-Transcendent Attractors in Generalized Kaprekar Routines

Paper draft and reproducibility code.

## Layout

- **`paper.md`** — the complete paper, stitched from all sections (~1,800 lines, ~165 KB). This is the primary deliverable.
- **`sections/`** — individual section and appendix files, useful for editing. Concatenating these in order (01 → 07, A → E) reproduces `paper.md`.
- **`scripts/`** — Python reproducibility scripts for every exhaustive claim in the paper.

## Paper summary

The paper establishes that the integer **60714** is a dimension-transcendent attractor: it is a universal full-variable fixed point at every digit length $d \geq 5$ under an explicit family of lifted rules. Four theorems are proven:

- **Theorem 3.1–3.4** — exhaustive classification of universal full-variable fixed points at $d = 3, 4, 5, 6$ (0, 4, 33, 507 fps respectively).
- **Theorem 4.1** — of the 33 universal fps at $d = 5$, exactly one (60714) also universalizes at $d = 6$.
- **Theorem 5.2** — 60714 is universal at every $d \geq 5$, proven via a block-structure decomposition and finite-state enumeration at $d \leq 16$.
- **Theorem 6.1** — the classical Kaprekar fixed point 6174 has a characterized cross-dimensional pattern at $d = 4, \ldots, 9$: strict universal at $d = 4$, algebraic obstruction at $d = 5$, dynamic obstruction at $d = 6$, and near-universal with monotonically improving basin at $d = 7, 8, 9$.

## Reproducing the main claims

All claims in the paper that rely on exhaustive enumeration have corresponding Python scripts in `scripts/`. From the `scripts/` directory:

```
python3 classify_at_d.py 5                # Theorem 3.3 — runs in ~5 seconds
python3 classify_at_d.py 6 --save-txt     # Theorem 3.4 + d6_fps.txt — runs in ~3 hours
python3 cross_check_d5_to_d6.py           # Theorem 4.1 — runs in ~30 minutes
python3 verify_60714_ladder.py 20         # Theorem 5.2 construction — <1 second
python3 verify_lemma_5_2.py               # Proposition 5.2 — runs in ~5 minutes
python3 audit_6174_d8_d9.py 8             # Theorem 6.1, part 5 — runs in ~3 minutes
python3 audit_6174_d8_d9.py 9             # Theorem 6.1, part 6 — runs in ~60 minutes
```

Scripts are pure Python 3 (≥ 3.8) with no external dependencies.

## Generating the d6_fps.txt supplementary file

The paper references a supplementary file `d6_fps.txt` listing all 507 universal full-variable fixed points at $d = 6$. To generate it, run:

```
python3 scripts/classify_at_d.py 6 --save-txt
```

This produces `d6_fps.txt` with one line per fixed point, including zero-digit count and digit multiset. Total runtime ~3 hours on commodity hardware.

The script also accepts `--save` to additionally produce a richer JSON file (`d6_classification.json`) with per-fp rule counts and sample permutations. The `--save` and `--save-txt` flags can be used together.

## Paper status

Pre-submission revision complete. All five pre-submission items resolved:

1. §4 Tables 4.1 and 4.2 filled with all 32 dimension-locked fps at $d = 5$.
2. $d = 15$ odd-ladder hinge argument strengthened in Appendix C.4 (Lemmas C.7, C.8 + 3-case proof).
3. All 22 TRANS fps at $d_F = 7$ documented in Appendix D from the April 2026 audit.
4. `sum_locked_spans` invariant tested beyond the $\{7,6,4,1\}$-thread; Observation 6.2 honestly narrowed to within-thread.
5. `d6_fps.txt` generation script (`classify_at_d.py 6 --save-txt`) prepared.

## Citation

*(To be filled in upon submission.)*
