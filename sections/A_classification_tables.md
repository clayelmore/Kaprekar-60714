[← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [Next: 2. Framework →](02_framework.md)](01_introduction.md) · [Next: 3. Classification of Universal Full-Variable Fixed Points at $d \leq 6$ →](03_classifications.md)](02_framework.md) · [Next: 4. Cross-Dimensional Cross-Check: $d = 5 \to d = 6$ →](04_cross_check.md)](03_classifications.md) · [Next: 5. Dimension-Transcendence of $F = 60714$ →](05_theorem_60714.md)](04_cross_check.md) · [Next: 6. The $\{7, 6, 4, 1\}$-Thread →](06_thread_7641.md)](05_theorem_60714.md) · [Next: 7. Open Questions and Conjectures →](07_open_questions.md)](06_thread_7641.md) · [Next: Appendix A. Classification Tables at $d = 3, 4, 5, 6$ →](A_classification_tables.md)](07_open_questions.md) · [Next: Appendix B. Coefficient-preserving ladder for $F = 60714$ →](B_60714_ladder.md)

---

# Appendix A. Classification Tables at $d = 3, 4, 5, 6$

This appendix provides the complete enumerated classifications at digit lengths $d = 3, 4, 5, 6$. Each section lists all universal full-variable fixed points at the given $d$ along with representative data for one universal rule per fixed point. Sign-flipped duplicates are not listed separately (see Proposition 2.2).

The classifications were computed by exhaustive enumeration in Python. Runtime on commodity hardware: negligible at $d = 3, 4$; 3 seconds at $d = 5$; roughly 3 hours at $d = 6$. Source code for the enumerations is available in the supplementary materials.

## A.1 Classification at $d = 3$

**Full-variable rules enumerated:** $3! \cdot D_3 = 6 \cdot 2 = 12$.
**Admissible inputs enumerated:** $720$ (non-repdigit, non-near-repdigit $3$-digit integers).
**Universal full-variable fixed points:** $0$.

No full-variable rule at $d = 3$ is universal for any fixed point. For every rule, iteration from at least some admissible input enters a cycle or a non-universal fixed point.

**Note on the dimension-agnostic fixed point $495$.** The classical rule $K_0$ at $d = 3$ is universal for $495$, but has algebraic rank $2$ (the middle-position coefficient vanishes; see §1.1). $495$ is thus an sv$=2$ fixed point, not an sv$=3$ fixed point, and is outside the scope of the full-variable classification.

## A.2 Classification at $d = 4$

**Full-variable rules enumerated:** $4! \cdot D_4 = 24 \cdot 9 = 216$.
**Admissible inputs enumerated:** $8{,}991$.
**Universal full-variable fixed points:** $4$.
**Universal full-variable rules (total, counting sign-flip pairs):** $8$.

| Fixed point | Digit multiset | Sample $\pi$ | Sample $\sigma$ | Sample coefficient vector |
|:---:|:---:|:---:|:---:|:---|
| $1746$ | $\{1, 4, 6, 7\}$ | $(0, 3, 2, 1)$ | $(1, 2, 3, 0)$ | $(-9, 900, 90, -999 + 18)$ |
| $2538$ | $\{2, 3, 5, 8\}$ | $(1, 0, 3, 2)$ | $(2, 3, 0, 1)$ | $(-90, -999, 999, 90)$ |
| $5382$ | $\{2, 3, 5, 8\}$ | $(2, 1, 0, 3)$ | $(3, 0, 1, 2)$ | $(-900, 9, -9, 900)$ |
| $6174$ | $\{1, 4, 6, 7\}$ | $(0, 1, 2, 3)$ | $(3, 2, 1, 0)$ | $(-999, -90, 90, 999)$ |

**Note on $6174$.** One of the two universal rules for $6174$ is the classical Kaprekar rule $K_0$ (descending minus ascending), recovering Kaprekar's original 1949 result within our classification.

**Note on anagram clusters.** The four fps fall into two anagram pairs: $\{1746, 6174\}$ (multiset $\{1, 4, 6, 7\}$) and $\{2538, 5382\}$ (multiset $\{2, 3, 5, 8\}$). In each cluster, the two fps sum to $7920$, a specific instance of reverse-pair identity at $d = 4$.

## A.3 Classification at $d = 5$

**Full-variable rules enumerated:** $5! \cdot D_5 = 120 \cdot 44 = 5{,}280$.
**Admissible inputs enumerated:** $99{,}540$.
**Universal full-variable fixed points:** $33$.
**Universal full-variable rules (total, counting sign-flip pairs):** $66$.

The $33$ fixed points grouped by digit multiset:

