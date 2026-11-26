## Odd lengths

Section 3 treats the even lengths $L = 2n$: the half-swap rule $R_n$ exchanges place $q$ with place $q+n$ for every $q$, and it is universal in every base $b \geq 3$ (Theorem 3.3). This section treats the odd lengths. We first observe that at odd length the place permutation of a rule cannot consist of exchanged pairs: it must fix a place or move letters around a cycle of odd length at least $3$. We then define a rule $M_n$ at length $2n+1$ that fixes the middle place and exchanges the other places in pairs, as $R_n$ does, and we prove that it is universal in every base $b \geq 3$, with an explicit bound on the number of steps. Together with Section 3 this gives one scheme for every length $L \geq 6$ (Theorem 4.17).

As in Section 2, places are counted from the least significant digit, which is place $0$, and the letters $s_0 \geq s_1 \geq \dots \geq s_{L-1}$ are the sorted digits of a string. In letter forms, $\mathtt{A} = s_0$, $\mathtt{B} = s_1$, and so on, and each word is written with its most significant place first.

### Place permutations at odd length

**Definition 4.1.** *Let $(\alpha, \beta)$ be a rule of length $L$ (Definition 2.1), so that letter $i$ is at place $\alpha(i)$ in word 1 and at place $\beta(i)$ in word 2. Its* place permutation *is $\pi = \beta \circ \alpha^{-1}$: the letter at place $a$ in word 1 is at place $\pi(a)$ in word 2. The rule* exchanges places in pairs *if $\pi$ is an involution without fixed points, that is, $\pi(\pi(a)) = a$ and $\pi(a) \neq a$ for every place $a$.*

The rule $R_n$ of Section 3 exchanges places in pairs: its place permutation exchanges $q$ and $q+n$ for $0 \leq q \leq n-1$.

**Proposition 4.2.** *(Proven.) Let $L$ be odd. Then no rule of length $L$ exchanges places in pairs. More precisely, the place permutation $\pi$ of every rule of length $L$ has a fixed place or a cycle of odd length at least $3$. If $\pi$ fixes place $a$, the letter at place $a$ is the same in both words, and its contributions to word 1 and word 2 cancel in the difference.*

*Proof.* The cycles of $\pi$ partition the $L$ places, so their lengths add up to $L$. Since $L$ is odd, at least one cycle has odd length, and that cycle has length $1$ (a fixed place) or odd length at least $3$. An involution has only cycles of length $1$ and $2$; if it has no fixed point, all its cycles have length $2$ and $L$ is even. So no rule of odd length exchanges places in pairs. Finally, if $\pi(a) = a$ and letter $i$ is at place $a$ in word 1, then $\beta(i) = \pi(\alpha(i)) = a = \alpha(i)$, so letter $i$ is at place $a$ in word 2 as well, and the difference of the words contains $b^a s_i - b^a s_i = 0$. $\blacksquare$

So at odd length a rule must fix a place or move letters around a cycle of odd length at least $3$. We take the first option, with exactly one fixed place, in the middle. It is the device of Kaprekar's three-digit routine $\mathtt{ABC} - \mathtt{CBA}$, whose middle letter cancels. Proposition 4.2 says nothing about universality, and rules built on a cycle of odd length at least $3$ are not treated here.

### The rule $M_n$

**Definition 4.3.** *Let $n \geq 3$ and $L = 2n+1$, with letters $s_0 \geq \dots \geq s_{2n}$. Let $(P_q, M_q)$, $0 \leq q \leq n-1$, be the pairs of the half-swap rule $R_n$ (Definitions 3.1 and 3.2), which are written on the letters $0, \dots, 2n-1$. Relabel them by the map $\lambda$ defined by $\lambda(0) = 0$ and $\lambda(i) = i+1$ for $1 \leq i \leq 2n-1$; thus $\lambda$ is a bijection onto $\{0, 2, 3, \dots, 2n\}$, and letter $1$ is left out. The rule $M_n$ is the rule of length $2n+1$ with:*

- *word 1: letter $\lambda(P_q)$ at place $q+n+1$ and letter $\lambda(M_q)$ at place $q$, for $0 \leq q \leq n-1$, and letter $1$ at place $n$;*
- *word 2: letter $\lambda(M_q)$ at place $q+n+1$ and letter $\lambda(P_q)$ at place $q$, for $0 \leq q \leq n-1$, and letter $1$ at place $n$.*

Two warnings on notation. The rule $M_n$ (indexed by the half-length $n$) and the letter $M_q$ (the second entry of the pair at place $q$) are different symbols. In this section $\lambda$ always denotes the relabeling map above; Section 3 uses $\lambda$ for a different quantity inside one proof.

The place permutation of $M_n$ exchanges place $q$ with place $q+n+1$ for $0 \leq q \leq n-1$ and fixes the middle place $n$, which holds the second largest letter $s_1$ in both words. Written out, with "place $q$: $(i, j)$" meaning $(\lambda(P_q), \lambda(M_q)) = (i, j)$, the pairs of $M_n$ are as follows. Here $i$ and $j$ are letters of the $(2n+1)$-digit string.

- $n$ odd, $n = 2k+1$: place $0$: $(n+1, n+2)$; place $1$: $(0, 2n)$; place $2$: $(n, n-1)$; and for $1 \leq j \leq k-1$, place $n+1-2j$: $(2j+1, 2j)$ and place $n-2j$: $(2n-2j, 2n+1-2j)$.
- $n$ even, $n = 2k+2$: place $0$: $(n-1, n)$; place $1$: $(2, 2n)$; place $2$: $(0, 2n-1)$; place $3$: $(n+2, n+1)$; and for $1 \leq j \leq k-1$, place $n+1-2j$: $(2j+2, 2j+1)$ and place $n-2j$: $(2n-1-2j, 2n-2j)$.

These lists are obtained from those of $R_n$ by applying $\lambda$ to every letter. In letters, the first three rules are
$$M_3:\ \mathtt{DAEBCGF} - \mathtt{CGFBDAE}, \qquad M_4:\ \mathtt{GACDBFHIE} - \mathtt{FHIEBGACD},$$
$$M_5:\ \mathtt{DIFAGBCJEKH} - \mathtt{CJEKHBDIFAG}.$$
In each, the middle letter of both words is $\mathtt{B}$, and the first $n$ letters of word 1 are the last $n$ letters of word 2 and conversely.

