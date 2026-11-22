# Factor family: a small-table criterion and a lifting theorem (2026-11-21)

Status: derived 2026-11-21. Machine checks are listed in section 4. Refereed the same day by an independent AI
pass (`referee_factor_lift/`, own code on digit strings, 2,258 complete enumerations in bases 2, 4, 6, 8, 10,
no counterexample): verdict "sound with fixable gaps"; its points (definition of universal, step count,
orientation convention, labeling of the class-C counts) are fixed below. No human review. Sections 1 and 2 hold for every half-swap rule; section 3 is the new theorem.
What this does NOT give: endpoints of arbitrary shape. Every endpoint here is a multiple of b^n - 1.

## 0. Setting

Base b, length 2n, strings with leading zeros allowed. Letters s_0 >= s_1 >= ... >= s_{2n-1} are the digits
sorted descending. A **half-swap rule** assigns the 2n letters to slots (P_q, M_q), q = 0..n-1: word 1 has
letter P_q at place q+n and letter M_q at place q, word 2 the reverse. Then

    K(s) = |word 1 - word 2| = (b^n - 1) m,    m = |V|,    V(s) = sum_q b^q (s_{P_q} - s_{M_q}).

The assignment is a bijection: every letter is in exactly one pair. Reversing every pair changes V to -V and
gives the same rule. "Universal with endpoint F" means: F is not 0, K(F) = F, and every non-repdigit string
reaches F under iteration of K.

In sections 2 and 3 the base b is **even**. Odd bases need extra care (a string made of the digit
(b-1)/2 is its own mirror image) and are not covered.

## 1. Two facts about every half-swap rule (any base)

These are sections 1.2 and 1.3 of `PROOF_HALFSWAP.md`, which use nothing about the particular rule R_n.

**1.1 Zero lemma.** V(s) = 0 if and only if s_{P_q} = s_{M_q} for every q.
Proof. Each d_q = s_{P_q} - s_{M_q} lies in [-(b-1), b-1]. If some d_q is nonzero, take the lowest such q;
then V is congruent to b^q d_q modulo b^{q+1}, which is not 0. QED

**1.2 Gap cover.** Say the rule **covers gap j** (j = 0..2n-2) if some pair has min(P_q, M_q) <= j <
max(P_q, M_q). Then: K(s) = 0 only for repdigits  <=>  the rule covers every gap.
Proof. (<=) If V(s) = 0, every pair has equal letters (1.1). For a gap j covered by a pair with letters
u <= j < v, s_u = s_v and sortedness give s_j = s_{j+1}. Every gap is covered, so all letters are equal.
(=>) If gap j is not covered, the string with j+1 ones followed by zeros has every pair on one side of the gap,
so V = 0, and it is not a repdigit. QED

**1.3 Shape of an image.** If m >= 1 then m <= b^n - 1 (each |d_q| <= b-1). Put N = m - 1, with n digits
x_{n-1} .. x_0. Then K = N b^n + (b^n - 1 - N): the digits of K are the x_i followed by their complements
b-1-x_i. Define the deficit r(x) = min(x, b-1-x) and let rho_1 <= ... <= rho_n be the sorted deficits of the
x_i. The sorted digits of K are

    s_{i-1} = b-1-rho_i,      s_{2n-i} = rho_i      (i = 1..n).

Call rho the **state** of K. The state determines the sorted digits, hence the next image. There are
C(n + H, n) states, H = floor((b-1)/2).

## 2. The small-table criterion (b even)

For b even, 0 <= rho_i <= (b-2)/2 < b/2 <= b-1-rho_j, so the string built from a state is never a repdigit.
For a rule that covers every gap, define T(rho) = state of K(string of rho). T maps states to states.

**Criterion.** For b even, a half-swap rule is universal if and only if
(a) it covers every gap, and
(b) there is a state tau with T(tau) = tau that every state reaches under T.
The endpoint is then F = (b^n - 1) |V(tau)|.

Proof. Suppose (a), (b). Let G = K(string of tau). G has state T(tau) = tau, so its sorted digits are those of
the string of tau, hence K(G) = G. A non-repdigit s has K(s) != 0 by (a) and 1.2; K(s) is a string with some
state rho (1.3); its later images have states T(rho), T^2(rho), ..., which reach tau; the image after a string
of state tau is G. Conversely, a universal rule sends no non-repdigit to 0 (0 is a repdigit and maps to 0), so
(a) holds by 1.2; and every state is the state of a non-repdigit string, whose orbit reaches F, so every state
reaches the state of F, which is fixed. QED

So in base 10 a rule on 8 digits is settled by a table of 70 states, on 10 digits by 126, on 12 by 210, on 14
by 330, on 16 by 495, instead of all digit multisets (24,310; 92,378; 293,930; ...).