| Multiset | Fixed points | Cluster size |
|:---|:---|:---:|
| $\{0, 0, 0, 4, 5\}$       | $54$                             | $1$ |
| $\{0, 3, 3, 5, 7\}$       | $3753$                           | $1$ |
| $\{0, 1, 4, 6, 7\}$       | $60417$, $60714$                 | $2$ |
| $\{2, 3, 5, 8, 9\}$       | $28539$, $53928$, $58239$         | $3$ |
| $\{1, 2, 3, 4, 8\}$       | $18342$, $21834$, $24183$, $41832$, $42183$ | $5$ |
| $\{1, 5, 6, 7, 8\}$       | $16578$, $16758$, $17685$, $65781$, $67581$ | $5$ |
| $\{3, 4, 5, 7, 8\}$       | $37584$, $37854$, $38754$, $43758$, $43785$, $43875$ | $6$ |
| $\{1, 2, 4, 5, 6\}$       | $12456$, $14562$, $15642$, $16524$, $21456$, $24156$, $24561$, $41562$, $45612$, $45621$ | $10$ |

The complete list of $33$ fixed points in ascending order:

$$54,\ 3753,\ 12456,\ 14562,\ 15642,\ 16524,\ 16578,\ 16758,\ 17685,\ 18342,$$
$$21456,\ 21834,\ 24156,\ 24183,\ 24561,\ 28539,\ 37584,\ 37854,\ 38754,\ 41562,$$
$$41832,\ 42183,\ 43758,\ 43785,\ 43875,\ 45612,\ 45621,\ 53928,\ 58239,\ 60417,$$
$$60714,\ 65781,\ 67581.$$

**Representative rules at the $\{0, 1, 4, 6, 7\}$ cluster** (the $\{7, 6, 4, 1\}$-thread of §6):

| Fixed point | $\pi$ | $\sigma$ | Coefficient vector |
|:---:|:---:|:---:|:---|
| $60714$ | $(4, 1, 2, 3, 0)$ | $(2, 0, 1, 4, 3)$ | $(9900,\; 9,\; 90,\; -9000,\; -999)$ |
| $60417$ | $(4, 1, 0, 3, 2)$ | $(0, 2, 1, 4, 3)$ | $(9999,\; -90,\; -9,\; -9000,\; -900)$ |

**Note on $54$.** The fixed point $54$ appears in the $d = 5$ full-variable classification under the rule $\pi = (1, 2, 4, 3, 0)$, $\sigma = (2, 0, 3, 4, 1)$ with coefficient vector $(-90, 99, 9000, -9000, -9)$. This rule is algebraically full-variable at $d = 5$ ($\mathrm{sv} = 5$), but its effective rank at $F = 54$ is only $2$ — three of the five coefficients land on zero digits of $F$'s sorted-descending form $(5, 4, 0, 0, 0)$ and do not contribute to $K(F) = F$. Thus $\mathrm{sv}_F(K_{54}) = 2 < 5 = \mathrm{sv}(K_{54})$. This is structurally analogous to the $495$ phenomenon at $d = 3$ (§1.1), occurring at higher digit length within a genuinely full-variable rule.

**Note on $3753$.** Similarly, $3753$ has sorted-descending form $(7, 5, 3, 3, 0)$ at $d = 5$ with one zero digit. Its effective rank under its native rule is $\mathrm{sv}_F = 4 < 5$.

Both $54$ and $3753$ are dimension-locked at $d = 5 \to d = 6$: the cross-check of §4 finds no universal full-variable rule for either at $d = 6$.

## A.4 Classification at $d = 6$

**Full-variable rules enumerated:** $6! \cdot D_6 = 720 \cdot 265 = 190{,}800$.
**Admissible inputs enumerated:** $999{,}900$.
**Universal full-variable fixed points:** $506$.
**Universal full-variable rules (total, counting sign-flip pairs):** $1{,}174$.

## A.4.1 Summary statistics

The $506$ fixed points distribute by zero-digit count:

| Zero-digit count | Fixed-point count |
|:---:|:---:|
| $0$ | $205$ |
| $1$ | $240$ |
| $2$ | $53$  |
| $3$ | $8$   |
| $4$ | $1$   |

And by digit sum (every universal fp at $d = 6$ has digit sum divisible by $9$):

| Digit sum | Fixed-point count |
|:---:|:---:|
| $9$ | $8$ |
| $18$ | $156$ |
| $27$ | $244$ |
| $36$ | $96$ |
| $45$ | $3$ |

## A.4.2 Distinguished fixed points

The following $d = 6$ universal full-variable fixed points are singled out elsewhere in the paper:

| Fixed point | Digit multiset | Note |
|:---:|:---:|:---|
| $549945$ | $\{4, 4, 5, 5, 9, 9\}$ | zero-zero fp; algebraically obstructed at $d = 6 \to d = 7$ |
| $60714$ | $\{0, 0, 1, 4, 6, 7\}$ | central result; universal at every $d \geq 5$ (Theorem 5.2) |
| $146070$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$; transcendent to $d = 7$ |
| $170460$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$ |
| $607140$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$; transcendent to $d = 7$ |
| $631764$ | $\{1, 3, 4, 6, 6, 7\}$ | attractor at $d = 6$ under classical rule with basin $0.0625$ [Dahl 2026] |

## A.4.3 Fixed points with two or more zero digits

The complete list of $506$ universal full-variable fixed points at $d = 6$ is lengthy; we provide it in the supplementary materials as a plain-text file (`d6_fps.txt`). The enumeration is fully reproducible from the source code.

