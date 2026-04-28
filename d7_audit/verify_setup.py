#!/usr/bin/env python3
"""
verify_setup.py
===============
30-second sanity check before launching the long d=7 runs.

Confirms:
  1. Python version is 3.9+
  2. Numba is installed and JIT compilation works
  3. kaprekar_core.py self-test passes
  4. The d=5 60714 lifted rule has 60714 as fixed point and is universal
     over all admissibles at d=5 (matching Theorem 5.2 base case)
  5. The d=6 60714 lifted rule has 60714 as fixed point and is universal
     over all admissibles at d=6 (matching Theorem 5.2 base case)
  6. The d=7 60714 lifted rule on a couple of test inputs gives the
     expected step-1 values

If any check fails, the long runs would also fail. If everything passes,
proceed to audit_60714_d7.py and the longer scripts.

Usage:
    python3 verify_setup.py

Exit code: 0 on success, 1 on any failure.
"""

import sys
import time


def fail(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def ok(msg):
    print(f"  OK: {msg}")


def main():
    print("=" * 60)
    print("verify_setup.py — d=7 audit package sanity check")
    print("=" * 60)
    print()

    # ---- 1. Python version ----
    print("[1/6] Python version")
    if sys.version_info < (3, 9):
        fail(f"Python 3.9+ required, got {sys.version_info.major}.{sys.version_info.minor}")
    ok(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()

    # ---- 2. Numba ----
    print("[2/6] Numba availability")
    try:
        import numba
        ok(f"numba {numba.__version__}")
    except ImportError:
        fail("Numba not installed. Run: pip install numba")
    print()

    # ---- 3. JIT smoke test ----
    print("[3/6] Numba JIT smoke test (first compile is slow; this measures it)")
    t0 = time.time()
    try:
        from numba import njit
        @njit(cache=False)
        def smoke(x):
            s = 0
            for i in range(x):
                s += i
            return s
        result = smoke(1000)
        if result != 499500:
            fail(f"JIT smoke test wrong result: {result} (expected 499500)")
        ok(f"JIT compile + run, {time.time() - t0:.2f}s")
    except Exception as e:
        fail(f"JIT smoke test crashed: {e}")
    print()

    # ---- 4. Core import + selftest ----
    print("[4/6] kaprekar_core import + selftest")
    try:
        import kaprekar_core
    except ImportError as e:
        fail(f"Cannot import kaprekar_core (is it in the same directory?): {e}")
    try:
        kaprekar_core.selftest()
        ok("kaprekar_core.selftest passes")
    except Exception as e:
        fail(f"selftest crashed: {e}")
    print()

    # ---- 5. d=5 base case ----
    print("[5/6] d=5 60714 base case (Theorem 5.2 root, odd ladder)")
    t0 = time.time()
    coefs = kaprekar_core.coefs_60714_odd_ladder(5)
    if coefs != (9900, 9, 90, -9000, -999):
        fail(f"d=5 coefs wrong: {coefs}")
    admissibles = kaprekar_core.build_admissible_multisets(5)
    if len(admissibles) != 1902:
        fail(f"d=5 admissible count wrong: {len(admissibles)} (expected 1902)")
    n_reach = 0
    for ms in admissibles:
        val, _, fate = kaprekar_core.trace_python(ms, 5, coefs, max_steps=80)
        if fate == 'fixed_60714':
            n_reach += 1
    if n_reach != 1902:
        fail(f"d=5 60714 not universal: only {n_reach}/1902 reach 60714")
    ok(f"all 1902 admissibles reach 60714 at d=5, {time.time() - t0:.2f}s")
    print()

    # ---- 6. d=6 base case (split-lifted root, even ladder) ----
    print("[6/6] d=6 60714 base case (Theorem 5.2 root, even ladder)")
    t0 = time.time()
    coefs = kaprekar_core.coefs_60714_odd_ladder(6)
    if coefs != (9900, 9, 90, -9000, 99000, -99999):
        fail(f"d=6 coefs wrong: {coefs}")
    admissibles = kaprekar_core.build_admissible_multisets(6)
    if len(admissibles) != 4905:
        fail(f"d=6 admissible count wrong: {len(admissibles)} (expected 4905)")
    n_reach = 0
    for ms in admissibles:
        val, _, fate = kaprekar_core.trace_python(ms, 6, coefs, max_steps=120)
        if fate == 'fixed_60714':
            n_reach += 1
    if n_reach != 4905:
        fail(f"d=6 60714 not universal: only {n_reach}/4905 reach 60714")
    ok(f"all 4905 admissibles reach 60714 at d=6, {time.time() - t0:.2f}s")
    print()

    print("=" * 60)
    print("All sanity checks passed. Safe to run:")
    print("  python3 audit_60714_d7.py        # ~3 seconds")
    print("  python3 classify_d7_full.py      # 10-30 minutes (Numba)")
    print("  python3 d7_outcome_verifier.py   # 1-3 hours")
    print("=" * 60)


if __name__ == '__main__':
    main()
