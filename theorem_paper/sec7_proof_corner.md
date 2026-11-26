### The base-free map, proved

The observation made for the second example of this section, that the deficits on its cycle do not depend on the base, can be made precise for every half-swap rule. Fix a half-swap rule on $2n$ digits, $n \ge 1$, with pairs $(P_q, M_q)$, $q = 0, \dots, n-1$ (Definition 5.1); the pairs do not depend on $b$. Throughout, $\rho = (\rho_1 \le \dots \le \rho_n)$ is a nondecreasing $n$-tuple of nonnegative integers with largest entry $D = \rho_n$. It is a state in base $b$ exactly when $D \le H = \lfloor (b-1)/2 \rfloor$. Definition 5.8 is stated for even $b$. For any base $b$ and any state $\rho$ with $V(s^\rho) \ne 0$ we use the same words: $T_b(\rho)$ is the state of the image $K(s^\rho)$. This needs only Lemma 5.6, which holds in every base.

**High and low letters.** For an index $j \in \{0, \dots, 2n-1\}$ call $j$ *high* if $j \le n-1$ and *low* if $j \ge n$, and put
$$a_j = \rho_{j+1} \ \ (j \le n-1), \qquad a_j = \rho_{2n-j} \ \ (j \ge n).$$
By the definition of $s^\rho$ in Section 5, in every base $b$ in which $\rho$ is a state, $s^\rho_j = b - 1 - a_j$ for high $j$ and $s^\rho_j = a_j$ for low $j$. A pair is *mixed* if one of its indices is high and the other is low. To pair $q$ we attach two integers $\varepsilon_q \in \{-1, 0, 1\}$ and $\gamma_q$, which depend on $\rho$ and on the rule but not on $b$:

| pair $q$ | $\varepsilon_q$ | $\gamma_q$ |
|:--|:-:|:-:|
| $P_q$, $M_q$ both high | $0$ | $a_{M_q} - a_{P_q}$ |
| $P_q$, $M_q$ both low | $0$ | $a_{P_q} - a_{M_q}$ |
| $P_q$ high, $M_q$ low | $1$ | $-1 - a_{P_q} - a_{M_q}$ |
| $P_q$ low, $M_q$ high | $-1$ | $1 + a_{P_q} + a_{M_q}$ |

**The base-free map $T_\infty$.** Let $\mathrm{sgn}(\rho) = 0$ if $(\varepsilon_q, \gamma_q) = (0, 0)$ for every $q$. Otherwise let $q^*$ be the largest $q$ with $(\varepsilon_q, \gamma_q) \ne (0,0)$; let $\mathrm{sgn}(\rho) = \varepsilon_{q^*}$ if $\varepsilon_{q^*} \ne 0$, and let $\mathrm{sgn}(\rho) \in \{1, -1\}$ be the sign of $\gamma_{q^*}$ if $\varepsilon_{q^*} = 0$. When $\mathrm{sgn}(\rho) \ne 0$, put $\varepsilon'_q = \mathrm{sgn}(\rho)\, \varepsilon_q$, $\gamma'_q = \mathrm{sgn}(\rho)\, \gamma_q$, $\varepsilon'_{-1} = 0$, and
$$h_k = \gamma'_k + \varepsilon'_{k-1} - [k = 0] \qquad (k = 0, \dots, n-1),$$
where $[k=0]$ is $1$ for $k = 0$ and $0$ otherwise. Compute $\theta_0, \dots, \theta_{n-1}$ and borrows $\kappa_0, \dots, \kappa_n$ by
$$\kappa_0 = 0, \qquad \theta_k = h_k + \kappa_k, \qquad \kappa_{k+1} = \begin{cases} -1 & \theta_k < 0, \\ 0 & \theta_k \ge 0, \end{cases}$$
so that here, unlike in the proof of Proposition 7.1, each borrow $\kappa_k$ lies in $\{-1, 0\}$. Put $u_k = \theta_k$ if $\theta_k \ge 0$ and $u_k = -1 - \theta_k$ if $\theta_k < 0$, that is, $u_k = \max(\theta_k, -1-\theta_k) \ge 0$. Then $T_\infty(\rho)$ is the tuple $(u_0, \dots, u_{n-1})$ sorted in increasing order. If $\mathrm{sgn}(\rho) = 0$, $T_\infty(\rho)$ is not defined. Only integer arithmetic on $\rho$ and the pairs enters; the base does not appear.

