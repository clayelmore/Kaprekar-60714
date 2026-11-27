# One length decides: a threshold for extended cores (2026-11-27)

Status: derived and machine-checked on 2026-11-27 by an AI model (Claude), then checked by one independent AI
referee pass with its own code (verdict: sound with fixable gaps; the gaps are fixed below, see Review at the
end). Not reviewed by a human mathematician. The proof reuses the lemmas of
`PROOF_146070.md` (Step 0 and Lemmas 0 to 3 and 2'), restated here for a core of any size N so that this
note can be read on its own.

Origin: in a conversation with the author on 2026-11-27, ChatGPT (OpenAI) asserted, without a written proof,
that a seed rule of m letters which is universal at length 2m + 19 stays universal at every greater length.
This note proves a statement of that kind with the smaller threshold 2N + 14, and records that for N = 6 and
N = 7 complete computation gives 2N + 9.

## Setting

Fix N >= 2 and two permutations a, b of {0, ..., N-1} (a *core*; the censuses use cores with a_i != b_i for
every i, but that is not needed here). Put c_i = 10^(a_i) - 10^(b_i) for i < N-1, x = a_(N-1), y = b_(N-1).
For d >= N let s_0 >= s_1 >= ... >= s_(d-1) be the digits of a d-digit string, leading zeros allowed, sorted
descending. The *extended rule* at length d is

    K_d(s) = | H + L |,
    H = sum_{k=N}^{d-1} 10^k g_(k-1),      g_j = s_j - s_(j+1) >= 0,
    L = c_0 s_0 + ... + c_(N-2) s_(N-2) - 10^y s_(N-1) + 10^x s_(d-1).

This is the difference of two rearrangements of the sorted digits: sorted digit i goes to place A(i) in the
first number and B(i) in the second, with A = (a_0, ..., a_(N-2), N, N+1, ..., d-1, a_(N-1)) and
B = (b_0, ..., b_(N-1), N, ..., d-1). At d = N it is the core's own rule. The identity
c_0 + ... + c_(N-2) + 10^x - 10^y = 0 holds because a and b are permutations of the same set.

A string is a *repdigit* if all its digits are equal. The rule is *universal at length d* if there is one
integer F != 0 with K_d(F) = F that every d-digit string other than a repdigit reaches under iteration of
K_d. The condition K_d(F) = F is part of the definition: a rule under which every start falls into one
common cycle of period 2 or more is not universal (the referee pass found such rules, for example the core
a = (0,1,2), b = (2,1,0) at lengths 20 and 21, where every start enters 495 -> 3105 -> 504 -> 495).

For a state write 9^t + R + zeros: t is the number of digits equal to 9, R the multiset of digits 1..8, and
sigma = t + |R| the number of nonzero digits.

## The lemmas, for general N

**Step 0 (shape of one step).** The gaps are digits, and all of them together sum to s_0 - s_(d-1) <= 9
(those that appear in H sum to s_(N-1) - s_(d-1)). L is the difference of two
nonnegative integers below 10^N (the first has the digits s_0, ..., s_(N-2), s_(d-1) at places
a_0, ..., a_(N-2), x; the second has s_0, ..., s_(N-1) at places b_0, ..., b_(N-1)), so |L| < 10^N. H is 0 or at least 10^N, so H + L > 0
whenever H > 0. Three cases: (i) H = 0: the image is |L|, with at most N digits. (ii) H > 0, L >= 0: places
0..N-1 hold L and place k >= N holds the gap g_(k-1). (iii) H > 0, L < 0: a borrow lowers the lowest nonzero
gap digit by one, writes 9 at every place between place N and it, and places 0..N-1 hold 10^N - |L|.

**Lemma 0 (a finite condition on the core).** H = 0 exactly when s_(N-1) = ... = s_(d-1), and then
K_d(s) = | c_0 s_0 + ... + c_(N-2) s_(N-2) + (10^x - 10^y) s_(N-1) |, the core's own value on the N sorted
digits (s_0, ..., s_(N-1)). Say the core *satisfies Lemma 0* if that value is 0 only when
s_0 = ... = s_(N-1). If the core satisfies Lemma 0, then at every length K_d(s) = 0 only for repdigits (when
H > 0 the value is at least 10^N - |L| > 0). If it does not, some non-repdigit maps to 0 at every length
d >= N (take the offending N digits and repeat the last one), so the rule is universal at no length.

**Lemma 1 (one step lands in a thin family).** For every s, K_d(s) = 9^t + R + zeros with |R| <= N + 9.
Proof: by Step 0 the nonzero digits other than a run of 9s written by the borrow are at most 9 gap digits
(their sum is at most 9) and at most N low digits.

**Lemma 2 (nine-count rule).** Let the state be 9^t + R + zeros with t >= N, not all 9s, and let m <= 8 be
its smallest digit. Then its image has exactly t - 1 - x digits equal to 9, plus one more if m = 8, and at
most 9 other nonzero digits.
Proof: s_0 = ... = s_(N-1) = 9 and s_(d-1) = m, so by the identity above
L = 9 (c_0 + ... + c_(N-2) - 10^y) + 10^x m = -10^x (9 - m) < 0. The state is not all 9s, so t < d, and the
lowest nonzero gap among those in H is g_(t-1) = 9 - s_t >= 1 at place t >= N; so H > 0 and case (iii) applies. The borrow writes t - N nines at places N..t-1 and lowers
g_(t-1) to at most 8. The low places hold 10^N - 10^x (9 - m): N - 1 - x nines at places x+1..N-1, the digit
1 + m at place x, zeros below. The other gaps sum to at most 8, so none is 9. Count of 9s:
(t - N) + (N - 1 - x) = t - 1 - x, plus one if 1 + m = 9. The other nonzero digits are the digit 1 + m (when
m <= 7) and the nonzero gap digits after the borrow, which sum to 9 - m - 1; so there are at most
1 + (8 - m) <= 9 of them.

**Lemma 3 (length-free dynamics).** If a state has a zero digit, then s_(d-1) = 0 and K_d(s) depends only on
the nonzero digits n_0 >= n_1 >= ... >= n_(sigma-1) of s:

    K_d(s) = | c_0 n_0 + ... + c_(N-2) n_(N-2) - 10^y n_(N-1) + sum_{j>=N} 10^j (n_(j-1) - n_j) |,

with n_j = 0 for j >= sigma. Call the induced map on multisets of nonzero digits Phi. It does not involve d.
For a multiset S of nonzero digits and any d >= max(|S| + 1, N), the nonzero digits of K_d(S + zeros) are
Phi(S).

**Lemma 4 (growth by at most one).** For a multiset S of nonzero digits with sigma elements, Phi(S) has at
most max(sigma + 1, N) elements.
Proof: if sigma < N then n_(N-1) = 0, H = 0, and the image is |L| < 10^N. If sigma >= N, the gap
n_(sigma-1) - 0 >= 1 sits at place sigma, so 10^sigma <= H <= 9 * 10^sigma (the gaps sum to at most 9 and
the top place is sigma), and 0 < H + L < 9 * 10^sigma + 10^N <= 10^(sigma+1).

## Seeds and the closure check

A *seed* is a nonempty multiset of nonzero digits with at most N - 1 nines and at most N + 9 other digits
(so sigma <= 2N + 8). The core *passes the closure check* if it satisfies Lemma 0 and there is one nonempty
multiset f with Phi(f) = f such that the Phi-orbit of every seed reaches f. This is the mathematical content
of test B in `censusN.c` and of `closure_all.c` (which use N = 6 and general N).

**Proposition 1 (orbits of seeds stay small).** Every multiset on the Phi-orbit of a seed has at most
2N + 13 elements.
Proof. Let S_0 be a seed and S_1 = Phi(S_0). By Lemma 4, sigma(S_1) <= 2N + 9, and by Lemma 1 (through
Lemma 3) S_1 has at most N + 9 digits other than 9. If S_1 has at most N - 1 nines it is a seed or empty.
Otherwise let t_1 >= N be its number of nines; t_1 <= sigma(S_1) <= 2N + 9. Follow S_(j+1) = Phi(S_j) while
t_j >= N. These states have a zero (Phi is the rule on states with a zero), so m = 0 in Lemma 2:
t_(j+1) = t_j - 1 - x <= t_1 - j, and S_(j+1) has at most 9 digits other than 9. Hence

    sigma(S_(j+1)) <= t_1 - j + 9 <= 2N + 18 - j,     and by Lemma 4     sigma(S_(j+1)) <= 2N + 9 + j.

The smaller of the two bounds is at most 2N + 13 for every j >= 1 (it equals 2N + 9 + j for j <= 4 and
2N + 18 - j for j >= 5). The nine-count drops at every step, so some S_j has at most N - 1 nines; it has at
most 9 other digits, so it is a seed or empty, and the argument starts again from it. The empty multiset is
fixed by Phi.

Remark. The bound is not claimed sharp. For cores with a_i != b_i for every i, the largest value seen in the
computations below is 2N + 9. The referee pass, which also ran cores with some a_i = b_i, saw 2N + 10 (for
cores with a_(N-1) = b_(N-1) = 0) and nothing larger, by complete enumeration of all seeds for N = 2, 3, 4
and by sampling for N = 5, 6.

**Proposition 2 (closure implies universality at long lengths).** If the core passes the closure check and M
is the largest number of elements of any multiset on the Phi-orbit of a seed (2N + 8 <= M <= 2N + 13: a seed
with 2N + 8 elements exists, and Proposition 1 gives the upper bound), then the extended rule is universal at
every length d >= M + 1, with the same F at all of them.
Proof. This is the assembly of `PROOF_146070.md`, section "General cores", written for N letters. Note
d >= M + 1 >= 2N + 9. Let s be a d-digit string that is not a repdigit.
(a) No image of a non-repdigit is a repdigit. It is not 0 by Lemma 0. It is not 9^d: 10^d - 1 is a
difference of two d-digit numbers only as (10^d - 1) - 0, and those are not rearrangements of one multiset.
It is not r^d with 1 <= r <= 8, because by Lemma 1 an image has at most N + 9 < d digits in 1..8.
(b) By Lemma 1 the first image is 9^t + R + zeros with |R| <= N + 9. While t >= N apply Lemma 2 (the state
is not all 9s by (a)): the nine-count becomes t - 1 - x, or t - x if the state has no zero and m = 8. So it
strictly decreases, except when x = 0, the state has no zero, and m = 8; in that case the image is
9^t + zeros (the other gaps are 0 and the low digit 1 + m is a 9), which has a zero because R was not empty,
so the count decreases at the next step. Hence some image has at most N - 1 nines. It has at most N + 9
other nonzero digits (Lemma 1), so its nonzero digits form a seed, with sigma <= 2N + 8 < d: it has a zero.
(c) From there on every state has at most M < d nonzero digits, so it has a zero, Lemma 3 applies at each
step, and the orbit of nonzero-digit multisets is the Phi-orbit of that seed. It reaches f. A state whose
nonzero digits are f maps to an integer G whose nonzero digits are again f, and K_d(G) = G because K_d
depends only on the digits. G = |V(f)| does not depend on d or on s, and G != 0 because f is not empty.
So F = G.

**Proposition 3 (universality at one long length implies closure).** If the extended rule is universal at
some length d* >= 2N + 14, the core passes the closure check.
Proof. Lemma 0 holds, by the last sentence of Lemma 0. Let S be a seed. The string S + zeros of length d* is
not a repdigit (it has a nonzero digit, and a zero because sigma <= 2N + 8 < d*). By Proposition 1 every
multiset on the Phi-orbit of S has at most 2N + 13 <= d* - 1 elements, so by induction with Lemma 3 the
nonzero digits of the K_(d*)-orbit of S + zeros are exactly the Phi-orbit of S. By universality that
K-orbit reaches F and stays there, so the Phi-orbit of S reaches the multiset f of nonzero digits of F, and
Phi(f) = f. F != 0, so f is not empty, and f is the same for every seed.

**Theorem (one length decides).** Let (a, b) be a core with N letters. The following are equivalent:
  (1) the extended rule is universal at some length d* >= 2N + 14;
  (2) the core passes the closure check;
  (3) the extended rule is universal at every length d >= 2N + 14, with one fixed integer F.
If they hold, the rule is universal with that same F at every length d >= M + 1 (and M + 1 >= 2N + 9).
Proof. (1) implies (2) by Proposition 3; (2) implies (3) and the last sentence by Propositions 1 and 2;
(3) implies (1) trivially.

In words: from length 2N + 14 on, whether the rule is universal does not depend on the length, and testing
one such length, or running the finite closure check, settles all of them. Lengths below 2N + 14 are not
covered and must be checked one by one; the audit has cores that are universal at length 7, not at 8 or 9,
and again from 10 on.

## What the theorem does not say

* It concerns one extension recipe (the one above). Other ways of lengthening a rule are not covered.
* It gives no way to decide the closure check without running it, and no way to construct a core with a
  prescribed endpoint.
* The threshold 2N + 14 comes from the bound 2N + 13 in Proposition 1, which is probably not sharp.

## Computed (machine checks, 2026-11-27)

* `threshold_lemma_checks.py` (direct subtraction of the two rearranged strings, no gap form; random cores
  with N = 4..8): Lemma 1 on 70,000 states, Lemma 2 on 70,000, Lemma 4 and Lemma 3 on 32,923 each, and
  Proposition 1 on 20,946 seed orbits. No failure. Largest nonzero count seen on a seed orbit: 2N + 9 for
  each N (17, 19, 21, 23, 25).
* `threshold_test.c` (`threshold_test_summary.txt`): for all 190,800 six-letter cores with a_i != b_i and all
  9,344,160 seven-letter ones, the reason the closure check fails and the largest nonzero count on the
  orbits that show the failure. Every failing core either fails Lemma 0, or the orbit of {1} runs into a
  cycle of period 2 or more, or the orbit of {1} reaches a fixed multiset and some seed runs into a cycle or
  into a different fixed multiset. In the last two cases the orbits involved (the failing seed's, and the
  orbit of {1} up to its fixed multiset) hold at most 2N + 8 nonzero digits (20 and 22), so they are orbits
  of the rule at every length d >= 2N + 9 and the rule is not universal there. The passing cores are exactly the
  551 and 22,426 of the audit (the 551 were rerun; the 22,426 were taken from `catalog_n7.tsv`). So for
  N = 6 and N = 7 the equivalence of the theorem holds from length 2N + 9 on for failing cores, and from
  M + 1 on for passing ones. This is a computation for those two sizes, not a proof for all N.
* `threshold_bruteforce.txt` (`censusN.c`, complete enumeration of every multiset; cores with a_i != b_i for
  every i only): for all 5,280 such five-letter cores, the cores universal at length 24 and at length 25 are
  the same 17, and they are exactly the 17 that pass the closure check. For N = 3 and N = 4 no such core is
  universal at any length tested (15 to 21, and 14 to 23) and none passes the closure check. (Cores with
  some a_i = b_i do pass: the referee pass found 2 of 36 at N = 3, 21 of 576 at N = 4 and 274 of 14,400 at
  N = 5, the 17 above among them.)
* All three programs count a rule as universal only if the common endpoint is a fixed point; a common cycle
  of period 2 or more counts as a failure.

## Review

One independent AI referee pass on 2026-11-27, with code written from scratch from the Setting section
(`referee_threshold_2026-11-27/`). Verdict: sound with fixable gaps. One real gap: the definition of
"universal" did not require K_d(F) = F, and under that wording Proposition 3 fails (counterexamples above,
rules whose starts all fall into one common cycle). Fixed by putting the fixed point into the definition.
The other findings were wording and scope: the N = 3, 4, 5 computed claims hold for cores with a_i != b_i
only; the largest orbit value is 2N + 10 once cores with a_i = b_i are allowed; Lemma 3 needs d >= N;
max(2N + 9, M + 1) is always M + 1. All are fixed above. The referee found nothing wrong in Step 0,
Lemmas 0 to 4, or Propositions 1 to 3 beyond these.
Referee computations: the gap form against direct subtraction on 236,000 states; Lemmas 1 to 4 on 110,000 to
236,000 states each; Proposition 1 on every seed of every core for N = 2, 3, 4 and of 136 and 44 sampled
cores for N = 5, 6 (nothing above 2N + 10); the Theorem end to end by brute force for every core with N = 2,
3, 4 at lengths up to 2N + 15 and for 86 cores with N = 5 at lengths 24 and 25, with no disagreement between
brute force and the closure check at any length d >= 2N + 14.
Not checked by the referee: the N = 6 and N = 7 computations of `threshold_test.c`, `censusN.c` itself, and
`PROOF_146070.md`. The edits made after the referee's report were not re-read by a referee.
