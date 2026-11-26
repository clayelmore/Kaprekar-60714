## Even lengths

This section proves that at every even length $2n \geq 6$ and in every base $b \geq 3$ there is an explicit rule, the half-swap rule $R_n$, that sends every string of $2n$ digits that is not a repdigit to the constant $F = (b-1)(b^n - 1)$. The rule depends on $n$, but not on $b$.

Notation is as in Section 2, with $L = 2n$. Throughout the section we fix a base $b \geq 3$ and an integer $n \geq 3$. We call the sorted digit $s_i$ *letter* $i$, and places are counted from the least significant digit, which is at place $0$.

### The half-swap rules

**Definition 3.1.** A *half-swap rule* is an assignment, to each place $q \in \{0, \dots, n-1\}$, of an ordered pair $(P_q, M_q)$ of letters, such that the $2n$ entries $P_0, M_0, \dots, P_{n-1}, M_{n-1}$ are the letters $0, 1, \dots, 2n-1$, each once. *Word 1* is the string with $s_{P_q}$ at place $q + n$ and $s_{M_q}$ at place $q$, for every $q$; *word 2* has $s_{M_q}$ at place $q + n$ and $s_{P_q}$ at place $q$. The rule sends a string with sorted digits $s$ to
$$K(s) = \lvert \text{word 1} - \text{word 2} \rvert.$$

Here $K(s)$ means the value of the rule on any string whose sorted digits are $s$ (Definition 2.1 writes $K(x)$ for a string $x$); it depends only on $s$. Between the two words every letter moves exactly $n$ places. We write "place $q$: $(P_q, M_q)$" to give the pair at place $q$.

**Definition 3.2 (the rule $R_n$).** For $n$ odd, $n = 2k+1$, the rule $R_n$ has
$$\text{place } 0: (n,\ n+1), \qquad \text{place } 1: (0,\ 2n-1), \qquad \text{place } 2: (n-1,\ n-2),$$
and, for $j = 1, \dots, k-1$,
$$\text{place } n+1-2j: (2j,\ 2j-1), \qquad \text{place } n-2j: (2n-1-2j,\ 2n-2j).$$
For $n$ even, $n = 2k+2$, the rule $R_n$ has
$$\text{place } 0: (n-2,\ n-1), \qquad \text{place } 1: (1,\ 2n-1),$$
$$\text{place } 2: (0,\ 2n-2), \qquad \text{place } 3: (n+1,\ n),$$
and, for $j = 1, \dots, k-1$,
$$\text{place } n+1-2j: (2j+1,\ 2j), \qquad \text{place } n-2j: (2n-2-2j,\ 2n-1-2j).$$

For $k = 1$ the lists over $j$ are empty. In both cases the places listed are $0, 1, \dots, n-1$, each once, and the letters listed are $0, 1, \dots, 2n-1$, each once, so $R_n$ is a half-swap rule. In letters, with word 1 and word 2 written from the most significant place down, $R_3$ is $\mathtt{CADBFE} - \mathtt{BFECAD}$, $R_4$ is $\mathtt{FABCEGHD} - \mathtt{EGHDFABC}$, and $R_5$ is $\mathtt{CHEAFBIDJG} - \mathtt{BIDJGCHEAF}$.

**Theorem 3.3.** *(Proven.) For every base $b \geq 3$ and every $n \geq 3$, every $2n$-digit string that is not a repdigit reaches $F = (b-1)(b^n - 1)$ under iteration of $R_n$, and $F$ is fixed. Repdigits map to $0$. In base $b$, the digits of $F$ (without leading zeros) are $b-2$, then $n-1$ digits $b-1$, then $1$; in base $10$, $F$ is $8991$, $89991$, $899991$, $\dots$ for $n = 3, 4, 5, \dots$. The number of applications of $R_n$ needed to reach $F$ is at most $7$ for $n$ even, at most $b/3 + 9$ for $n$ odd with $n \geq 5$, and at most $b/2 + 10$ for $n = 3$.*

The proof occupies the rest of the section. We first reduce the rule to a map on a short vector of *deficits* (Lemmas 3.4 to 3.8), then treat odd $n$ and even $n$ separately, and assemble the pieces at the end.

*Remark.* (Computed.) Lengths $2$ and $4$ are excluded for a reason. A complete census of all half-swap rules finds none universal at length $2$ in any of the bases $3$ to $16$. At length $4$ it finds none universal in base $4$, $7$, $8$, $9$, $10$, or $16$, so no half-swap rule of length $4$ is universal in every base. For one half-swap rule of length $4$, the block exchange $\mathtt{ABCD} - \mathtt{CDAB}$, Young [Young 1995] classified the cycles in every base $g$ and proved that, among the bases $g \geq 3$, the rule yields a single nonzero constant precisely when $g = 3 \cdot 2^k$. In that classification some inputs may also fall to $0$, so this is weaker than universality in the sense of Definition 2.2: in base $3$ some inputs do fall to $0$ (the string $2210$ maps to $1111$ and then to $0$, although $32$ is the only nonzero fixed value), while in bases $6$, $12$ and $24$ the rule is universal (Computed).

### The common reduction

For a sorted string $s$ and a half-swap rule we write $d_q = s_{P_q} - s_{M_q}$ for the difference at place $q$.

**Lemma 3.4 (factorization).** *(Proven.) For a half-swap rule,*
$$K(s) = (b^n - 1)\, m, \qquad m = \lvert V \rvert, \qquad V = \sum_{q=0}^{n-1} b^q\, d_q,$$
*and $m \leq b^n - 1$. For the rule $R_n$, $m = 0$ exactly when the string is a repdigit.*

*Proof.* The pair at place $q$ contributes $s_{P_q} b^{q+n} + s_{M_q} b^q$ to word 1 and $s_{M_q} b^{q+n} + s_{P_q} b^q$ to word 2, so it contributes $(b^{q+n} - b^q)\, d_q = (b^n - 1)\, b^q d_q$ to their difference. Summing over $q$ gives the factorization. Each $d_q$ lies in $[-(b-1), b-1]$, so $m \leq (b-1)(1 + b + \dots + b^{n-1}) = b^n - 1$.