As in Section 3, $K(s) = \lvert \text{word 1} - \text{word 2} \rvert$ denotes the rule applied to a string $s$; in this section the rule is always $M_n$.

**Lemma 4.4.** *(Proven.) Let $n \geq 3$ and $b \geq 3$, and let $K$ be the rule $M_n$. For every string $s$ of length $2n+1$,*
$$K(s) = (b^{n+1} - 1)\, m, \qquad m = |V|, \qquad V = \sum_{q=0}^{n-1} b^q \bigl(s_{\lambda(P_q)} - s_{\lambda(M_q)}\bigr).$$
*Moreover $0 \leq m \leq b^n - 1$, and $m = 0$ exactly when $s$ is a repdigit.*

*Proof.* Letter $1$ is at place $n$ in both words and cancels. The pair at place $q$ contributes $b^{q+n+1} s_{\lambda(P_q)} + b^q s_{\lambda(M_q)}$ to word 1 and $b^{q+n+1} s_{\lambda(M_q)} + b^q s_{\lambda(P_q)}$ to word 2, so its contribution to the difference is $(b^{q+n+1} - b^q)(s_{\lambda(P_q)} - s_{\lambda(M_q)}) = (b^{n+1} - 1)\, b^q (s_{\lambda(P_q)} - s_{\lambda(M_q)})$. Summing over $q$ gives the factorization.

Write $d_q = s_{\lambda(P_q)} - s_{\lambda(M_q)}$. Each $d_q$ lies in $[-(b-1), b-1]$, so $m \leq (b-1)(1 + b + \dots + b^{n-1}) = b^n - 1$. If $s$ is a repdigit, every $d_q$ is $0$. Conversely, suppose $V = 0$ but some $d_q \neq 0$, and let $q$ be the lowest such index. Then $V \equiv b^q d_q \pmod{b^{q+1}}$, and $b^q d_q \not\equiv 0 \pmod{b^{q+1}}$ because $0 < |d_q| < b$. This is a contradiction, so every $d_q$ is $0$. For $n$ odd the pair $(0, 2n)$ then gives $s_0 = s_{2n}$, so all letters are equal. For $n$ even the pairs $(0, 2n-1)$ and $(2, 2n)$ give $s_0 = s_{2n-1}$ and $s_2 = s_{2n}$; since the letters are sorted, the first makes $s_0, \dots, s_{2n-1}$ equal and the second makes $s_2, \dots, s_{2n}$ equal, so all letters are equal. In both cases $s$ is a repdigit. $\blacksquare$

**Lemma 4.5.** *(Proven.) Let $n \geq 3$, $b \geq 3$, $K = M_n$, and let $s$ be a string of length $2n+1$ that is not a repdigit. Put $N = m - 1$, so $0 \leq N \leq b^n - 2$, and write $N$ with $n$ digits $x_{n-1} \dots x_0$. Then*
$$K(s) = N\, b^{n+1} + (b^{n+1} - 1 - N).$$
*The digits of $K(s)$ are $x_i$ at place $n+1+i$ and $b-1-x_i$ at place $i$, for $0 \leq i \leq n-1$, and $b-1$ at place $n$. So the digit multiset of $K(s)$ consists of one digit $b-1$ and the pairs $\{x_i, b-1-x_i\}$. Let $\rho_1 \leq \dots \leq \rho_n$ be the deficits $r(x_0), \dots, r(x_{n-1})$ in increasing order; then $0 \leq \rho_i \leq H$, and the letters of $K(s)$ are*
$$s_0 = b-1, \qquad s_i = b-1-\rho_i \ \ (1 \leq i \leq n), \qquad s_{2n+1-i} = \rho_i \ \ (1 \leq i \leq n).$$
*No image $K(s)$ is a repdigit. For the value $F = (b-1)(b^{n+1} - 1)$ we have $N = b-2$, and its sorted deficits are $\tau = (0, \dots, 0, 1)$.*

*Proof.* By Lemma 4.4, $K(s) = (b^{n+1} - 1)(N+1) = N b^{n+1} + (b^{n+1} - 1 - N)$. Since $0 \leq N < b^n$, the number $b^{n+1} - 1 - N$ lies in $[0, b^{n+1})$, and its $n+1$ digits are the complements $b-1-x_i$ at places $0, \dots, n-1$ and $b-1-0 = b-1$ at place $n$ (the digit of $N$ at place $n$ is $0$). The term $N b^{n+1}$ puts the $x_i$ at places $n+1, \dots, 2n$. For each pair $\{x_i, b-1-x_i\}$ the smaller entry is $r(x_i)$ and the larger is $b-1-r(x_i)$. Since every deficit is at most $H \leq (b-1)/2$, every larger entry $b-1-\rho_i \geq b-1-H$ is at least every smaller entry $\rho_j \leq H$. Sorting therefore puts $b-1$ first, then $b-1-\rho_1 \geq \dots \geq b-1-\rho_n$, then $\rho_n \geq \dots \geq \rho_1$, which is the display.

If $K(s)$ were a repdigit, all its digits would equal its digit $b-1$ at place $n$; then $x_0 = b-1$ and $b-1-x_0 = b-1$, so $b-1 = 0$, which is false. For $F$ we have $m = b-1$ and $N = b-2$, so $x_0 = b-2$ and $x_i = 0$ for $i \geq 1$; since $b \geq 3$, $r(b-2) = \min(b-2, 1) = 1$ and $r(0) = 0$. $\blacksquare$

We use the multiset notation of Section 3: $\uplus$ is the union of multisets (multiplicities add), $x^{[t]}$ denotes $t$ copies of $x$, and $x^+ = \max(x, 0)$. A state is a nondecreasing $n$-tuple $\rho = (\rho_1 \leq \dots \leq \rho_n)$ of integers in $[0, H]$, as in Definition 3.5, and a multiset of $n$ values in $[0, H]$ is identified with the state that lists it in nondecreasing order.

**Definition 4.6.** *Let $n \geq 3$ and $b \geq 3$. A string of length $2n+1$* has state $\rho$ *if $\rho$ is a state and the digit multiset of the string is*
$$\{b-1\} \uplus \biguplus_{i=1}^{n} \{b-1-\rho_i,\ \rho_i\}.$$

