# A Kaprekar-type constant at every even length >= 6 in every base >= 3 (proof, 2026-11-21)

Status: derived 2026-11-21, machine-checked as listed at the end. Refereed the same day by an independent AI
pass (`referee_halfswap/`): verdict "sound with fixable gaps"; the one real gap (section 1.5) and two minor
ones are fixed below. Its own code found no counterexample for n = 3..8. No human review yet.

## Statement

Fix a base b >= 3 and n >= 3; work with strings of 2n digits (leading zeros allowed). Write the digits sorted
descending as letters s_0 >= s_1 >= ... >= s_{2n-1}. A **half-swap rule** is a partition of the 2n letters
into n ordered pairs (P_q, M_q), q = 0..n-1. Word 1 puts letter P_q at place q+n and M_q at place q; word 2
does the reverse; the rule is K(s) = |word 1 - word 2|. Every letter moves exactly n places.

**The rule R_n.**
* n odd, n = 2k+1:   place 0: (n, n+1);  place 1: (0, 2n-1);  place 2: (n-1, n-2);
  and for j = 1..k-1:  place n+1-2j: (2j, 2j-1);  place n-2j: (2n-1-2j, 2n-2j).
* n even, n = 2k+2:  place 0: (n-2, n-1);  place 1: (1, 2n-1);  place 2: (0, 2n-2);  place 3: (n+1, n);
  and for j = 1..k-1:  place n+1-2j: (2j+1, 2j);  place n-2j: (2n-2-2j, 2n-1-2j).

In letters: n = 3 is CADBFE - BFECAD; n = 4 is FABCEGHD - EGHDFABC; n = 5 is CHEAFBIDJG - BIDJGCHEAF.

**Theorem.** For every b >= 3 and n >= 3, every 2n-digit string that is not a repdigit reaches
F = (b-1)(b^n - 1) under iteration of R_n, and F is fixed. In base b, F is (b-2)(b-1)...(b-1)1 with n-1 digits
b-1; in base 10 it is 8991, 89991, 899991, ... Repdigits map to 0. The number of steps is at most 7 for n even,
at most b/3 + 9 for n odd >= 5, and at most b/2 + 10 for n = 3.

## 1. Common part

**1.1 Factorization.** K(s) = (b^n - 1) m with m = |V|, V = sum_q b^q (s_{P_q} - s_{M_q}), since each pair
contributes (b^{q+n} - b^q)(s_P - s_M).

**1.2 Size and zeros.** Each difference lies in [-(b-1), b-1], so m <= (b-1)(1 + b + ... + b^{n-1}) = b^n - 1.
If V = 0 then every difference is 0 (look at the lowest q with a nonzero difference: V would be nonzero
modulo b^{q+1}). R_n contains the pair (0, 2n-1) (n odd), or the pairs (0, 2n-2) and (1, 2n-1) (n even), so all
differences zero forces s_0 = s_{2n-1} (for n even: s_0 = s_{2n-2} makes letters 0..2n-2 equal, and
s_1 = s_{2n-1} adds the last one): a repdigit. So m = 0 exactly for repdigits.

**1.3 Shape of an image.** For a non-repdigit, 1 <= m <= b^n - 1. Put N = m - 1, with n digits x_{n-1}..x_0.
Then K = N b^n + (b^n - 1 - N): the digits of K are the x_i and their complements b-1-x_i. Define the
**deficit** of a digit x as r(x) = min(x, b-1-x), and let rho_1 <= ... <= rho_n be the sorted deficits of
x_0..x_{n-1}. Then 0 <= rho_i <= H := floor((b-1)/2), and the sorted digits of K are

    s_{i-1} = b-1-rho_i  (i = 1..n),      s_{2n-i} = rho_i  (i = 1..n).

So after one step the state is the multiset rho, and we may compute the next state from it. A state is a
repdigit only if all rho_i = (b-1)/2 (b odd). The value F has N = b-2, so its state is tau = (0,...,0,1).

**1.4 A sorting lemma.** Let a multiset consist of values each taken an even number of times, together with one
extra copy of a and one extra copy of a+1 (a >= 0). Sort it and pair consecutive entries (1st,2nd), (3rd,4th),
... Then exactly one pair has difference 1 and all other pairs have difference 0. (Values below a fill whole
pairs; a occurs an odd number of times, so the last a is paired with the first a+1; the remaining copies of a+1
and everything above fill whole pairs.)

