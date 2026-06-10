---
title: "Universal Fixed Points of Generalized Kaprekar Routines: Two Liftings and the Cost of a Convergence Proof"
author: "Clay Elmore"
date: "2026"
abstract: |
  Sorting the digits of a $d$-digit integer and subtracting one rearrangement from another defines a family of $d!\,(d!-1)$ maps at each length, of which Kaprekar's descending-minus-ascending routine is one. We study the integers these maps fix, with the emphasis on what can be proved. A finite-state criterion reduces universality — every admissible input iterates to the fixed point — to the conjunction of fixed-point uniqueness and acyclicity, and an exhaustive census locates all universal full-variable fixed points at lengths $d \leq 6$: there are $0$, $4$, $33$, and $506$ of them, and exactly one of the thirty-three at $d=5$, the integer $60714$, is again universal at $d=6$. Two liftings raise universality across dimension. Zero-padding extends $60714$ to every length $d \geq 5$, with a proof that runs on an absorbing set built from its zero digits. Digit duplication, formalized here as a folding operation on rules, governs the multisets $\{1,4,6,7\}^m$: folding provably preserves the fixed-point equation at every multiplicity, and complete enumerations show it preserves universality often — all eight universal rules at $d=4$ double universally to $d=8$, and $144$ of the $312$ universal pair-symmetric rules at $d=8$ double universally to $d=16$. The folds of a single four-digit rule, the one fixing $1746$, give universal fixed points at multiplicities $2$, $4$, and $5$, the last a complete enumeration of all $10{,}014{,}995$ multisets at $d=20$, where only proxy evidence existed before; a folded twelve-digit rule is universal at $d=24$ ($38{,}567{,}090$ multisets). Whether $\{1,4,6,7\}^m$ carries a universal fixed point at every $m$ remains open; we prove that the obstruction begins at the base of the chain, where the classical four-digit convergence admits no polynomial Lyapunov function of degree six or less — though, correcting a natural first reading, one of degree exactly seven exists. The paper closes with a map of the proof strategies that fail, and why.
---

## Introduction

Kaprekar observed in 1949 that the map which sorts the digits of a four-digit integer into descending and ascending order and subtracts sends every input with at least two distinct digits to $6174$, in at most seven steps [Kaprekar 1955]. The three-digit analogue converges to $495$ [Trigg 1974]; the five-digit analogue converges to nothing, every orbit falling into one of three cycles [Prichett 1981]. For seventy-five years these facts have been verified the same way they were discovered, by finite enumeration, and the absence of any other proof is not an accident of neglect. Part of the purpose of this paper is to make that absence precise.

The classical routine is one member of a large family. Fix a length $d$, pad integers to $d$ digits, and let any ordered pair of distinct permutations rearrange the sorted digit string before the subtraction. This yields $d!\,(d!-1)$ maps at each length. Within the family, the question "which integers are fixed?" splits into a hierarchy of sharper questions — fixed by what, attracting how much, persisting to which lengths — and the answers organize themselves around two phenomena that this paper develops in parallel.

The first is *selection*. Universality — every admissible input reaching the fixed point — is rare, and universality that survives a change of length is rarer. An exhaustive census at $d \leq 6$ (Section 3) finds four universal full-variable fixed points at $d=4$, thirty-three at $d=5$, five hundred six at $d=6$; of the thirty-three, exactly one, $60714$, is universal again at $d=6$. That one survivor then extends to every length (Section 4), by a lifting whose proof mechanism — an absorbing set built out of the zeros that padding creates — is worth isolating, because it is precisely the mechanism the second half of the paper lacks.

The second phenomenon is *duplication*. The multiset $\{1,4,6,7\}$ of the digits of $6174$ can be taken with multiplicity $m$, giving a $4m$-digit problem, and universal fixed points of $\{1,4,6,7\}^m$ exist at every $m \leq 6$ — this is known by enumeration, and the present paper extends and sharpens the computational record, including the first complete-basin verification at $d=20$. The natural conjecture, that they exist at every $m$, is open. Section 5 introduces a folding operation that makes the algebraic half of the duplication story a theorem at all $m$, and Section 6 reports the central computational finding of this paper: folding preserves universality often — every measured doubling step has survival fraction $100\%$ or $46\%$ — and the folds of one four-digit rule give fully verified universal fixed points at multiplicities $1, 2, 4, 5$, with a single twelve-digit rule covering $3$ and $6$. The pattern of *which* folds survive is nonetheless irregular, and Section 7 explains the difficulty of converting abundance into a proof for all $m$: the base case of the chain — Kaprekar's own theorem — has no light certificate. We prove that no polynomial Lyapunov function of degree $\leq 6$ exists for the four-digit gap dynamics, by exact Farkas certificates, and that degree $7$ is exactly where one appears. The difficulty of the duplication conjecture is then located not in any single length but in the absence of anything *uniform in $m$* to transport.