The letters of a string with state $\rho$ are those displayed in Lemma 4.5, by the same sorting argument: $s_0 = b-1$, $s_i = b-1-\rho_i$ and $s_{2n+1-i} = \rho_i$ for $1 \leq i \leq n$. Every state is allowed, including, for $b$ odd, the state with all entries $(b-1)/2$, which Section 3 calls the repdigit state. Here a string with that state is not a repdigit, because of the extra digit $b-1 \neq (b-1)/2$. More generally, no string with a state is a repdigit, since it contains the digits $b-1$ and $\rho_1 \leq H < b-1$. The lemmas below cover the state with all entries $(b-1)/2$ without exception: for $n$ odd it falls under case (Z) of Lemma 4.7, with $A = (b-1)/2 \geq 1$, and for $n$ even under case (Z) of Lemma 4.11, in the subcase $\sigma = 0$.

By Lemma 4.5, the image $K(s)$ of a string that is not a repdigit has the state of its sorted deficits; in particular $F$ has state $\tau$. Since $K$ depends only on the digit multiset, $K(s)$ for a string $s$ with state $\rho$ depends only on $\rho$, and since $s$ is not a repdigit, $K(s)$ again has a state. We write $\rho'$ for this state and call $\rho \mapsto \rho'$ the *reduced map*. In base $b$, $F = (b-2)\, b^{n+1} + (b-1)(b^n + \dots + b) + 1$: its digits are $b-2$, then $n$ digits $b-1$, then $1$, which is $n+2$ digits, written as a string of length $2n+1$ with $n-1$ leading zeros.

*Remark (comparison with the even rule).* Put $t_i = s_{\lambda(i)}$ for $0 \leq i \leq 2n-1$. For a string with state $\rho$, $t_0 = b-1$, $t_i = b-1-\rho_{i+1}$ for $1 \leq i \leq n-1$, and $t_i = \rho_{2n-i}$ for $n \leq i \leq 2n-1$. These are the letters of an even-length image with the same state $\rho$ (Lemma 3.6), except that letter $0$ there is $b-1-\rho_1$ instead of $b-1$. Letter $0$ occurs in exactly one pair of $R_n$, as its first entry, at place $1$ for $n$ odd and at place $2$ for $n$ even. So $V$ is the even rule's $V$ for the state $\rho$ plus $\rho_1 b$ ($n$ odd) or $\rho_1 b^2$ ($n$ even). The proofs below do not depend on this remark; they compute $V$ directly.

### Odd $n$

**Lemma 4.7.** *(Proven.) Let $n = 2k+1 \geq 3$ and $b \geq 3$, and let $\rho$ be a state. Put*
$$w_j = \rho_{2j+1} - \rho_{2j} \ \ (1 \leq j \leq k), \qquad A = b - 1 - \rho_1.$$
*Then $(b-1)/2 \leq A \leq b-1$, $r(A) = \rho_1$ and $0 \leq w_j \leq H$. A string with state $\rho$ has*
$$V = bA - (b^2 - 1)\, w_k - \sum_{j=1}^{k-1} w_j (b-1)\, b^{n-2j}.$$
*The next state $\rho'$ is as follows.*

- *(G) Some $w_j \geq 1$. Let $J$ be the largest such $j$. Then*
$$\begin{aligned}\rho' = {} & \biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \\ & \uplus \{w_J - 1,\ w_J\} \uplus \{0^{[2(k-J)]}\} \uplus \{\rho_1\}.\end{aligned}$$
- *(Z) All $w_j = 0$. Then $m = bA$ with $A \geq 1$, $N = (A-1)\,b + (b-1)$, and*
$$\rho' = \{0^{[n-1]},\ r(A-1)\}.$$

*The state $\tau$ is fixed by the reduced map, and every string with state $\tau$ maps to $F$.*

*Proof.* Since $0 \leq \rho_1 \leq H \leq (b-1)/2$, we have $(b-1)/2 \leq A \leq b-1$, hence $r(A) = b-1-A = \rho_1$. The $w_j$ are nonnegative, and $\sum_j w_j \leq \rho_n - \rho_2 \leq H$, so each $w_j \leq H$.

We compute the differences $s_{\lambda(P_q)} - s_{\lambda(M_q)}$ for a string with state $\rho$, using $s_0 = b-1$, $s_i = b-1-\rho_i$ for $1 \leq i \leq n$ and $s_{2n+1-i} = \rho_i$. Place $1$ is $(0, 2n)$ and gives $s_0 - s_{2n} = (b-1) - \rho_1 = A$. Place $0$ is $(n+1, n+2)$ and gives $\rho_n - \rho_{n-1} = w_k$. Place $2$ is $(n, n-1)$ and gives $(b-1-\rho_n) - (b-1-\rho_{n-1}) = -w_k$. For $1 \leq j \leq k-1$, place $n+1-2j$ is $(2j+1, 2j)$ and gives $\rho_{2j} - \rho_{2j+1} = -w_j$, and place $n-2j$ is $(2n-2j, 2n+1-2j)$ and gives $\rho_{2j+1} - \rho_{2j} = w_j$. Hence
$$V = bA + w_k - b^2 w_k - \sum_{j=1}^{k-1} w_j \bigl(b^{n+1-2j} - b^{n-2j}\bigr),$$
which is the stated formula.

Since $bA \leq b(b-1) < b^2 - 1 < (b-1) b^3$, and $n - 2j \geq 3$ for $j \leq k-1$, we get $V < 0$ as soon as some $w_j \geq 1$. In that case
$$m = \sum_{j=1}^{k-1} w_j (b-1)\, b^{n-2j} + (b^2 - 1)\, w_k - bA.$$
For $1 \leq w \leq H$ we have the base-$b$ expansions
$$w(b-1) = (w-1)\, b + (b-w),$$
$$(b^2 - 1)\, w - bA = (w-1)\, b^2 + (b-1-A)\, b + (b-w),$$
in which every coefficient is a digit: $0 \leq w - 1 \leq H - 1$, $0 \leq b-1-A \leq b-1$, and $1 \leq b-w \leq b-1$. The block of $j \leq k-1$ occupies places $n-2j$ and $n+1-2j$, which are at least $3$, and the last three terms occupy places $0, 1, 2$, so the blocks do not overlap. We also use the deficits $r(w-1) = w-1$, $r(b-w) = w-1$ and $r(b-1-w) = w$ for $1 \leq w \leq H$, and $r(b-1-A) = r(A) = \rho_1$.

