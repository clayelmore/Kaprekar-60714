# OEIS Submission Draft

This is the prepared OEIS submission for the |E_d^(1)| sequence from
Lemma 5.2.2.

**This is not a new-sequence submission. The numerical sequence is a trivial
offset of A000582 (binomial C(n, 9), in OEIS since 1973). What is new is
the combinatorial interpretation: |E_d^(1)| counts the step-1 escape class
of the lifted Kaprekar operator at digit length d.**

The right submission is therefore one of two options:

  Option A. Submit a comment to A000582 noting the new interpretation.
  Option B. Submit B_NEW as a new sequence with %F line referencing
            A000582 explicitly, and an %N line that emphasizes the
            combinatorial origin (Kaprekar escape class) rather than the
            arithmetic.

Option B is appropriate here because the interpretation under
the lifted Kaprekar operator is sufficiently distinct from the
multiset-of-digits / 9-simplex interpretations that already exist on
A000582 that giving it its own A-number with a clear cross-reference is
the cleanest editorial choice. It is also the form that supports the
paper's reproducibility chain (citing a unique A-number for E_d^(1)).

Pre-submission required: cross-check with the OEIS editor before sending.
The decision between Option A (comment-on-existing) and Option B
(new-sequence-with-cross-reference) belongs to OEIS, not to the author.
The author's job is to present the cross-reference clearly enough that
the editor can choose.

**All numerical claims in this file are reproducible by running:**

```python
from math import comb
# B_NEW (the underlying combinatorial sequence):
[comb(k+9, 9) - 10 for k in range(2, 16)]
# Equivalent in terms of A000582:
[A000582(k+9) - 10 for k in range(2, 16)]   # where A000582(n) = C(n, 9)
# A_NEW (paired d-indexed version for the paper's notation):
[comb((d-3)//2 + 9, 9) - 10 for d in range(7, 21)]
```

## Submit at: https://oeis.org/submit.html

## %S — Sequence A_NEW (paired version, one term per d on the 60714 ladder)

This is the sequence as it appears in the paper, with terms paired across
the two ladders (odd d=7,9,11,...; even d=8,10,12,...).

```
%I A_NEW
%S A_NEW 45,45,210,210,705,705,1992,1992,4995,4995,11430,11430,24300,24300
%N A_NEW |E_d^(1)|: number of step-1 collapse inputs at digit length d for
the generalized Kaprekar lifting K^(d) of 60714, for d = 7, 8, 9, 10, ...
%C A_NEW E_d^(1) is the set of admissible inputs at digit length d whose
sorted-descending form has all entries beyond position d_F-1 = 4 equal,
modulo zero padding; equivalently, the inputs whose K^(d) image equals 0
in one step. This is the step-1 component of the escape class E_d defined
in [Elmore 2026, Definition 5.2 and Lemma 5.2.2].
%C A_NEW Sequence is paired: a(d) = a(d+1) for odd d, reflecting the
two-ladder (odd, even) structure of the 60714 lifting.
%C A_NEW Numerical values are A000582(k+9) - 10 where k = floor((d-3)/2).
The "minus 10" subtracts the ten repdigit multisets (one per digit value),
which are excluded from the admissible set under Kaprekar's classical
exclusion. The combinatorial interpretation under the lifted Kaprekar
operator (escape class size) is distinct from A000582's existing
interpretations (9-simplex figurate numbers, multisets of size n from a
10-letter alphabet, words read in nondecreasing order).
%F A_NEW a(d) = C(floor((d-3)/2) + 9, 9) - 10 for d >= 7. Equivalently,
a(d) = A000582(floor((d-3)/2) + 9) - 10.
%H A_NEW C. Elmore, <a href="https://arxiv.org/abs/PENDING">Universal Full-Variable
Fixed Points Under Coefficient-Preserving Liftings: Classification at d <= 6
and the Cross-Dimensional Survivor 60714</a>, arXiv preprint, 2026.
%Y A_NEW Cf. A000582 (the underlying binomial C(n, 9); a(d) above is
A000582(floor((d-3)/2) + 9) - 10).
%e A_NEW At d = 7: |E_7^(1)| = C(2+9, 9) - 10 = C(11, 9) - 10 = 55 - 10 = 45.
%e A_NEW At d = 11: |E_11^(1)| = C(4+9, 9) - 10 = C(13, 9) - 10 = 715 - 10 = 705.
%e A_NEW At d = 19: |E_19^(1)| = C(8+9, 9) - 10 = C(17, 9) - 10 = 24310 - 10 = 24300.
%K A_NEW nonn,easy
%O A_NEW 7,1
%A A_NEW Clay Elmore, [DATE]
```

## %S — Sequence B_NEW (one term per k, unpaired)

The deeper combinatorial sequence — the multiset coefficient minus 10.
This is the more natural form for OEIS since it has no pairing artifact.

