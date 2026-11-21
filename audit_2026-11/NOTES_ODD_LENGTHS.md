# Odd lengths: the passenger-digit rule (partial proof, 2026-11-21)

Status: PARTIAL. Sections 1-4 are proved and machine-checked (`oddpass.py`). Section 5 is an open conjecture
supported by complete enumeration. Not refereed. No human review.

## The rule G_n

Base b >= 3, n odd, n >= 3, strings of 2n+1 digits (leading zeros allowed). Sorted digits
s_0 >= s_1 >= ... >= s_2n. Put

    g   = s_{2n-1} - s_{2n}          (bottom gap)
    p   = s_0 - s_{2n-1}
    e_q = s_{2q-1} - s_{2q}          (q = 1..n-1; the neighboring pairs among letters 1..2n-2)

    G_n(s) = (b^n - 1) | p - b^n g - sum_q b^q e_q |.

As a word subtraction: the smallest letter sits at place 2n in word 1 and place n in word 2; letter 0 at
places n and 0; letter 2n-1 at places 0 and 2n; letter 2q-1 at places q and q+n; letter 2q at places q+n and q.
Every letter moves. n = 3 is GAF,E-D,C-B in the notation of `oddswap.c`.

How it comes from the even route: drop the smallest letter and the term b^n g. What is left,
E_n(s_0..s_{2n-1}) = (b^n - 1)|p - sum_q b^q e_q|, is a half-swap rule at length 2n. So

    G_n = E_n on the top 2n digits, minus b^n times the bottom gap.

The extra digit enters through one variable, g.

Note 0 <= g, p, e_q;  g + p = s_0 - s_2n <= b-1;  e_q <= s_1 - s_{2n-2} <= p.

## 1. Factorization and zeros (proved)

Each coefficient is a multiple of b^n - 1, giving the formula above. If V = p - b^n g - sum b^q e_q = 0 then
b | p, so p = 0, so s_0 = s_{2n-1}, so every e_q = 0, so g = 0: a repdigit. So G_n(s) = 0 exactly for repdigits.

## 2. One image shape (proved)

For a non-repdigit s, the digits of G_n(s) are a **triple** summing to b-1 plus n-1 complementary pairs:

* g = 0 and all e_q = 0:   {0, p-1, b-p} and n-1 pairs {0, b-1}.
* otherwise V < 0 (since b^n g + sum b^q e_q >= b > p) and m = b^n g + sum b^q e_q - p.
  - some e_q >= 1, lowest such q = q0:  triple {g, p, b-1-g-p};  pairs {y, b-1-y} with y = b-1 for q < q0,
    y = e_q0 - 1 for q = q0, y = e_q for q > q0.
  - all e_q = 0 (so g >= 1):  triple {g-1, p, b-g-p} and n-1 pairs {0, b-1}.

Proof. Write m = t b^n + r with 0 <= r < b^n. When p >= 1 the subtraction of p borrows from place q0 (or from
the b^n g term), which gives t and the digits y_q of r-1 as listed, with lowest digit y_0 = b-1-p, and r >= 1.
Then K = t b^{2n} + (r-1-t) b^n + (b^n - r). The low n digits are the complements of the digits of r-1. In the
middle block only the lowest digit changes, from y_0 to y_0 - t, and y_0 - t >= b-1-p-g >= 0, so there is no
borrow. Hence the digits are t, y_0 - t, p (the complement of y_0), and the pairs for q >= 1. When p = 0 all
e_q = 0 and m = b^n g, which gives the last line directly.  []

Unlike the family U_n of audit section 4.13, there is exactly one shape and no borrow variants.

## 3. The passenger identity (proved)

If s_{2n-1} = s_{2n} (g = 0) then G_n(s) = E_n(s_0, ..., s_{2n-1}), and the image is a 0 followed by the even
rule's 2n-digit image. Machine check: E_n is universal at lengths 6, 10, 14 with the same endpoint as G_n
(`halfswap.c`, base 10; length 10 also bases 3, 4, 5).

## 4. The endgame (proved)

Let S = strings containing at least two 0s and at least one b-1 (so g = 0 and p = b-1).

**Proposition.** Every s in S reaches F = (b^n - 1)(b^{k+1} + b^k - b + 1), k = (n-1)/2, in at most 4 steps, and
F is fixed. In base 10: 100899 (n = 3), 109098909 (n = 5), 109909989009 (n = 7).

Proof. By section 2 with g = 0, p = b-1, the image of s has triple {0, 0, b-1} (or is the first case, treated
below), so it is again in S and consists of two 0s, one b-1 and n-1 complementary pairs with deficits
d_1 <= ... <= d_{n-1} (deficit of {y, b-1-y} = min(y, b-1-y) <= (b-1)/2). For such a string
s_i = b-1-d_i and s_{2n-1-i} = d_i (i = 1..n-1), so with w_j = d_{2j} - d_{2j-1} (j = 1..k):

    e_q = w_q for q <= k,     e_q = w_{n-q} for q > k.

If some w_j >= 1, let J be the lowest. Section 2 gives the next deficits:
{0, 2(J-1) times} + {w_J - 1, w_J} + {w_j twice : j > J}. By the sorting lemma (PROOF_HALFSWAP.md 1.4) the new
w has exactly one entry 1 and the rest 0. Applying the same formula to such a w gives deficits {0, ..., 0, 1},
i.e. w = (0, ..., 0, 1) =: tau, and tau maps to itself. If all w_j = 0 the image is the first case of section 2
with p = b-1: digits 0, {b-2, 1} and pairs {0, b-1}, which is tau again. A string with state tau has
m = b^k + b^{n-k} - (b-1), so its image is F; and F has state tau. Count: s -> image -> one-1 state -> tau -> F.  []

