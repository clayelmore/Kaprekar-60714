# One scheme for every length >= 6, even and odd, in every base >= 3 (proof, 2026-11-21)

Status: derived 2026-11-21. Machine-checked as listed at the end. Refereed the same day by an independent AI
pass (`referee_fixedmiddle/`): verdict "sound, with fixable gaps", no mathematical error and no counterexample;
its four presentation gaps are fixed below. No human review yet. The even half is `PROOF_HALFSWAP.md`; this file proves the odd half and states the
combined theorem.

## Combined statement

Fix a base b >= 3 and a length L >= 6. Put h = ceil(L/2). Write the L digits (leading zeros allowed) sorted
descending as letters s_0 >= s_1 >= ... . Both words of the subtraction are arrangements of the letters, and

    place q is exchanged with place q + h, for every q with q + h < L.

* L = 2h (even): all places are paired. This is the half-swap rule R_h of `PROOF_HALFSWAP.md`.
* L = 2h - 1 (odd): the middle place h-1 has no partner (h-1+h = L is not a place). The letter put there stays
  there in both words and cancels, exactly as the middle digit does in Kaprekar's three-digit routine
  (ABC - CBA, constant 495). The rule M_n below (n = h-1) puts the second-largest digit s_1 there.

**Theorem.** For every b >= 3 and L >= 6, every L-digit string that is not a repdigit reaches

    F = (b-1)(b^h - 1),      h = ceil(L/2),

and F is fixed. Repdigits map to 0. In base 10: lengths 7 and 8 give 89991, lengths 9 and 10 give 899991,
lengths 11 and 12 give 8999991.

**Why odd lengths cannot be done exactly like even ones.** A rule is a permutation pi of the places (the
letter at place a in word 1 is at place pi(a) in word 2). "Every place is exchanged with one partner" means pi
is an involution without fixed points, which exists only on an even number of places. On an odd number of
places every permutation has a fixed point or a cycle of odd length >= 3. So an odd-length rule must either
keep one letter in place (this file) or rotate three or more letters (the three-letter rotation of
`NOTES_ODD_LENGTHS.md`, whose images carry a triple instead of a pair and whose proof is still open).

## The rule M_n (length 2n+1, n >= 3)

Letters s_0 >= ... >= s_2n. Let (P_q, M_q), q = 0..n-1, be the pairs of R_n (`PROOF_HALFSWAP.md`), written on
letters 0..2n-1, and relabel them by r(0) = 0, r(i) = i+1 for i >= 1. Word 1 has letter r(P_q) at place q+n+1
and r(M_q) at place q; word 2 the reverse; letter 1 is at place n in both. So

    M_n(s) = (b^{n+1} - 1) |V|,     V = sum_q b^q (s_{r(P_q)} - s_{r(M_q)}).

Explicitly (indices are letters of the 2n+1 digit string):
* n odd, n = 2k+1:   place 0: (n+1, n+2);  place 1: (0, 2n);  place 2: (n, n-1);
  for j = 1..k-1:  place n+1-2j: (2j+1, 2j);  place n-2j: (2n-2j, 2n+1-2j).
* n even, n = 2k+2:  place 0: (n-1, n);  place 1: (2, 2n);  place 2: (0, 2n-1);  place 3: (n+2, n+1);
  for j = 1..k-1:  place n+1-2j: (2j+2, 2j+1);  place n-2j: (2n-1-2j, 2n-2j).

n = 3 in letters: word 1 = D A E B C G F, word 2 = C G F B D A E.

## 1. Common part

**1.1 Size and zeros.** Each difference lies in [-(b-1), b-1], so m := |V| <= b^n - 1. If V = 0 then every
difference is 0 (the lowest nonzero one would survive modulo b^{q+1}). For n odd the pair (0, 2n) then gives
s_0 = s_2n. For n even the pairs (0, 2n-1) and (2, 2n) give s_0 = s_{2n-1} and s_2 = s_2n, hence all equal.
So m = 0 exactly for repdigits.

**1.2 Shape of an image.** For a non-repdigit put N = m - 1, 0 <= N <= b^n - 2, with n digits x_{n-1}..x_0.
Then M_n(s) = N b^{n+1} + (b^{n+1} - 1 - N). The low n+1 digits are the complements of N written with n+1
digits, so they are b-1 (at place n, the complement of a leading 0) and b-1-x_i. The digits of the image are

    one digit b-1,  and the pairs {x_i, b-1-x_i}, i = 0..n-1.