**1.5 No image is a repdigit.** By 1.3 a repdigit image would be c^{2n} with c = (b-1)/2, b odd, i.e.
m = (b^n+1)/2. Later images are never of this form: a (G) image (sections 2.1, 3.1) contains w_J - 1 and w_J,
which differ, and a (Z) image contains at least two zeros while c >= 1. For the first image, write
d_q = s_{P_q} - s_{M_q} for an arbitrary sorted string, so V = sum_q b^q d_q with |d_q| <= b-1, and suppose
V = +-(b^n+1)/2. Note b = 2c+1 and (b^n+1)/2 has base-b digits c, ..., c, c+1.
* n odd: d_0 = s_n - s_{n+1} >= 0, d_1 = s_0 - s_{2n-1} >= 0, d_2 = s_{n-1} - s_{n-2} <= 0, and
  d_0 + |d_2| <= d_1 (two disjoint gaps inside the full range). Reading V modulo b, b^2, b^3 with these signs:
  V > 0 forces d_0 = c+1, d_1 = c, d_2 = -(c+1); V < 0 forces d_0 = c, d_1 = c, d_2 = -(c+1). Either way
  d_0 + |d_2| >= 2c+1 > c = d_1. Contradiction.
* n even: d_0 = s_{n-2} - s_{n-1} >= 0, d_1 = s_1 - s_{2n-1} >= 0, d_2 = s_0 - s_{2n-2} >= 0,
  d_3 = s_{n+1} - s_n <= 0, and d_0 + |d_3| <= s_{n-2} - s_{n+1} <= d_1. V > 0 forces d_0 = c+1, d_1 = c, but
  d_0 <= d_1. V < 0 forces d_0 = d_1 = d_2 = c, d_3 = -(c+1), so d_0 + |d_3| = 2c+1 > d_1. Contradiction.
(Each "forces": the residue of the remaining quotient modulo b has exactly two representatives in
[-(b-1), b-1], one of each sign, and the sign is known.)

## 2. n odd, n = 2k+1

**2.1 Reduced map.** For a state rho put w_j = rho_{2j+1} - rho_{2j} (j = 1..k), A = b-1-2 rho_1 (so
0 <= A <= b-1), and g = min(2 rho_1, b-1-2 rho_1) = r(A). Substituting 1.3 into the pairs:
place 1 gives +A; places 0 and 2 give +w_k and -w_k; for j < k places n+1-2j and n-2j give -w_j and +w_j. So

    V = b A - (b^2 - 1) w_k - sum_{j<k} w_j (b-1) b^{n-2j}.

Here b A <= b(b-1) < b^2 - 1 < (b-1) b^3, so V < 0 as soon as some w_j >= 1, and then
m = sum_{j<k} w_j (b-1) b^{n-2j} + (b^2-1) w_k - b A. The blocks do not overlap (j < k occupies places n-2j and
n+1-2j >= 3, the last three terms occupy places 0..2), and for 1 <= w <= H:
w(b-1) = (w-1) b + (b-w), and (b^2-1) w - b A = (w-1) b^2 + (b-1-A) b + (b-w).

* (G) Some w_j >= 1. Let J be the largest such j.
  - If J = k: N = m - 1 lowers the last digit b - w_k to b-1-w_k. The digits of N are (w_j - 1, b - w_j) for each
    j < k with w_j >= 1, (0, 0) for each j < k with w_j = 0, and (w_k - 1, b-1-A, b-1-w_k).
  - If J < k: w_k = 0, and N = (extras) - b A - 1. The block of J ends in the digit b - w_J >= 1 at place n-2J >= 3,
    and b A + 1 < b^3, so the borrow lowers that digit to b-1-w_J and turns every lower place into b-1 except
    place 1, which becomes b-1-A.
  In both cases the deficits of N are

      rho' = { (w_j - 1)^+ twice : j < J }  +  { w_J - 1, w_J }  +  { 0, 2(k-J) times }  +  { g }

  (n values in all; for J < k the zeros come from the blocks J < j < k and from places 0 and 2).
* (Z) All w_j = 0. Then A >= 1 (A = 0 with all w_j = 0 means all rho_i = (b-1)/2, a repdigit), m = b A,
  N = (A-1) b + (b-1), and rho' = { 0 (n-1 times), r(A-1) }.