Throughout, claims carry one of four labels. **Proven** means a mathematical proof appears here. **Computed** means a finite exhaustive enumeration, machine-verified; unless marked otherwise, every such enumeration was re-run independently for this paper (Section 8 details the few exceptions, marked [S], which are taken from the project's computational log). **Evidence** means a claim that passes every feasible test but whose state space exceeds exhaustive reach. **Conjectured** means exactly that.

## Rules, coefficients, and the universality criterion

Fix $d \geq 2$. For an integer $n$ with at most $d$ digits, write $\mathrm{sort}_\downarrow(n) = (s_0, \dots, s_{d-1})$ for its digits padded to length $d$ and sorted descending. For a permutation $\tau \in S_d$ let $\tau \cdot s$ denote the integer $\sum_k 10^{\,d-1-k} s_{\tau(k)}$.

**Definition 2.1.** *For an ordered pair $(\pi, \sigma) \in S_d \times S_d$ with $\pi \neq \sigma$, the rule $K_{\pi,\sigma}$ acts by*
$$K_{\pi,\sigma}(n) \;=\; \bigl|\, \pi \cdot \mathrm{sort}_\downarrow(n) \;-\; \sigma \cdot \mathrm{sort}_\downarrow(n) \,\bigr|.$$
*The classical Kaprekar map is the pair (identity, reversal).*

Since the rule reads $n$ only through its sorted digits, orbits live on digit multisets, and all state counts below are multiset counts. Expanding the difference,
$$K_{\pi,\sigma}(n) = \Bigl|\, \sum_{i=0}^{d-1} c_i\, s_i \,\Bigr|, \qquad c_i = 10^{\,d-1-\pi^{-1}(i)} - 10^{\,d-1-\sigma^{-1}(i)}, \qquad \sum_i c_i = 0.$$
The coefficient vector $c$ determines the dynamics completely and is how rules are specified below; note that $c$ and $-c$ induce the same map, so rules come in sign pairs with identical dynamics.

**Lemma 2.2.** *(Proven.) (a) $K_{\pi,\sigma}(n) \equiv 0 \pmod 9$ for every rule and every input. (b) The rules with $c_i \neq 0$ for all $i$ — the* full-variable *rules — number $d!\,D_d$, where $D_d$ is the number of derangements of $d$ letters: $12$, $216$, $5{,}280$, $190{,}800$ at $d = 3,4,5,6$.*

*Proof.* (a) Each $c_i$ is a difference of two powers of $10$, and $10^a \equiv 1 \pmod 9$. (b) $c_i = 0$ exactly when $\pi^{-1}(i) = \sigma^{-1}(i)$, so $c$ has no zero entry exactly when $\sigma^{-1}\pi$ is fixed-point-free; for each of the $d!$ choices of $\pi$ there are $D_d$ such $\sigma$. $\blacksquare$

Two integer invariants grade a rule against a fixed point $F$ with sorted digits $(f_0, \dots, f_{d-1})$. The *rank* $\mathrm{sv}(K) = \#\{i : c_i \neq 0\}$ counts the sorted positions the rule reads; the *effective rank* $\mathrm{sv}_F(K) = \#\{i : c_i \neq 0 \text{ and } f_i \neq 0\}$ counts those that actually carry weight at $F$. A rule can be full-variable while $\mathrm{sv}_F < d$; the gap is invisible in the equation $K(F) = F$ and decisive for everything else (Section 3).

**Definition 2.3.** *$F$ is* universal *for $K$ at length $d$ if $K(F) = F$ and every admissible input reaches $F$ under iteration of $K$. Repdigits are always inadmissible (every rule sends them to $0$). In the small-length censuses of Section 3 the ninety near-repdigits (one digit occurring $d-1$ times) are also excluded, following the classical convention; in the duplication chain of Sections 5–6 only repdigits are excluded. Each count below states its convention.*

Everything in the paper passes through one elementary fact.

**Lemma 2.4 (universality criterion).** *(Proven.) Let $T$ be the multiset map $X \mapsto \mathrm{sort}_\downarrow K(X)$ on the finite set of admissible multisets, and let $F$ be a fixed point of $T$. Then $F$ is universal if and only if $F$ is the unique fixed point of $T$ and $T$ has no periodic orbit of period $\geq 2$.*

*Proof.* If $F$ is universal, a second fixed point $G$ would satisfy $T^k(G) = G \neq F$ for all $k$, and a periodic orbit $C$ of period $\geq 2$ never meets $F$ (orbits of points of $C$ stay in $C$); either contradicts universality. Conversely, finiteness forces every forward orbit to repeat, hence to enter a periodic orbit; with no period $\geq 2$ available that orbit is a fixed point, and by uniqueness it is $F$. $\blacksquare$

The two conditions are independent: Section 5 exhibits a rule with two fixed points and a rule with one fixed point plus cycles. The criterion makes universality decidable by finite search and splits its failure into the two modes — a competing fixed point, or a cycle — that recur throughout.

## The spectrum at small lengths

A fixed point can command anything from nothing to everything. It is useful to fix the scale before populating it.

- **L0 (collapse).** Every admissible orbit reaches $0$; the rule fixes nothing worth the name.
- **L1–L2 (fixed, partial).** $K(F) = F$ but the basin is a strict fraction of the space — possibly tiny, possibly large, in the worst case erratically either.
- **L3 (degenerate universal).** $F$ is universal but $\mathrm{sv}_F(K) < d$: the universality is that of a lower-rank map wearing $d$ coordinates.
- **L4 (full universal).** $F$ is universal with $\mathrm{sv}_F(K) = d$.
- **L5 (dimension-transcendent).** $F$, or an explicitly described family, is a full universal at infinitely many lengths under a fixed lifting recipe.

**Proposition 3.1 (collapse is inhabited).** *(Computed.) At $d = 4$, the rule with $c = (0,0,9,-9)$ — nine times the gap between the two smallest sorted digits — sends all $615$ admissible multisets to $0$. There are exactly $84$ collapse rules among the $552$ rules at $d = 4$, and $6$ among the $30$ at $d = 3$.*

At the other end of L0–L2, this paper's census found that no fixed point of any rule at $d=4$ has a one-multiset basin (Computed): strict bareness does not occur at four digits. What occurs instead, abundantly, is the partial fixed point, and the duplication family of Section 5 will furnish the canonical example of how wildly partial basins can behave inside one algebraically uniform family.

**Theorem 3.2 (census).** *(Computed; exhaustive over all full-variable rules and all admissible multisets, near-repdigits excluded.) The universal full-variable fixed points at $d = 3, 4, 5, 6$ number $0$, $4$, $33$, $506$.*

1. *At $d = 3$ there are none. The universal fixed points over all thirty rules are $45$, $450$, $495$, each universal for a sign-flip pair of rank-$2$ rules ($c = \pm(99, 0, -99)$ for $495$, $\pm(9,0,-9)$ for $45$, $\pm(90,0,-90)$ for $450$); their effective ranks are $\mathrm{sv}_F = 2$, $1$, $1$. The classical three-digit constant is a degenerate universal.*
2. *At $d = 4$ the four are $1746, 2538, 5382, 6174$, each universal for exactly one sign-flip pair of rules:*
$$1746: \pm(9, -900, 900, -9) \qquad 2538: \pm(90, 999, -999, -90)$$
$$5382: \pm(900, -9, 9, -900) \qquad 6174: \pm(999, 90, -90, -999).$$
*They form two anagram clusters, $\{1,4,6,7\}$ and $\{2,3,5,8\}$, and all have digit sum $\equiv 0 \pmod 9$ (as Lemma 2.2(a) forces for any fixed point).*
3. *At $d = 5$ the thirty-three are listed in Appendix A. Two are effectively degenerate at their fixed point despite full-variable rules: $54$, with sorted form $(5,4,0,0,0)$ and $\mathrm{sv}_F = 2$, and $3753$, with $\mathrm{sv}_F = 4$. The remaining thirty-one have $\mathrm{sv}_F = 5$. Among them is $60714$, universal for the rule $c = (9900, 9, 90, -9000, -999)$ — in arrangement form, $71460 - 10746 = 60714$.*
4. *At $d = 6$ the five hundred six stratify by zero count as $205, 240, 53, 8$ (zero through three zeros) and by digit sum as $8, 156, 244, 96, 2$ across sums $9, 18, 27, 36, 45$.*

The count matters less than what sits inside it. The classical map is not full-variable at odd lengths — its borrow chain zeroes the middle coefficient, $c = (99, 0, -99)$ at $d=3$ — so the classical failure at $d = 5$ is the failure of a rank-4 map asked a rank-5 question. The thirty-three show the question itself has answers.

**Theorem 3.3 (cross-dimensional selection).** *(Computed.) Of the thirty-three universal full-variable fixed points at $d = 5$, exactly one — $60714$ — is again a universal full-variable fixed point at $d = 6$ under some rule. The $\{0,0,1,4,6,7\}$ multiset carries exactly four of the $506$ universals at $d=6$: $60714$, $146070$, $170460$, $607140$.*

This was verified directly for this paper by intersecting the full $d=5$ and $d=6$ censuses. The selection is the right way to meet $60714$: it is not chosen for its digits, it is the unique survivor of an exhaustive test. The next section shows the survivor goes on forever, and why.

## Lifting by zeros: $60714$ at every length

**Theorem 4.1 (zero-padding transcendence).** *(Proven, with a finite-state component as stated below.) There is an explicit family of full-variable rules, one at each $d \geq 5$, related by a coefficient-preserving lifting, under which $60714$ is a fixed point at every $d \geq 5$ (Proven), universal at $d = 5$ and $d = 6$ (Computed, exhaustive), and universal on $A_d \setminus E_d$ at every $d \geq 7$, where $A_d$ is the admissible set and $E_d$ is the escape class of Definition 4.6, whose orbits collapse to $0$. The reaching-time bound underlying the induction is proven algebraically for odd $d \geq 15$ and even $d \geq 18$ (Appendix E) and closed by complete enumeration for $7 \leq d \leq 16$ — about $25$ million multisets, re-run in full for this paper.*

The construction and the proof skeleton follow; the point of including them is that every step leans on the zeros.

**The ladders.** The native rule has $c^{(5)} = (9900, 9, 90, -9000, -999)$ and acts on sorted form $(7,6,4,1,0)$. For $d \geq 7$ odd, define $c^{(d)}$ by appending to $c^{(d-2)}$ the zero-sum pair $(+9 \cdot 10^{d-2},\, -9\cdot 10^{d-2})$ at the two new bottom ranks. The even ladder lifts the same way from the root
$$c^{(6)} = (9900,\ 9,\ 90,\ -9000,\ 99000,\ -99999),$$
the native $-999$ split across the two zero positions, $99000 - 99999 = -999$. Both ladders preserve the four coefficients at $60714$'s nonzero digits verbatim.

**Proposition 4.2 (fixedness is free).** *(Proven.) Every rule on either ladder fixes $60714$.*

*Proof.* The sorted form of the padded fixed point is $(7,6,4,1,0,\dots,0)$. All appended (and split) coefficients sit at ranks holding zero digits, so $\sum_i c_i f_i = 9900\cdot 7 + 9 \cdot 6 + 90\cdot 4 - 9000 \cdot 1 = 60714$ at every length. $\blacksquare$

This was verified mechanically at every $d \leq 20$ and at $d = 100$ (Computed). The content of Theorem 4.1 is never the fixed-point equation; it is the basin, and the basin argument has three moving parts.

**Lemma 4.3 (absorbing set).** *(Proven.) Let $T_d$ be the admissible multisets whose sorted form ends in two zeros. For $d \geq 7$ on either ladder and $n \in T_d$,*
$$K^{(d)}(n) = K^{(d-2)}\bigl((s_0, \dots, s_{d-3})\bigr), \quad\text{and}\quad K^{(d)}(n) \in T_d.$$

*Proof.* The appended pair multiplies $s_{d-2} = s_{d-1} = 0$ and vanishes; what remains is the rule two rungs down on the first $d-2$ sorted digits, since those coefficients are copied verbatim. The output is below $10^{d-2}$, so its $d$-digit padding has at least two zeros, which sort to the tail. $\blacksquare$

**Lemma 4.4 (core positivity).** *(Proven.) For every sorted-descending $s$, the native part $\mathrm{core}(s) = 9900 s_0 + 9 s_1 + 90 s_2 - 9000 s_3 - 999 s_4$ satisfies $0 \leq \mathrm{core}(s) \leq 89{,}991 < 10^5$.*

*Proof.* The upper bound drops the negative terms. For the lower bound: if $s_3 = s_4 = 0$ all terms are nonnegative. If $s_3 \geq 1, s_4 = 0$, then $\mathrm{core} = 9000(s_0 - s_3) + 900 s_0 + 9 s_1 + 90 s_2 \geq 0$. If $s_3, s_4 \geq 1$, use $s_1 \geq s_4$ and $s_2 \geq s_3$, then $s_3, s_4 \leq s_0$:
$$\mathrm{core}(s) \;\geq\; 9900 s_0 + 9 s_4 + 90 s_3 - 9000 s_3 - 999 s_4 \;=\; 9900 s_0 - 8910 s_3 - 990 s_4 \;\geq\; 9900(s_0 - s_3) \;\geq\; 0. \qquad\blacksquare$$

The even ladder's six-coefficient root obeys the same bounds one decimal place higher: expanding $99000 s_4 - 99999 s_5 = -999 s_4 + 99999(s_4 - s_5)$ gives $\mathrm{core}_6(s) = \mathrm{core}(s_0, \dots, s_4) + 99999\,(s_4 - s_5)$, and since $0 \leq s_4 - s_5 \leq 9$, also $0 \leq \mathrm{core}_6(s) \leq 989{,}982 < 10^6$.

**Lemma 4.5 (zeros are produced).** *(Proven.) Each appended pair contributes $9 \cdot 10^{e_k}\, \delta_k$ with $\delta_k \geq 0$ a digit gap and the place $e_k$ two higher than the previous pair's; the $\delta_k$ are disjoint adjacent differences in a sorted string, so $\sum_k \delta_k \leq 9$. By Lemma 4.4 and its even-ladder extension the absolute value is never active and the output decomposes, without carries, into two-digit blocks (the digits of $9\delta_k$) sitting above a five-digit core (odd ladder) or six-digit core (even ladder). A block contributes two zero digits if $\delta_k = 0$, one if $\delta_k = 1$, none if $\delta_k \geq 2$; since $2\,\#\{\delta_k \geq 2\} + \#\{\delta_k = 1\} \leq \sum_k \delta_k \leq 9$, the output has at least $2M - 9$ zeros, $M$ the number of pairs. For $M \geq 6$ — that is, $d \geq 17$ on the odd ladder, $d \geq 18$ on the even — this is at least two zeros: every orbit enters $T_d$ in one step. A refined case analysis lowers the odd-ladder threshold to $d \geq 15$; it and the even ladder's full argument are in Appendix E.*

For $7 \leq d \leq 16$ the same conclusion (entry into $T_d$ within at most eight steps) holds by complete enumeration over all admissible multisets, every length re-run in full for this paper; the table is in Appendix E. One detail of the induction deserves its own lemma. When Lemma 4.3 drops an orbit to length $d - 2$, the projected multiset can fail admissibility there: a repdigit projection is block-aligned and belongs to the escape class, while a near-repdigit projection recovers admissibility within two further steps (Appendix E, projection lemma). Induction along each ladder then proves Theorem 4.1: orbits fall into $T_d$, where Lemma 4.3 reduces the length by two, the projection lemma hands the reduced orbit to the inductive hypothesis, and the roots $d = 5, 6$ are universal by the census. The ladder rules themselves are written out through $d = 20$, with the $d = 100$ instance, in Appendix F.

**Definition 4.6 (escape class).** The *block-aligned* multisets — constant on the native block and on each appended pair — are sent to $0$ in one step, because the native coefficients sum to zero and each pair sees equal digits. $E_d$ is the backward orbit of this set. At $d = 5, 6$ it is empty (the censuses show full universality there). At $d = 7$ the one-step part is the $45$ multisets $(x^5, y^2)$, $x > y$, and the full classification run for this paper found $|E_7| = 81$ of $11{,}340$ admissible multisets collapsing to $0$ with all other $11{,}259$ reaching $60714$; at $d = 8$, $|E_8| = 137$ of $24{,}210$ (Computed). The one-step part has a closed form: the admissible block-aligned multisets number $\binom{9+k}{k} - 10$, $k$ the number of blocks, which is $45$ at both $d = 7$ and $d = 8$ — confirmed by direct count of the inputs with $K(n) = 0$ at each (Computed). The classical map has the same structure at its own small lengths — the multiples of $1111$ at $d=4$ collapse to $0$ — so the escape class is a continuation of a classical phenomenon, not a new defect.

**The contrast: $6174$ does not climb.** The classical constant admits the same kind of coefficient-preserving lifting — keep $(999, 90, -90, -999)$ on the nonzero digits of $(7,6,4,1,0,\dots)$, append zero-sum pairs — and it never regains universality.

**Theorem 4.7.** *(Computed.) Padded $6174$ has no full-variable fixed-point rule at all at $d = 5$ (none of the $5{,}280$ rules fixes it — an algebraic obstruction, verified exhaustively here). At $d = 6$ exactly four full-variable rules fix it and the best basin is $0.9686$ of the $4{,}905$ admissible multisets (verified exhaustively here). Under the lifting family at $d = 7, 8, 9$ the best basins are $0.9897$, $0.9981$, $0.9991$ [S], with the non-reaching inputs at $d = 8, 9$ being exactly the $45$ multisets $(X^4, Y^4)$, $X > Y \geq 0$, each collapsing to $0$ [S].*

The structural diagnosis is short. $60714$'s native rule lands its largest coefficient, $-999$, on its zero digit: the zero positions, where lifting must do its work, already carry the rule's weight, and the absorbing set of Lemma 4.3 catches the escape candidates. $6174$ has no zero digit at its native length, so its lifts pad with zeros *outside* the native coefficients; the $(X^4, Y^4)$ inputs never meet the absorbing structure and survive as a permanent escape class. Where a fixed point keeps its zeros relative to its coefficients decides its fate across dimension. That is the lesson of the chain that works, and the standing problem of the chain that follows is that it has no zeros at all.

## Lifting by duplication: folding

Let $M_m = \{1,4,6,7\}^m$, a multiset of length $d = 4m$ with sorted form $\mathbf{s}_m = (7^m, 6^m, 4^m, 1^m)$. The duplication question asks for universal fixed points with this digit content at every $m$. The right algebraic tool is an operation on rules.

**Definition 5.1 (folding).** *Let $c = (c_0, \dots, c_{d_0-1})$ be the coefficient vector of a rule at length $d_0$ and let $k \geq 1$. The $k$-fold $c^{\otimes k}$ at length $k d_0$ assigns to rank $ki + j$ ($0 \leq i < d_0$, $0 \leq j < k$) the coefficient $c_i \cdot 10^{\,d_0 (k-1-j)}$.*

**Proposition 5.2.** *(Proven.) (a) $c^{\otimes k}$ is a valid rule (realizable by a permutation pair), full-variable if $c$ is. (b) For every multiset $X$ at length $d_0$, writing $X^k$ for the multiset with each multiplicity multiplied by $k$,*
$$T^{\otimes k}(X^k) = \bigl(T(X)\bigr)^k :$$
*the $k$-fold states are closed under the folded rule, and the folded dynamics on them is conjugate to the base dynamics. (c) If $K(W) = W$ then the $k$-fold rule fixes the concatenation $W^{(k)} = W \cdot \sum_{j<k} 10^{j d_0}$; if the base rule is universal, every $k$-fold state reaches $W^{(k)}$.*

*Proof.* (a) If $c_i = 10^{a_i} - 10^{b_i}$ with $\{a_i\}$ and $\{b_i\}$ each a complete residue list $\{0, \dots, d_0 - 1\}$, then the folded coefficients are $10^{\,d_0(k-1-j) + a_i} - 10^{\,d_0(k-1-j)+b_i}$, and $\{ d_0 t + a_i \}$, $\{ d_0 t + b_i\}$ each enumerate $\{0, \dots, kd_0 - 1\}$ exactly once. (b) The sorted form of $X^k$ repeats each sorted digit of $X$ at $k$ consecutive ranks, so ranks $ki, \dots, ki + k - 1$ all hold $s_i$, and
$$\sum_{i,j} c_i 10^{\,d_0(k-1-j)} s_i = R_k \cdot \sum_i c_i s_i, \qquad R_k = \textstyle\sum_{j<k} 10^{j d_0}.$$
Taking absolute values, $K^{\otimes k}(X^k) = R_k \cdot K(X)$, and since $K(X) < 10^{d_0}$ — it is a difference of two $d_0$-digit numbers — multiplication by $R_k$ concatenates $k$ copies of its padded digit string without carries. The digit multiset of the output is therefore $(T(X))^k$. (c) Immediate from (b). $\blacksquare$

Folding explains the duplication chain's classical landmarks at a stroke.

**Corollary 5.3.** *(Proven.) The $m$-fold of the classical rule — the* interleaved *rule, with coefficients $999\cdot 10^{4(m-1-j)}, 90 \cdot 10^{4(m-1-j)}, -90\cdot 10^{4(m-1-j)}, -999\cdot10^{4(m-1-j)}$ on the four rank-blocks — fixes $F_m = 6174 \cdot R_m$, the string $6174$ written $m$ times, at every $m \geq 1$. Its restriction to $m$-fold states is conjugate to the classical four-digit map, so all of them lie in $F_m$'s basin.*

So fixed points with the duplicated digit content exist at every $m$, provably. What the algebra does not control is everything off the folded subspace, and there the family comes apart.

**Computed 5.4 (the interleaved basins).** *Over all non-repdigit multisets (the duplication-chain convention), the basin of $F_m$ under the interleaved rule is*

| $m$ | $d$ | states | basin of $F_m$ |
|---:|---:|---:|---:|
| 1 | 4 | 705 | $100\%$ |
| 2 | 8 | $24{,}300$ | $100\%$ |
| 3 | 12 | $293{,}920$ | $14.86\%$ |
| 4 | 16 | $2{,}042{,}965$ | $99.69\%$ |
| 5 | 20 | $10{,}014{,}995$ | $9.52\%$ |

*All five rows were enumerated in full for this paper. At $m = 3$ the rule has exactly two fixed points — $617461746174$ and $535549955994$, the latter with a basin of $100$ multisets — and $250{,}148$ of the $293{,}920$ states end in cycles.*

The sequence $100, 100, 14.9, 99.7, 9.5$ is the family's character witness: one algebraically uniform construction, basins scattered across the unit interval with no trend. The second fixed point at $m = 3$ also matters for the record — it shows coefficient-positivity conditions (the rule is monotone in the sense below) do not force fixed-point uniqueness, a hypothesis the project's earlier notes briefly entertained and later refuted.

For the rest of the section, restrict to the rules adapted to $M_m$. Call a rule *pair-symmetric* if there are bijections between its seven-rank and one-rank coefficient blocks, and between its six-rank and four-rank blocks, under which corresponding coefficients are negatives. Write $S_7 = \sum_{\text{7-block}} c_i$ and $S_6 = \sum_{\text{6-block}} c_i$, and let $C_j = c_0 + \cdots + c_j$ be the partial sums, so that for any sorted input, using $\sum c_i = 0$,
$$\sum_i c_i s_i \;=\; \sum_{j=0}^{d-2} C_j\, g_j, \qquad g_j = s_j - s_{j+1} \geq 0.$$

**Proposition 5.5.** *(Proven.) For a pair-symmetric rule at $d = 4m$: (a) $C_{m-1} = C_{3m-1} = S_7$ and $C_{2m-1} = S_7 + S_6$; (b) the value on the sorted form $\mathbf{s}_m$, whose only nonzero gaps are $g_{m-1} = 1$, $g_{2m-1} = 2$, $g_{3m-1} = 3$, is*
$$V \;=\; 6 S_7 + 2 S_6 \;=\; 4C_{m-1} + 2C_{2m-1};$$
*(c) the rule fixes an arrangement of $M_m$ if and only if $|V|$ has digit multiset $M_m$, a condition depending only on the partition of positions into the four blocks, not on the within-block coefficient assignment; (d) the interleaved rule is monotone — $C_j \geq 0$ for all $j$ — at every $m$.*

*Proof.* (a) Pair-symmetry gives $S_1 = -S_7$ and $S_4 = -S_6$, so $C_{3m-1} = S_7 + S_6 + S_4 = S_7 = C_{m-1}$. (b) Substituting into the gap form, $V = C_{m-1} + 2C_{2m-1} + 3C_{3m-1} = S_7 + 2(S_7 + S_6) + 3S_7 = 6S_7 + 2S_6$; directly, $V = 7S_7 + 6S_6 + 4S_4 + 1\cdot S_1 = 6S_7 + 2S_6$. (c) The multiset map sends $M_m$ to the digit multiset of $|V|$; if that is $M_m$ the orbit of $M_m$ is fixed and the fixed integer is $|V|$. Both $S_7$ and $S_6$ are sums of $10^a - 10^b$ over the block's position pairings, hence depend only on the position sets. (d) For the interleaved rule the partial sums climb through the seven- and six-blocks; inside the four-block, $C = 999 R_m + 90 R_m - 90 \sum_{k \geq m-t} 10^{4k} \geq 999 R_m \geq 0$ after $t$ steps; inside the one-block, $C = 999\bigl(R_m - \sum_{k \geq m-t} 10^{4k}\bigr) \geq 0$. $\blacksquare$

Part (c) reduces the *fixing* question to explicit arithmetic over partitions — at $m = 2$, for instance, exactly $36$ of the $2{,}520$ partitions fix an arrangement of $M_2$ (Computed) — and part (d), with Corollary 5.3, says the algebraic requirements of the duplication conjecture (a fixing, monotone, full-variable rule at every $m$) are met uniformly. By Lemma 2.4, everything open lives in two dynamical conditions: no second fixed point, no cycle.

**Computed 5.6 (the universal landscape, $m \leq 6$).** *Universal fixed points of $M_m$ exist at $m = 1, \dots, 6$. The counts of universal arrangements are $2$, $465$ ($481$ under the strict near-repdigit convention), $46$, $\geq 313$, $\geq 1$, $\geq 1$ [S]. Within the pair-symmetric class at $m = 2$, this paper's exhaustive enumeration found $312$ universal rules concentrated on $12$ arrangements (Appendix C). For $m \geq 3$ no universal arrangement has a block decomposition [S]; in particular $F_m$ is never among them for $m \geq 3$ (its basins are the table above). The following full-basin verifications were performed for this paper, each over the complete non-repdigit multiset space:*

| $m$ | $d$ | states | a verified universal | rule |
|---:|---:|---:|:---|:---|
| 3 | 12 | $293{,}920$ | $666141417774$ | the project's $m=3$ rule, re-verified |
| 4 | 16 | $2{,}042{,}965$ | $1746174617461746$ | $(9,-900,900,-9)^{\otimes 4}$ |
| 5 | 20 | $10{,}014{,}995$ | $17461746174617461746$ | $(9,-900,900,-9)^{\otimes 5}$ |
| 6 | 24 | $38{,}567{,}090$ | $666141417774$ written twice | the $m=3$ rule, $2$-folded |

*The $d = 20$ row is, to the author's knowledge, the first complete-enumeration universality verification at $m = 5$; the project's previous $m=5$ witness ($14617461774617461746$) rested on a necessary-condition proxy [S]. The $d=24$ row gives a second verified universal arrangement at $m = 6$ alongside the project's $666174141466617777741414$ [S].*

**Conjecture 5.7.** *$M_m$ carries a universal full-variable fixed point at every $m \geq 1$.*

The evidence now includes six consecutive multiplicities with full-basin witnesses, and witness-count estimates that grow like $3\cdot 10^3$, $2 \cdot 10^7$, $3\cdot 10^8$ at $m = 3, 4, 5$ [S, sampling estimates calibrated against the exact $m=3$ enumeration]. What it does not include is any uniform description: the universal arrangements for $m \geq 3$ are scrambled, and the structural features that characterize them at one multiplicity provably fail at the next (Section 7). The table's most interesting column is the last one, and it is the subject of the next section: four of the six witnesses are folds.

## When folding preserves universality

Proposition 5.2 transports the fixed point along $m \mapsto km$ for free; it says nothing about the basin off the folded subspace. The experiments reported here measure exactly that. All "universal" verdicts below are complete enumerations; all "fails" verdicts are definitive, because the witness of failure is an admissible input (a multiset over $\{1,4,6,7\}$) that demonstrably does not reach the fixed point. The rules used are written out in Appendix D.

**Computed 6.1 (first doubling: everything survives at $d=4$).** *The $2$-folds of all eight universal full-variable rules at $d = 4$ (Theorem 3.2) are universal at $d = 8$, each verified over all $24{,}300$ multisets. In particular the $2$-fold of the classical rule is the interleaved $m=2$ rule, whose universality is the $m = 2$ row of Computed 5.4. This is a property of the four-digit bases, not a law: the $2$-fold of $60714$'s native five-digit rule fixes $6071460714$ at $d = 10$ with basin $53.34\%$ of the $92{,}368$ non-repdigit multisets — the chain that climbs perfectly by zero-padding does not climb by doubling.*

**Computed 6.2 (second doubling: selection).** *Iterating the doubling, exactly one of the four $d=4$ fixed points survives: the $2$-fold of the $2$-fold of $(9,-900,900,-9)$ — the $1746$ rule — is universal at $d = 16$ ($2{,}042{,}965$ multisets), while the doubled doubles of the $2538$, $5382$, and $6174$ rules all fail, each trapping admissible $\{1,4,6,7\}$-multisets. For the classical rule the obstruction is a period-two cycle through the multisets of $5355517553558172$ and $4995599449954176$, which captures $14$ of the $965$ alphabet multisets.*

**Computed 6.3 (the $1746$ fold spectrum).** *For the $1746$ rule $c = (9, -900, 900, -9)$ and $2 \leq k \leq 8$:*

| $k$ | $d$ | verdict | basis |
|---:|---:|:---|:---|
| 2 | 8 | **universal** | complete enumeration, $24{,}300$ |
| 3 | 12 | fails ($15.48\%$) | complete enumeration |
| 4 | 16 | **universal** | complete enumeration, $2{,}042{,}965$ |
| 5 | 20 | **universal** | complete enumeration, $10{,}014{,}995$ |
| 6 | 24 | fails | alphabet witness ($523/2921$ reach $F$) |
| 7 | 28 | fails | alphabet witness |
| 8 | 32 | fails | alphabet witness ($6533/6541$) |

*The $k = 4$ entry is the direct $4$-fold; the iterated double-double — a different within-block assignment on the same partition — is also universal at $d = 16$ (Computed 6.2). The $5$-folds of the other three $d=4$ rules fail at $k=5$; the $3$-folds of all four fail. Mixed towers also fail where tested ($3$-fold of the $2$-fold at $d=24$: fails). The iterated double-double-double of the $1746$ rule at $d = 32$ — which differs from the direct $8$-fold only in its within-block coefficient assignment — fixes $1746$ written eight times, sends all $6{,}541$ alphabet multisets and $200{,}000$ random admissible multisets to it, and exceeds exhaustive reach at $\binom{41}{9} \approx 3.5 \times 10^8$ states (Evidence).*

**Computed 6.4 (folding from $m = 2$: survival is common).** *Of the $312$ universal pair-symmetric rules at $m = 2$, exactly $144$ — spanning nine of the twelve universal arrangements — have universal $2$-folds at $m = 4$, every one verified by complete enumeration over all $2{,}042{,}965$ multisets. Among them are sixteen rules whose folds fix $F_4 = 6174$ written four times: the block fixed point that the interleaved rule fails to make universal ($99.69\%$, Computed 5.4) is made universal by other doublings of the same partition, which explains, in folding terms, the project's observation that $F_4$ is universal only under scrambled within-block orderings [S]. The alphabet test was a perfect filter here: $144$ of $312$ doubled rules passed it, and all $144$ proved universal.*

**Computed 6.5 (folding from $m = 3$).** *The $2$-fold of the project's verified $m = 3$ universal rule is universal at $m = 6$: all $38{,}567{,}090$ non-repdigit multisets at $d = 24$ reach $666141417774666141417774$.*

Three things follow from this body of computation, and a fourth is suggested.

First, the duplication chain *does* have a working lifting — in instances. The project's earlier searches had tested and rejected a position-insertion lifting $m \to m+1$ (best basin $3.07\%$ across all natural variants [S]) and a family of $m$-periodic constructions (each universal at some multiplicities and provably cyclic at others [S]); the conclusion drawn was that universality does not transport. Folding shows the conclusion was too broad. The map $m \to km$ transports the entire algebraic package by Proposition 5.2, and the dynamics follows it in verified cases substantial enough to populate Computed 5.6's table: a single four-digit rule covers $m \in \{1, 2, 4, 5\}$ and a single twelve-digit rule covers $\{3, 6\}$.

Second, the survival pattern is irregular — $k = 2, 4, 5$ work from the $1746$ root and $k = 3, 6, 7, 8$ do not, the direct $8$-fold fails while the iterated doubling passes every feasible test, and the within-block assignment (the only difference between those two) is decisive. This is the duplication chain's recurring signature, now visible inside a single rule's fold family.

Third, doubling-survival is not rare: eight of eight rules from $m = 1$, $144$ of $312$ from $m = 2$, one of one tested from $m = 3$. At the only two doubling steps where the survival fraction could be measured exhaustively it is $100\%$ and $46\%$, which makes the truth of Conjecture 5.7 look like the generic outcome of an abundant mechanism rather than a sequence of coincidences — the strongest structural evidence the conjecture currently has. What *is* selective is iterated survival along a fixed tower: of the four $d = 4$ roots, only the $1746$ rule's tower passes the second doubling, and it then passes everything testable at the third. The selection is precisely parallel to $60714$'s — one survivor of an exhaustive cross-dimensional test — and it nominates a single candidate for the duplication chain's L5 occupant.

**Conjecture 6.6 (dyadic tower).** *The iterated $2$-fold of $(9, -900, 900, -9)$ is universal at $d = 2^{j+2}$ for every $j \geq 0$ — equivalently, $1746$ written $2^j$ times is a full universal fixed point at every dyadic multiplicity.*

This is the sharpest available subconjecture of Conjecture 5.7: a single explicit self-similar family, fixedness proven at every level, universality fully verified at $j \leq 2$ and supported by all feasible evidence at $j = 3$. It is worth stating why a proof might be less hopeless here than for the general conjecture. The earlier no-go evidence [S] rules out *$m$-periodic* uniform constructions — rules whose position structure repeats with the block — by exhibiting cycles at specific multiplicities. The folded towers are not periodic; their coefficient structure is self-similar across scales, with the base rule's geometry reproduced at every dyadic level, and the no-go arguments do not apply to them. What is missing is any analogue of Lemma 4.3: a closed set that the folded dynamics provably enters in bounded time and on which the multiplicity provably drops. The $k$-fold states are closed and reduce $km$ to $m$ (Proposition 5.2(b)), but nothing forces an orbit *into* them — they are an atoll, not a drain. Finding a fold-adapted absorbing structure, playing the role zeros play in Section 4, is in the author's view the most concrete open *proof* problem this subject now offers.

A remark on what folding cannot do even in principle. A fold realizes multiplicity $m$ only from a universal base at some $m_0$ properly dividing $m$, so folds from the verified bases $m_0 \leq 6$ can at best reach the $m$ whose least prime factor is at most $5$ — and reach them only when the particular fold survives, which Computed 6.3 shows is not for free. The multiplicities with least prime factor $\geq 7$, beginning with $m = 7, 11, 13$, need witnesses of their own at the bottom of their divisor chains. Folding reorganizes the conjecture around its prime levels; it does not exhaust it.

## The cost of a certificate

Every universality statement in this paper is, by Lemma 2.4, the statement that a finite functional graph has one root and no cycles. Such statements always have proofs — trace the graph — and the question that separates Section 4 from Section 6 is whether they have proofs *smaller than the graph*. For the zero-padding chain they do: Lemmas 4.3–4.5 are a certificate of total size independent of $d$. This section measures the same question at the base of the duplication chain and finds the answer sharply different.

The classical four-digit map factors through two coordinates. For sorted digits $a \geq b \geq c \geq e$, the map computes $999(a - e) + 90(b - c)$, so with $p = a - e \in \{1, \dots, 9\}$ and $q = b - c \in \{0, \dots, p\}$ the dynamics lives on $54$ states, with unique fixed point $(6,2)$ (this is $6174$: $p = 7 - 1$, $q = 6 - 4$). The system is acyclic with maximal reaching time $6$, and its iterated images shrink as $54, 20, 14, 10, 7, 4, 1$ (Computed). A *polynomial Lyapunov function of degree $D$* is a $\Phi \in \mathbb{R}[p,q]$, $\deg \Phi \leq D$, with $\Phi(\text{next}) < \Phi(\text{current})$ at all $53$ non-fixed states; its existence is a linear program in the $\binom{D+2}{2}$ coefficients.

**Theorem 7.1 (the Lyapunov degree of Kaprekar's theorem is exactly seven).** *(Proven.) No polynomial Lyapunov function of degree $\leq 6$ exists for the four-digit gap system: for each $D = 2, \dots, 6$ there is an exact rational Farkas certificate — a nonnegative rational combination of the $53$ decrease constraints summing to a contradiction — verified in integer arithmetic (the $D = 4$ certificate is supported on $15$ states; Appendix B). A Lyapunov function of degree $7$ exists: an explicit rational polynomial, verified in exact arithmetic to decrease strictly along all $53$ transitions.*

Two readings of this theorem are wrong and one is right. It does not say the convergence is unprovable — it is provable by a $54$-state enumeration, and indeed by a $36$-coefficient polynomial. It also does not say (as a first pass over this project's data once suggested) that certificates exist only at the trivial interpolation threshold, degree $9$, where polynomials span all functions on the state set and the reaching time itself becomes a vacuous witness; degree $7$ is strictly below that threshold, so a genuinely non-tautological algebraic certificate exists. What the theorem says is quantitative: the cheapest polynomial witness of the seventy-five-year-old fact costs $36$ coefficients on a $54$-point system. Nothing about it is light, and nothing about it is structural — the certificate is a found object, not an explanation, and there is no visible way to write it as the first member of a family indexed by $m$.

That is the correct statement of the base-case obstruction, and it propagates. Each of the standard strategies for Conjecture 5.7 was pursued seriously in this project and failed for a reason now identifiable with the base case's lack of transportable structure; the table records the sharp form of each failure (all [S], from the project's verified computational log; the basin and enumeration figures quoted were re-verified here where marked).

| strategy | sharp obstruction |
|:---|:---|
| uniform / periodic construction | the one clean recipe universal at $m=3,4$ fails at $m=2$ and $m=5$ (period-$8$ and period-$16$ cycles); position-insertion lifting $m \to m{+}1$: best basin $3.07\%$ |
| induction on excluded cycles | obstruction cycles do not stabilize: the $m=5$ cycle families do not occur at $m = 3, 4$; each multiplicity grows new ones |
| structural characterization of universal rules | the property characterizing universal partitions at $m = 3, 4$ (seven-block at the top) yields zero universals at $m=5$ in an $11.3$-million-sample search; the verified $m=5$ winner has a different shape |
| Lyapunov / monovariant | LP-infeasible over digit-count and quadratic feature classes at $d = 16$; at the base, Theorem 7.1 |
| modular invariant | no modulus in $2, \dots, 300$ separates the basin from the cycles; mod $9$ (Lemma 2.2) is universal and hence empty |
| union bound / local lemma over cycles | the dominant cycle alone captures ${\sim}67\%$ of candidate rules — far too dense |
| counting lower bound | the universal fraction is erratic ($6.94\%$ exact at $m=3$, ${\sim}28\%$ at $m=4$, ${\sim}0.04\%$ at $m=5$); only the absolute count grows, and no provable lower bound for it is known |

The common root is uniformity: universal rules exist in abundance at every tested $m$, but the *description* of where they sit changes with $m$, which simultaneously defeats construction, induction, characterization, and any local-to-global probabilistic argument. A workable proof must either find structure that is genuinely scale-free — the dyadic towers of Section 6 are the first candidate family of that kind to survive testing — or dispense with description entirely and prove existence by a counting argument robust to wild fluctuation in the universal fraction. Both are research programs, not techniques.

It is worth closing the circle with Section 4. The zero-padding proof never confronts any of this, because it never proves convergence at a fixed length at all: it proves a *reduction between lengths* (Lemma 4.3) and pays a bounded, $d$-independent cost to reach the reducing set (Lemma 4.5). The duplication chain has the reduction (Proposition 5.2(b)) but not the reaching — its folded set is measure-zero and nothing drives orbits toward it. The precise frontier, stated once more as a problem:

**Open Problem 7.2.** *Exhibit, for some universal base rule $c$ and some $k \geq 2$, a set $\mathcal{A}_m \supseteq \{k\text{-fold states}\}$ of multisets at length $k d_0$, closed under $c^{\otimes k}$, reached from every admissible input in boundedly many steps, on which the dynamics provably reduces to a system solved at the base — without using zero digits. Conjecture 6.6 would follow for the corresponding tower.*

**Open Problem 7.3.** *Prove any lower bound on the number of universal rules for $M_m$ that is positive for infinitely many $m$.*

## Methods and provenance

All computations are over digit multisets; a rule's orbit depends only on the sorted digit vector, which is what makes complete enumeration feasible — $\binom{d+9}{9}$ states minus exclusions, against $10^d$ integers. Conventions: the censuses of Section 3 and the $60714$ chain exclude repdigits and near-repdigits ($615$, $1{,}902$, $4{,}905$, $11{,}340$, $24{,}210$ admissible multisets at $d = 4, \dots, 8$); the duplication chain excludes repdigits only ($24{,}300$; $293{,}920$; $2{,}042{,}965$; $10{,}014{,}995$; $38{,}567{,}090$ at $d = 8, 12, 16, 20, 24$). Basins were computed by orbit tracing with terminal memoization; the $d = 20, 24$ enumerations use a combinatorial ranking of multisets into a flat byte array (at most $\binom{d+9}{9}$ bytes of state), which is what brings the previously "infeasible" $d = 20$ complete basin (Computed 5.6) to under two minutes in an interpreted language. The Lyapunov LPs of Theorem 7.1 were solved with an exterior solver and then *re-verified in exact rational arithmetic*: the infeasibility certificates are nonnegative rational vectors checked to annihilate the constraint matrix over $\mathbb{Q}$, and the degree-$7$ function was rationalized and its $53$ strict decreases checked exactly.

Results marked [S] are quoted from the project's computational log and were not re-executed for this paper; they comprise the $6174$ lifting basins at $d = 7, 8, 9$, the exhaustive one-step closure confirmations at $d = 17, 18, 20$ and the Case-2 reaching-time maxima through $d = 30$ cited in Appendix E, the duplication-chain counts at $m \geq 3$ and their witness-count estimates, the $m = 3$ complete pair-symmetric enumeration ($3{,}000$ universal rules among $43{,}200$ monotone fixing rules), the obstruction-cycle and no-go analyses summarized in Section 7's table, and the $m = 6$ witness $666174141466617777741414$. The $d \leq 16$ reaching-time enumeration behind Theorem 4.1 — about $25$ million multisets — was re-run in full for this paper (Appendix E.3), as were the one-step escape counts at $d = 7, 8$ and the $d = 6$ census lists of Appendix A. Everything else — the full censuses at $d \leq 6$ with the collapse counts and the selection theorem, the $60714$ ladder checks through $d = 100$ and full classifications at $d = 7, 8$, the five interleaved basins, the two-fixed-point inventory at $d = 12$, the $m=2$ pair-symmetric enumeration, every fold verdict in Section 6 — including the $144$ complete $d=16$ basin enumerations of Computed 6.4 and the complete enumerations at $d = 8, 20, 24$ — and both directions of Theorem 7.1 — was computed afresh for this paper from the engine, and the verification scripts accompany the manuscript.

## Acknowledgments {.unnumbered}

The enumerations, searches, and verification harness were built and run in collaboration with Anthropic's Claude, used as a research instrument; several of the project's intermediate claims (a uniqueness hypothesis for monotone rules; a first reading of the Lyapunov threshold) were retracted or corrected when verification contradicted them, and the corrected statements appear above. The questions, the direction, and the responsibility for the results are the author's.

```{=latex}
\appendix
```

## The census lists

$$54,\ 3753,\ 12456,\ 14562,\ 15642,\ 16524,\ 16578,\ 16758,\ 17685,\ 18342,\ 21456,$$
$$21834,\ 24156,\ 24183,\ 24561,\ 28539,\ 37584,\ 37854,\ 38754,\ 41562,\ 41832,\ 42183,$$
$$43758,\ 43785,\ 43875,\ 45612,\ 45621,\ 53928,\ 58239,\ 60417,\ 60714,\ 65781,\ 67581.$$

All thirty-three were found by exhaustive enumeration of the $5{,}280$ full-variable rules against the $1{,}902$ admissible multisets. The two with $\mathrm{sv}_F < 5$ are $54$ ($\mathrm{sv}_F = 2$) and $3753$ ($\mathrm{sv}_F = 4$); these are the five-digit analogues of the degenerate three-digit constants and, like the other thirty-one except $60714$, do not survive to $d = 6$ (Theorem 3.3).

At $d = 6$, the high-zero strata of the $506$ — where cross-dimensional behavior concentrates — are small enough to list, and both lists below were checked against this paper's recomputed census. The eight fixed points with three zero digits are all arrangements of the single multiset $\{0,0,0,2,2,5\}$:
$$252,\ 2520,\ 20025,\ 25200,\ 200025,\ 200250,\ 250200,\ 252000.$$
The fifty-three with two zero digits fall into eight multiset clusters, of sizes $32$ ($\{9,9,8,1,0,0\}$), $7$ ($\{5,5,4,4,0,0\}$), $5$ ($\{9,7,1,1,0,0\}$), $4$ ($\{7,6,4,1,0,0\}$ — the thread of Theorem 3.3: $60714$, $146070$, $170460$, $607140$), $2$ ($\{7,7,3,1,0,0\}$), and three singletons ($9225$, $67023$, $52605$). The full sorted list:
$$4545,\ 7191,\ 8919,\ 8991,\ 9189,\ 9225,\ 10899,\ 17019,\ 37017,\ 44505,\ 52605,\ 54450,$$
$$60714,\ 67023,\ 80919,\ 80991,\ 81099,\ 89019,\ 90819,\ 90918,\ 91809,\ 98091,\ 100899,$$
$$108099,\ 109809,\ 146070,\ 170460,\ 180909,\ 189009,\ 190089,\ 190809,\ 445005,$$
$$445050,\ 504450,\ 544500,\ 607140,\ 700191,\ 701901,\ 707130,\ 719100,\ 809091,$$
$$809109,\ 810909,\ 890091,\ 900891,\ 901890,\ 908091,\ 908109,\ 908190,\ 908901,$$
$$909081,\ 910089,\ 910809.$$
The remaining $445$ fixed points ($205$ with no zero digit, $240$ with one) are in the repository's census file.

## The degree-4 Farkas certificate

For $D = 4$ the Lyapunov LP has $15$ unknowns and $53$ constraints, one per non-fixed gap state $(p,q)$, each of the form $w \cdot \bigl(\mathbf{m}(G(p,q)) - \mathbf{m}(p,q)\bigr) \leq -1$ with $\mathbf{m}$ the monomial vector of degree $\leq 4$ and $G$ the gap map. The exact infeasibility certificate found and verified for Theorem 7.1 is a rational vector $y \geq 0$, supported on the fifteen states
$$(1,0),\ (2,0),\ (4,2),\ (4,3),\ (5,1),\ (5,3),\ (5,5),\ (6,0),\ (6,3),\ (7,1),\ (7,3),\ (8,0),\ (9,2),\ (9,6),\ (9,9),$$
with common denominator $10{,}885{,}528{,}810$, satisfying $\sum_s y_s \bigl(\mathbf{m}(G(s)) - \mathbf{m}(s)\bigr) = 0$ exactly and $\sum_s y_s = 1$: any $\Phi$ of degree $\leq 4$ would have to decrease along a nonnegative combination of transitions that exactly cancels, which is absurd. Certificates for $D = 2, 3, 5, 6$ have supports of sizes $6$, $10$, $21$, $28$ and were verified the same way. The degree-$7$ Lyapunov function has $36$ rational coefficients and worst strict-decrease margin $-0.979$ after rationalization; its coefficient vector is in the accompanying repository.

## The pair-symmetric universal rules at $m = 2$

Exhaustive enumeration for this paper: $2{,}520$ ordered partitions of the eight positions into the four blocks, of which $36$ fix an arrangement of $M_2$ (Proposition 5.5(c)); $64$ within-block coefficient assignments each; $312$ of the resulting rules are universal over all $24{,}300$ non-repdigit multisets, fixing $12$ distinct arrangements with multiplicities
$$14617746,\ 17461746,\ 17746146\ (48\ \text{rules each}); \quad 61461774,\ 61746174,\ 61774614\ (32);$$
$$14177466,\ 17417466,\ 17741466\ (16); \quad 14661774,\ 17466174,\ 17746614\ (8).$$
Twenty-four of the $312$ are monotone. The fold experiments of Computed 6.4 take this set as their base.

## Rules used in Section 6

The twelve-digit universal rule (Computed 5.6, $m = 3$; re-verified here over all $293{,}920$ multisets) has coefficient vector
$$c = (99999999999,\ 9990000000,\ 999900000,\ 99999000,\ 999900,\ 9990,$$
$$\ -99999000,\ -999900,\ -9990,\ -99999999999,\ -9990000000,\ -999900000)$$
and fixed point $666141417774$; it is pair-symmetric and is not itself a fold. Its $2$-fold (Definition 5.1, $d_0 = 12$, $k = 2$) is the $d = 24$ rule of Computed 6.5. The $k$-folds of the $1746$ rule are fully determined by Definition 5.1 from $c = (9, -900, 900, -9)$: rank $5i + j$ of the $5$-fold at $d = 20$ carries $c_i \cdot 10^{\,16 - 4j}$, giving
$$\bigl(9\cdot 10^{16}, 9\cdot 10^{12}, 9\cdot 10^{8}, 9\cdot 10^{4}, 9,\ -900\cdot 10^{16}, \dots, -900,\ 900\cdot 10^{16}, \dots, 900,\ -9\cdot 10^{16}, \dots, -9\bigr),$$
with fixed point $1746$ written five times. The iterated dyadic tower at $d = 32$ is $\bigl((c^{\otimes 2})^{\otimes 2}\bigr)^{\otimes 2}$, which differs from $c^{\otimes 8}$ in the within-block assignment of equal-magnitude coefficients to ranks; the former passes all feasible universality tests at $d=32$, the latter fails the alphabet test (Computed 6.3).

## The reaching-time bound in full

This appendix proves the reaching-time half of Theorem 4.1 at full rigor: every admissible orbit enters the absorbing set $T_d$ within a bounded number of steps, the bound being one step for odd $d \geq 15$ and even $d \geq 18$, and at most eight steps for $7 \leq d \leq 16$ by complete enumeration. It closes with the projection lemma that the induction of Section 4 quietly uses.

**The decomposition.** By Lemmas 4.4 and 4.5 the absolute value in $K^{(d)}$ is never active, and the output splits without carries into a core plus disjoint two-digit blocks:
$$K^{(d)}(x) \;=\; \mathrm{core}(x) + \sum_{k=1}^{M} 9 \cdot 10^{e_k}\, \delta_k, \qquad \delta_k = x_{e_k - 2} - x_{e_k - 1} \in \{0, \dots, 9\},$$
with $M$ pairs at places $e_k$ ascending by two. Writing $9\delta_k = 10u_k + v_k$, the block at places $(e_k, e_k + 1)$ carries digits $(v_k, u_k)$: two zeros if $\delta_k = 0$, one zero ($u_k = 0$) if $\delta_k = 1$, none if $\delta_k \geq 2$, since $9\delta_k \in \{18, 27, \dots, 81\}$ then has both digits nonzero. Each block value is at most $81 < 100$, so blocks never carry into one another; the core is below $10^5$ (odd) or $10^6$ (even) and at most one carry enters the lowest block, where the combined value $9\delta_1 + 1 \leq 82$ still occupies two digits.

**E.1 (odd ladder, $d \geq 15$).** *(Proven.) For odd $d \geq 15$, every admissible input satisfies $K^{(d)}(x) \in T_d$.*

*Proof.* Let $Z_0, Z_1, Z_{2+}$ count the pairs with $\delta_k = 0$, $1$, $\geq 2$. The blocks contribute $2Z_0 + Z_1$ zero digits, and from $2Z_{2+} + Z_1 \leq \sum_k \delta_k \leq 9$ (Lemma 4.5),
$$2Z_0 + Z_1 \;=\; 2M - Z_1 - 2Z_{2+} \;\geq\; 2M - 9.$$
For odd $d \geq 17$, $M = (d-5)/2 \geq 6$ and the block region alone has $\geq 3$ zeros. At $d = 15$, $M = 5$ gives only $\geq 1$, and the second zero comes from a case split on $x_4$:

*Case $x_4 = 0$.* Sorting forces $x_5 = \cdots = x_{14} = 0$, every $\delta_k = 0$, and the block region is ten zeros.

*Case $1 \leq x_4 \leq 7$.* The five $\delta_k$ are alternate adjacent differences among positions $5, \dots, 14$, so their sum telescopes below $x_5 - x_{14} \leq x_5 \leq x_4 \leq 7$, whence $2Z_0 + Z_1 \geq 10 - 7 = 3$.

*Case $x_4 \in \{8, 9\}$.* Sorting forces $x_0, \dots, x_3 \in \{8, 9\}$, and a direct check of the two subcases $x_0 = x_3$ and $x_0 = x_3 + 1$ gives $\mathrm{core}(x) \leq 999$ and $\mathrm{core}(x) \leq 9999$ respectively — in both, $\mathrm{core}(x) < 10^4$, so decimal place $4$ of the output is zero, joining the $\geq 1$ block zero. $\blacksquare$

**E.2 (even ladder, $d \geq 18$).** *(Proven.) For even $d \geq 18$, every admissible input satisfies $K^{(d)}(x) \in T_d$.*

*Proof.* The even core $\mathrm{core}_6$ occupies places $0$–$5$ (its exact maximum over the $5{,}005$ sorted $6$-tuples is $899{,}991 < 10^6$, attained at $(9,9,9,9,9,0)$), and the first appended pair sits at places $(7, 8)$: place $6$ belongs to neither core nor any block, so it is identically zero in the output. With $M' = (d-6)/2$ pairs the block count gives $2Z_0 + Z_1 \geq 2M' - 9$ as before, and the free zero at place $6$ makes the total $\geq 2M' - 8$, which is $\geq 4$ once $M' \geq 6$, that is $d \geq 18$. $\blacksquare$

**E.3 (the enumerated range).** *(Computed; every row re-run in full for this paper.) For $7 \leq d \leq 16$, the maximum number of steps for an admissible orbit to enter $T_d$, over all admissible multisets on the appropriate ladder, is*

| $d$ | admissible multisets | max steps to $T_d$ |
|---:|---:|---:|
| $7$ | $11{,}340$ | $8$ |
| $8$ | $24{,}210$ | $6$ |
| $9$ | $48{,}520$ | $3$ |
| $10$ | $92{,}278$ | $3$ |
| $11$ | $167{,}860$ | $2$ |
| $12$ | $293{,}830$ | $2$ |
| $13$ | $497{,}320$ | $2$ |
| $14$ | $817{,}090$ | $2$ |
| $15$ | $1{,}307{,}404$ | $1$ |
| $16$ | $2{,}042{,}875$ | $1$ |

*The $d = 15, 16$ rows confirm one-step closure where E.1 applies and just below the even threshold; exhaustive one-step confirmations at $d = 17$ ($3{,}124{,}450$ multisets), $d = 18$ ($4{,}686{,}725$), and $d = 20$ ($10{,}014{,}905$) are in the project log [S].*

E.1–E.3 together give a uniform reaching-time bound at every $d \geq 7$, which is Lemma 4.5's role in the induction. One gap remains: when an orbit lands in $T_d$ and Lemma 4.3 projects it to length $d - 2$, the projected multiset may not be admissible there.

**E.4 (projection lemma).** *For $n \in A_d \cap T_d$ with sorted form $(x_0, \dots, x_{d-3}, 0, 0)$, write $m$ for the length-$(d-2)$ projection. Exactly three things can happen. If $m$ is admissible, the inductive hypothesis applies. If $m$ is a repdigit $(v, \dots, v)$, then $n$ is block-aligned, $K^{(d)}(n) = 0$, and $n \in E_d$. If $m$ is a near-repdigit, the orbit recovers an admissible projection within two further steps and the induction proceeds.*

*Proof of the recovery claim.* The admissible Case-2 inputs at $d$ have sorted form $(v^{d-3}, w, 0, 0)$ with $v \neq 0$, $w \neq v$ — eighty-one $(v, w)$ pairs. For $w < v$ and $d - 2 \geq 7$ the projected value has the closed form $K^{(d-2)}(m) = 9(v - w) \cdot 10^{d-3}$: if $v - w \geq 2$ this has two distinct nonzero digits and $d - 4$ zeros, an admissible multiset at $d-2$, and the induction resumes after one step. If $v - w = 1$ the value is $9 \cdot 10^{d-3}$, whose projection $(9, 0, \dots, 0)$ is again near-repdigit; one further step gives $K^{(d-2)} = 9 \cdot 9900 = 89{,}100$, with projection $(9, 8, 1, 0, \dots, 0)$ — admissible. The $w > v$ cases and the ladder roots $d - 2 \in \{5, 6\}$, where the closed form does not apply, were checked by direct enumeration: at every $7 \leq d \leq 20$, all eighty-one Case-2 multisets reach $60714$, seventy-two recovering in one step and nine in two ($81$/$0$ at $d = 7$), with total reaching time at most $27$ steps on the odd ladder and $15$ on the even, the maxima stable in $d$ through $d = 30$ [S]. $\blacksquare$

## The ladder, explicitly

Labelling sorted positions $a = s_0, b = s_1, c = s_2, \dots$ in descending order, a rule is two letter-strings whose $k$-th letter names the position feeding decimal place $10^{d-1-k}$ of the respective rearrangement. The ladder of Theorem 4.1 reads:

| $d$ | ladder | $\pi$ | $\sigma$ |
|---:|:---|:---|:---|
| 5 | odd (root) | `adcbe` | `deacb` |
| 6 | even (root) | `eadcbf` | `fdeacb` |
| 7 | odd | `fgadcbe` | `gfdeacb` |
| 8 | even | `hgeadcbf` | `ghfdeacb` |
| 9 | odd | `hifgadcbe` | `ihgfdeacb` |
| 10 | even | `jihgeadcbf` | `ijghfdeacb` |
| 11 | odd | `jkhifgadcbe` | `kjihgfdeacb` |
| 12 | even | `lkjihgeadcbf` | `klijghfdeacb` |
| 13 | odd | `lmjkhifgadcbe` | `mlkjihgfdeacb` |
| 14 | even | `nmlkjihgeadcbf` | `mnklijghfdeacb` |
| 15 | odd | `nolmjkhifgadcbe` | `onmlkjihgfdeacb` |
| 16 | even | `ponmlkjihgeadcbf` | `opmnklijghfdeacb` |
| 17 | odd | `pqnolmjkhifgadcbe` | `qponmlkjihgfdeacb` |
| 18 | even | `rqponmlkjihgeadcbf` | `qropmnklijghfdeacb` |
| 19 | odd | `rspqnolmjkhifgadcbe` | `srqponmlkjihgfdeacb` |
| 20 | even | `tsrqponmlkjihgeadcbf` | `stqropmnklijghfdeacb` |

Each rung extends the rung two above by one prepended letter-pair — the appended zero-sum coefficients $(\pm 9 \cdot 10^{d-2}, \mp 9 \cdot 10^{d-2})$, the two ladders differing only in the pair's sign convention — and the four coefficients $(9900, 9, 90, -9000)$ at $60714$'s nonzero digits recur verbatim in every row. Under the fixed-point assignment $a = 7$, $b = 6$, $c = 4$, $d = 1$, all later letters zero, every row evaluates to $\pi \cdot s = 71460$ and $\sigma \cdot s = 10746$, so $K = |71460 - 10746| = 60714$; each row of the table was machine-checked (Computed).

The recipe is mechanical at any length. At $d = 100$ (even ladder): positions $0$–$3$ carry the locked coefficients $(9900, 9, 90, -9000)$, positions $4$–$5$ the split pair $(99000, -99999)$, and positions $6$–$99$ carry forty-seven appended zero-sum pairs $(\mp 9 \cdot 10^{2k+6}, \pm 9 \cdot 10^{2k+6})$. Every coefficient from position $4$ on multiplies a zero digit of the padded fixed point, and
$$K(60714) \;=\; |\,9900 \cdot 7 + 9 \cdot 6 + 90 \cdot 4 - 9000 \cdot 1\,| \;=\; |69300 + 54 + 360 - 9000| \;=\; 60714,$$
the same five-term arithmetic at every length (machine-checked at $d = 100$). What is engineered here is only the fixed-point equation; the basin, which is the theorem, is Section 4 and Appendix E.

## References {.unnumbered}

[Kaprekar 1955] D. R. Kaprekar, "An interesting property of the number 6174," *Scripta Mathematica* **15** (1955), 244–245.

[Trigg 1974] C. W. Trigg, "All three-digit integers lead to 495," *The Mathematics Teacher* **67** (1974), 41–45.

[Prichett 1981] G. D. Prichett, A. L. Ludington, and J. F. Lapenta, "The determination of all decadic Kaprekar constants," *The Fibonacci Quarterly* **19** (1981), 45–52.