```
%I B_NEW
%S B_NEW 45,210,705,1992,4995,11430,24300,48610,92368,167950,293920,497410,817180,1307494
%N B_NEW C(k+9, 9) - 10: the size of the step-1 escape class at digit
length d = 2k+5 (odd ladder) or d = 2k+6 (even ladder) of the lifted
Kaprekar operator at 60714, for k >= 2.
%C B_NEW Numerically, this is A000582(k+9) - 10. The "minus 10" subtracts
the ten repdigit multisets (one per digit value); these are excluded from
the admissible set under Kaprekar's classical exclusion. The interpretation
as an escape-class size under the lifted Kaprekar operator is the
contribution of [Elmore 2026]; the underlying binomial C(k+9, 9) has
been in OEIS as A000582 since 1973 with multiple combinatorial
interpretations (9-simplex figurate numbers, multisets of size k from a
10-letter alphabet, words of length k over {0..9} read in nondecreasing
order).
%C B_NEW The Kaprekar interpretation: at each d on the 60714 ladder, the
sorted-descending admissible inputs whose top digits are equal up to
position d_F-1 = 4 (with the remaining (d - d_F)/2 pairs of trailing
digits each having matched values) form an escape class on which K^(d)
collapses to 0 in one step. There are exactly C(k+9, 9) such multisets
including the 10 repdigit cases, hence C(k+9, 9) - 10 admissible escape
multisets.
%F B_NEW a(k) = C(k+9, 9) - 10 = (k+9)!/(9! k!) - 10 for k >= 2.
%F B_NEW a(k) = A000582(k+9) - 10 for k >= 2.
%H B_NEW C. Elmore, <a href="https://arxiv.org/abs/PENDING">Universal Full-Variable
Fixed Points Under Coefficient-Preserving Liftings: Classification at d <= 6
and the Cross-Dimensional Survivor 60714</a>, arXiv preprint, 2026.
%Y B_NEW Cf. A000582 (the underlying binomial C(n, 9); a(k) above is
A000582(k+9) - 10). Cf. A_NEW (the d-indexed paired version of this
sequence).
%e B_NEW At k=2: A000582(11) - 10 = 55 - 10 = 45.
%e B_NEW At k=3: A000582(12) - 10 = 220 - 10 = 210.
%e B_NEW At k=8: A000582(17) - 10 = 24310 - 10 = 24300.
%K B_NEW nonn,easy
%O B_NEW 2,1
%A B_NEW Clay Elmore, [DATE]
```

## Pre-submission checks

1. **Confirm A000582 is the right cross-reference.** Run:
   ```python
   from math import comb
   # A000582 starts at n=9 with value C(9,9) = 1
   A000582 = [comb(n, 9) for n in range(9, 30)]
   # Compare to B_NEW: should differ by exactly 10 at each position
   B_NEW = [comb(k+9, 9) - 10 for k in range(2, 16)]
   for k, b in zip(range(2, 16), B_NEW):
       assert A000582[k] - 10 == b, f"mismatch at k={k}"
   print("✓ B_NEW(k) = A000582(k+9) - 10 verified")
   ```

2. **Decide between Option A (comment on A000582) and Option B (new sequence).**
   Send a brief email to OEIS at editors@oeis.org before submitting; describe
   the paper's interpretation and ask whether they prefer a comment on
   A000582 or a new sequence with cross-reference. The OEIS editorial
   convention favors new entries when the interpretation is sufficiently
   distinct, but the editor's call is the right call here.

3. **Final verification.** The asserts at the top of this file should run
   silently. Before submission, also run:
   ```python
   from math import comb
   assert [comb((d-3)//2 + 9, 9) - 10 for d in range(7, 21)] == \
       [45,45,210,210,705,705,1992,1992,4995,4995,11430,11430,24300,24300]
   assert [comb(k+9, 9) - 10 for k in range(2, 16)] == \
       [45,210,705,1992,4995,11430,24300,48610,92368,167950,293920,497410,817180,1307494]
   ```

## Recommended order

1. Post arXiv preprint.
2. Email OEIS editors with the cross-reference question (1-2 paragraph
   inquiry, not a submission). Wait for response.
3. Submit B_NEW (or comment on A000582, per editor guidance) referencing
   the arXiv DOI.
4. After acceptance, optionally submit A_NEW with B_NEW and A000582 as
   cross-references.

## Process note

A previous version of this file (now corrected) had:
- An off-by-one error in the closed-form formula (+10 instead of +9 in the
  binomial argument).
- Hand-computed terms that diverged from the formula at higher k.
- No cross-reference to A000582, presented as a fully novel sequence
  rather than a new interpretation of an existing one.

The reproducibility-first design of this version (every numerical claim
generated by Python execution against the formula, plus an explicit
cross-reference to A000582) addresses both failure modes. This file
is now ready for submission once the arXiv DOI is available; the
A000582 cross-reference is a courtesy to the OEIS editorial team,
since they would identify the relationship within minutes of receiving
a "new sequence" submission.