We call a base $b$ *admissible* for $\rho$ if $b \ge 2D+1$ and $b - 1 > a_{P_q} + a_{M_q}$ for every mixed pair $q$. Every $b \ge 2D + 2$ is admissible, since $a_{P_q} + a_{M_q} \le 2D$. If $b$ is admissible, then $D \le (b-1)/2$, so $\rho$ is a state in base $b$.

**Lemma 7.2.** *(Proven.)* Fix a half-swap rule on $2n$ digits and a nondecreasing $n$-tuple $\rho$ of nonnegative integers with largest entry $D$. Put $B(D) = 4D + 3$.

(a) For every admissible base $b$: $V(s^\rho) = 0$ if and only if $\mathrm{sgn}(\rho) = 0$, and otherwise $V(s^\rho)$ has the sign $\mathrm{sgn}(\rho)$. Moreover $\mathrm{sgn}(\rho) = 0$ exactly when the rule has no mixed pair and $\gamma_q = 0$ for every $q$.

(b) If $\mathrm{sgn}(\rho) \ne 0$, every entry of $T_\infty(\rho)$ is at most $2D + 1$.

(c) Let $\mathrm{sgn}(\rho) \ne 0$ and let $b$ be admissible. Then $T_b(\rho) = T_\infty(\rho)$ if and only if $b \ge 2\max T_\infty(\rho) + 1$.

(d) In particular, for every base $b \ge B(D)$: whether $V(s^\rho)$ is zero, and its sign if not, are given by $\mathrm{sgn}(\rho)$ and do not depend on $b$; and if $V(s^\rho) \ne 0$, then $T_b(\rho) = T_\infty(\rho)$ does not depend on $b$, and its largest entry is at most $2D+1$.

*Proof.* *Step 1 (the differences).* Let $b$ be admissible and $d_q = s^\rho_{P_q} - s^\rho_{M_q}$, so that $V(s^\rho) = \sum_q b^q d_q$. We show
$$d_q = \varepsilon_q\, b + \gamma_q \qquad (q = 0, \dots, n-1).$$
If both indices are high, $d_q = (b-1-a_{P_q}) - (b-1-a_{M_q}) = a_{M_q} - a_{P_q}$. If both are low, $d_q = a_{P_q} - a_{M_q}$. If $P_q$ is high and $M_q$ low, $d_q = b - 1 - a_{P_q} - a_{M_q}$. If $P_q$ is low and $M_q$ high, $d_q = a_{P_q} - (b - 1 - a_{M_q}) = -b + 1 + a_{P_q} + a_{M_q}$. In each case this is $\varepsilon_q b + \gamma_q$ with the table above. Since all $a_j$ lie in $[0, D]$, we also have:
$$\begin{aligned}
|\gamma_q| &\le D && \text{if } \varepsilon_q = 0, \\
-2D-1 \le \gamma_q &\le -1 && \text{if } \varepsilon_q = 1, \\
1 \le \gamma_q &\le 2D+1 && \text{if } \varepsilon_q = -1.
\end{aligned} \tag{1}$$
For a pair that is not mixed, $d_q = \gamma_q$ is an integer independent of $b$. For a mixed pair, $|d_q| = b - 1 - a_{P_q} - a_{M_q} > 0$ by admissibility, and $d_q$ has the sign $\varepsilon_q$. So in every case $d_q \ne 0$ if and only if $(\varepsilon_q, \gamma_q) \ne (0,0)$, and then the sign of $d_q$ is $\varepsilon_q$ if $\varepsilon_q \ne 0$ and the sign of $\gamma_q$ otherwise.