If some $d_q$ is nonzero, let $q$ be the lowest place with $d_q \neq 0$. Then $V \equiv b^q d_q \pmod{b^{q+1}}$, and since $0 < \lvert d_q \rvert < b$, $b^{q+1}$ does not divide $b^q d_q$, so $V \neq 0$. Hence $V = 0$ exactly when every $d_q$ is $0$. For $n$ odd, $R_n$ contains the pair $(0, 2n-1)$, so all differences zero forces $s_0 = s_{2n-1}$, a repdigit. For $n$ even, $R_n$ contains the pairs $(0, 2n-2)$ and $(1, 2n-1)$: $s_0 = s_{2n-2}$ makes letters $0, \dots, 2n-2$ equal, and then $s_1 = s_{2n-1}$ makes the last letter equal to them as well. Conversely, for a repdigit every $d_q$ is $0$. $\blacksquare$

In particular repdigits map to $0$.

**Definition 3.5 (deficits and states).** The *deficit* of a digit $x \in \{0, \dots, b-1\}$ is $r(x) = \min(x,\ b-1-x)$. Put $H = \lfloor (b-1)/2 \rfloor$, so $0 \leq r(x) \leq H$. A *state* is a nondecreasing $n$-tuple $\rho = (\rho_1 \leq \rho_2 \leq \dots \leq \rho_n)$ of integers in $[0, H]$. A $2n$-digit string *has state $\rho$* if its digit multiset is
$$\{\, b-1-\rho_1,\ \dots,\ b-1-\rho_n,\ \rho_1,\ \dots,\ \rho_n \,\}.$$
We write $\tau$ for the state $\tau = (0, \dots, 0, 1)$ (it is fixed by the reduced map: Lemmas 3.9 and 3.15).

Since $\rho_n \leq H \leq (b-1)/2$, a string with state $\rho$ has sorted digits
$$s_{i-1} = b-1-\rho_i, \qquad s_{2n-i} = \rho_i \qquad (i = 1, \dots, n). \tag{3.1}$$
Such a string is a repdigit exactly when $s_0 = s_{2n-1}$, that is, $\rho_1 = (b-1)/2$; since every $\rho_i$ lies between $\rho_1$ and $H$, this happens exactly when $b$ is odd and every $\rho_i = (b-1)/2$. We call that state the *repdigit state*. For $b$ even there is none. Because $K$ depends only on the digit multiset, $K$ of a string with state $\rho$ depends only on $\rho$.

**Lemma 3.6 (shape of an image).** *(Proven.) Let $s$ be a string with $m \geq 1$, and write $N = m - 1$ with $n$ base-$b$ digits $x_{n-1}, \dots, x_0$ (place $i$ carries $x_i$; leading zeros allowed). Then*
$$K(s) = N\, b^n + (b^n - 1 - N),$$
*and the $2n$ digits of $K(s)$ are $x_0, \dots, x_{n-1}$ and $b-1-x_0, \dots, b-1-x_{n-1}$. Consequently $K(s)$ has the state $\rho$ whose entries are the sorted deficits $r(x_0), \dots, r(x_{n-1})$. The value $F = (b-1)(b^n-1)$ has state $\tau$, and its base-$b$ digits are as stated in Theorem 3.3.*

*Proof.* By Lemma 3.4, $1 \leq m \leq b^n - 1$, so $0 \leq N \leq b^n - 2$. Then $K(s) = (b^n - 1)m = (m-1) b^n + (b^n - m) = N b^n + (b^n - 1 - N)$. Both $N$ and $b^n - 1 - N$ lie in $[0, b^n - 1]$, so the upper $n$ digits of $K(s)$ are those of $N$ and the lower $n$ digits are those of $b^n - 1 - N$. Since every digit of $b^n - 1$ equals $b-1$, the subtraction has no borrows, and the digits of $b^n - 1 - N$ are $b-1-x_0, \dots, b-1-x_{n-1}$. Each pair $\{x_i, b-1-x_i\}$ equals $\{b-1-r(x_i),\ r(x_i)\}$, which gives the state.

For $F$ we have $m = b-1$, so $N = b-2$, with $x_0 = b-2$ and all other $x_i = 0$. Since $b \geq 3$, $r(b-2) = 1$, and $r(0) = 0$, so the state is $\tau$. The upper half of $F$ is $b - 2$ and the lower half is $b^n - 1 - (b-2) = (b-1)(b^{n-1} + \dots + b) + 1$, whose digits are $n-1$ digits $b-1$ followed by $1$. $\blacksquare$

So after one step every value has a state, and from then on the next value is computed from the state alone. From here on $K$ is the rule $R_n$. For a state $\rho$ other than the repdigit state, write $\rho'$ for the state of $K(s)$, where $s$ is any string with state $\rho$; this is well defined because such an $s$ is not a repdigit, so $m \geq 1$ by Lemma 3.4 (whose statement that $m = 0$ only for repdigits is for $R_n$). We call $\rho \mapsto \rho'$ the *reduced map* of $R_n$.

We write $\uplus$ for the union of multisets (multiplicities add), $x^{[t]}$ for $t$ copies of $x$, and $x^+ = \max(x, 0)$. A multiset of $n$ values in $[0, H]$ is identified with the state that lists it in nondecreasing order.

**Lemma 3.7 (sorting).** *(Proven.) Let a finite multiset consist of values each taken an even number of times, together with one extra copy of $a$ and one extra copy of $a+1$, for some integer $a \geq 0$. Sort it in nondecreasing order and pair consecutive entries: (1st, 2nd), (3rd, 4th), and so on. Then exactly one pair has difference $1$, and every other pair has difference $0$.*

*Proof.* The multiset has an even number of entries. Each value below $a$ occurs an even number of times; going through these values in increasing order, each block of equal values starts at an odd position and fills whole pairs. The value $a$ occurs an odd number of times and its block starts at an odd position, so its copies fill whole pairs except the last copy, which is at an odd position and is paired with the next entry. That entry is the smallest value above $a$, namely $a + 1$, so this pair has difference $1$. The remaining copies of $a+1$ are even in number and start at an odd position, so they and every larger value fill whole pairs. A pair inside a block of equal values has difference $0$. $\blacksquare$

**Lemma 3.8 (the first image is not a repdigit).** *(Proven.) If $s$ is not a repdigit, then $K(s)$, computed with $R_n$, is not a repdigit.*

The lemma is not automatic for half-swap rules: the length-$4$ half-swap rule $\mathtt{ABCD} - \mathtt{CDAB}$ (place $0$: $(1, 3)$, place $1$: $(0, 2)$) sends the base-$3$ string $2210$, which is not a repdigit, to the repdigit $1111$.

