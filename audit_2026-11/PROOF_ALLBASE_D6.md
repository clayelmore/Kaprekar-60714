# A six-digit Kaprekar-type constant in every base b >= 3 (proof, 2026-11-21)

Status: derived 2026-11-21. Refereed the same day by an independent AI pass (`referee_allbase/`): verdict
"sound with fixable gaps", all gaps fixed below; its own code confirms the direct rule for every six-digit
string in bases 3..80. The reduced map is machine-checked for bases 3..200. No human review yet.
Scope: length 6 only. The same rule extended to lengths 7 and up is tested but NOT proved (see the end).

## Statement

Fix a base b >= 3. For a six-digit string (leading zeros allowed) let s0 >= s1 >= ... >= s5 be its digits
sorted descending, written as letters A..F. Define

    K(s) = | EABDFC - DFCEAB |
         = | (b^4 - b) s0 + (b^3 - 1) s1 - (b^3 - 1) s2 - (b^5 - b^2) s3 + (b^5 - b^2) s4 - (b^4 - b) s5 |.

**Theorem.** Every six-digit string that is not a repdigit reaches F = (b-1)(b^3-1) under iteration of K, and
F is fixed. In base b, F has digits (b-2)(b-1)(b-1)1; in base 10, F = 8991. The number of steps is at most
b/2 + 10. Repdigits map to 0.

## Proof

Write p = s0 - s5, u = s1 - s2, v = s3 - s4. These are >= 0 and u + v <= p <= b - 1.

**Step 1 (factorization).** Grouping the six terms in pairs,

    K(s) = (b^3 - 1) * m,    m = | b p + u - b^2 v |.

**Step 2 (m = 0 only for repdigits).** If b p + u = b^2 v then b divides u, so u = 0 (as u <= b-1); then
p = b v, so v = 0 and p = 0 (as p <= b-1), i.e. s0 = s5.

**Step 3 (shape of an image).** m <= max(b(b-1) + (b-1), b^2 (b-1)) < b^3, so for a non-repdigit
1 <= m <= b^3 - 1. Put n = m - 1, with base-b digits (x, y, z). Then K = (b^3-1) m = n b^3 + (b^3 - 1 - n), so the
six digits of K are x, y, z and their complements b-1-x, b-1-y, b-1-z. Let fold(t) = max(t, b-1-t) and

    M = { fold(x), fold(y), fold(z) } = { mu1 >= mu2 >= mu3 },   each mu_i >= (b-1)/2.

Sorted, the digits of K are (mu1, mu2, mu3, b-1-mu3, b-1-mu2, b-1-mu1). So for an image,
p = 2 mu1 - (b-1) =: A,   u = v = mu2 - mu3 =: w,   and the next value has m' = | b A - (b^2 - 1) w |.
Here 0 <= A <= b-1 and 0 <= w <= floor((b-1)/2); also A has the parity of b-1 and 2w <= A. The state after
the first step is the pair (A, w). (For b even, A is odd, so the pair (0,0) cannot arise at all.)

**Step 4 (the map on (A, w)).**
* w = 0, A >= 1: m' = b A, n' = (A-1) b + (b-1), digits (0, A-1, b-1), so M' = { b-1, b-1, fold(A-1) } and
  (A', w') = ( b-1, b-1 - fold(A-1) ).
* w >= 1: (b^2-1) w >= b^2 - 1 > b(b-1) >= b A, so m' = (b^2-1) w - b A and
  n' = (w-1) b^2 + (b-1-A) b + (b-1-w), digits (w-1, b-1-A, b-1-w). Since w <= (b-1)/2,
  fold(w) = b-1-w and fold(w-1) = b-w. With Y = fold(A), M' = { b-w, b-1-w, Y }. Two cases, exhaustive because
  Y is an integer:
  - (i)  Y >= b-w:    (A', w') = ( 2Y - (b-1), 1 ).
  - (ii) Y <= b-1-w:  (A', w') = ( b+1-2w, b-1-w-Y ).
* (A, w) = (0, 0) is the repdigit ((b-1)/2)^6 (b odd). It is never an image: no case above produces it
  (w' = 1 in (i); A' >= 1 in (ii) and when w = 0), and it is not a first image, because that would need
  m = (b^3+1)/2. With m = b p + u - b^2 v <= b^2 - 1 this is too small; with m = b^2 v - b p - u, reducing
  2m = b^3 + 1 modulo b twice gives u = (b-1)/2, p = (b-1)/2, v = (b+1)/2, contradicting u + v <= p.