Of particular relevance to §5 (the $60714$ theorem) and §6 (the $\{7, 6, 4, 1\}$-thread) are the fps with at least two zero digits, since these are the strata where dimension-transcendent behavior empirically concentrates (cf. Conjecture 7.2).

**The $8$ fps with $3$ zero digits.** All eight share digit multiset $\{5, 2, 2, 0, 0, 0\}$ and are distinct integer arrangements of the same digits:

$$252,\ \ 2520,\ \ 20025,\ \ 25200,\ \ 200025,\ \ 200250,\ \ 250200,\ \ 252000.$$

That all eight 3-zero fps belong to a single multiset is a notable structural fact — at higher zero-count strata, the multiset diversity drops sharply.

**The $53$ fps with $2$ zero digits**, grouped by digit multiset:

| Multiset | Cluster size | Sample fps |
|:---|:---:|:---|
| $\{9, 9, 8, 1, 0, 0\}$ | $32$ | $8919, 8991, 9189, 10899, 80919, 80991, \ldots$ |
| $\{5, 5, 4, 4, 0, 0\}$ | $7$  | $4545, 44505, 54450, 445005, 445050, 504450, 544500$ |
| $\{9, 7, 1, 1, 0, 0\}$ | $5$  | $7191, 17019, 700191, 701901, 719100$ |
| $\{7, 6, 4, 1, 0, 0\}$ | $4$  | $60714, 146070, 170460, 607140$ |
| $\{7, 7, 3, 1, 0, 0\}$ | $2$  | $37017, 707130$ |
| $\{9, 5, 2, 2, 0, 0\}$ | $1$  | $9225$ |
| $\{7, 6, 3, 2, 0, 0\}$ | $1$  | $67023$ |
| $\{6, 5, 5, 2, 0, 0\}$ | $1$  | $52605$ |

The complete sorted list of all $53$ fps with $2$ zero digits:

$$4545, 7191, 8919, 8991, 9189, 9225, 10899, 17019, 37017, 44505, 52605, 54450,$$
$$60714, 67023, 80919, 80991, 81099, 89019, 90819, 90918, 91809, 98091, 100899,$$
$$108099, 109809, 146070, 170460, 180909, 189009, 190089, 190809, 445005,$$
$$445050, 504450, 544500, 607140, 700191, 701901, 707130, 719100, 809091,$$
$$809109, 810909, 890091, 900891, 901890, 908091, 908109, 908190, 908901,$$
$$909081, 910089, 910809.$$

**The $\{7, 6, 4, 1, 0, 0\}$ multiset cluster.** The four fps in this cluster — $60714, 146070, 170460, 607140$ — share the multiset structure of the central object of §5 (60714 padded to $d = 6$). They are precisely the universal full-variable fps in this multiset at $d = 6$, and the cross-dimensional behavior of all four is documented at §6 and in Appendix D.

**Note on the unique $4$-zero fp.** §A.4.1 records one universal full-variable fp at $d = 6$ with $4$ zero digits. Its identity is recorded in `d6_fps.txt` in the supplementary materials but is not analyzed individually in this paper.

**Fixed points with $0$ or $1$ zero digit.** The remaining $445$ fps ($205$ with $0$ zeros, $240$ with $1$ zero) are listed in the supplementary file and are not analyzed individually here. Cross-dimensional behavior at $d = 6 \to d = 7$ for fps with fewer than $2$ zeros is empirically rare (cf. Observation D.1).

## A.5 Cross-reference to §4 and §6

The $33$ fixed points at $d = 5$ of §A.3 are the subject of §4's cross-check: the exhaustive computation of which are dimension-locked at $d = 5 \to d = 6$. The result ($17$ algebraic obstruction, $15$ dynamic obstruction, $1$ universal lifting to $d = 6$) is proven at that section.

The $8$ fixed points with $3$ zero digits at $d = 6$ of §A.4.1 are the subject of §6's transcendent-fp analysis at $d = 6 \to d = 7$ (empirical observations recorded in Appendix D).

---

*End of Appendix A.*

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [← Previous: [← Back to paper](../README.md#table-of-contents) · [Next: 2. Framework →](02_framework.md)](01_introduction.md) · [Next: 3. Classification of Universal Full-Variable Fixed Points at $d \leq 6$ →](03_classifications.md)](02_framework.md) · [Next: 4. Cross-Dimensional Cross-Check: $d = 5 \to d = 6$ →](04_cross_check.md)](03_classifications.md) · [Next: 5. Dimension-Transcendence of $F = 60714$ →](05_theorem_60714.md)](04_cross_check.md) · [Next: 6. The $\{7, 6, 4, 1\}$-Thread →](06_thread_7641.md)](05_theorem_60714.md) · [Next: 7. Open Questions and Conjectures →](07_open_questions.md)](06_thread_7641.md) · [Next: Appendix A. Classification Tables at $d = 3, 4, 5, 6$ →](A_classification_tables.md)](07_open_questions.md) · [Next: Appendix B. Coefficient-preserving ladder for $F = 60714$ →](B_60714_ladder.md)