*Proof.* By Lemma 3.4, $m \geq 1$, so by Lemma 3.6 $K(s)$ has a state. By Definition 3.5, a repdigit with a state is the string with all $2n$ digits equal to $\kappa$, where $b = 2\kappa + 1$ is odd and $\kappa = (b-1)/2 \geq 1$. Its value is $\kappa(b^{2n} - 1)/(b-1) = (b^n - 1)(b^n + 1)/2$, so it would require $m = (b^n + 1)/2$, that is, $V = \pm (b^n + 1)/2$. Write $E_t = 1 + b + \dots + b^{t-1}$ (so $E_0 = 0$); then $(b^n + 1)/2 = \kappa E_n + 1$.

We read $V = \sum_q b^q d_q$ one place at a time. Put $Q_0 = V$ and $Q_{t+1} = (Q_t - d_t)/b$; then $Q_t = \sum_{q \geq t} b^{q-t} d_q$ is an integer and $d_t \equiv Q_t \pmod b$. When $Q_t \not\equiv 0 \pmod b$, exactly two integers in $[-(b-1), b-1]$ are congruent to $Q_t$, one positive and one negative, so the sign of $d_t$ determines $d_t$. Below, the residues that occur are $\kappa$ and $\kappa+1$, both nonzero modulo $b$. The two representatives of $\kappa$ are $\kappa$ and $\kappa - b = -(\kappa+1)$; those of $\kappa+1$ are $\kappa+1$ and $-\kappa$.

*Case $V > 0$.* $Q_0 = \kappa E_n + 1 \equiv \kappa + 1$. If $d_0 \geq 0$ then $d_0 = \kappa+1$ and $Q_1 = \kappa E_{n-1}$. For $1 \leq t \leq n-1$, if $Q_t = \kappa E_{n-t}$ then $Q_t \equiv \kappa$; if moreover $d_t \geq 0$, then $d_t = \kappa$ and $Q_{t+1} = \kappa E_{n-t-1}$; if $d_t \leq 0$, then $d_t = -(\kappa+1)$.

*Case $V < 0$.* For $0 \leq t \leq n-1$, if $Q_t = -(\kappa E_{n-t} + 1)$ then $Q_t \equiv -(\kappa+1) \equiv \kappa$. If $d_t \geq 0$ then $d_t = \kappa$, and $Q_{t+1} = -(\kappa E_{n-t} + 1 + \kappa)/b = -(\kappa E_{n-t-1} + 1)$, because $\kappa E_{n-t} + \kappa + 1 = \kappa b E_{n-t-1} + 2\kappa + 1 = b(\kappa E_{n-t-1} + 1)$. If $d_t \leq 0$ then $d_t = -(\kappa+1)$. The case starts with $Q_0 = -(\kappa E_n + 1)$.

*$n$ odd.* Here $d_0 = s_n - s_{n+1} \geq 0$, $d_1 = s_0 - s_{2n-1} \geq 0$ and $d_2 = s_{n-1} - s_{n-2} \leq 0$. The two gaps $s_{n-2} - s_{n-1}$ and $s_n - s_{n+1}$ lie inside the full range $s_0 - s_{2n-1}$ and do not overlap, so $d_0 + \lvert d_2 \rvert \leq d_1$. If $V > 0$, the readings above give $d_0 = \kappa+1$, $d_1 = \kappa$, $d_2 = -(\kappa+1)$. If $V < 0$, they give $d_0 = \kappa$, $d_1 = \kappa$, $d_2 = -(\kappa+1)$. Either way $d_0 + \lvert d_2 \rvert \geq 2\kappa + 1 > \kappa = d_1$, a contradiction.

*$n$ even.* Here $d_0 = s_{n-2} - s_{n-1} \geq 0$, $d_1 = s_1 - s_{2n-1} \geq 0$, $d_2 = s_0 - s_{2n-2} \geq 0$ and $d_3 = s_{n+1} - s_n \leq 0$. Since $s_{n-1} \geq s_n$, $d_0 + \lvert d_3 \rvert \leq s_{n-2} - s_{n+1}$, and since $n - 2 \geq 1$ and $n + 1 \leq 2n - 1$, this is at most $s_1 - s_{2n-1} = d_1$. If $V > 0$, then $d_0 = \kappa + 1$ and $d_1 = \kappa$, contradicting $d_0 \leq d_1$. If $V < 0$, then $d_0 = d_1 = d_2 = \kappa$ and $d_3 = -(\kappa+1)$, so $d_0 + \lvert d_3 \rvert = 2\kappa + 1 > d_1$, a contradiction. $\blacksquare$

### The case $n$ odd (length $2n \equiv 2 \pmod 4$)

In this subsection $n = 2k + 1$ with $k \geq 1$.

**Lemma 3.9 (reduced map, $n$ odd).** *(Proven.) Let $\rho$ be a state other than the repdigit state, and put*
$$w_j = \rho_{2j+1} - \rho_{2j} \ (j = 1, \dots, k), \qquad A = b - 1 - 2\rho_1, \qquad g = r(A).$$
*(Here $A$ is a number, not the letter $\mathtt{A}$ of the rule displays, and $g$ is not a gap $g_j$ of Section 2.) Then $0 \leq A \leq b-1$, $g = \min(2\rho_1,\ b-1-2\rho_1)$, $0 \leq w_j \leq H$, and a string with state $\rho$ has*
$$V = bA - (b^2 - 1)\, w_k - \sum_{j=1}^{k-1} w_j\, (b-1)\, b^{n-2j}.$$

- *(G) If some $w_j \geq 1$, let $J$ be the largest such $j$. Then*
$$\begin{aligned} \rho' = {} & \biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \\ & \uplus \{w_J - 1,\ w_J\} \uplus \{0^{[2(k-J)]}\} \uplus \{g\}. \end{aligned}$$
- *(Z) If every $w_j = 0$, then $A \geq 1$ and $\rho' = \{0^{[n-1]},\ r(A-1)\}$.*

*In both cases $\rho'$ is not the repdigit state. Moreover $\tau' = \tau$, and every string with state $\tau$ maps to $F$; in particular $F$ is fixed.*

*Proof.* Since $0 \leq \rho_1 \leq H \leq (b-1)/2$, $0 \leq A \leq b-1$, and $b - 1 - A = 2\rho_1$ gives the formula for $g$. Also $0 \leq w_j \leq \rho_{2j+1} \leq H$.