## 3. The lifting theorem (b even)

**Class C.** A half-swap rule at length 2n, oriented by the global sign, is in class C if
* (S) V(rho) > 0 for every state rho (V computed on the string of rho);
* (U) some state tau is fixed by T and reached from every state;
* (C1) for every state rho with rho_1 >= 1, the state T(rho) contains a 0.

(S) makes T defined on every state. Class C does not ask the seed to cover every gap, and the theorem does
not need it: a seed that fails gap cover is not universal itself, but its lifts are. (C1) says: an image whose digits avoid 0 and b-1 is followed by an image
that has a 0 and a b-1.

**The two lifts.** From a rule at length 2n build rules at length 2n+2, with letters s_0 .. s_{2n+1}:
* top lift: old pair (P_q, M_q) becomes (P_q + 1, M_q + 1) at the same place q; the new pair at place n is
  (P, M) = (0, 2n+1).
* bottom lift: old pair (P_q, M_q) becomes (P_q + 1, M_q + 1) at place q+1; the new pair at place 0 is
  (P, M) = (2n+1, 0).

In both, the new largest and new smallest letters form the new pair and the old rule acts on the 2n letters in
between.

**Theorem.** Let b be even and let a rule of class C at length 2n have fixed state tau and m* = V(tau),
N* = m* - 1 (written with n digits). Then both lifts are in class C at length 2n+2 and are universal, with
* top lift: m' = (b-1) b^n + m*, i.e. N' = (b-1) followed by N*;
* bottom lift: m' = b m* - (b-1), i.e. N' = N* followed by 0.

Consequently, applying i top lifts and j bottom lifts in any order gives a universal rule at length
2(n+i+j) whose endpoint is F = N followed by its digit complement, where

    N = (b-1)^i  N*  0^j      (i digits b-1, then the n digits of N*, then j zeros).

In particular a rule of class C that covers every gap is itself universal (section 2), and it yields a
universal rule at every longer even length.

**Proof.** Let mu = (mu_1 <= ... <= mu_{n+1}) be a state at length 2n+2. Write x = mu_1 and
rho = (mu_2, ..., mu_{n+1}). By 1.3 the string of mu has s_0 = b-1-x, s_{2n+1} = x, and its inner letters
t_j = s_{j+1} (j = 0..2n-1) satisfy t_{i-1} = b-1-rho_i and t_{2n-i} = rho_i for i = 1..n. So the inner letters
are exactly the string of the state rho at length 2n, and the old pairs, shifted by one letter, compute V(rho).
Put A = s_0 - s_{2n+1} = b-1-2x. Since b is even, A is odd, so 1 <= A <= b-1. By (S), 1 <= V(rho) <= b^n - 1;
write V(rho) = m_rho and N_rho = m_rho - 1, an n-digit string whose sorted deficits are T(rho).

Top lift. V'(mu) = b^n A + V(rho) > 0. So m' = b^n A + m_rho and N' = m' - 1 = b^n A + N_rho: the digit A
followed by the n digits of N_rho.

Bottom lift. V'(mu) = b V(rho) - A >= b - (b-1) > 0. So m' = b m_rho - A and
N' = b (m_rho - 1) + (b-1-A), with 0 <= b-1-A <= b-2: the n digits of N_rho followed by the digit b-1-A.
(m' <= b (b^n - 1) - 1 < b^{n+1}, so N' has n+1 digits.)

In both cases the new state is

    T'(mu) = { phi(mu_1) }  together with  T(mu_2, ..., mu_{n+1}),     phi(x) = r(b-1-2x)       (*)

because r(A) = r(b-1-A). Note phi(0) = r(b-1) = 0.

(S) for the lift: shown above (V' > 0).
(C1) for the lift: if mu_1 >= 1 then rho_1 >= 1, so T(rho) contains a 0 by (C1), and so does T'(mu) by (*).
(U) for the lift: let tau' = {0} together with tau. Take any state mu.
  - If mu_1 >= 1, then T'(mu) contains a 0, as just shown. So after at most one step the smallest deficit is 0.
  - If mu_1 = 0, then by (*) T'(mu) = {0} together with T(rho). Its smallest element is 0, and removing one
    copy of 0 leaves the multiset T(rho). By induction on k, T'^k(mu) = {0} together with T^k(rho). By (U),
    T^k(rho) = tau for some k, so T'^k(mu) = tau'; and T'(tau') = {0} together with T(tau) = tau'.
