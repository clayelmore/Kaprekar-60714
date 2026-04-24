# Appendix B. Coefficient-preserving ladder for $F = 60714$

For each digit length $d \geq 5$, the following tables give the permutation-pair rule $K^{(d)}$ under which $F = 60714$ is a universal fixed point, as constructed in §5.

**Conventions.** At digit length $d$, sorted-descending digit positions are labeled $x_0, x_1, \ldots, x_{d-1}$ with $x_0 \geq x_1 \geq \cdots \geq x_{d-1}$. We assign letters $a, b, c, d, e, f, g, \ldots$ to these positions in order, so $a = x_0$, $b = x_1$, etc. The rule $K = \pi \cdot x - \sigma \cdot x$ is written as two letter strings: reading each string left-to-right, the $k$-th letter indicates which sorted-descending position contributes the digit at place $10^{d-1-k}$ of the resulting integer. The coefficient vector is $c_i = 10^{\pi_i} - 10^{\sigma_i}$ for $i = 0, 1, \ldots, d-1$.

**Fixed-point verification.** At every $d$, the assignment $a = 7, b = 6, c = 4, d = 1$, and every subsequent letter $= 0$ corresponds to $F = 60714$'s sorted-descending form (padded to $d$ digits). Under this assignment, $\pi \cdot x$ evaluates to $71460$ and $\sigma \cdot x$ evaluates to $10746$, so $K(F) = |71460 - 10746| = 60714$ at every $d$.

## Table B.1. Ladder rules through $d = 20$

| $d$ | Ladder | $\pi$ (letters) | $\sigma$ (letters) | $\pi \cdot F$ | $\sigma \cdot F$ | $K(F)$ |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 5  | odd (native)    | `adcbe`                    | `deacb`                    | 71460 | 10746 | 60714 |
| 6  | even (split)    | `eadcbf`                   | `fdeacb`                   | 71460 | 10746 | 60714 |
| 7  | odd             | `fgadcbe`                  | `gfdeacb`                  | 71460 | 10746 | 60714 |
| 8  | even            | `hgeadcbf`                 | `ghfdeacb`                 | 71460 | 10746 | 60714 |
| 9  | odd             | `hifgadcbe`                | `ihgfdeacb`                | 71460 | 10746 | 60714 |
| 10 | even            | `jihgeadcbf`               | `ijghfdeacb`               | 71460 | 10746 | 60714 |
| 11 | odd             | `jkhifgadcbe`              | `kjihgfdeacb`              | 71460 | 10746 | 60714 |
| 12 | even            | `lkjihgeadcbf`             | `klijghfdeacb`             | 71460 | 10746 | 60714 |
| 13 | odd             | `lmjkhifgadcbe`            | `mlkjihgfdeacb`            | 71460 | 10746 | 60714 |
| 14 | even            | `nmlkjihgeadcbf`           | `mnklijghfdeacb`           | 71460 | 10746 | 60714 |
| 15 | odd             | `nolmjkhifgadcbe`          | `onmlkjihgfdeacb`          | 71460 | 10746 | 60714 |
| 16 | even            | `ponmlkjihgeadcbf`         | `opmnklijghfdeacb`         | 71460 | 10746 | 60714 |
| 17 | odd             | `pqnolmjkhifgadcbe`        | `qponmlkjihgfdeacb`        | 71460 | 10746 | 60714 |
| 18 | even            | `rqponmlkjihgeadcbf`       | `qropmnklijghfdeacb`       | 71460 | 10746 | 60714 |
| 19 | odd             | `rspqnolmjkhifgadcbe`      | `srqponmlkjihgfdeacb`      | 71460 | 10746 | 60714 |
| 20 | even            | `tsrqponmlkjihgeadcbf`     | `stqropmnklijghfdeacb`     | 71460 | 10746 | 60714 |

## Table B.2. Coefficient vectors through $d = 12$

The coefficient vectors are the same data as the letter strings, presented numerically. For readability we show the first 12 digit lengths only; higher $d$ vectors follow the same pattern (see §B.3 below).

| $d$ | Ladder | Coefficient vector |
|:---:|:---|:---|
| 5  | odd  | $(9900,\ 9,\ 90,\ -9000,\ -999)$ |
| 6  | even | $(9900,\ 9,\ 90,\ -9000,\ 99000,\ -99999)$ |
| 7  | odd  | $(9900,\ 9,\ 90,\ -9000,\ -999,\ 900000,\ -900000)$ |
| 8  | even | $(9900,\ 9,\ 90,\ -9000,\ 99000,\ -99999,\ -9\,000\,000,\ 9\,000\,000)$ |
| 9  | odd  | $(9900,\ 9,\ 90,\ -9000,\ -999,\ 900000,\ -900000,\ 90\,000\,000,\ -90\,000\,000)$ |
| 10 | even | $(9900,\ 9,\ 90,\ -9000,\ 99000,\ -99999,\ -9\,000\,000,\ 9\,000\,000,\ -900\,000\,000,\ 900\,000\,000)$ |
| 11 | odd  | $(9900,\ 9,\ 90,\ -9000,\ -999,\ 900000,\ -900000,\ 90\,000\,000,\ -90\,000\,000,\ 9\,000\,000\,000,\ -9\,000\,000\,000)$ |
| 12 | even | $(9900,\ 9,\ 90,\ -9000,\ 99000,\ -99999,\ -9\,000\,000,\ 9\,000\,000,\ -900\,000\,000,\ 900\,000\,000,\ -90\,000\,000\,000,\ 90\,000\,000\,000)$ |

