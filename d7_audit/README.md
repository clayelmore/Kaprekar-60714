# d7_audit — d=7 verification package for the Kaprekar-60714 paper

This package runs four complementary jobs:

- **Run A** (`audit_60714_d7.py`) — Quick (~3 sec) audit of 60714's coefficient-preserving lifting at d=7 (odd ladder). Confirms basin density, escape-class size, max reaching time. Empirically validates Theorem 5.2 at d=7.

- **Run A2** (`audit_60714_d8.py`) — Quick (~2 sec) audit at d=8 (even ladder). Same scope as Run A but along the complementary ladder. Gives basin/escape data at d=8 for ladder-decay analysis.

- **Run B** (`classify_d7_full.py`) — Sound exhaustive enumeration over all 9,344,160 sv=7 rules to find every universal full-variable fixed point at d=7. Closes the gap that Appendix D currently labels "non-exhaustive."

- **Run C** (`d7_outcome_verifier.py`) — For each of the 53 two-zero d=6 universal fps (Appendix A.4.3), enumerates all sv=7 rules that fix it, computes exact basin, and classifies TRANS / NEAR / LOCK at d=7.

## Setup

```
pip install -r requirements.txt
```

That installs `numba` (one dependency, ~1 minute on M5 Pro). The package is otherwise pure Python.

## Quick start

```
./reproduce.sh
```

Runs all stages in sequence. Total wall time: ~1-4 hours on a modern laptop, dominated by Run C.

## Individual stages

```
python3 verify_setup.py            # 30-sec sanity check (do this first)
python3 audit_60714_d7.py          # Run A:  ~3 sec
python3 audit_60714_d8.py          # Run A2: ~2 sec
python3 classify_d7_full.py        # Run B:  ~5-30 min with Numba parallel
python3 d7_outcome_verifier.py     # Run C:  ~1-3 hours
```

All scripts support `--help` for options.

## Crash recovery

Both Run B and Run C are checkpointed:
- Run B saves to `d7_classify.checkpoint` every 60 seconds; restart picks up where it left off.
- Run C saves to `d7_verified_partial.json` after every fp completes.

If the process is interrupted (Ctrl-C, kernel panic, power loss), simply re-invoke the same script. It will resume automatically.

## What each output file contains

| File | Source | Content |
|---|---|---|
| `audit_60714_d7.json` | Run A | Basin density, |E_7^(1)|, |E_7|, max reaching time, sample trajectories (d=7 odd ladder) |
| `audit_60714_d8.json` | Run A2 | Same metrics, d=8 even ladder |
| `d7_classification.json` | Run B | Per-fp metadata: multiset, zero-count, sample rules, signatures |
| `d7_fps.txt` | Run B | Sorted fp list, one per line, with multiset and rule-count |
| `d7_progress.log` | Run B | Time-stamped progress trace |
| `d7_verified_outcomes.json` | Run C | Per-fp data: best basin, best rule, all rules, outcome |
| `d7_summary.txt` | Run C | One-line-per-fp TRANS/NEAR/LOCK summary |
| `d7_classifier_analysis.txt` | Run C | Cycle-signature × outcome cross-tab |
| `d7_verified_partial.json` | Run C | Resume checkpoint (also viewable as a JSON snapshot) |

## Validation cases for Run C

Run C was tested against four reference fps in the {7,6,4,1}-thread:

| F | Expected outcome | Verified outcome |
|---|---|---|
| 60714 | TRANS | TRANS, best basin 0.992857 (4 rules ≥ 0.99) |
| 146070 | TRANS | TRANS, best basin 1.000000 (4 rules ≥ 0.99) |
| 170460 | LOCK | LOCK, best basin 0.922928 (0 rules ≥ 0.99) |
| 607140 | NEAR | NEAR, best basin 0.985450 (0 rules ≥ 0.99) |

All four classifications match expectations. The exact best-basin numbers are independently verified by brute-force enumeration of all 9.3M sv=7 rules per fp.

## TRANS / NEAR / LOCK thresholds

- **TRANS**: best basin ≥ 0.99 — universal modulo small escape class
- **NEAR**: best basin in [0.95, 0.99) — near-universal with substantial competing attractor
- **LOCK**: best basin < 0.95 — substantially sub-universal, dimension-locked

These thresholds match the empirical groupings used in the paper.

## Architecture

`kaprekar_core.py` — shared infrastructure. Numba-accelerated `step_encoded` (one K iteration on encoded multisets), pure-Python `trace_python` (used by audit_60714_d7), full-variable rule enumerator, cycle-signature computation, 60714 ladder rule construction.

The performance trick in Runs B and C is **multiset memoization**: every admissible multiset is encoded as a base-10 int64, and a flat 10^7-slot lookup table maps encoded multisets to compact admissible indices. Within each rule's basin computation, the fate of each multiset visited is cached, so repeated traces collapse into a single connected-components walk. Combined with Numba JIT, this gives ~0.03 ms per rule on average for Run B (early-out on non-universal rules) and a few milliseconds per F-fixing rule for Run C.

## Files in this package

```
d7_audit/
├── README.md                  ← this file
├── requirements.txt           ← numba, numpy
├── kaprekar_core.py           ← shared infrastructure
├── verify_setup.py            ← Stage 1: sanity check
├── audit_60714_d7.py          ← Stage 2: Run A  (d=7 odd ladder)
├── audit_60714_d8.py          ← Stage 3: Run A2 (d=8 even ladder)
├── classify_d7_full.py        ← Stage 4: Run B (full d=7 classification)
├── d7_outcome_verifier.py     ← Stage 5: Run C (52-fp verifier)
└── reproduce.sh               ← runs all stages in sequence
```

## Sending results back

After all runs complete, send back:

```
audit_60714_d7.json
audit_60714_d8.json
d7_classification.json
d7_fps.txt
d7_verified_outcomes.json
d7_summary.txt
d7_classifier_analysis.txt
```

These are the inputs needed for analysis: paper Appendix D extension, classifier confirmation/refutation on the larger 52-fp sample, and any sub-classifier search within the long-cycle bucket.