By (3.1), letter $t$ is $b - 1 - \rho_{t+1}$ for $t \leq n-1$ and $\rho_{2n-t}$ for $t \geq n$. Substituting into the pairs of $R_n$:

- place $0$: $d_0 = s_n - s_{n+1} = \rho_n - \rho_{n-1} = w_k$;
- place $1$: $d_1 = s_0 - s_{2n-1} = (b-1-\rho_1) - \rho_1 = A$;
- place $2$: $d_2 = s_{n-1} - s_{n-2} = \rho_{n-1} - \rho_n = -w_k$;
- place $n+1-2j$ ($1 \leq j \leq k-1$): $s_{2j} - s_{2j-1} = \rho_{2j} - \rho_{2j+1} = -w_j$;
- place $n-2j$ ($1 \leq j \leq k-1$): $s_{2n-1-2j} - s_{2n-2j} = \rho_{2j+1} - \rho_{2j} = w_j$.

Hence $V = w_k + bA - b^2 w_k + \sum_{j<k} w_j (b^{n-2j} - b^{n+1-2j})$, which is the stated formula.

*Sign of $V$.* We have $bA \leq b(b-1) < b^2 - 1 < (b-1) b^3$. If $w_k \geq 1$, then $(b^2 - 1) w_k > bA$; if $w_j \geq 1$ for some $j < k$, then the sum is at least $(b-1) b^{n-2j} \geq (b-1) b^3 > bA$, since $n - 2j \geq 3$. So $V < 0$ as soon as some $w_j \geq 1$, and then
$$m = \sum_{j<k} w_j (b-1)\, b^{n-2j} + (b^2-1)\, w_k - bA.$$
For $1 \leq w \leq H$ we have the base-$b$ expansions
$$w(b-1) = (w-1)\,b + (b-w),$$
$$(b^2-1)\,w - bA = (w-1)\,b^2 + (b-1-A)\,b + (b-w),$$
in which every coefficient is a digit and $b - w \geq 1$. The block of $j < k$ occupies places $n - 2j$ and $n + 1 - 2j$, which lie in $[3, n-1]$; the last three terms occupy places $0, 1, 2$. So the blocks do not overlap.

We also use: for $1 \leq w \leq H$, $r(w-1) = r(b-w) = w-1$ and $r(b-1-w) = r(w) = w$, because $2w \leq b - 1$. And $r(b-1-A) = r(A) = g$.

*(G), $J = k$.* All terms above are nonnegative and occupy disjoint places, so they are the digits of $m$. The digit at place $0$ is $b - w_k \geq 1$, so $N = m - 1$ just lowers it to $b - 1 - w_k$. The digits of $N$ are: $(w_j - 1,\ b - w_j)$ at places $n+1-2j, n-2j$ for each $j < k$ with $w_j \geq 1$; $(0, 0)$ there for each $j < k$ with $w_j = 0$; and $(w_k - 1,\ b-1-A,\ b-1-w_k)$ at places $2, 1, 0$. Their deficits are $(w_j - 1)^+$ twice for each $j < k$, and $w_k - 1$, $g$, $w_k$. This is the formula with $J = k$.

*(G), $J < k$.* Then $w_k = 0$ and $w_j = 0$ for $J < j < k$, so $N = X - (bA + 1)$, where $X$ is the sum of the blocks with $j \leq J$. Put $p = n - 2J \geq 3$. The lowest nonzero digit of $X$ is $b - w_J \geq 1$, at place $p$, and $X$ has zeros at all places below $p$. Since $0 < bA + 1 < b^3 \leq b^p$, we get $N = (X - b^p) + (b^p - 1 - bA)$. The first part lowers the digit at place $p$ to $b - 1 - w_J$ and leaves the higher digits unchanged. The second part is less than $b^p$ and has digit $b - 1 - A$ at place $1$ and $b - 1$ at every other place below $p$. The deficits of $N$ are therefore: $(w_j - 1)^+$ twice for each $j < J$; $w_J - 1$ and $w_J$ from places $p + 1$ and $p$; $g$ from place $1$; and $0$ from each of the $p - 1 = 2(k - J)$ places $0, 2, 3, \dots, p-1$. This is the formula. (The places $3, \dots, p-1$ are those of the blocks with $J < j < k$.)

*(Z).* If $A = 0$ then $\rho_1 = (b-1)/2 = H$, so every $\rho_i = H = (b-1)/2$, the repdigit state, which is excluded. So $A \geq 1$, $V = bA$, $m = bA$, and $N = (A-1)\,b + (b-1)$: digits $b-1$ at place $0$, $A - 1$ at place $1$, and $0$ at places $2, \dots, n-1$. The deficits are $n - 1$ zeros and $r(A-1)$.

*Not the repdigit state.* In (G), $\rho'$ contains $w_J - 1$ and $w_J$, which differ, so its entries are not all equal. In (Z), $\rho'$ contains $n - 1 \geq 2$ zeros, while the repdigit state has every entry equal to $(b-1)/2 \geq 1$.

*The state $\tau$.* For $\tau$, $\rho_1 = 0$, so $A = b-1$ and $g = 0$; also $w_k = \rho_n - \rho_{n-1} = 1$ and $w_j = 0$ for $j < k$. So (G) applies with $J = k$, and $\tau' = \{0^{[2(k-1)]}\} \uplus \{0, 1\} \uplus \{0\} = \tau$. The value is $V = b(b-1) - (b^2 - 1) = -(b-1)$, so $m = b - 1$ and $K = (b-1)(b^n - 1) = F$. Since $F$ has state $\tau$ (Lemma 3.6), $F$ is fixed. $\blacksquare$

**Lemma 3.10.** *(Proven.) Let $n$ be odd and let $\rho$ be a state with $\rho_1 = 0$. Then $\rho' = \tau$ or $\rho'' = \tau$.*