(G), $J = k$. Then $m$ is the sum of the blocks above, digit by digit, and $N = m - 1$ lowers the digit $b - w_k \geq 1$ at place $0$ to $b-1-w_k$ with no borrow. The digits of $N$ are $(w_j - 1, b - w_j)$ at places $(n+1-2j, n-2j)$ for each $j < k$ with $w_j \geq 1$, the digits $(0, 0)$ there for each $j < k$ with $w_j = 0$, and $(w_k - 1, b-1-A, b-1-w_k)$ at places $2, 1, 0$. Their deficits are $(w_j - 1)^+$ twice for each $j < k$, and $w_k - 1$, $\rho_1$, $w_k$. This is the formula with $J = k$.

(G), $J < k$. Then $w_j = 0$ for $J < j \leq k$, and $N = X - (bA + 1)$, where $X$ is the sum of the blocks of $j \leq J$. The block of $J$ ends in the digit $b - w_J \geq 1$ at place $p = n - 2J \geq 3$, and $X$ is a multiple of $b^p$. Since $1 \leq bA + 1 < b^3 \leq b^p$, the subtraction lowers that digit to $b-1-w_J$, leaves the higher digits unchanged, and replaces places $0, \dots, p-1$ by the digits of $b^p - 1 - bA$, which are the complements of the digits of $bA$: $b-1-A$ at place $1$ and $b-1$ at the other $p - 1 = 2(k-J)$ places. The deficits are $(w_j - 1)^+$ twice for $j < J$, then $w_J - 1$ and $w_J$, then $0$ repeated $2(k-J)$ times, then $\rho_1$. In both cases this is $n$ values in all, and it is the formula of (G).

(Z). Then $V = bA$, and $A \geq (b-1)/2 \geq 1$. So $m = bA$ and $N = bA - 1 = (A-1)\, b + (b-1)$, with digit $A - 1 \in [0, b-2]$ at place $1$, digit $b-1$ at place $0$, and $0$ at places $2, \dots, n-1$. The deficits are $r(A-1)$ and $n-1$ zeros.

For $\tau = (0, \dots, 0, 1)$ we have $\rho_1 = 0$, $w_k = \rho_n - \rho_{n-1} = 1$ and $w_j = 0$ for $j < k$. So we are in (G) with $J = k$, and $\rho' = \{0^{[2(k-1)]}\} \uplus \{0, 1\} \uplus \{0\} = \tau$. For a string with state $\tau$, $A = b-1$, and $V = b(b-1) - (b^2 - 1) = -(b-1)$, so $m = b-1$ and the image is $(b^{n+1} - 1)(b-1) = F$. $\blacksquare$

**Lemma 4.8.** *(Proven.) Let $n = 2k+1 \geq 3$, $b \geq 3$, and let $\rho$ be a state with $\rho_1 = 0$. Then $\rho'' = \tau$, and if $\rho$ is in case (Z), already $\rho' = \tau$. So a state with $\rho_1 = 0$ reaches $\tau$ in at most $2$ steps of the reduced map.*

