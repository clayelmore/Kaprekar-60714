# Kaprekar Multiplicity Chain — Universal Fixed Points on {1,4,6,7}^m

Research on universal fixed points of generalized (pair-symmetric) Kaprekar rules
on the multiplicity chain {1,4,6,7}^m at digit length d = 4m.

## Key documents
- **PROOF.md** — the mathematical results: fixed-point theorem (proven, all m),
  the monotone–acyclic decomposition of universality, the rigorous finiteness
  criterion (Lemma A), and the open proof program.
- **THEORY_AND_RULES.md** — the pair-symmetric construction, explicit rules, predictions.
- **CAMPAIGN_FINDINGS.md** — the computational search campaign (d=16 through d=24).

## Verified results
| m | d | classical universal fixed points |
|---:|---:|---|
| 1 | 4 | 2 (classical Kaprekar 6174, 1746) |
| 2 | 8 | 481 |
| 3 | 12 | 42 |
| 4 | 16 | 341 |
| 5 | 20 | ≥1 (F = 17461746146174617746) |
| 6 | 24 | ≥1 (F = 666174141466617777741414) |

## Central result (this work)
**Universal ⟺ Monotone ∧ Acyclic** — universality of a pair-symmetric rule
factors into a clean algebraic condition (cumulative coefficient sums ≥ 0) and the
classical Kaprekar cycle-exclusion. Verified at d=12 and d=16 with zero exceptions.

## Data
JSON files contain the verified universal rules (π, σ permutations) and search results.