With deficits r(x) = min(x, b-1-x), sorted rho_1 <= ... <= rho_n (0 <= rho_i <= H := floor((b-1)/2)):

    s_0 = b-1,     s_i = b-1-rho_i (i = 1..n),     s_{2n+1-i} = rho_i (i = 1..n).

No image is a repdigit (it contains b-1 and a pair {x, b-1-x}, and x = b-1 forces the digit 0). The state after
one step is the multiset rho. F has N = b-2, state tau = (0, ..., 0, 1).

**1.3 Comparison with the even rule.** The ignored letter 1 is b-1-rho_1. Under r, the letters used are
s_0 = b-1, then b-1-rho_2, ..., b-1-rho_n, rho_n, ..., rho_1. That is the even image of `PROOF_HALFSWAP.md` 1.3
with one change: its letter 0 has the value b-1 instead of b-1-rho_1. So V is the even rule's V with the single
term containing letter 0 increased by rho_1 times its place value.

**1.4 Sorting lemma** (as in `PROOF_HALFSWAP.md` 1.4). If a multiset consists of values each taken an even
number of times plus one extra a and one extra a+1, then sorting and pairing consecutive entries gives exactly
one pair with difference 1 and all others 0.

## 2. n odd, n = 2k+1

**2.1 Reduced map.** Put w_j = rho_{2j+1} - rho_{2j} (j = 1..k) and A = b-1-rho_1 (so (b-1)/2 <= A <= b-1,
and r(A) = rho_1). By 1.3 and `PROOF_HALFSWAP.md` 2.1,

    V = b A - (b^2 - 1) w_k - sum_{j<k} w_j (b-1) b^{n-2j}.

The digit computations of that section use only 0 <= A <= b-1 and 1 <= w_j <= H (true here, since
w_j <= rho_n - rho_2 <= H), so they apply unchanged; the digit at place 1 is b-1-A = rho_1:
* (G) some w_j >= 1, J the largest such j:

      rho' = { (w_j - 1)^+ twice : j < J } + { w_J - 1, w_J } + { 0, 2(k-J) times } + { rho_1 }.

* (Z) all w_j = 0: m = b A with A >= 1, N = (A-1) b + (b-1), rho' = { 0 (n-1 times), r(A-1) }.

tau is fixed (rho_1 = 0, w_k = 1). A string with state tau has V = b(b-1) - (b^2-1), m = b-1, image F.

**2.2 From rho_1 = 0, at most 2 steps to tau.** (Z): A = b-1, rho' = {0^{n-1}, r(b-2)} = tau. (G): rho'
contains rho_1 = 0; the other n-1 values satisfy 1.4 with a = w_J - 1, so exactly one w'_j is 1 and the rest
are 0, and rho'_1 = 0. One more (G) step gives {0,...} + {0, 1} + {0,...} + {0} = tau.

**2.3 Bad states.** Call a state bad if rho_1 >= 1 and every w_j >= 2. If rho_1 >= 1 and the state is not bad,
then rho' contains a 0: in (Z) because n-1 >= 2; in (G) because J < k, or w_J = 1, or some w_j <= 1 with j < J.