*Proof.* Here $A = b-1$. In (Z), $\rho' = \{0^{[n-1]}, r(b-2)\} = \tau$, since $r(b-2) = 1$ for $b \geq 3$; and $\tau$ is fixed. In (G), $\rho'$ contains the value $\rho_1 = 0$, so $\rho'_1 = 0$. Removing one $0$ leaves the multiset
$$\biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \uplus \{0^{[2(k-J)]}\} \uplus \{w_J - 1,\ w_J\},$$
in which every value is taken an even number of times except for one extra copy of $a = w_J - 1 \geq 0$ and one extra copy of $a+1$. Its sorted entries are $\rho'_2, \dots, \rho'_n$, and the differences $w'_j = \rho'_{2j+1} - \rho'_{2j}$ are the differences of its consecutive pairs. By the sorting lemma (Lemma 3.7), exactly one $w'_j$ equals $1$ and the others are $0$. Then $\rho'$ is in case (G) with $\rho'_1 = 0$, its largest index $J'$ has $w'_{J'} = 1$, and
$$\rho'' = \{0^{[2(J'-1)]}\} \uplus \{0, 1\} \uplus \{0^{[2(k-J')]}\} \uplus \{0\} = \tau. \ \blacksquare$$

**Bad states, $n$ odd.** For $n = 2k+1 \geq 3$, a state $\rho$ is called *bad* if $\rho_1 \geq 1$ and $w_j \geq 2$ for every $j$, $1 \leq j \leq k$.

**Lemma 4.9.** *(Proven.) Let $n = 2k+1 \geq 3$ and $b \geq 3$. If $\rho_1 \geq 1$ and $\rho$ is not bad, then $\rho'_1 = 0$.*

*Proof.* It suffices that $\rho'$ contains a $0$. In (Z), $\rho'$ contains $n - 1 \geq 2$ zeros. In (G) there are three cases. If $J < k$, $\rho'$ contains $2(k-J) \geq 2$ zeros. If $J = k$ and $w_k = 1$, it contains $w_J - 1 = 0$. If $J = k$ and $w_k \geq 2$, then, since $\rho$ is not bad, some $j < k$ has $w_j \leq 1$, and $\rho'$ contains $(w_j - 1)^+ = 0$. $\blacksquare$

**Lemma 4.10.** *(Proven.) Let $n = 2k+1 \geq 3$ and $b \geq 3$. If $\rho$ is bad, then $\rho$ is in case (G) with $J = k$,*
$$\rho' = \biguplus_{j<k} \{w_j - 1,\ w_j - 1\} \uplus \{w_k - 1,\ w_k\} \uplus \{\rho_1\},$$
*and $\max(\rho') \leq \rho_n - 1$. A bad state has $\rho_n \geq 3$. Consequently a run of consecutive bad states along an orbit of the reduced map has length at most $\max(0, H-2)$; for $H \leq 2$ there are no bad states.*

*Proof.* In a bad state every $w_j \geq 2$, so $J = k$ and $(w_j - 1)^+ = w_j - 1$, which gives the formula. Since $\rho_2 \geq \rho_1 \geq 1$, every $w_j \leq \rho_n - \rho_2 \leq \rho_n - 1$. Also $\rho_1 \leq \rho_2 = \rho_3 - w_1 \leq \rho_n - 2$. So every entry of $\rho'$ is at most $\rho_n - 1$. A bad state has $\rho_n \geq \rho_3 = \rho_2 + w_1 \geq 1 + 2 = 3$. Along a run of $\ell \geq 1$ bad states the largest deficit drops by at least $1$ at each step, starts at most at $H$, and is at least $3$ at the last state of the run, so $H - (\ell-1) \geq 3$, that is, $\ell \leq H - 2$. If $H \leq 2$, no state has $\rho_n \geq 3$. $\blacksquare$

### Even $n$

**Lemma 4.11.** *(Proven.) Let $n = 2k+2 \geq 4$ and $b \geq 3$, and let $\rho$ be a state. Put*
$$w_j = \rho_{2j+2} - \rho_{2j+1} \ \ (1 \leq j \leq k), \qquad \sigma = b - 1 - \rho_1 - \rho_2,$$
$$\eta = r(\sigma), \qquad \sigma_2 = b - 1 - \rho_2.$$
*Then $0 \leq \sigma \leq b-1$, $(b-1)/2 \leq \sigma_2 \leq b-1$ (so $\sigma_2 \geq 1$), $r(\sigma_2) = \rho_2$ and $0 \leq w_j \leq H$. A string with state $\rho$ has*
$$V = b^2 \sigma_2 + b\,\sigma - (b^3 - 1)\, w_k - \sum_{j=1}^{k-1} w_j (b-1)\, b^{n-2j}.$$
*The next state $\rho'$ is as follows.*

- *(G) Some $w_j \geq 1$. Let $J$ be the largest such $j$. Then*
$$\begin{aligned}\rho' = {} & \biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \\ & \uplus \{w_J - 1,\ w_J\} \uplus \{0^{[2(k-J)]}\} \uplus \{\eta,\ \rho_2\}.\end{aligned}$$
- *(Z) All $w_j = 0$. Then $m = b^2 \sigma_2 + b\,\sigma > 0$. If $\sigma \geq 1$, then $N = \sigma_2 b^2 + (\sigma - 1)\, b + (b-1)$ and*
$$\rho' = \{0^{[n-2]},\ \rho_2,\ r(\sigma - 1)\}.$$
  *If $\sigma = 0$, then $N = (\sigma_2 - 1)\, b^2 + (b-1)\, b + (b-1)$ and*
$$\rho' = \{0^{[n-1]},\ r(\sigma_2 - 1)\}.$$

*The state $\tau$ is fixed by the reduced map, and every string with state $\tau$ maps to $F$.*

*Proof.* Since $\rho_1 + \rho_2 \leq 2H \leq b-1$, we have $0 \leq \sigma \leq b-1$. Since $\rho_2 \leq H \leq (b-1)/2$, we have $(b-1)/2 \leq \sigma_2 \leq b-1$ and $r(\sigma_2) = b-1-\sigma_2 = \rho_2$. The $w_j$ are nonnegative, and $\sum_j w_j \leq \rho_n - \rho_3 \leq H$.

For a string with state $\rho$: place $1$ is $(2, 2n)$ and gives $s_2 - s_{2n} = (b-1-\rho_2) - \rho_1 = \sigma$. Place $2$ is $(0, 2n-1)$ and gives $s_0 - s_{2n-1} = (b-1) - \rho_2 = \sigma_2$. Place $0$ is $(n-1, n)$ and gives $(b-1-\rho_{n-1}) - (b-1-\rho_n) = w_k$. Place $3$ is $(n+2, n+1)$ and gives $\rho_{n-1} - \rho_n = -w_k$. For $1 \leq j \leq k-1$, place $n+1-2j$ is $(2j+2, 2j+1)$ and gives $\rho_{2j+1} - \rho_{2j+2} = -w_j$, and place $n-2j$ is $(2n-1-2j, 2n-2j)$ and gives $\rho_{2j+2} - \rho_{2j+1} = w_j$. Hence
$$V = b^2 \sigma_2 + b\,\sigma + w_k - b^3 w_k - \sum_{j=1}^{k-1} w_j \bigl(b^{n+1-2j} - b^{n-2j}\bigr),$$
which is the stated formula.

We have $b^2 \sigma_2 + b\,\sigma \leq b^3 - b < b^3 - 1 < (b-1)\, b^4$, and $n - 2j \geq 4$ for $j \leq k-1$, so $V < 0$ as soon as some $w_j \geq 1$. For $1 \leq w \leq H$,
$$\begin{aligned}(b^3 - 1)\, w - b^2 \sigma_2 - b\,\sigma = {} & (w-1)\, b^3 + (b-1-\sigma_2)\, b^2 \\ & + (b-1-\sigma)\, b + (b-w),\end{aligned}$$
with every coefficient a digit, and the blocks $w_j (b-1) b^{n-2j} = ((w_j - 1) b + (b - w_j))\, b^{n-2j}$ for $j < k$ occupy places $n-2j \geq 4$ and $n+1-2j$, so nothing overlaps. The deficits needed are $r(b-1-\sigma_2) = \rho_2$, $r(b-1-\sigma) = \eta$, and those listed in the proof of Lemma 4.7.

(G), $J = k$. Then $N = m - 1$ lowers the digit $b - w_k$ at place $0$ to $b-1-w_k$. The digits of $N$ at places $3, 2, 1, 0$ are $(w_k - 1, b-1-\sigma_2, b-1-\sigma, b-1-w_k)$, with deficits $w_k - 1$, $\rho_2$, $\eta$, $w_k$, and the blocks of $j < k$ give $(w_j - 1)^+$ twice each.

(G), $J < k$. Then $w_k = 0$, and $N = X - (b^2 \sigma_2 + b\,\sigma + 1)$, where $X$ is the sum of the blocks of $j \leq J$. The block of $J$ ends in a digit $b - w_J \geq 1$ at place $p = n - 2J \geq 4$, and $1 \leq b^2 \sigma_2 + b\,\sigma + 1 \leq b^3 - b + 1 < b^3 \leq b^p$. So the subtraction lowers that digit to $b-1-w_J$, every place between $3$ and $p-1$ becomes $b-1$, and places $2, 1, 0$ become $b-1-\sigma_2$, $b-1-\sigma$, $b-1$. The places $0$ and $3, \dots, p-1$ number $p - 2 = 2(k-J)$, and they give deficit $0$. Places $1$ and $2$ give $\eta$ and $\rho_2$.

In both cases of (G) this is the stated $\rho'$, with $n$ values in all.

(Z). Then $m = b^2 \sigma_2 + b\,\sigma \geq b^2 > 0$. If $\sigma \geq 1$, then $N = \sigma_2 b^2 + (\sigma - 1)\, b + (b-1)$; the deficits are $\rho_2$ (place $2$), $r(\sigma - 1)$ (place $1$), $0$ (place $0$), and $0$ at places $3, \dots, n-1$, which is $n-2$ zeros in all. If $\sigma = 0$, then $N = \sigma_2 b^2 - 1 = (\sigma_2 - 1)\, b^2 + (b-1)\, b + (b-1)$; the deficits are $r(\sigma_2 - 1)$ and $n-1$ zeros.

For $\tau$ we have $\rho_1 = \rho_2 = 0$, so $\sigma = \sigma_2 = b-1$ and $\eta = 0$; also $w_k = 1$ and $w_j = 0$ for $j < k$. So we are in (G) with $J = k$, and $\rho' = \{0^{[2(k-1)]}\} \uplus \{0, 1\} \uplus \{0, 0\} = \tau$. For a string with state $\tau$,
$$V = b^2(b-1) + b(b-1) - (b^3 - 1) = -(b-1),$$
so $m = b-1$ and the image is $F$. $\blacksquare$

**Lemma 4.12.** *(Proven.) Let $n = 2k+2 \geq 4$, $b \geq 3$, and let $\rho$ be a state with $\rho_2 = 0$. Then $\rho'' = \tau$, and if $\rho$ is in case (Z), already $\rho' = \tau$. So a state with $\rho_2 = 0$ reaches $\tau$ in at most $2$ steps of the reduced map.*

*Proof.* Here $\rho_1 = \rho_2 = 0$, so $\sigma = \sigma_2 = b-1$ and $\eta = 0$. In (Z), $\sigma \geq 1$ and $\rho' = \{0^{[n-2]}, 0, r(b-2)\} = \tau$. In (G), $\rho'$ contains the two zeros $\eta$ and $\rho_2$, so $\rho'_1 = \rho'_2 = 0$. Removing two zeros leaves
$$\biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \uplus \{0^{[2(k-J)]}\} \uplus \{w_J - 1,\ w_J\},$$
whose sorted entries are $\rho'_3, \dots, \rho'_n$; the differences $w'_j = \rho'_{2j+2} - \rho'_{2j+1}$ are those of its consecutive pairs. By the sorting lemma (Lemma 3.7), exactly one $w'_j$ is $1$ and the others are $0$. Then $\rho'$ is in case (G) with $\rho'_1 = \rho'_2 = 0$, hence $\eta' = 0$, and its largest index $J'$ has $w'_{J'} = 1$, so
$$\rho'' = \{0^{[2(J'-1)]}\} \uplus \{0, 1\} \uplus \{0^{[2(k-J')]}\} \uplus \{0, 0\} = \tau. \ \blacksquare$$

**Bad states, $n$ even.** For $n = 2k+2 \geq 4$, a state $\rho$ is called *bad* if $\rho_2 \geq 1$, $w_j \geq 2$ for every $j < k$, $w_k \geq 1$, and it is not the case that $w_k = 1$ and $\eta = 0$. For $n = 4$ we have $k = 1$, and the clause "$w_j \geq 2$ for every $j < k$" is vacuous.

**Lemma 4.13.** *(Proven.) Let $n = 2k+2 \geq 4$ and $b \geq 3$. If $\rho_2 \geq 1$ and $\rho$ is not bad, then $\rho'_2 = 0$. A bad state is in case (G) with $J = k$, and*
$$\rho' = \biguplus_{j<k} \{w_j - 1,\ w_j - 1\} \uplus \{w_k - 1,\ w_k\} \uplus \{\eta,\ \rho_2\}.$$
*In every state, $\eta \leq \rho_1 + \rho_2 \leq 2 \rho_2$.*

*Proof.* It suffices that $\rho'$ contains two zeros. In (Z), $\rho'$ contains at least $n - 2 \geq 2$ zeros. In (G), a state with $\rho_2 \geq 1$ that is not bad has $w_j \leq 1$ for some $j < k$, or $w_k = 0$, or $w_k = 1$ and $\eta = 0$. If $w_k = 0$, then $J < k$ and $\rho'$ contains $2(k-J) \geq 2$ zeros. If $w_k \geq 1$, then $J = k$; if moreover $w_j \leq 1$ for some $j < k$, then $(w_j - 1)^+ = 0$ occurs twice; and if $w_k = 1$ and $\eta = 0$, then $w_k - 1 = 0$ and $\eta = 0$ are two zeros. In a bad state $w_k \geq 1$, so $J = k$, and $(w_j - 1)^+ = w_j - 1$ for $j < k$, which gives the formula. Finally $\eta = r(\sigma) \leq b - 1 - \sigma = \rho_1 + \rho_2 \leq 2 \rho_2$. $\blacksquare$

For a state at time $t$ along an orbit of the reduced map we write $\Lambda_t = \rho_n$ (its largest deficit) and $\mu_t = \rho_2$.

**Lemma 4.14.** *(Proven.) Let $n = 2k+2 \geq 6$ (so $k \geq 2$) and $b \geq 3$. A run of consecutive bad states along an orbit of the reduced map has length at most $\max(0, H - 2)$.*

*Proof.* Let $\rho$ be bad, with $\Lambda = \rho_n$ and $\mu = \rho_2$, and let $\rho'$ be the next state, with $\Lambda'$ and $\mu'$. We have $\sum_j w_j \leq \rho_n - \rho_3 \leq \Lambda - \mu$, and every $w_j \geq 1$; since $k \geq 2$, each $w_j$ is at most $\Lambda - \mu - 1$. By Lemma 4.13 the entries of $\rho'$ are $w_j - 1$ ($j < k$, twice each), $w_k - 1$, $w_k$, $\eta \leq 2\mu$ and $\rho_2 = \mu$, so
$$\Lambda' \leq \max(\Lambda - \mu - 1,\ 2\mu).$$
Also $\rho'$ contains $w_1 - 1$ twice (because $1 < k$) and contains $w_k - 1$ and $w_k$, so its second smallest entry satisfies $\mu' \leq \min(w_1 - 1, w_k)$. Hence
$$2\mu' \leq w_1 + w_k - 1 \leq \Lambda - \mu - 1.$$

Now suppose the states at times $t$ and $t+1$ are both bad; then $\mu_t, \mu_{t+1} \geq 1$. Applying the first inequality at time $t+1$ and the second at time $t$,
$$\begin{aligned}\Lambda_{t+2} & \leq \max(\Lambda_{t+1} - \mu_{t+1} - 1,\ 2\mu_{t+1}) \\ & \leq \max(\Lambda_{t+1} - 2,\ \Lambda_t - \mu_t - 1),\end{aligned}$$
and the right side is at most $\max(\Lambda_t, \Lambda_{t+1}) - 2$. Put $\Lambda^*_t = \max(\Lambda_t, \Lambda_{t+1})$. If the states at times $t$, $t+1$, $t+2$ are bad, this bound applied at $t$ and at $t+1$ gives $\Lambda_{t+2} \leq \Lambda^*_t - 2$ and $\Lambda_{t+3} \leq \max(\Lambda_{t+1}, \Lambda_{t+2}) - 2 \leq \Lambda^*_t - 2$, so $\Lambda^*_{t+2} \leq \Lambda^*_t - 2$.

Let the states at times $t_0, \dots, t_0 + \ell - 1$ be bad, with $\ell \geq 1$. Since $\Lambda^*_{t_0} \leq H$, induction gives $\Lambda_{t_0 + 2i} \leq \Lambda^*_{t_0 + 2i} \leq H - 2i$ whenever $2i \leq \ell - 1$. A bad state has $\Lambda \geq \rho_3 + \sum_j w_j \geq 1 + (2(k-1) + 1) \geq 4$. Take $i = \lfloor (\ell-1)/2 \rfloor$; then $4 \leq H - 2i$ and $\ell \leq 2i + 2 \leq H - 2$. $\blacksquare$

**Lemma 4.15.** *(Proven.) Let $n = 4$ (so $k = 1$) and $b \geq 3$. A run of consecutive bad states along an orbit of the reduced map has length at most $\max(0, 2H - 2) \leq b - 3$.*

*Proof.* Here $\rho = (\rho_1, \rho_2, \rho_3, \rho_4)$, $w = w_1 = \rho_4 - \rho_3$, and for a bad state $w \geq 1$ and $\rho' = \{w - 1, w, \eta, \rho_2\}$. Let the states at times $t$ and $t+1$ be bad, write $\rho$ for the state at time $t$ and $\Lambda = \rho_4$. We claim $\Lambda_{t+2} \leq \Lambda - 1$. Since the state $\rho'$ at time $t+1$ is bad, the state at time $t+2$ is $\{w' - 1, w', \eta', \rho'_2\}$, so $\Lambda_{t+2} = \max(w', \eta', \rho'_2)$, where $w' = \rho'_4 - \rho'_3$ and $\eta'$ is the value of $\eta$ for $\rho'$. We bound the three terms.

- $\rho'_2 \leq w$, because $\rho'$ contains the two entries $w - 1$ and $w$. And $w \leq \Lambda - \rho_3 \leq \Lambda - 1$.
- $\eta' \leq \rho'_1 + \rho'_2$ (Lemma 4.13), and the sum of the two smallest entries of $\rho'$ is at most the sum of any two of its entries, so $\eta' \leq (w - 1) + \rho_2 = \rho_4 - \rho_3 - 1 + \rho_2 \leq \Lambda - 1$.
- If $\rho'_4 = \eta$, then $\rho'_3$ is the largest of the other three entries, $\max(w, \rho_2)$, so $w' = \eta - \max(w, \rho_2) \leq \eta - \rho_2 \leq \rho_1 \leq \rho_2 \leq \rho_3 \leq \Lambda - 1$. Otherwise $w' \leq \rho'_4 = \max(w, \rho_2) \leq \Lambda - 1$, since $\rho_2 \leq \rho_3 \leq \Lambda - 1$.

This proves the claim. Let the states at times $t_0, \dots, t_0 + \ell - 1$ be bad, with $\ell \geq 1$. Applying the claim at $t_0, t_0 + 2, \dots$ gives $\Lambda_{t_0 + 2i} \leq H - i$ whenever $2i \leq \ell - 1$. A bad state has $\Lambda = \rho_3 + w \geq \rho_2 + 1 \geq 2$. Take $i = \lfloor (\ell-1)/2 \rfloor$; then $2 \leq H - i$, so $\ell \leq 2i + 2 \leq 2H - 2$. Finally $2H - 2 \leq (b-1) - 2 = b - 3$, which is nonnegative for $b \geq 3$. (For $b = 3, 4$ we have $H = 1$, and no state has $\Lambda \geq 2$, so there are no bad states.) $\blacksquare$

### The theorem for $M_n$

**Theorem 4.16.** *(Proven.) Let $b \geq 3$ and $n \geq 3$, and let $K$ be the rule $M_n$. Under iteration of $K$, every string of length $2n+1$ (leading zeros allowed) that is not a repdigit reaches*
$$F = (b-1)(b^{n+1} - 1),$$
*and $K(F) = F$. Repdigits map to $0$. The number of steps is at most:*

- *$H + 3 \leq b/2 + 3$ for $n$ odd;*
- *$b/2 + 5$ for $n$ even, $n \geq 6$;*
- *$b + 2$ for $n = 4$.*

*In base $b$, $F$ is the $(n+2)$-digit string $(b-2)(b-1)\cdots(b-1)1$ with $n$ digits $b-1$, written with $n-1$ leading zeros.*

*Proof.* Repdigits map to $0$ by Lemma 4.4. The base-$b$ form of $F$ was computed after Definition 4.6. The string $F$ has state $\tau$: its digit multiset is $\{b-1\}$ together with the pairs $\{b-1-\tau_i, \tau_i\}$ of $\tau$. Every string with state $\tau$ maps to $F$ by Lemma 4.7 ($n$ odd) or Lemma 4.11 ($n$ even), so $F$ is fixed.

Let $y_0$ be a string that is not a repdigit and $y_t = K^t(y_0)$. By Lemmas 4.4 and 4.5, each $y_t$ with $t \geq 1$ has a state $S_t$ (Definition 4.6), and $S_{t+1}$ is the image of $S_t$ under the reduced map. If $S_t = \tau$, then $y_{t+1} = F$ (Lemma 4.7 or 4.11). So it suffices to bound the first $t$ with $S_t = \tau$.

Let $\ell \geq 0$ be the number of bad states at the start of the sequence $S_1, S_2, \dots$, so that $S_1, \dots, S_\ell$ are bad and $S_{\ell+1}$ is not; $\ell$ is finite by Lemmas 4.10, 4.14 and 4.15. For $n$ odd, $S_{\ell+1}$ has $\rho_1 = 0$, or it has $\rho_1 \geq 1$ and then $S_{\ell+2}$ has $\rho_1 = 0$ (Lemma 4.9). For $n$ even the same holds with $\rho_2$ in place of $\rho_1$ (Lemma 4.13). By Lemma 4.8 or 4.12, $S_t = \tau$ for some $t \leq \ell + 4$, so $y_{\ell+5} = F$. The number of steps is at most $\ell + 5$.

$n$ odd. If $H \geq 2$, Lemma 4.10 gives $\ell \leq H - 2$, so at most $H + 3$ steps. If $H = 1$ (that is, $b = 3$ or $b = 4$), the only state with $\rho_1 \geq 1$ is $(1, \dots, 1)$, which is in case (Z) with $A = b-2$ and has $\rho' = \{0^{[n-1]}, r(b-3)\}$. For $b = 4$ this is $\tau$, since $r(1) = 1$. For $b = 3$ it is the all-zero state, which is in case (Z) with $A = b-1$ and maps to $\tau$ by Lemma 4.8. So if $S_1$ has $\rho_1 = 0$, then $S_3 = \tau$ (Lemma 4.8), and otherwise $S_2 = \tau$ ($b = 4$) or $S_3 = \tau$ ($b = 3$). In all cases $y_4 = F$, which is $H + 3$ steps. Finally $H + 3 \leq (b-1)/2 + 3 < b/2 + 3$.

$n$ even, $n \geq 6$. Lemma 4.14 gives $\ell \leq \max(0, H - 2) \leq H$, so at most $H + 5 \leq b/2 + 5$ steps.

$n = 4$. Lemma 4.15 gives $\ell \leq b - 3$, so at most $b + 2$ steps. $\blacksquare$

For $n$ even, $n \geq 6$, the same argument in fact gives at most $5 + \max(0, H-2) = \max(5, H+3)$ steps, since Lemma 4.14 bounds $\ell$ by $\max(0, H-2)$. The run bounds of Lemmas 4.10 and 4.15, and with them the bound $b + 2$ for $n = 4$, are not sharp in general. *(Computed.)* Iterating the reduced map from every state, for $3 \leq b \leq 40$, the longest run of bad states is at most $3$ for $n = 3$, against $H - 2 = 17$ at $b = 40$; for $n = 4$ it is $H$ or $H - 1$ (for example $4$ at $b = 10$ and $18$ at $b = 40$), against $2H - 2$.

*Remark (the choice of fixed letter).* The value of the fixed letter $s_1$ cancels, but its rank in the sorted order does not: changing one digit of the input can change which digit is the second largest, and so can change the output. The fixed letter cannot be $s_0$ in a rule of this kind. If letter $0$ is the fixed letter and the other $2n$ letters are exchanged in pairs, then $V$ depends only on $s_1, \dots, s_{2n}$, so every string whose last $2n$ letters are equal maps to $0$, for example $9111111$ in base $10$, which is not a repdigit. With $s_1$ fixed, Lemma 4.4 shows that only repdigits map to $0$.

### All lengths at least $6$

**Theorem 4.17.** *(Proven.) Let $b \geq 3$ and $L \geq 6$, and put $h = \lceil L/2 \rceil$. Take the rule $R_h$ of Section 3 if $L = 2h$, and the rule $M_{h-1}$ of Definition 4.3 if $L = 2h - 1$. In both rules place $q$ is exchanged with place $q + h$ for every $q$ with $q + h < L$; for odd $L$ the middle place $h - 1$ has no partner and holds $s_1$ in both words. Under iteration of this rule, every string of length $L$ that is not a repdigit reaches*
$$F = (b-1)(b^h - 1),$$
*and $F$ is fixed. Repdigits map to $0$. In base $b$, $F$ is the $(h+1)$-digit string $(b-2)(b-1)\cdots(b-1)1$ with $h - 1$ digits $b-1$, written as a string of length $L$ with $L - h - 1$ leading zeros.*

*Proof.* For $L = 2h$ we have $h \geq 3$, and this is the even-length theorem for $R_h$ (Theorem 3.3), with $n = h$. Its place permutation exchanges $q$ and $q + h$ for $0 \leq q \leq h-1$, which are all $q$ with $q + h < 2h$.

For $L = 2h - 1$ we have $L \geq 7$, so $n = h - 1 \geq 3$, and this is Theorem 4.16: its endpoint is $(b-1)(b^{n+1} - 1) = (b-1)(b^h - 1)$, written with $n - 1 = L - h - 1$ leading zeros. The place permutation of $M_n$ exchanges $q$ and $q + n + 1 = q + h$ for $0 \leq q \leq n - 1 = h - 2$, which are all $q$ with $q + h < 2h - 1$, and fixes place $n = h - 1$. $\blacksquare$

The two lengths $2h - 1$ and $2h$ share the endpoint. In base $10$, length $6$ gives $8991$, lengths $7$ and $8$ give $89991$, lengths $9$ and $10$ give $899991$, and lengths $11$ and $12$ give $8999991$. For even $L$ the step bounds are those of Theorem 3.3. For odd $L$ they are those of Theorem 4.16 applied with $n = h - 1$, whose parity is opposite to that of $h$. For example, $L = 7$ has $n = 3$ and the bound $H + 3$, and $L = 9$ has $n = 4$ and the bound $b + 2$. For odd $L$ every one of these bounds grows with $b$, so this proof does not bound the number of steps independently of the base.