## B.3. The construction, stated formally

The tables above are the output of a simple recursive recipe that generalizes to every $d \geq 5$:

**Base cases.**  
Odd ladder root: at $d = 5$, $\pi = (4, 1, 2, 3, 0)$, $\sigma = (2, 0, 1, 4, 3)$, coefficient vector $(9900, 9, 90, -9000, -999)$.  
Even ladder root: at $d = 6$, $\pi = (4, 1, 2, 3, 5, 0)$, $\sigma = (2, 0, 1, 4, 3, 5)$, coefficient vector $(9900, 9, 90, -9000, 99000, -99999)$.

**Inductive step.** Given the rule at $d$ on a ladder, the rule at $d + 2$ on the same ladder is obtained by appending two new positions:

$$\pi_{d} = \begin{cases} d + 1 & \text{(odd ladder)} \\ d & \text{(even ladder)} \end{cases}, \quad \pi_{d+1} = \begin{cases} d & \text{(odd ladder)} \\ d + 1 & \text{(even ladder)} \end{cases},$$

$$\sigma_{d} = \begin{cases} d & \text{(odd ladder)} \\ d + 1 & \text{(even ladder)} \end{cases}, \quad \sigma_{d+1} = \begin{cases} d + 1 & \text{(odd ladder)} \\ d & \text{(even ladder)} \end{cases}.$$

In both cases, the two appended coefficients $c_d = 10^{\pi_d} - 10^{\sigma_d}$ and $c_{d+1} = 10^{\pi_{d+1}} - 10^{\sigma_{d+1}}$ satisfy $c_d + c_{d+1} = 0$ — they form a **zero-sum pair**. The only difference between ladders is the sign convention on the new pair.

## Table B.3. Demonstration at $d = 100$

To show the recipe is not merely finite-table-bound but scales mechanically, we give the rule at $d = 100$ on the even ladder.

**Structure of the coefficient vector at $d = 100$.**

- Positions $0$ through $3$: $(9900,\ 9,\ 90,\ -9000)$. These are the coefficients at $F$'s four nonzero-digit positions, preserved verbatim from the native rule at $d = 5$. (Locked nonzero coefficients.)
- Positions $4, 5$: $(99000,\ -99999)$. These are the even-ladder "split" coefficients fixed at the even root ($d = 6$).
- Positions $6, 7, 8, \ldots, 99$: 47 zero-sum pairs, one appended at each even-ladder step from $d = 8$ to $d = 100$.

The $k$-th appended pair (for $k = 1, 2, \ldots, 47$) consists of

$$c_{2k + 4} = -10^{2k + 4} \cdot 9 + (\text{higher-order terms}) = -\,\underbrace{\overbrace{9 \cdot 10^{2k + 4}}^{\text{negative}}}_{\text{(see table)}}, \qquad c_{2k + 5} = +9 \cdot 10^{2k + 4}.$$

Concretely, the first four appended pairs at $d = 10, 12, 14, 16$ are:

| Pair index $k$ | Positions | $(c_i, c_{i+1})$ |
|:---:|:---:|:---|
| 1 | (6, 7)   | $(-9 \times 10^6,\ +9 \times 10^6)$ |
| 2 | (8, 9)   | $(-9 \times 10^8,\ +9 \times 10^8)$ |
| 3 | (10, 11) | $(-9 \times 10^{10},\ +9 \times 10^{10})$ |
| 4 | (12, 13) | $(-9 \times 10^{12},\ +9 \times 10^{12})$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| 47 | (98, 99) | $(-9 \times 10^{98},\ +9 \times 10^{98})$ |

**Fixed-point verification at $d = 100$.** The digits of $F = 60714$ padded to $100$ digits, sorted in descending order, are $a = 7$, $b = 6$, $c = 4$, $d = 1$, and 96 trailing zeros. Under this assignment, every appended coefficient $c_i$ for $i \geq 4$ multiplies a zero digit and contributes nothing to $K(F)$. The computation reduces to

$$K(F) = | (9900)(7) + (9)(6) + (90)(4) + (-9000)(1) | = |\,69300 + 54 + 360 - 9000\,| = 60714.$$

This is the same arithmetic at every $d \geq 5$. **The coefficient-preserving lifting makes the fixed-point equation trivial at every $d$** because the structural content of the lifting lives entirely in the zero-digit positions, which absorb the new coefficients without affecting $K(F)$.

The nontrivial content of Theorem 3 is not that $K(F) = F$ at every $d$ — that is automatic from the construction. The nontrivial content is that every non-quasi-repdigit orbit at every $d \geq 5$ reaches $F$, which is the work done by Lemmas 5.1 and 5.2.