tau is fixed: rho_1 = 0, w_k = 1, J = k, rho' = {0,...,0} + {0, 1} + {0} = tau. The value after state tau has
V = b(b-1) - (b^2-1), m = b-1, i.e. it is F; and F has state tau, so F is fixed.

**2.2 From rho_1 = 0, at most 2 steps to tau.** If rho_1 = 0 then g = 0 and A = b-1.
(Z): rho' = {0^{n-1}, r(b-2)} = tau since b >= 3. (G): rho' contains g = 0, so rho'_1 = 0; removing that zero,
the rest is as in Lemma 1.4 with a = w_J - 1, so exactly one w'_j equals 1 and the others are 0. Apply (G) again:
rho'' = {0,...} + {0, 1} + {0,...} + {0} = tau.

**2.3 A step with rho_1 >= 1 gives rho'_1 = 0 unless it is bad.** Call a state *bad* if rho_1 >= 1 and
w_j >= 2 for all j. If the state is not bad and rho_1 >= 1, rho' contains a 0: in (Z) because n-1 >= 2; in (G)
because J < k, or w_J = 1, or some w_j <= 1 with j < J. (If all w_j >= 2 then J = k.)

**2.4 Bad runs are finite.** In a bad state J = k and rho' = {(w_j - 1) twice : j < k} + {w_k - 1, w_k} + {g}.
* n = 3 (k = 1). rho' = {w-1, w, g}: this is exactly the map of `PROOF_ALLBASE_D6.md` Step 4 (there
  mu = b-1-rho, with the same w and A). If g <= w-1 (its case (i)) then rho' = (g, w-1, w) has w' = 1, which is
  not bad. So a step from a bad state to a bad state is of its type (ii), and its Step 7 bounds a run of such
  steps by (b+5)/2. Hence at most (b+7)/2 consecutive bad states.
* n >= 5 (k >= 2). Write lam = rho_1 and Lam = rho_n of a state. sum_j w_j <= rho_n - rho_2 <= Lam - lam, and
  each w_j >= 2, so max_j w_j <= Lam - lam - 2(k-1) and min_j w_j <= (Lam - lam)/k. Also g <= 2 lam. Hence, for
  a bad state followed by state ',

      Lam' = max(rho') <= max( Lam - lam - 2(k-1), 2 lam ),      lam' = min(rho') <= min_j w_j - 1 <= (Lam - lam)/k - 1.

  If the states at times t and t+1 are both bad, then with k >= 2 and lam >= 1:
  Lam_{t+2} <= max( Lam_{t+1} - lam_{t+1} - 2, 2 lam_{t+1} ) <= max( Lam_{t+1} - 3, Lam_t - lam_t - 2 )
  <= max(Lam_t, Lam_{t+1}) - 3. Applying this at t and t+1 (states t, t+1, t+2 bad),
  M_{t+2} <= M_t - 3 for M_t = max(Lam_t, Lam_{t+1}). With R consecutive bad states starting at t_0 this gives
  Lam_{t_0+2i} <= H - 3i for 2i <= R-1. A bad state has Lam >= 1 + 2k >= 5, so i <= (H-5)/3 and
  R <= 2(H-5)/3 + 2 < 2H/3 + 4 <= b/3 + 4.

**2.5 Assembly (n odd).** A non-repdigit maps to a state (1.2, 1.3). While the state is bad, step; the run
ends (2.4). The next step lands on rho_1 = 0 (2.3), or the state already has rho_1 = 0. Then at most 2 steps to
tau (2.2), and one more step gives F (2.1). Steps: 1 + run + 1 + 2 + 1.

## 3. n even, n = 2k+2

**3.1 Reduced map.** Put w_j = rho_{2j+2} - rho_{2j+1} (j = 1..k), sigma = b-1-rho_1-rho_2 (0 <= sigma <= b-1),
h = r(sigma). From 1.3: places 1 and 2 both give +sigma (s_0 - s_{2n-2} = s_1 - s_{2n-1} = sigma); places 0 and 3
give +w_k and -w_k; for j < k places n+1-2j and n-2j give -w_j and +w_j. So

    V = (b^2 + b) sigma - (b^3 - 1) w_k - sum_{j<k} w_j (b-1) b^{n-2j}.

