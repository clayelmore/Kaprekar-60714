# Fourth review of PROOF_146070.md (2026-11-25)

Independent code, written from scratch from the rule's place maps, not using the repository's programs.

* `enum.c`: complete enumeration of every digit multiset at each length. Checks that every non-repdigit reaches 146070 with no cycle and no other fixed point; records maximum steps (to the target digits and to the integer) and maximum |R| of Lemma 1. Build `cc -O2 -o enum enum.c`, run `./enum 6 30`. Expect `bad=0`, `fixedpoints(multiset-level)=2`, and for d >= 8 41 steps to the target digits and 42 to the integer. Each length's integer-steps line prints just before its summary line. `enum_13_30.txt` is the output for d = 13 to 30.
* `clos.c`: the closure over S. Run `cc -O2 -o clos clos.c && ./clos 5 15`. Expect 2,941,883 seeds, 2,942,591 states, 0 failures, at most 20 nonzero digits, at most 41 steps, 0 formula mismatches.
* `bigtest.py`, `bigtest2.py`: the same large-d tests (the second computes K by direct subtraction) of Lemmas 1 to 3, the main claim and the step bound. Run `python3 bigtest2.py 21 100 400`. `big_400_1000.txt` has the d = 400 result; the d = 1000 run was stopped unfinished.