Gap cover for the lift: the new pair has letters 0 and 2n+1, so it covers every gap.
So the lift is in class C, and by section 2 it is universal. Its endpoint comes from the state tau', where
x = 0 and A = b-1: top lift m' = (b-1) b^n + m*; bottom lift m' = b m* - (b-1), N' = b N*. The statement for
i top and j bottom lifts follows by induction, since each lift is again in class C: a top lift prepends the
digit b-1 to N, a bottom lift appends the digit 0, and these two operations commute.  QED

**Step count.** If every state of the seed reaches tau in at most D steps of T, every state of a lift reaches
tau' in at most D + 1 steps (one step to get a 0, then D). A string with state tau' has the digits of F but
need not be F, so one more application may be needed. So after i + j lifts every non-repdigit reaches F in at
most D + i + j + 2 applications of K (first image, D + i + j state steps, one more to land on F). The referee
found this bound attained.

**Remark (what (C1) is for).** Without (C1) the lift can still be universal, but that is then a separate
finite check at the new length and it does not propagate. In the base-10 census, 384 of the 520 universal rules
at 8 digits have a universal top lift at 10 digits (each rule oriented so that V > 0 at its fixed state; 120
of the 520 are not sign-definite, so this convention matters), yet none of the 520 is in class C.

## 4. What was computed (base 10 unless stated)

`factor_family.py` (census by the criterion of section 2), `factor_classZ.py` (class C), `factor_to_order.py`
(rule for a chosen endpoint), `factor_brute.py`, `factor_allbase.py`, `factor_lift.py`; outputs in `factor/`.

| length | rules covering every gap (up to sign) | universal | m fixed by some rule | m with a universal rule | class C and covering every gap: rules | endpoints |
|---|---|---|---|---|---|---|
| 4 | 8 | 0 | 0 | 0 | 0 | 0 |
| 6 | 240 | 12 | 94 | 6 | 0 | 0 |
| 8 | 14,208 | 520 | 1,772 | 136 | 0 | 0 |
| 10 | 1,355,520 | 71,390 | 35,020 | 9,524 | 5,590 | 688 |

Class C as defined (gap cover not required) is larger; counted by the referee: 76 rules with 24 fixed states
at 8 digits (none universal itself; all 152 lifts are among the 5,590), and 10,862 rules with 1,364 fixed
states at 10 digits. Other even bases (referee): class C at 6 and 8 digits has 76 and 4,664 rules in base 4,
10 and 1,648 in base 6, 6 and 248 in base 8.

These are complete enumerations of the family at each length; each "universal" is a proof by the table of
section 2 for that length and base 10.

Checks of the theorem (not part of the proof):
* 400 class-C rules at 10 digits, each lifted twice in all four orders (3,200 lifted rules at 12 and 14
  digits): the complete state table gives the predicted endpoint every time.
* `factor_brute.py`: 6 class-C rules, with both lifts at 12 digits and four two-level lifts at 14 digits,
  42 runs of `univcheck` (every digit multiset, independent C code that knows nothing of states): all PASS.
* The census numbers agree with `halfswap.c` of section 4.12 of the audit where they overlap (12 rules up to
  sign at 6 digits = 24 with sign; the tool reproduces the 2 census rules for m = 1675).

Example. Endpoint 6870031299 = 99999 x 68701 at 10 digits: DHFBIJGECA - JGECADHFBI (class C; table in
`factor/cert_68701.txt`, 126 states, at most 9 steps from a state). By the theorem, with new largest letter
first and new smallest letter in the middle (top lift), 968700031299 at 12 digits, 99687000031299 at 14,
and so on; with the bottom lift 687000312999 at 12 digits, and mixed forms such as 96870000312999.

## 5. Limits, stated plainly

* Endpoints are multiples of b^n - 1 of the form N followed by its complement. 5445 at 9 digits and
  1657575000000 are not of this form at their lengths, so this does not explain them.
* Seeds are found by search. There is no recipe that produces a class-C rule for a given N*; at 10 digits 688
  of the 99,999 possible m have one that is itself universal. The lifts only add digits 9 on the left of N and 0 on the right.
* Base 10 (and even bases) only. Across bases the family is poor: at 6 and 8 digits the rules that are
  universal in every base tested (7 to 16, then 22, 31, 50, 97, 200) number 12 and 112, and all their
  endpoints are arrangements of one digit multiset (b-2, 1, n-1 digits b-1, n-1 zeros). See
  `factor/allbase_n3.txt`, `factor/allbase_n4.txt`. "Every base tested" is not "every base".
  At 10 digits the picture widens: 21,641 rules show no failure in a complete census of bases 7-13 and 16 plus
  sampled states in bases 22 to 640, with 189 endpoint digit patterns (`factor/allbase_sampled_n5.txt`).
  That is sampling, not proof.
* Odd bases are not covered by sections 2 and 3.