(b^2+b) sigma <= b^3 - b < b^3 - 1 < (b-1) b^4, so V < 0 as soon as some w_j >= 1 (blocks with j < k sit at
places >= 4). For 1 <= w <= H: (b^3-1) w - (b^2+b) sigma = (w-1) b^3 + (b-1-sigma) b^2 + (b-1-sigma) b + (b-w).

* (G) Some w_j >= 1, J the largest. As in 2.1 (the borrow of (b^2+b) sigma + 1 < b^4 stops at the block of J),

      rho' = { (w_j - 1)^+ twice : j < J } + { w_J - 1, w_J } + { 0, 2(k-J) times } + { h, h }.

* (Z) All w_j = 0. Then sigma >= 1 (sigma = 0 with all w_j = 0 forces rho_1 = rho_2 = (b-1)/2 and hence a
  repdigit), m = (b^2+b) sigma, N = sigma b^2 + (sigma-1) b + (b-1), and
  rho' = { 0 (n-2 times), r(sigma), r(sigma-1) }.

tau is fixed (rho_1 = rho_2 = 0, sigma = b-1, h = 0, w_k = 1), and the value after tau has
V = (b^2+b)(b-1) - (b^3-1) = -(b-1), so it is F.

**3.2 After one reduced step, every w_j is 0 or 1 and at most one is 1.** In (G), rho' satisfies Lemma 1.4
with a = w_J - 1 (h occurs twice); the pairs defining w' are the pairs of 1.4 other than the first. In (Z),
the only pair that can be nonzero is the top one, and |r(sigma) - r(sigma-1)| <= 1.

**3.3 From rho_1 = rho_2 = 0, at most 2 steps to tau.** Then sigma = b-1, h = 0. (Z): rho' = {0^{n-2}, 0, r(b-2)}
= tau. (G): rho' contains two zeros (h, h) and by 3.2 has all w' in {0,1} with at most one 1; one more step,
(Z) or (G), gives tau as just computed ((G): {0,...} + {0,1} + {0,0}).

**3.4 Reaching rho_1 = rho_2 = 0.** Take a state that already satisfies 3.2 (any state after one reduced step).
* n >= 6 (k >= 2): (Z) gives n-2 >= 2 zeros. (G) with the single w_J = 1 gives rho' = {0, 1} + zeros + {h, h}
  with 2(k-1) + 1 >= 3 zeros. Either way rho'_1 = rho'_2 = 0.
* n = 4 (k = 1): (Z) gives {0, 0, ., .}. (G) with w = 1 gives {0, 1, h, h}: if h = 0 this is tau; if h >= 1 it
  is (0, 1, h, h) with w' = 0, and the next step (Z) gives {0, 0, ., .}.

**3.5 Assembly (n even).** First step to a state; one reduced step to reach 3.2; at most 1 more (n >= 6) or 2
more (n = 4) to reach rho_1 = rho_2 = 0; at most 2 to tau; 1 to F. At most 6 steps (n >= 6) or 7 (n = 4).  QED

## Machine checks

* `halfswap_family.py`, `halfswap_even.py`: on every 2n-digit string, the direct rule agrees step by step with
  the reduced maps above and reaches F: n = 3 (bases 3-8), 5 (3-6), 7 (3-4); n = 4 (3-9), 6 (3-5), 8 (3).
* The reduced maps, from every admissible state (or 100,000+ sampled states where there are too many):
  n = 3..15 odd and 4..14 even, bases 3 to 1001: all reach tau. Longest bad run observed: 12 (n=3, b=1001),
  9 (n=5), 5 (n=7); even n: 2 (n=4), 1 (n>=6).
* Inequality 2.4 on 218,674 sampled bad runs (n = 5, 7, 9; bases 20 to 5000): no violation.
* `halfswap.c` (direct enumeration of every digit multiset, independent C code): R_n is universal with endpoint
  (b-1)(b^n-1) for n = 3, 5, 7 in bases 3, 4, 5, 7, 10, 13 (and 16 for n = 3, 5); n = 9 in bases 3, 4, 5, 7, 10;
  n = 4, 6 in bases 3, 4, 5, 7, 10, 13; n = 8 in bases 3, 4, 5, 7, 10.

## Remarks

* Lengths 2 and 4 are excluded for a reason: the census of all half-swap rules found none universal at length 2
  in any base, and none universal in every base at length 4.
* Odd lengths are not covered: a half-swap needs an even number of digits.
* The rule changes with the length (it is a family, one rule per n), unlike 146070's single extended rule.