Machine check (`oddpass.py`): sections 1-3 on every string for n = 3 (bases 3-12) and n = 5 (bases 3-6); from
every string in S the digit multiset of F is reached within 3 steps. Sampled strings in S for n = 3, 5, 7, 9 in
bases 3, 4, 10, 97, 1000 (20,000 each): F itself within 4 steps, never more.

## 5. What is not proved: the descent

**Conjecture.** Every non-repdigit reaches S (two 0s and a b-1) under G_n.

With section 4 this would give: G_n has the single endpoint F at every length 2n+1 = 7, 11, 15, ... in every base.

Evidence. Complete enumeration (`oddswap.c`): G_n is universal with endpoint F for n = 3, 5, 7 in bases 3, 4, 5,
7, 10, 13 (n = 3 also bases 6, 8, 9, 11, 12, 16). Sampling to base 10,000 for n = 3, 5, 7, 9: no failure.

Why this part is hard. The descent is a subtract-and-compare process, like Euclid's algorithm: each new digit
is a difference of two old ones. Its length grows like log b (sampled maximum, bases 10 / 100 / 1000 / 10000:
n = 3: 7, 18, 24, 29;  n = 5: 4, 8, 11, 14;  n = 7: 4, 6, 8, 11). The even-length proof worked because mirror
symmetry forced exact coincidences in a bounded number of steps; here the triple breaks the symmetry by two
free parameters. Candidate shrinking quantities tested on 50,000+ orbit steps each:
* sum of deficits, maximum deficit, b-1-p, and four others: all violated over 1 step and over 2 steps (n = 3, 5, 7).
* over 3 steps, the sum of deficits looked non-increasing at n = 5, 7 in a first sample. A larger sample found
  a counterexample at n = 5, base 97 (+7 over 3 steps). The lead as first stated is FALSE.
* Gap form. With gaps c_i = s_i - s_{i+1} (i = 0..2n-1) and W = s_0 - s_2n: e_q = c_{2q-1}, g = c_{2n-1},
  p = W - g. So the image consists of the odd-numbered gaps, their complements, W - g and b-1-W. The quantity
  T(s) = b-1 - (c_0 + c_2 + ... + c_{2n-2}) (odd gaps plus the wrap-around gap) did not increase over 3 steps
  in 115,000+ sampled orbit steps at n = 5 and 98,000+ at n = 7 (bases 97, 1000), and never over 4 steps.
  At n = 3 it increases over 3 and over 4 steps (172 and 130 cases in 183,847). Observation only.
* Mechanism seen in the data: a gap can be copied into both halves of the next image (the total can nearly
  double in one step), and the two copies cancel one or two steps later. Any proof has to span several steps.

## 5b. Odd-length numbers by padding (proved, but a different process)

Leading zeros are allowed in `PROOF_HALFSWAP.md`, so its theorem already covers odd-length inputs: write the
2n-1 digit number with one leading zero and run the even rule R_n at length 2n. Every nonzero number reaches
(b-1)(b^n - 1) in at most 7 steps (n even), b/3 + 9 (n odd >= 5) or b/2 + 10 (n = 3). In base 10: 5-digit
numbers reach 8991, 7-digit numbers 89991, 9-digit numbers 899991. Checked by complete enumeration for lengths
5, 7, 9 in base 10, lengths 5, 7 in base 7, length 5 in base 16, length 7 in base 13 (maximum 4 to 7 steps).
This is not an odd-length rule: the working length is 2n, and the padded zero is treated like any other digit.
The intrinsic question (a rule that keeps 2n+1 places and moves every letter) is the conjecture of section 5.

On the "halves" picture (.5, 1, 1, .5): within a fixed odd length the three-letter rotation is already that
arrangement. One letter (2n-1) occupies both end places, 0 and 2n, and two letters share the middle place n.
Its cost is the triple of section 2. A mirror-symmetric odd image would need a digit equal to its own
complement, (b-1)/2, which exists only in odd bases. Splitting the wrap-around gap b-1-W into its two ends,
(b-1-s_0) and s_2n, gives 2n+2 intervals with a true mirror symmetry, but every rule here depends only on
differences of digits, so it sees only the sum of those two halves.

## 6. Negative results from the search (all by computation)

* No odd-length rule examined finishes in a bounded number of steps. True orbit depths (`oddscan.py`,
  `oddswap/depth_n4.txt`) grow with the base for all 22 length-7 rules and for the best of the 1,401 length-9
  rules; the average depth grows like log b for every length-7 rule. (The `maxsteps` printed by `oddswap.c`
  and `halfswap.c` is a path length to an already-visited state, not a depth; do not use it.)
* U_n of section 4.13 has depth growing linearly in b (114 steps at base 800, n = 3).
* Adding a passenger digit to a universal even rule does not always give a universal odd rule: at length 9,
  base 10, 14 even rules have the pair (A, H) at place 0, 25 odd rules have the passenger form, and only 8 match.
  At length 7 the match is exact in bases 7-11 and 16 (4 and 4).
* n even: the neighboring-pair rule above is not universal in every base at length 9. The working length-9 passenger rules
  use the pair (1, 2n-2) (e.g. IAH,G-B,F-E,D-C); no general-n family for even n has been tested yet.