**Step 5 (the target).** T = (A, w) = (b-1, 1): Y = fold(b-1) = b-1 >= b - w, case (i), image (b-1, 1). Fixed.
F itself is fixed: its sorted digits are (b-1, b-1, b-2, 1, 0, 0), so p = b-1, u = v = 1, m = b(b-1) + 1 - b^2
in absolute value = b-1, and K(F) = (b-1)(b^3-1) = F. (Several multisets M give the state T, namely
{ b-1, c, c-1 }; the Assembly handles that.)

**Step 6 (everything outside long chains reaches T fast).**
* (a) A = b-1: if w = 0 the image is (b-1, b-1-fold(b-2)) = (b-1, 1) = T (b >= 3). If w >= 1 then Y = b-1, case
  (i), image T. One step.
* (b) w = 0, A >= 1: image has A' = b-1, then (a). Two steps.
* (c) w = 1: if Y = b-1, case (i) gives T. Otherwise Y <= b-2, case (ii) gives (b-1, b-2-Y), then (a). At most two steps.
* (d) w >= 2, case (i): image has w' = 1, then (c). Three steps.

**Step 7 (chains of case (ii) are finite).** Suppose states k-1, k, k+1 are consecutive, with both steps of
type (ii). Then A_k = b+1-2w_{k-1}, so fold(A_k) = max(b+1-2w_{k-1}, 2w_{k-1}-2), and

    w_{k+1} = b-1-w_k-fold(A_k) = -w_k + min(2w_{k-1} - 2, b+1-2w_{k-1}).

With omega_k = w_k - (b+3)/4 this reads

    omega_{k+1} + omega_k = -2 - 2 |omega_{k-1}|.

Hence |omega_k| + |omega_{k+1}| >= 2 + 2|omega_{k-1}|, so max(|omega_k|, |omega_{k+1}|) >= |omega_{k-1}| + 1.
The identity holds for k = 1..L-1 in a run sigma_0, ..., sigma_L of L type-(ii) steps. Choose indices
j_0 = 0 < j_1 < ... with j_{t+1} in { j_t + 1, j_t + 2 } and |omega_{j_{t+1}}| >= |omega_{j_t}| + 1; this is
possible while j_t + 2 <= L, and j_t <= 2t, so j_t exists for every t <= floor(L/2), with |omega_{j_t}| >= t.
But 0 <= w <= (b-1)/2 gives |omega| <= (b+3)/4. Hence floor(L/2) <= (b+3)/4 and L <= (b+5)/2.

**Assembly.** Take a non-repdigit. Its image is a state (A, w) != (0,0) (Steps 2-4). Follow type-(ii) steps
while they last; by Step 7 the run ends, at a state with w = 0 or in case (i). By Step 6 it then reaches T in
at most 3 more steps. A value whose state is T need not be F itself (the state records only the folded
digits), but its image has m' = |b(b-1) - (b^2-1)| = b-1, i.e. it is exactly F = (b-1)(b^3-1). Total:
1 + (b+5)/2 + 3 + 1 steps, which is at most b/2 + 10.  QED

## Machine checks (`allbase_d6.py`)

* The reduction (Steps 1-4) agrees with the direct rule on every six-digit string, bases 3..12.
* The reduced map sends every admissible multiset M to T, bases 3..200. Observed maximum number of steps after
  the first: 5 at b = 10, 7 at b = 20, 9 at b = 50, 11 at b = 100..200. Observation only: growth looks
  logarithmic in b, so Step 7's linear bound is far from sharp.
* Referee's independent direct-rule run (`referee_allbase/ref_d6.c`), bases 3..80: every non-repdigit reaches F,
  maximum steps 3 (b=3..5), 6 (b=10), 8 (b=18..30), 10 (b=34..78), 11 (b=79..80).

## What is not proved

The census extends a six-letter rule to length d > 6 by adding sum_{k>=6} b^k (s_{k-1} - s_k) and moving the
closing coefficient. For this rule that gives, with h = s5 - s_{d-1},

    K_d(s) = | sum_{k>=6} (b^k - b) g_{k-1} + (b^3 - 1)(b p + u - b^2 v) |,

which is no longer a multiple of b^3 - 1, so the argument above does not apply. Evidence for d >= 7: the
all-lengths check passes in bases 4..10, and brute force finds no failure in bases 3, 11, 13-17, 19, 24, 36 at
lengths up to 8-22 (`bases/verify20_b*.txt`). Universality at every length in every base is a conjecture.