*Proof.* Here $g = 0$ and $A = b - 1$. In case (Z), $\rho' = \{0^{[n-1]},\ r(b-2)\} = \tau$, since $r(b-2) = 1$ for $b \geq 3$. In case (G), $\rho'$ contains $g = 0$, so $\rho'_1 = 0$. The quantities $w'_j = \rho'_{2j+1} - \rho'_{2j}$ are the differences of the consecutive pairs $(\rho'_2, \rho'_3), (\rho'_4, \rho'_5), \dots, (\rho'_{n-1}, \rho'_n)$ of the sorted list obtained by removing one zero from $\rho'$. That list is $\biguplus_{j<J}\{(w_j-1)^+, (w_j-1)^+\} \uplus \{w_J - 1, w_J\} \uplus \{0^{[2(k-J)]}\}$, which satisfies Lemma 3.7 with $a = w_J - 1$. So exactly one $w'_j$ equals $1$ and the others are $0$. Since $\rho'_1 = 0$, case (G) applies to $\rho'$ with $g' = 0$, and
$$\rho'' = \{0^{[2(J'-1)]}\} \uplus \{0, 1\} \uplus \{0^{[2(k-J')]}\} \uplus \{0\} = \tau,$$
where $J'$ is the index with $w'_{J'} = 1$. $\blacksquare$

**Definition 3.11.** For $n$ odd, a state is *bad* if $\rho_1 \geq 1$ and $w_j \geq 2$ for every $j = 1, \dots, k$.

**Lemma 3.12.** *(Proven.) Let $n$ be odd and let $\rho$ be a state other than the repdigit state, with $\rho_1 \geq 1$, that is not bad. Then $\rho'_1 = 0$.*

*Proof.* It suffices to show that $\rho'$ contains a $0$. In case (Z), $\rho'$ contains $n - 1 \geq 2$ zeros. In case (G), since $\rho$ is not bad and $\rho_1 \geq 1$, some $w_j \leq 1$. If $J < k$, $\rho'$ contains $2(k-J) \geq 2$ zeros. If $J = k$ and $w_k = 1$, then $w_J - 1 = 0$. If $J = k$ and $w_k \geq 2$, the index with $w_j \leq 1$ satisfies $j < J$, and $(w_j - 1)^+ = 0$. $\blacksquare$

In a bad state every $w_j \geq 2$, so case (G) applies with $J = k$, and
$$\rho' = \biguplus_{j<k} \{w_j - 1,\ w_j - 1\} \uplus \{w_k - 1,\ w_k\} \uplus \{g\}. \tag{3.2}$$

**Lemma 3.13 (bad runs, $n = 3$).** *(Proven.) Let $n = 3$. Bad states exist only when $H \geq 3$. If $S_0, S_1, \dots, S_T$ are states with $S_{t+1} = S_t'$ for $0 \leq t \leq T-1$, and all of them are bad, then the number $T + 1$ of states is at most $(b+7)/2$.*

*Proof.* For $n = 3$ we have $k = 1$; a state is $(\rho_1, \rho_2, \rho_3)$ with the single quantity $w = \rho_3 - \rho_2$, and $A = b - 1 - 2\rho_1$, $g = r(A)$. A bad state has $\rho_3 \geq \rho_1 + w \geq 3$, and $\rho_3 \leq H$, which gives the first claim. By Lemma 3.9, if $w \geq 1$ then $\rho' = \{w-1,\ w,\ g\}$. We say the step from a state with $w \geq 1$ is of *type (i)* if $g \leq w - 1$, and of *type (ii)* if $g \geq w$; since $g$ and $w$ are integers, one of the two holds.

- Type (i): $\rho' = (g,\ w-1,\ w)$, so $w' = 1$ and $A' = b - 1 - 2g$.
- Type (ii): $\rho' = (w-1,\ w,\ g)$, so $w' = g - w$ and $A' = b - 1 - 2(w-1) = b + 1 - 2w$.

A bad state has $w \geq 2$. If its step is of type (i), the next state has $w' = 1$ and is not bad. So every step from a bad state to a bad state is of type (ii).

We now prove more generally: if $S_0, \dots, S_T$ satisfy $S_{t+1} = S_t'$ and each step $S_t \to S_{t+1}$ ($0 \leq t \leq T-1$) is of type (ii), then $T \leq (b+5)/2$. Write $w^{(t)}$, $A^{(t)}$, $g^{(t)}$ for the quantities of $S_t$. For $1 \leq t \leq T-1$, the step $S_{t-1} \to S_t$ is of type (ii), so $A^{(t)} = b + 1 - 2w^{(t-1)}$ and
$$g^{(t)} = r(A^{(t)}) = \min(b + 1 - 2w^{(t-1)},\ 2w^{(t-1)} - 2);$$
the step $S_t \to S_{t+1}$ is of type (ii), so $w^{(t+1)} = g^{(t)} - w^{(t)}$. Hence, for $1 \leq t \leq T-1$,
$$w^{(t+1)} + w^{(t)} = \min(2w^{(t-1)} - 2,\ b + 1 - 2w^{(t-1)}).$$
Put $\omega_t = w^{(t)} - (b+3)/4$, a rational number. Then $2w^{(t-1)} - 2 = (b-1)/2 + 2\omega_{t-1}$ and $b + 1 - 2w^{(t-1)} = (b-1)/2 - 2\omega_{t-1}$, so the minimum is $(b-1)/2 - 2\lvert \omega_{t-1} \rvert$. Since $w^{(t+1)} + w^{(t)} = \omega_{t+1} + \omega_t + (b+3)/2$,
$$\omega_{t+1} + \omega_t = -2 - 2\lvert \omega_{t-1} \rvert \qquad (1 \leq t \leq T-1).$$
Therefore $\lvert \omega_t \rvert + \lvert \omega_{t+1} \rvert \geq 2 + 2\lvert \omega_{t-1} \rvert$, and so
$$\max(\lvert \omega_t \rvert,\ \lvert \omega_{t+1} \rvert) \geq \lvert \omega_{t-1} \rvert + 1 \qquad (1 \leq t \leq T-1).$$
Choose times $t_0 = 0 < t_1 < t_2 < \dots$ as follows: while $t_i + 2 \leq T$, apply the last inequality with $t = t_i + 1$ and let $t_{i+1} \in \{t_i + 1,\ t_i + 2\}$ satisfy $\lvert \omega_{t_{i+1}} \rvert \geq \lvert \omega_{t_i} \rvert + 1$. By induction $t_i \leq 2i$, so $t_i$ is defined for every $i \leq \lfloor T/2 \rfloor$, and $\lvert \omega_{t_i} \rvert \geq i$. But $0 \leq w \leq (b-1)/2$ gives $-(b+3)/4 \leq \omega \leq (b-5)/4$, so $\lvert \omega \rvert \leq (b+3)/4$. Hence $\lfloor T/2 \rfloor \leq (b+3)/4$ and $T \leq 2\lfloor T/2 \rfloor + 1 \leq (b+5)/2$.

Finally, if $S_0, \dots, S_T$ are all bad, each of the $T$ steps between them goes from a bad state to a bad state and so is of type (ii). Hence $T \leq (b+5)/2$, that is, $T + 1 \leq (b+7)/2$. $\blacksquare$

**Lemma 3.14 (bad runs, $n \geq 5$).** *(Proven.) Let $n = 2k + 1 \geq 5$. If some state is bad, then $H \geq 5$, and any nonempty sequence of consecutive states of the reduced map that are all bad has $\ell$ terms with*
$$\ell \leq \tfrac{2}{3}(H - 5) + 2 < \tfrac{2}{3}H + 4 \leq \tfrac{b}{3} + 4.$$
*In every case a run of consecutive bad states has fewer than $b/3 + 4$ terms.*

*Proof.* For a state write $\lambda = \rho_1$ and $\Lambda = \rho_n$. A bad state has $\Lambda \geq \rho_1 + \sum_j w_j \geq 1 + 2k \geq 5$; since $\Lambda \leq H$, a bad state can exist only if $H \geq 5$. If there is no bad state the last sentence holds trivially, so assume $\ell \geq 1$.

Let $\rho$ be bad. Since $\rho_{2k+1} - \rho_2$ is the sum of the $w_j$ and of the nonnegative gaps $\rho_{2j+2} - \rho_{2j+1}$ ($1 \leq j \leq k-1$), and $\rho_2 \geq \lambda$, we have $\sum_j w_j \leq \Lambda - \lambda$. Each $w_j \geq 2$, so
$$\max_j w_j \leq \Lambda - \lambda - 2(k-1), \qquad \min_j w_j \leq (\Lambda - \lambda)/k.$$
Also $g \leq 2\lambda$. By (3.2), the entries of $\rho'$ are $w_j - 1$ ($j < k$, twice each), $w_k - 1$, $w_k$ and $g$, so
$$\Lambda' \leq \max\bigl(\Lambda - \lambda - 2(k-1),\ 2\lambda\bigr),$$
$$\lambda' \leq \min_j w_j - 1 \leq \frac{\Lambda - \lambda}{k} - 1.$$

Index the states of the orbit by time $t$, with $\lambda_t, \Lambda_t$. Suppose the states at times $t$ and $t+1$ are both bad. The bound on $\Lambda'$ at time $t+1$, with $2(k-1) \geq 2$, gives
$$\Lambda_{t+2} \leq \max\bigl(\Lambda_{t+1} - \lambda_{t+1} - 2,\ 2\lambda_{t+1}\bigr).$$
In the first term, $\lambda_{t+1} \geq 1$ gives $\Lambda_{t+1} - \lambda_{t+1} - 2 \leq \Lambda_{t+1} - 3$. In the second, the bound on $\lambda'$ at time $t$, with $k \geq 2$ and $\Lambda_t - \lambda_t \geq 0$, gives $2\lambda_{t+1} \leq 2(\Lambda_t - \lambda_t)/k - 2 \leq \Lambda_t - \lambda_t - 2$, and $\lambda_t \geq 1$ makes this at most $\Lambda_t - 3$. Hence
$$\Lambda_{t+2} \leq \max(\Lambda_t,\ \Lambda_{t+1}) - 3.$$
Put $\Lambda^*_t = \max(\Lambda_t, \Lambda_{t+1})$. If the states at times $t$, $t+1$, $t+2$ are all bad, applying the last inequality at $t$ and at $t+1$ gives $\Lambda_{t+2} \leq \Lambda^*_t - 3$ and $\Lambda_{t+3} \leq \max(\Lambda_{t+1}, \Lambda_{t+2}) - 3 \leq \Lambda^*_t - 3$, so $\Lambda^*_{t+2} \leq \Lambda^*_t - 3$.

Let the bad states occupy times $t_0, \dots, t_0 + \ell - 1$. Since every $\Lambda \leq H$, $\Lambda^*_{t_0} \leq H$, and the last inequality gives $\Lambda_{t_0 + 2i} \leq \Lambda^*_{t_0 + 2i} \leq H - 3i$ whenever $2i \leq \ell - 1$. Take $i = \lfloor (\ell-1)/2 \rfloor$. The state at time $t_0 + 2i$ is bad, so $5 \leq \Lambda_{t_0+2i} \leq H - 3i$, and $i \leq (H - 5)/3$. Since $\ell \leq 2i + 2$, we get $\ell \leq 2(H-5)/3 + 2$. Finally $2(H-5)/3 + 2 < 2H/3 + 4$, and $H \leq (b-1)/2$ gives $2H/3 + 4 \leq b/3 + 4$. $\blacksquare$

### The case $n$ even (length $2n \equiv 0 \pmod 4$)

In this subsection $n = 2k + 2$ with $k \geq 1$.

**Lemma 3.15 (reduced map, $n$ even).** *(Proven.) Let $\rho$ be a state other than the repdigit state, and put*
$$w_j = \rho_{2j+2} - \rho_{2j+1} \ (j = 1, \dots, k), \qquad \sigma = b - 1 - \rho_1 - \rho_2, \qquad \eta = r(\sigma).$$
*Then $0 \leq \sigma \leq b - 1$, $0 \leq w_j \leq H$, and a string with state $\rho$ has*
$$V = (b^2 + b)\,\sigma - (b^3 - 1)\, w_k - \sum_{j=1}^{k-1} w_j\, (b-1)\, b^{n-2j}.$$

- *(G) If some $w_j \geq 1$, let $J$ be the largest such $j$. Then*
$$\begin{aligned} \rho' = {} & \biguplus_{j<J} \{(w_j - 1)^+,\ (w_j - 1)^+\} \\ & \uplus \{w_J - 1,\ w_J\} \uplus \{0^{[2(k-J)]}\} \uplus \{\eta,\ \eta\}. \end{aligned}$$
- *(Z) If every $w_j = 0$, then $\sigma \geq 1$ and $\rho' = \{0^{[n-2]},\ r(\sigma),\ r(\sigma - 1)\}$.*

*In both cases $\rho'$ is not the repdigit state. Moreover $\tau' = \tau$, and every string with state $\tau$ maps to $F$; in particular $F$ is fixed.*

*Proof.* Since $\rho_1 + \rho_2 \leq 2H \leq b - 1$, $0 \leq \sigma \leq b-1$; and $0 \leq w_j \leq \rho_{2j+2} \leq H$. By (3.1), substituting into the pairs of $R_n$:

- place $0$: $s_{n-2} - s_{n-1} = \rho_n - \rho_{n-1} = w_k$;
- place $1$: $s_1 - s_{2n-1} = (b-1-\rho_2) - \rho_1 = \sigma$;
- place $2$: $s_0 - s_{2n-2} = (b-1-\rho_1) - \rho_2 = \sigma$;
- place $3$: $s_{n+1} - s_n = \rho_{n-1} - \rho_n = -w_k$;
- place $n+1-2j$ ($1 \leq j \leq k-1$): $s_{2j+1} - s_{2j} = \rho_{2j+1} - \rho_{2j+2} = -w_j$;
- place $n-2j$ ($1 \leq j \leq k-1$): $s_{2n-2-2j} - s_{2n-1-2j} = \rho_{2j+2} - \rho_{2j+1} = w_j$.

This gives the formula for $V$.

*Sign of $V$.* We have $(b^2 + b)\sigma \leq (b^2+b)(b-1) = b^3 - b < b^3 - 1 < (b-1)\, b^4$, and the blocks with $j < k$ sit at places $n - 2j \geq 4$. As in Lemma 3.9, $V < 0$ as soon as some $w_j \geq 1$. For $1 \leq w \leq H$,
$$\begin{aligned} (b^3 - 1)\,w - (b^2 + b)\,\sigma = {} & (w-1)\,b^3 + (b-1-\sigma)\,b^2 \\ & + (b-1-\sigma)\,b + (b-w), \end{aligned}$$
with every coefficient a digit and $b - w \geq 1$; and $w(b-1) b^{n-2j}$ has digits $w - 1$ and $b - w$ at places $n+1-2j$ and $n-2j$, as before.

*(G), $J = k$.* The digits of $N = m - 1$ are those of the blocks $j < k$, as in Lemma 3.9, followed by $w_k - 1$, $b-1-\sigma$, $b-1-\sigma$, $b-1-w_k$ at places $3, 2, 1, 0$. Their deficits are $(w_j-1)^+$ twice for each $j < k$, and $w_k - 1$, $\eta$, $\eta$, $w_k$.

*(G), $J < k$.* Then $N = X - \bigl((b^2+b)\sigma + 1\bigr)$, where $X$ is the sum of the blocks with $j \leq J$, whose lowest nonzero digit $b - w_J \geq 1$ is at place $p = n - 2J \geq 4$. Since $0 < (b^2 + b)\sigma + 1 \leq b^3 - b + 1 < b^4 \leq b^p$, the borrow stops at place $p$, as in Lemma 3.9: the digit there becomes $b - 1 - w_J$, places $1$ and $2$ become $b - 1 - \sigma$, and places $0, 3, 4, \dots, p-1$ become $b - 1$. These last are $p - 2 = 2(k-J)$ places with deficit $0$; places $1$ and $2$ give $\eta, \eta$; places $p+1, p$ give $w_J - 1, w_J$; and the blocks $j < J$ give $(w_j - 1)^+$ twice each.

*(Z).* If $\sigma = 0$ then $\rho_1 + \rho_2 = b - 1$ with $\rho_1, \rho_2 \leq (b-1)/2$, which forces $b$ odd and $\rho_1 = \rho_2 = (b-1)/2$, hence every $\rho_i = (b-1)/2$: the repdigit state, which is excluded. So $\sigma \geq 1$, $m = (b^2 + b)\sigma$, and $N = \sigma b^2 + (\sigma - 1)\, b + (b-1)$, with digits $b-1$, $\sigma-1$, $\sigma$ at places $0, 1, 2$ and $0$ at places $3, \dots, n-1$. The deficits are $1 + (n-3) = n-2$ zeros, $r(\sigma)$ and $r(\sigma - 1)$.

*Not the repdigit state.* In (G), $\rho'$ contains the distinct values $w_J - 1$ and $w_J$. In (Z), $\rho'$ contains $n - 2 \geq 2$ zeros, while the repdigit state has every entry equal to $(b-1)/2 \geq 1$.

*The state $\tau$.* For $\tau$, $\rho_1 = \rho_2 = 0$ (as $n \geq 4$), so $\sigma = b - 1$ and $\eta = 0$; also $w_k = 1$ and $w_j = 0$ for $j < k$. Case (G) with $J = k$ gives $\tau' = \{0^{[2(k-1)]}\} \uplus \{0, 1\} \uplus \{0, 0\} = \tau$, and $V = (b^2 + b)(b-1) - (b^3 - 1) = -(b-1)$, so $m = b - 1$ and the value is $F$. Since $F$ has state $\tau$, $F$ is fixed. $\blacksquare$

**Lemma 3.16.** *(Proven.) Let $n$ be even and let $\rho$ be a state other than the repdigit state. Then every $w'_j$ of $\rho'$ is $0$ or $1$, and at most one of them is $1$.*

*Proof.* The quantities $w'_j = \rho'_{2j+2} - \rho'_{2j+1}$ ($j = 1, \dots, k$) are the differences of the consecutive pairs $(\rho'_3, \rho'_4), \dots, (\rho'_{n-1}, \rho'_n)$ of the sorted list $\rho'$, that is, of all pairs in Lemma 3.7's pairing except the first, $(\rho'_1, \rho'_2)$. In case (G), every value in $\rho'$ is taken an even number of times except for one extra $w_J - 1$ and one extra $w_J$ (note that $\eta$ occurs twice), so Lemma 3.7 applies with $a = w_J - 1$: exactly one pair of the pairing has difference $1$ and the rest have difference $0$. In case (Z), the sorted list is $n - 2$ zeros followed by $\min(r(\sigma), r(\sigma-1))$ and $\max(r(\sigma), r(\sigma-1))$, so only the top pair, which defines $w'_k$, can have a nonzero difference, and that difference is $\lvert r(\sigma) - r(\sigma - 1) \rvert \leq 1$, since $r$ changes by at most $1$ when its argument changes by $1$. $\blacksquare$

**Lemma 3.17.** *(Proven.) Let $n$ be even and let $\rho$ be a state with $\rho_1 = \rho_2 = 0$. Then $\rho' = \tau$ or $\rho'' = \tau$.*

*Proof.* Here $\sigma = b - 1$ and $\eta = 0$. In case (Z), $\rho' = \{0^{[n-2]},\ r(b-1),\ r(b-2)\} = \{0^{[n-1]}, 1\} = \tau$, since $b \geq 3$. In case (G), $\rho'$ contains the two zeros $\eta, \eta$, so $\rho'_1 = \rho'_2 = 0$, and by Lemma 3.16 all $w'_j$ are in $\{0, 1\}$ with at most one equal to $1$. If all $w'_j = 0$, case (Z) applied to $\rho'$ gives $\rho'' = \tau$, as just computed. If $w'_{J'} = 1$ and the others are $0$, case (G) applied to $\rho'$, with $\eta' = 0$, gives
$$\rho'' = \{0^{[2(J'-1)]}\} \uplus \{0, 1\} \uplus \{0^{[2(k-J')]}\} \uplus \{0, 0\} = \tau. \qquad \blacksquare$$

**Lemma 3.18.** *(Proven.) Let $n$ be even and let $\rho$ be a state, other than the repdigit state, whose $w_j$ are all in $\{0, 1\}$ with at most one equal to $1$.*

- *If $n \geq 6$, then $\rho'_1 = \rho'_2 = 0$.*
- *If $n = 4$, then $\rho'_1 = \rho'_2 = 0$, or $\rho' = (0, 1, \eta, \eta)$ with $\eta = r(b-1-\rho_1-\rho_2) \geq 1$ as in Lemma 3.15, in which case $\rho''_1 = \rho''_2 = 0$.*

*Proof.* Let $n \geq 6$, so $k \geq 2$. In case (Z), $\rho'$ contains $n - 2 \geq 4$ zeros. In case (G), the single $w_J = 1$ and every other $w_j = 0$, so
$$\rho' = \{0^{[2(J-1)]}\} \uplus \{0, 1\} \uplus \{0^{[2(k-J)]}\} \uplus \{\eta, \eta\},$$
with $2(k-1) + 1 \geq 3$ zeros. Either way $\rho'_1 = \rho'_2 = 0$.

Let $n = 4$, so $k = 1$ and there is a single $w = \rho_4 - \rho_3$. In case (Z), $\rho' = \{0, 0, r(\sigma), r(\sigma-1)\}$, so $\rho'_1 = \rho'_2 = 0$. In case (G), $w = 1$ and $\rho' = \{0, 1, \eta, \eta\}$. If $\eta = 0$ this is $\tau$, which has $\rho'_1 = \rho'_2 = 0$. If $\eta \geq 1$, then $\rho' = (0, 1, \eta, \eta)$ has $w' = \eta - \eta = 0$, so case (Z) applies to $\rho'$ and $\rho''$ begins with two zeros. $\blacksquare$

### Proof of Theorem 3.3

Repdigits map to $0$ by Lemma 3.4, and the digits of $F$ were found in Lemma 3.6. Let $y_0$ be a $2n$-digit string that is not a repdigit, and let $y_t$ be its image after $t$ applications of $R_n$. By Lemmas 3.4 and 3.6, $y_1$ has a state $S_1$, and by Lemma 3.8 $S_1$ is not the repdigit state. By Lemmas 3.9 and 3.15 and induction, for every $t \geq 1$ the value $y_t$ has a state $S_t$, $S_{t+1} = S_t'$, and $S_t$ is not the repdigit state. If $S_t = \tau$ for some $t$, then $S_u = \tau$ for all $u \geq t$, and $y_u = F$ for all $u > t$, because a string with state $\tau$ maps to $F$ and $F$ is fixed (Lemmas 3.9 and 3.15). So it suffices to bound the first $t$ with $S_t = \tau$; the number of steps to $F$ is at most that $t$ plus one.

*$n$ odd.* Let $\ell \geq 0$ be the number of bad states at the start of the sequence, so that $S_1, \dots, S_\ell$ are bad and $S_{\ell+1}$ is not; $\ell$ is finite by Lemmas 3.13 and 3.14. If $S_{\ell+1}$ has $\rho_1 = 0$, put $u = \ell + 1$. Otherwise $S_{\ell+1}$ has $\rho_1 \geq 1$ and is not bad, so $S_{\ell+2}$ has $\rho_1 = 0$ by Lemma 3.12; put $u = \ell + 2$. By Lemma 3.10, $S_{u+2} = \tau$ (using that $\tau$ is fixed). So $y_t = F$ for every $t \geq u + 3$, and $u + 3 \leq \ell + 5$. For $n = 3$, Lemma 3.13 gives $\ell \leq (b+7)/2$, so the number of steps is at most $(b+7)/2 + 5 = (b+17)/2 \leq b/2 + 10$. For $n \geq 5$, Lemma 3.14 gives $\ell < b/3 + 4$, so the number of steps is less than $b/3 + 9$.

*$n$ even.* By Lemma 3.16, $S_2$ has all $w_j$ in $\{0, 1\}$, with at most one equal to $1$. If $n \geq 6$, Lemma 3.18 gives $\rho_1 = \rho_2 = 0$ for $S_3$, Lemma 3.17 gives $S_5 = \tau$, and $y_6 = F$: at most $6$ steps. If $n = 4$, Lemma 3.18 gives $\rho_1 = \rho_2 = 0$ for $S_3$ or for $S_4$; Lemma 3.17 then gives $S_6 = \tau$ (using that $\tau$ is fixed), and $y_7 = F$: at most $7$ steps.

In both cases $F$ is reached, within the stated number of steps. $\blacksquare$

*Remark.* (Computed.) The bounds that grow with $b$ are far from sharp. The proof gives at most $(b+17)/2$ steps for $n = 3$, at most $6$ steps for even $n \geq 6$, and at most $7$ for $n = 4$. By complete enumeration of digit multisets, the largest number of steps to $F$ under $R_3$ is $8$ over all bases $3$ to $20$ (it is $6$ in base $10$, where the proof allows $13$). From every state of the reduced map of $R_3$ in each base $3$ to $201$, at most $12$ steps reach $\tau$ (attained first at $b = 199$), so in these bases every string reaches $F$ within $14$ steps, against $(b+17)/2 = 109$ at $b = 201$. The observed maxima for even $n$ are also below the proof's: $5$ steps for $n = 4$ and $4$ for $n = 6$, over the bases $3$, $4$, $5$, $7$, $10$.
