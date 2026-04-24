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
| $60417$ | $(4, 3, 2, 0, 1)$ | $(0, 2, 3, 1, 4)$ | $(9999,\; -90,\; -9,\; -9000,\; -900)$ |

**Note on $54$.** The fixed point $54$ appears in the $d = 5$ full-variable classification under the rule $\pi = (1, 2, 4, 3, 0)$, $\sigma = (2, 0, 3, 4, 1)$ with coefficient vector $(-90, 99, 9000, -9000, -9)$. This rule is algebraically full-variable at $d = 5$ ($\mathrm{sv} = 5$), but its effective rank at $F = 54$ is only $2$ — three of the five coefficients land on zero digits of $F$'s sorted-descending form $(5, 4, 0, 0, 0)$ and do not contribute to $K(F) = F$. Thus $\mathrm{sv}_F(K_{54}) = 2 < 5 = \mathrm{sv}(K_{54})$. This is structurally analogous to the $495$ phenomenon at $d = 3$ (§1.1), occurring at higher digit length within a genuinely full-variable rule.

**Note on $3753$.** Similarly, $3753$ has sorted-descending form $(7, 5, 3, 3, 0)$ at $d = 5$ with one zero digit. Its effective rank under its native rule is $\mathrm{sv}_F = 4 < 5$.

Both $54$ and $3753$ are dimension-locked at $d = 5 \to d = 6$: the cross-check of §4 finds no universal full-variable rule for either at $d = 6$.

## A.4 Classification at $d = 6$

**Full-variable rules enumerated:** $6! \cdot D_6 = 720 \cdot 265 = 190{,}800$.
**Admissible inputs enumerated:** $999{,}900$.
**Universal full-variable fixed points:** $507$.
**Universal full-variable rules (total, counting sign-flip pairs):** $1{,}288$.

### A.4.1 Summary statistics

The $507$ fixed points distribute by zero-digit count:

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

### A.4.2 Distinguished fixed points

The following $d = 6$ universal full-variable fixed points are singled out elsewhere in the paper:

| Fixed point | Digit multiset | Note |
|:---:|:---:|:---|
| $549945$ | $\{0, 0, 0, 4, 5, 9\}$ | the unique fp with $4$ zero digits |
| $60714$ | $\{0, 0, 1, 4, 6, 7\}$ | central result; universal at every $d \geq 5$ (Theorem 5.2) |
| $146070$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$; transcendent to $d = 7$ |
| $170460$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$ |
| $607140$ | $\{0, 0, 1, 4, 6, 7\}$ | in the $\{7, 6, 4, 1\}$-thread; native at $d = 6$; transcendent to $d = 7$ |
| $631764$ | $\{1, 3, 4, 6, 6, 7\}$ | attractor at $d = 6$ under classical rule with basin $0.0625$ [Dahl 2026] |

### A.4.3 The complete $507$-fp list

The complete list of $507$ universal full-variable fixed points at $d = 6$ is lengthy; we provide it in the supplementary materials as a plain-text file (`d6_fps.txt`) rather than reproduce the full list here. The enumeration is fully reproducible from the source code in the supplementary materials.

Selected entries for reference (fps with two or three zero digits, highlighted because of their relevance to §5 and §6):

*Fixed points with $3$ zero digits at $d = 6$* (8 total):

$102948$, $109902$, $129168$, $149850$, $198090$, $251955$, $549945$, $702000$ —
(illustrative; full list in supplementary materials).

*Fixed points with $2$ zero digits at $d = 6$* (53 total, including $146070$, $607140$, $170460$):

$100089$, $100098$, $102960$, $105570$, $146070$, $170460$, $607140$, $108909$, ... —
(illustrative; full list in supplementary materials).

## A.5 Cross-reference to §4 and §6

The $33$ fixed points at $d = 5$ of §A.3 are the subject of §4's cross-check: the exhaustive computation of which are dimension-locked at $d = 5 \to d = 6$. The result ($17$ algebraic obstruction, $15$ dynamic obstruction, $1$ universal lifting to $d = 6$) is proven at that section.

The $8$ fixed points with $3$ zero digits at $d = 6$ of §A.4.1 are the subject of §6's transcendent-fp analysis at $d = 6 \to d = 7$ (empirical observations recorded in Appendix D).

---

*End of Appendix A.*