**2.4 Bad runs.** In a bad state J = k and rho' = {(w_j - 1) twice : j < k} + {w_k - 1, w_k} + {rho_1}.
Every w_j <= rho_n - rho_2 <= rho_n - 1, and rho_1 <= rho_2 <= rho_3 - w_1 <= rho_n - 2. Hence
max(rho') <= rho_n - 1: the largest deficit drops by at least 1 at every bad step. A bad state has
rho_n >= rho_2 + 2 >= 3, so a run of bad states has length at most max(0, H - 2). (For H = 1, i.e. b = 3 or 4,
there are no bad states.)

**2.5 Assembly.** First step to a state; a bad run (at most H - 2 steps); one step to rho_1 = 0 (2.3), unless
already there; at most 2 steps to tau (2.2); one step to F. For H >= 2 that is at most H + 3 <= b/2 + 3 steps.
For H = 1 a state with rho_1 >= 1 is (1, ..., 1), case (Z) with A = b-2: its image is tau (b = 4) or the
all-zero state, which maps to tau (b = 3). So at most 4 steps, again within b/2 + 3.

## 3. n even, n = 2k+2

**3.1 Reduced map.** Put w_j = rho_{2j+2} - rho_{2j+1} (j = 1..k), sigma = b-1-rho_1-rho_2, h = r(sigma),
and sigma2 = b-1-rho_2 (so r(sigma2) = rho_2 and sigma2 >= 1). Place 1 is (2, 2n): s_2 - s_2n = sigma. Place 2
is (0, 2n-1): s_0 - s_{2n-1} = sigma2. Places 0 and 3 give +w_k and -w_k; for j < k places n+1-2j and n-2j
give -w_j and +w_j. So

    V = b^2 sigma2 + b sigma - (b^3 - 1) w_k - sum_{j<k} w_j (b-1) b^{n-2j}.

b^2 sigma2 + b sigma <= b^3 - b < b^3 - 1 < (b-1) b^4, so V < 0 as soon as some w_j >= 1, and for 1 <= w <= H:
(b^3-1) w - b^2 sigma2 - b sigma = (w-1) b^3 + (b-1-sigma2) b^2 + (b-1-sigma) b + (b-w).
* (G) some w_j >= 1, J the largest. If J = k the digits of N at places 3..0 are (w_k - 1, b-1-sigma2,
  b-1-sigma, b-1-w_k), with deficits w_k - 1, rho_2, h, w_k. If J < k then w_k = 0 and N = (blocks) -
  (b^2 sigma2 + b sigma + 1); the subtrahend is below b^3 and the block of J ends in a digit b - w_J >= 1 at
  place n-2J >= 4, so that digit drops to b-1-w_J, every place between becomes b-1, and places 2, 1, 0 become
  b-1-sigma2, b-1-sigma, b-1. Either way:

      rho' = { (w_j - 1)^+ twice : j < J } + { w_J - 1, w_J } + { 0, 2(k-J) times } + { h, rho_2 }.

* (Z) all w_j = 0: m = b^2 sigma2 + b sigma > 0. If sigma >= 1: N = sigma2 b^2 + (sigma-1) b + (b-1) and
  rho' = { 0 (n-2 times), rho_2, r(sigma-1) }. If sigma = 0: N = (sigma2-1) b^2 + (b-1) b + (b-1) and
  rho' = { 0 (n-1 times), r(sigma2-1) }.

tau is fixed (rho_1 = rho_2 = 0, h = 0, w_k = 1): rho' = {0, 1} + {0, 0} + zeros. A string with state tau has
V = b^2(b-1) + b(b-1) - (b^3-1) = -(b-1), image F.

**3.2 From rho_2 = 0, at most 2 steps to tau.** Then rho_1 = 0, sigma = b-1, h = 0. (Z): rho' =
{0^{n-2}, 0, r(b-2)} = tau. (G): rho' contains h = rho_2 = 0 twice; the other n-2 values satisfy 1.4, so
exactly one w'_j is 1, the rest 0, and rho'_2 = 0. One more (G) step gives {0,...} + {0,1} + {0,...} + {0,0} = tau.

**3.3 Bad states.** Call a state bad if rho_2 >= 1, w_j >= 2 for all j < k, w_k >= 1, and not (w_k = 1 and
h = 0). If rho_2 >= 1 and the state is not bad, rho' contains two 0s, so rho'_2 = 0: in (Z) there are at least
n-2 >= 2 zeros; in (G) either J < k (two zeros from 2(k-J)), or some w_j <= 1 with j < J (twice), or w_k = 1
and h = 0. A bad state is in case (G) with J = k:

    rho' = { (w_j - 1) twice : j < k } + { w_k - 1, w_k } + { h, rho_2 }.

Write Lam = rho_n and mu = rho_2 for a state, and note h <= rho_1 + rho_2 <= 2 mu.

**3.4 Bad runs, n >= 6 (k >= 2).** sum_j w_j <= rho_n - rho_3 <= Lam - mu and every w_j >= 1, so
max_j w_j <= Lam - mu - 1. Hence Lam' <= max(Lam - mu - 1, 2 mu). Also rho' contains w_1 - 1 twice and
w_k - 1, w_k, so mu' = rho'_2 <= min(w_1 - 1, w_k), and 2 mu' <= w_1 + w_k - 1 <= Lam - mu - 1.
If the states at times t and t+1 are bad:

    Lam_{t+2} <= max(Lam_{t+1} - mu_{t+1} - 1, 2 mu_{t+1}) <= max(Lam_{t+1} - 2, Lam_t - mu_t - 1)
              <= max(Lam_t, Lam_{t+1}) - 2.

With t, t+1, t+2 bad this gives max(Lam_{t+2}, Lam_{t+3}) <= max(Lam_t, Lam_{t+1}) - 2. So in a run of R bad
states starting at t_0, Lam_{t_0+2i} <= H - 2i while 2i <= R-1. A bad state has Lam >= rho_3 + sum w_j >= 4,
so R <= H - 2 <= H.

**3.5 Bad runs, n = 4 (k = 1).** rho = (rho_1, .., rho_4), w = rho_4 - rho_3 >= 1, rho' = {w-1, w, h, rho_2}.
Let the states at t and t+1 be bad. Claim: Lam_{t+2} <= Lam_t - 1. Lam_{t+2} = max(w', h', rho'_2), where:
* rho'_2 <= w (rho' contains w-1 and w), and w <= Lam - rho_3 <= Lam - 1.
* h' <= rho'_1 + rho'_2 <= (w-1) + rho_2 <= rho_4 - rho_3 - 1 + rho_2 <= Lam - 1 (the two smallest of rho' sum
  to at most the sum of any two of its entries).