*Proof of (a).* Each $d_q$ is a difference of two digits, so $|d_q| \le b - 1$. If every $d_q$ is $0$, then $V = 0$. Otherwise let $q^*$ be the largest $q$ with $d_q \ne 0$. Then
$$\Bigl|\sum_{q < q^*} b^q d_q\Bigr| \le (b-1)(1 + b + \dots + b^{q^*-1}) = b^{q^*} - 1 < b^{q^*} |d_{q^*}|,$$
so $V \ne 0$ and $V$ has the sign of $d_{q^*}$. By Step 1, $q^*$ is also the largest $q$ with $(\varepsilon_q, \gamma_q) \ne (0,0)$, and the sign of $d_{q^*}$ is $\mathrm{sgn}(\rho)$. The last sentence of (a) holds because $\varepsilon_q \ne 0$ exactly for mixed pairs.

*The borrows.* Suppose $\mathrm{sgn}(\rho) \ne 0$. Multiplying (1) by $\mathrm{sgn}(\rho)$ keeps the following two implications:
$$\varepsilon'_q = 1 \implies \gamma'_q \le -1, \qquad \varepsilon'_q = -1 \implies \gamma'_q \ge 1. \tag{2}$$
We show by induction on $k$ that
$$\begin{aligned}
&\theta_k = \gamma'_k + \delta_k \ \text{ with } \delta_0 = -1 \text{ and } \delta_k \in \{-1, 0\}, \\
&\varepsilon'_k = 1 \implies \theta_k \le -1, \qquad \varepsilon'_k = -1 \implies \theta_k \ge 0.
\end{aligned} \tag{3}$$
For $k = 0$, $\theta_0 = h_0 = \gamma'_0 - 1$, so $\delta_0 = -1$; if $\varepsilon'_0 = 1$ then $\theta_0 \le -2$ by (2), and if $\varepsilon'_0 = -1$ then $\theta_0 \ge 0$ by (2). Let $k \ge 1$ and assume (3) for $k - 1$. Then $\theta_k = \gamma'_k + \delta_k$ with $\delta_k = \varepsilon'_{k-1} + \kappa_k$. If $\varepsilon'_{k-1} = 1$, then $\theta_{k-1} \le -1$, so $\kappa_k = -1$ and $\delta_k = 0$. If $\varepsilon'_{k-1} = -1$, then $\theta_{k-1} \ge 0$, so $\kappa_k = 0$ and $\delta_k = -1$. If $\varepsilon'_{k-1} = 0$, then $\delta_k = \kappa_k \in \{-1, 0\}$. So $\delta_k \in \{-1, 0\}$, and the two implications for $\theta_k$ follow from (2) as in the case $k = 0$. This proves (3).

*Proof of (b).* By (1), $|\gamma'_k| = |\gamma_k| \le 2D + 1$, so (3) gives $-2D - 2 \le \theta_k \le 2D + 1$. Hence $u_k = \theta_k \le 2D+1$ when $\theta_k \ge 0$, and $u_k = -1 - \theta_k \le 2D+1$ when $\theta_k < 0$.