* w' = rho'_4 - rho'_3. If rho'_4 = h: rho'_3 >= max(w, rho_2), so w' <= rho_1 + rho_2 - rho_2 = rho_1 <= rho_2
  <= rho_3 <= Lam - 1. Otherwise w' <= rho'_4 <= max(w, rho_2) <= Lam - 1.
So Lam_{t_0+2i} <= H - i while 2i <= R-1; a bad state has Lam >= 2, hence R <= max(0, 2H - 2) <= b - 3 (b >= 3; for b = 3, 4 there is no bad state with Lam >= 2).

**3.6 Assembly.** First step; a bad run (at most H steps for n >= 6, at most b-3 for n = 4); one step to
rho_2 = 0 (3.3) unless already there; at most 2 steps to tau (3.2); one step to F. At most b/2 + 5 steps
(n >= 6) or b + 2 (n = 4).  QED

## Machine checks

* `midfix_family.py`: on every (2n+1)-digit string the direct rule agrees step by step with the reduced maps
  and reaches F: n = 3 (bases 3-9), n = 4 (3-7), n = 5 (3-5), n = 6 (3-4).
* `midfix_checks.py`: statements 2.2, 2.3, 2.4, 3.2, 3.3, 3.4, 3.5 on the reduced map, from every state with
  deficits in [0, H] where there are at most 150,000 states and 60,000 sampled states otherwise: n = 3..11,
  bases 3-11, 16, 17, 40, 41, 200, 1001. No violation. Longest bad run seen: 500 (n = 4, b = 1001), 9 (n = 3),
  6 or fewer for n >= 5.
* `midfix.c` (independent C enumeration of every digit multiset): M_n has the single endpoint (b-1)(b^{n+1}-1)
  for n = 3, 4, 5, 6 in bases 3, 4, 5, 7, 10, 13 and n = 7 in bases 3, 4, 5, 7 (`midfix/familyM_check.txt`).
* Referee's independent code (`referee_fixedmiddle/`, word 1 - word 2 on actual digit strings): every
  non-repdigit reaches F for n = 3 (bases 3-14, 16, 20, 24, 30, 40), n = 4 (3-10, 12, 14, 16, 20), n = 5 (3-11),
  n = 6 (3-9); reduced maps and every inequality on every deficit state for n = 3 (to b = 301), 4 (to 121),
  5 (to 41), 6 (to 31), 7 (to 21), 8 (to 17), and on samples at b = 300, 301. The bound of 3.5 is attained at
  n = 4, b = 5; for n = 4 the longest bad run is H or H - 1 (corrected 2026-11-25: it is H - 1 at b = 20 and b = 40, H at b = 5, 7, 10, 11, 12, 30).
* Length 9 census (all 362,880 fixed-middle rules, bases 4, 7, 10): 5,224 rules have one endpoint in all three;
  160 end at (b-1)(b^5-1); the fixed letter is never the largest or the smallest digit.
* Census (`midfix.c`, all 5,040 fixed-middle rules at length 7, bases 3-12 and 16): 48 rules have one endpoint
  in every base; 6 of them end at (b-1)(b^4-1); in all 48 the fixed letter is s_1 or s_2. At length 5 no
  fixed-middle rule works in every base (none at all in bases 7, 9, 10, 11, 12, 16).

## Remarks

* The value of the fixed letter s_1 cancels, while its sorted rank stays fixed. (Changing an input digit can
  change which digit is second largest, and so can change the output.) An outside review (2026-11-21, separate
  session, own code: all 112 pairs L = 6..13, b = 3..16, 145,346,906 non-repdigit multisets; reduced maps on
  105,531,098 states) returned "sound" with these two wording clarifications only.
* Stated plainly: This is the same feature as the middle digit of Kaprekar's
  odd-length routine, and by the parity argument above it (or a longer rotation) cannot be avoided.
* Fixing the largest letter s_0 instead would make the odd reduced map identical to the even one, but then
  strings whose other 2n digits are all equal (for example 9111111) would map to 0. Fixing s_1 avoids that.
* Lengths 2 to 5 are excluded: no rule of these kinds works in every base there.