*Proof of (c).* By (a), $V = V(s^\rho) \ne 0$, so $T_b(\rho)$ is defined. If $T_b(\rho) = T_\infty(\rho)$, then every entry of $T_\infty(\rho)$ is a deficit in base $b$, hence at most $(b-1)/2$, and $b \ge 2\max T_\infty(\rho) + 1$. Conversely, let $b \ge 2u_k + 1$ for every $k$. By (a), $V$ has the sign $\mathrm{sgn}(\rho)$, so $m = |V| = \mathrm{sgn}(\rho)\, V \ge 1$ and, by Step 1,
$$N = m - 1 = \sum_{q=0}^{n-1} b^q (\varepsilon'_q b + \gamma'_q) - 1 = \sum_{k=0}^{n-1} h_k b^k + \varepsilon'_{n-1} b^n.$$
Put $x_k = \theta_k$ if $\theta_k \ge 0$ and $x_k = b + \theta_k$ if $\theta_k < 0$. If $\theta_k \ge 0$, then $u_k = \theta_k$ and $2\theta_k \le b - 1$, so $x_k = \theta_k$ is a digit with $x_k \le b - 1 - x_k$, and $r(x_k) = \theta_k = u_k$. If $\theta_k < 0$, then $u_k = -1 - \theta_k \ge 0$ and $b \ge 2u_k + 1 = -2\theta_k - 1$, so $x_k = b + \theta_k$ satisfies $0 \le -\theta_k - 1 \le x_k \le b - 1$; here $b - 1 - x_k = -1 - \theta_k = u_k \le x_k$, so $r(x_k) = u_k$. In both cases $x_k$ is a digit, $r(x_k) = u_k$, and $\theta_k = x_k + b\,\kappa_{k+1}$. Since $h_k = \theta_k - \kappa_k$ and $\kappa_0 = 0$,
$$\sum_{k=0}^{n-1} h_k b^k = \sum_{k=0}^{n-1} \bigl(x_k + b\,\kappa_{k+1} - \kappa_k\bigr) b^k = X + \kappa_n b^n,$$
where $X = \sum_{k=0}^{n-1} x_k b^k$. So $N = X + (\varepsilon'_{n-1} + \kappa_n)\, b^n$, where $0 \le X \le b^n - 1$, and $0 \le N \le b^n - 2$ by Lemma 5.2. Hence $b^n\, |\varepsilon'_{n-1} + \kappa_n| = |N - X| \le b^n - 1$, which forces $\varepsilon'_{n-1} + \kappa_n = 0$ and $N = X$. So the $n$ digits of $N$ are $x_{n-1}, \dots, x_0$, and by Lemma 5.6 the state of $K(s^\rho)$ is the sorted tuple of $r(x_0), \dots, r(x_{n-1})$, that is, of $u_0, \dots, u_{n-1}$. This is $T_\infty(\rho)$.

*Proof of (d).* Let $b \ge 4D + 3$. Then $b \ge 2D + 2$, so $b$ is admissible, and (a) applies. If $V(s^\rho) \ne 0$, then $\mathrm{sgn}(\rho) \ne 0$ by (a), every $u_k \le 2D + 1$ by (b), and $2u_k + 1 \le 4D + 3 \le b$; so (c) applies. $\blacksquare$

*Remarks.* (i) In words: each letter of $s^\rho$ is high ($b-1-\rho_i$) or low ($\rho_i$). A pair of two high or two low letters gives a difference $d_q$ that is an integer independent of $b$; a mixed pair gives $\pm(b - 1 - \rho_i - \rho_j)$, of known sign once $b$ is admissible. The sign of $V$ is that of the top nonzero $d_q$. Writing $|V| - 1$ as a polynomial in $b$ with the coefficients $h_k$, the digits of $N$ are obtained by borrows whose pattern is fixed by the signs of the $\theta_k$, and each digit is either $\theta_k \ge 0$ or $b$ minus $-\theta_k$; the deficit of either kind is $u_k$, which does not involve $b$.

(ii) If the rule covers gap $n - 1$ (in particular, if it covers every gap), the pair covering it has one index $\le n-1$ and one $\ge n$, so it is mixed, and $\mathrm{sgn}(\rho) \ne 0$ for every $\rho$ by (a). Then $T_\infty$ is a map from nondecreasing $n$-tuples of nonnegative integers to themselves.

(iii) Let $\rho^{(0)}, \dots, \rho^{(p-1)}$ be a cycle of $T_\infty$, and let $D$ be the largest entry of all its states. Then it is a cycle of $T_b$ in every base $b \ge 2D + 2$, and also in the base $b = 2D + 1$ when that base is admissible for each state of the cycle. Indeed, each $\mathrm{sgn}(\rho^{(i)})$ is nonzero, since $T_\infty(\rho^{(i)})$ is defined; each image $T_\infty(\rho^{(i)})$ is a state of the cycle, so its entries are at most $D$ and $2\max T_\infty(\rho^{(i)}) + 1 \le 2D + 1 \le b$; and every $b \ge 2D + 2$ is admissible for each $\rho^{(i)}$. So (c) gives $T_b(\rho^{(i)}) = T_\infty(\rho^{(i)})$ for every $i$. This is why the base $77 = 2 \cdot 38 + 1$ is included in Proposition 7.3.

(iv) The bound $B(D) = 4D + 3$ in (d) cannot be lowered as a bound valid for every rule, and the bound $2D + 1$ in (b) is attained. Take $n = 1$, the rule with the single pair $(P_0, M_0) = (0, 1)$, and $\rho = (D)$. Index $0$ is high and index $1$ is low, with $a_0 = a_1 = D$, so the pair is mixed with $\varepsilon_0 = 1$ and $\gamma_0 = -1 - 2D$. Then $\mathrm{sgn}(\rho) = 1$, $h_0 = \theta_0 = -2D - 2$, and $T_\infty(\rho) = (2D + 1)$. The base $b = 4D + 2$ is admissible, since $b \ge 2D + 1$ and $b - 1 = 4D + 1 > 2D$. But there $H = 2D$, so $2D + 1$ is not a deficit and $T_b(\rho) \ne T_\infty(\rho)$, in accordance with (c). (Directly: $V = b - 1 - 2D = 2D + 1$, $N = 2D$, and $T_b(\rho) = (2D)$.)

(v) In an odd base $b$, the state with every entry equal to $(b-1)/2$, whose string is the repdigit of Section 5, gets no value of $T_b$ from Lemma 7.2. Here $D = (b-1)/2$, so $b = 2D + 1$. If the rule has a mixed pair $q$, then $a_{P_q} + a_{M_q} = 2D = b - 1$, so $b$ is not admissible and the lemma does not apply. If it has no mixed pair, then $b$ is admissible, but every $\gamma_q$ is a difference of two equal entries, so $\mathrm{sgn}(\rho) = 0$, and (a) gives $V = 0$, so $T_b$ is not defined there.

**Proposition 7.3.** *(Proven.)* Let $R$ be the ten-digit rule $\mathtt{AFEJBGIDHC} - \mathtt{GIDHCAFEJB}$. Its pairs are
$$(P_q, M_q) = (1,2),\ (9,7),\ (4,3),\ (5,8),\ (0,6) \qquad (q = 0, 1, 2, 3, 4).$$
Put $\rho^{(0)} = (13,13,15,25,31)$, $\rho^{(1)} = (1,1,6,17,38)$ and $\rho^{(2)} = (4,4,18,21,36)$. In every base $b \ge 77$, even or odd,
$$T_b(\rho^{(0)}) = \rho^{(1)}, \qquad T_b(\rho^{(1)}) = \rho^{(2)}, \qquad T_b(\rho^{(2)}) = \rho^{(0)}.$$
The string $s^{\rho^{(0)}}$ is not a repdigit, and no string in its orbit under $K$ is a fixed point of $K$. Hence $R$ is not universal in any base $b \ge 77$. In a base $b \le 76$ this cycle does not exist, because $38$ is not a deficit in such a base.

The rule is universal in base $10$ (Computed: complete enumeration of the $92{,}378$ ten-digit multisets, in `checks/caution_check.py` and again in `checks/check_corner_proof.py`).

*Proof.* *The pairs.* In word 1, $\mathtt{AFEJBGIDHC}$, the letters at places $9, 8, 7, 6, 5$ are $\mathtt{A}, \mathtt{F}, \mathtt{E}, \mathtt{J}, \mathtt{B}$, that is, $P_4, P_3, P_2, P_1, P_0 = 0, 5, 4, 9, 1$, and the letters at places $4, \dots, 0$ are $\mathtt{G}, \mathtt{I}, \mathtt{D}, \mathtt{H}, \mathtt{C}$, that is, $M_4, \dots, M_0 = 6, 8, 3, 7, 2$. Word 2 must then be $M_4 \dots M_0$ followed by $P_4 \dots P_0$, which is $\mathtt{GIDHC}\,\mathtt{AFEJB}$, as given.

*The map $T_\infty$ for this rule.* Here $n = 5$; indices $0$ to $4$ are high and $5$ to $9$ are low, with $a_j = \rho_{j+1}$ for $j \le 4$ and $a_5, a_6, a_7, a_8, a_9 = \rho_5, \rho_4, \rho_3, \rho_2, \rho_1$. Pairs $0$ and $2$ are both high, pairs $1$ and $3$ are both low, and pair $4$, $(0, 6)$, is mixed with $P_4$ high. The table gives $\varepsilon_0 = \dots = \varepsilon_3 = 0$, $\varepsilon_4 = 1$ and
$$\begin{aligned}
&\gamma_0 = \rho_3 - \rho_2, \qquad \gamma_1 = \rho_1 - \rho_3, \qquad \gamma_2 = \rho_4 - \rho_5, \\
&\gamma_3 = \rho_5 - \rho_2, \qquad \gamma_4 = -1 - \rho_1 - \rho_4,
\end{aligned}$$
so that
$$\begin{aligned}
V(s^\rho) &= (\rho_3 - \rho_2) + b\,(\rho_1 - \rho_3) + b^2 (\rho_4 - \rho_5) \\
&\quad + b^3 (\rho_5 - \rho_2) + b^4 (b - 1 - \rho_1 - \rho_4).
\end{aligned}$$
The top pair has $\varepsilon_4 = 1$, so $\mathrm{sgn}(\rho) = 1$ for every $\rho$, and $\varepsilon'_{k-1} = 0$ for $k \le 4$. Hence
$$(h_0, \dots, h_4) = (\rho_3 - \rho_2 - 1,\ \rho_1 - \rho_3,\ \rho_4 - \rho_5,\ \rho_5 - \rho_2,\ -1 - \rho_1 - \rho_4).$$
For the three tuples the borrow computation gives:

| $\rho$ | $(h_0, \dots, h_4)$ | $(\theta_0, \dots, \theta_4)$ | $(u_0, \dots, u_4)$ |
|:----------------|:----------------|:----------------|:----------------|
| $(13,13,15,25,31)$ | $(1,-2,-6,18,-39)$ | $(1,-2,-7,17,-39)$ | $(1,1,6,17,38)$ |
| $(1,1,6,17,38)$ | $(4,-5,-21,37,-19)$ | $(4,-5,-22,36,-19)$ | $(4,4,21,36,18)$ |
| $(4,4,18,21,36)$ | $(13,-14,-15,32,-26)$ | $(13,-14,-16,31,-26)$ | $(13,13,15,31,25)$ |

Sorting the last column gives $T_\infty(\rho)$: $(1,1,6,17,38)$, $(4,4,18,21,36)$ and $(13,13,15,25,31)$.

For example, in the first row $\theta_0 = 1 \ge 0$, so $\kappa_1 = 0$ and $\theta_1 = -2$; then $\kappa_2 = -1$, $\theta_2 = -6 - 1 = -7$, $\kappa_3 = -1$, $\theta_3 = 18 - 1 = 17$, $\kappa_4 = 0$ and $\theta_4 = -39$. So $T_\infty$ maps $\rho^{(0)} \mapsto \rho^{(1)} \mapsto \rho^{(2)} \mapsto \rho^{(0)}$.

*The cycle in every base $b \ge 77$.* We apply Lemma 7.2(c) to each of the three tuples. Their largest entries are $31$, $38$ and $36$, so $2D + 1$ is $63$, $77$ and $73$, all at most $b$. The only mixed pair is pair $4$, with $a_{P_4} + a_{M_4} = a_0 + a_6 = \rho_1 + \rho_4$, which is $38$, $18$ and $25$ for the three tuples, all less than $76 \le b - 1$. So $b$ is admissible for each tuple. The values of $2\max T_\infty(\rho^{(i)}) + 1$ are $2 \cdot 38 + 1 = 77$, $2 \cdot 36 + 1 = 73$ and $2 \cdot 31 + 1 = 63$ for $i = 0, 1, 2$, all at most $b$. Since $\mathrm{sgn}(\rho^{(i)}) = 1$, Lemma 7.2(a) gives $V(s^{\rho^{(i)}}) > 0$, and Lemma 7.2(c) gives $T_b(\rho^{(i)}) = T_\infty(\rho^{(i)})$ for $i = 0, 1, 2$. This is the cycle.

*Non-universality.* Fix $b \ge 77$. All entries of the three tuples are at most $38 \le H$, so they are states and their strings are defined. Let $s = s^{\rho^{(0)}}$. Its largest letter is $b - 1 - 13 \ge 63$ and its smallest is $13$, so $s$ is not a repdigit. We show that for every $k \ge 0$, $K^k(s)$ has the same letters as $s^{\rho^{(k \bmod 3)}}$. For $k = 0$ this is clear. If $K^k(s)$ has the letters of $s^{\rho^{(i)}}$, then $K^{k+1}(s) = K(s^{\rho^{(i)}})$, since $K$ depends only on the letters. Here $V(s^{\rho^{(i)}}) > 0$, so $K(s^{\rho^{(i)}})$ is an image with $m \ge 1$, and its state is $T_b(\rho^{(i)}) = \rho^{(i+1 \bmod 3)}$. By Lemma 5.6 its letters are those of $s^{\rho^{(i+1 \bmod 3)}}$. This completes the induction.

The five smallest letters of $s^{\rho}$ are the entries of $\rho$, and the three tuples are distinct, so the strings $s^{\rho^{(0)}}, s^{\rho^{(1)}}, s^{\rho^{(2)}}$ have three different multisets of letters. Hence $K^k(s)$ and $K^{k+1}(s)$ have different letters for every $k \ge 0$, so $K^{k+1}(s) \ne K^k(s)$: no string in the orbit of $s$ is a fixed point of $K$. In particular the orbit of $s$ never reaches a nonzero fixed point $F$, and it never reaches $0$, which is fixed. So $R$ is not universal in base $b$. (Since $K^3(s)$ has the letters of $s$, $K^4(s) = K(s)$, and the three strings $K(s), K^2(s), K^3(s)$ form a cycle of $K$ of length $3$.)

*Bases $b \le 76$.* A deficit satisfies $r(x) = \min(x, b-1-x) \le (b-1)/2$. The state $\rho^{(1)}$ contains $38$, and $38 \le (b-1)/2$ only when $b \ge 77$. So for $b \le 76$ no image has the state $\rho^{(1)}$, and the three states cannot form a cycle of $T_b$. This says nothing about other cycles in small bases; by the second example of this section the rule is universal in every base from $3$ to $13$ and in base $16$ (complete enumeration). $\blacksquare$

(Computed confirmation: `checks/check_corner_proof.py` forms the digit string $s^{\rho^{(0)}}$ in every base $b$ from $77$ to $1200$ and in the bases $100003$, $1000003$ and $1000000007$, applies $K$ (word 1 minus word 2, absolute value) three times, and reads off the states $\rho^{(1)}$, $\rho^{(2)}$, $\rho^{(0)}$ after the three steps in every one of these bases.)
