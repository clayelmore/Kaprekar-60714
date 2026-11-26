## A finite certificate and a lifting theorem

This section treats a whole family of rules at once: every rule that swaps the two halves of a word, with any pairing of the letters. For every such rule in any base, an image is $(b^n - 1)m$ and is determined by a short list of deficits. In an even base this turns universality into a check on a table of $\binom{n+H}{n}$ states, and a subclass of these rules (class C) lifts from length $2n$ to every longer even length, with explicit endpoints. The section is self-contained. Section 3 treats one rule, $R_n$, in every base $b \ge 3$, odd bases included; this section treats every half-swap rule, in even bases, one base at a time.

### The setting: half-swap rules

Fix a base $b \ge 2$ and $n \ge 1$. We work with strings of $2n$ digits, leading zeros allowed. Places are counted from the least significant digit, which is place $0$. The digits of a string, sorted descending, are the letters
$$s_0 \ge s_1 \ge \dots \ge s_{2n-1}.$$
The rules below read a string only through its letters, so we identify a string with its sorted digits when we apply a rule.

**Definition 5.1.** A *half-swap rule* on $2n$ digits is a partition of the index set $\{0, 1, \dots, 2n-1\}$ into $n$ ordered pairs $(P_q, M_q)$, $q = 0, \dots, n-1$. *Word 1* is the $2n$-digit string with letter $s_{P_q}$ at place $q+n$ and letter $s_{M_q}$ at place $q$, for every $q$; *word 2* is the string with $s_{M_q}$ at place $q+n$ and $s_{P_q}$ at place $q$. The rule is
$$K(s) = |\,\text{word 1} - \text{word 2}\,|,$$
written as a $2n$-digit string. Put
$$V(s) = \sum_{q=0}^{n-1} b^q \,(s_{P_q} - s_{M_q}), \qquad m = |V(s)|.$$
The rule is *universal with endpoint $F$* if $F \ne 0$, $K(F) = F$, and every $2n$-digit string that is not a repdigit reaches $F$ under iteration of $K$. Here "reaches" allows zero steps: $F$ reaches itself.

This repeats Definition 3.1, and "universal" is used as in Definition 2.2. Every letter lies in exactly one pair, so word 1 and word 2 are both rearrangements of $s$, and every letter moves exactly $n$ places. Reversing every pair at once exchanges word 1 and word 2, replaces $V$ by $-V$, and gives the same rule $K$. Reversing only some of the pairs changes $K$ in general. An *orientation* of a rule is the choice between its list of pairs and the global reversal of that list (all pairs reversed together), which gives the same $K$; it is not a separate choice for each pair. The orientation matters in Definitions 5.10 and 5.11: class C is a condition on an oriented rule, and lifting the reversed orientation gives a different rule, which need not be universal. In letter notation ($\mathtt{A} = s_0$, $\mathtt{B} = s_1$, and so on) a rule is written as word 1 minus word 2, most significant place first. For example, $\mathtt{DHFBIJGECA} - \mathtt{JGECADHFBI}$ is the rule on $10$ digits with pairs $(8,0), (1,2), (5,4), (7,6), (3,9)$ at places $q = 0, 1, 2, 3, 4$.

Lemmas 5.2 and 5.3 are Lemma 3.4 for a general pairing.

**Lemma 5.2 (factorization).** *(Proven.)* For every half-swap rule and every string $s$, $K(s) = (b^n - 1)\,m$ with $m = |V(s)|$, and $0 \le m \le b^n - 1$.

*Proof.* Pair $q$ contributes $b^{q+n} s_{P_q} + b^q s_{M_q}$ to word 1 and $b^{q+n} s_{M_q} + b^q s_{P_q}$ to word 2. So
$$\text{word 1} - \text{word 2} = \sum_q (b^{q+n} - b^q)(s_{P_q} - s_{M_q}) = (b^n - 1)\,V(s).$$
Each difference $d_q = s_{P_q} - s_{M_q}$ lies in $[-(b-1), b-1]$, so $m \le (b-1)(1 + b + \dots + b^{n-1}) = b^n - 1$. Hence $K(s) \le (b^n-1)^2 < b^{2n}$, which is a $2n$-digit string. $\blacksquare$

**Lemma 5.3 (zero lemma).** *(Proven.)* $V(s) = 0$ if and only if $s_{P_q} = s_{M_q}$ for every $q$.

*Proof.* If every $d_q = s_{P_q} - s_{M_q}$ is $0$, then $V = 0$. Otherwise let $q$ be the lowest index with $d_q \ne 0$. Then $V \equiv b^q d_q \pmod{b^{q+1}}$, and $b^q d_q \not\equiv 0 \pmod{b^{q+1}}$ because $0 < |d_q| \le b-1$. So $V \ne 0$. $\blacksquare$

**Definition 5.4.** For $j = 0, \dots, 2n-2$, the rule *covers gap $j$* (the gap between letters $s_j$ and $s_{j+1}$) if some pair satisfies
$$\min(P_q, M_q) \le j < \max(P_q, M_q).$$
The rule *covers every gap* if it covers gap $j$ for every $j = 0, \dots, 2n-2$.

**Proposition 5.5 (gap cover).** *(Proven.)* In any base $b \ge 2$: $K(s) = 0$ holds only for repdigits $s$ if and only if the rule covers every gap.

*Proof.* Suppose the rule covers every gap and $K(s) = 0$. Then $V(s) = 0$, so by Lemma 5.3 every pair has equal letters. Take a gap $j$, covered by a pair with indices $u \le j < v$. Then $s_u = s_v$, and since $s_u \ge s_j \ge s_{j+1} \ge s_v$, we get $s_j = s_{j+1}$. This holds for every gap, so all letters are equal and $s$ is a repdigit.

Conversely, suppose gap $j$ is not covered. Let $s$ consist of $j+1$ digits $1$ followed by $2n-j-1$ digits $0$, so that $s_i = 1$ for $i \le j$ and $s_i = 0$ for $i > j$. It is not a repdigit, since $1 \le j+1 \le 2n-1$. Every pair lies on one side of the gap (both indices $\le j$ or both $> j$), so every pair has equal letters and $V(s) = 0$, that is, $K(s) = 0$. $\blacksquare$

Repdigits always map to $0$, by Lemma 5.3, and $K(0) = 0$.

The link with Section 2 is as follows. For a half-swap rule, $c_{P_q} = (b^n - 1)\, b^q$ and $c_{M_q} = -(b^n - 1)\, b^q$, so the gap weight is
$$C_j = (b^n - 1) \sum_{q \,:\, \text{pair } q \text{ covers gap } j} \pm\, b^q,$$
with sign $+$ when $P_q \le j < M_q$ and $-$ when $M_q \le j < P_q$; a pair that does not cover gap $j$ has both letters on the same side and contributes $0$. A signed sum of distinct powers of $b$ is $0$ only when it is empty (look at the lowest power, as in Lemma 5.3). So $C_j = 0$ exactly when gap $j$ is uncovered, and the "uncovered gap" half of Proposition 5.5 is Lemma 2.3(c).

The next lemma is Lemma 3.6 for a general pairing.

**Lemma 5.6 (shape of an image).** *(Proven.)* Let $s$ be a string with $m = |V(s)| \ge 1$, and put $N = m - 1$, written with $n$ digits $x_{n-1} \dots x_0$ (leading zeros allowed). Then
$$K(s) = N\, b^n + (b^n - 1 - N),$$
so the $2n$ digits of $K(s)$ are $x_{n-1}, \dots, x_0$ followed by their complements $b-1-x_{n-1}, \dots, b-1-x_0$. Define the *deficit* $r(x) = \min(x, b-1-x)$ and let $\rho_1 \le \dots \le \rho_n$ be the deficits $r(x_0), \dots, r(x_{n-1})$ in increasing order. Then $0 \le \rho_i \le H = \lfloor (b-1)/2 \rfloor$, and the letters of $K(s)$ are
$$s_{i-1} = b - 1 - \rho_i, \qquad s_{2n-i} = \rho_i \qquad (i = 1, \dots, n).$$

*Proof.* By Lemma 5.2, $1 \le m \le b^n - 1$, so $0 \le N \le b^n - 2$ and $N$ has $n$ digits. Then $K(s) = (b^n - 1)(N + 1) = N b^n + (b^n - 1 - N)$. Since $\sum_i (b-1-x_i)\, b^i = (b^n - 1) - N$ and each $b-1-x_i$ is a digit, the number $b^n - 1 - N$ has the $n$ digits $b-1-x_i$ at places $i = 0, \dots, n-1$, and $N b^n$ occupies places $n, \dots, 2n-1$. This gives the digits of $K(s)$.

The multiset of these $2n$ digits is the union over $i$ of $\{x_i, b-1-x_i\} = \{r(x_i), b-1-r(x_i)\}$, that is, $\{\rho_1, \dots, \rho_n\}$ together with $\{b-1-\rho_1, \dots, b-1-\rho_n\}$. Each $\rho_i \le H \le (b-1)/2$, so every $b - 1 - \rho_j \ge (b-1)/2 \ge \rho_i$. Hence the $n$ largest letters are $b-1-\rho_1 \ge \dots \ge b-1-\rho_n$ and the $n$ smallest are $\rho_n \ge \dots \ge \rho_1$, which is the stated formula. $\blacksquare$

We call $\rho = (\rho_1 \le \dots \le \rho_n)$ the *state* of the image $K(s)$. A state is a multiset of $n$ values in $\{0, \dots, H\}$, so there are $\binom{n+H}{n}$ states. For a state $\rho$, the *string of $\rho$*, written $s^\rho$, is the string with letters $s^\rho_{i-1} = b-1-\rho_i$ and $s^\rho_{2n-i} = \rho_i$ for $i = 1, \dots, n$. Two facts follow from Lemma 5.6. First, an image with state $\rho$ has the same letters as $s^\rho$, so its own image is $K(s^\rho)$: the state determines the next image. Second, the state of an image can be read off its letters, as $\rho_i = s_{2n-i}$; so two images with the same letters have the same state.

### The small-table criterion (b even)

From here to the end of the section the base $b$ is even, so $H = (b-2)/2$.

**Lemma 5.7.** *(Proven.)* Let $b$ be even. For every state $\rho$, the string $s^\rho$ is not a repdigit.

*Proof.* $s^\rho_0 = b - 1 - \rho_1 \ge b - 1 - (b-2)/2 = b/2$, while $s^\rho_{2n-1} = \rho_1 \le (b-2)/2 < b/2$. $\blacksquare$

**Definition 5.8.** Let $b$ be even. For a half-swap rule and a state $\rho$ with $V(s^\rho) \ne 0$, let $T(\rho)$ be the state of the image $K(s^\rho)$. If the rule covers every gap, then $V(s^\rho) \ne 0$ for every state (Lemma 5.7 and Proposition 5.5), so $T$ is a map from the set of states to itself. A state $\tau$ is an *attracting fixed state* of $T$ if $T(\tau) = \tau$ and every state reaches $\tau$ under iteration of $T$.

An attracting fixed state is the only fixed state of $T$, and $T$ then has no cycle of length $2$ or more, since every orbit ends at $\tau$. In this section $\tau$ always denotes the attracting fixed state of the rule at hand; for $R_n$ it is $(0, \dots, 0, 1)$ (Definition 3.5), but for other rules it can be a different state (Example 5.16).

**Theorem 5.9 (small-table criterion).** *(Proven.)* Let $b$ be even. A half-swap rule on $2n$ digits is universal if and only if

(a) it covers every gap, and

(b) its map $T$ on the $\binom{n+H}{n}$ states has an attracting fixed state $\tau$.

Condition (b) makes sense once (a) holds, since $T$ is then defined on every state (Definition 5.8). The endpoint is then
$$F = (b^n - 1)\,|V(s^\tau)|.$$

*Proof.* First a remark used in both directions. Let $s$ be a string with $K(s) \ne 0$, and let $\rho$ be the state of $K(s)$. Then for every $k \ge 0$, the image $K^{k+1}(s)$ is nonzero and has state $T^k(\rho)$, provided $T$ is defined along the way. For $k = 0$ this is the definition of $\rho$. If $K^{k+1}(s)$ has state $T^k(\rho)$, its letters are those of $s^{T^k(\rho)}$, so $K^{k+2}(s) = K(s^{T^k(\rho)})$, whose state is $T^{k+1}(\rho)$ by Definition 5.8.

Suppose (a) and (b). Let $G = K(s^\tau)$. By (a), Lemma 5.7 and Proposition 5.5, $G \ne 0$, and $G = (b^n-1)|V(s^\tau)|$ by Lemma 5.2. The state of $G$ is $T(\tau) = \tau$, so $G$ has the letters of $s^\tau$ and $K(G) = K(s^\tau) = G$. Now let $s$ be a string that is not a repdigit. By (a) and Proposition 5.5, $K(s) \ne 0$; let $\rho$ be its state. By (b) there is $k$ with $T^k(\rho) = \tau$, and by the remark $K^{k+1}(s)$ has state $\tau$, so $K^{k+2}(s) = K(s^\tau) = G$. Hence the rule is universal with endpoint $G$.

Conversely, suppose the rule is universal with endpoint $F$. If some gap were not covered, Proposition 5.5 would give a string $s$, not a repdigit, with $K(s) = 0$; since $K(0) = 0$, the orbit of $s$ stays at $0 \ne F$, a contradiction. So (a) holds, and $T$ is defined on every state. Since $F = K(F) \ne 0$, $F$ is an image; let $\tau$ be its state. The letters of $F$ are those of $s^\tau$, so $K(s^\tau) = K(F) = F$, and $T(\tau)$, the state of $K(s^\tau)$, is $\tau$. Also $F = K(s^\tau) = (b^n - 1)|V(s^\tau)|$. Now let $\rho$ be any state. By Lemma 5.7, $s^\rho$ is not a repdigit, so $K^k(s^\rho) = F$ for some $k \ge 0$. If $k = 0$, then $s^\rho$ and $F$ have the same letters, so $\rho = \tau$. If $k \ge 1$, then $K(s^\rho)$ has state $T(\rho)$, so by the remark $K^k(s^\rho)$ has state $T^k(\rho)$; it equals $F$, so $T^k(\rho) = \tau$. Thus every state reaches $\tau$, which is (b). $\blacksquare$

Theorem 5.9 replaces a complete enumeration of all digit multisets of length $2n$ by a table of $T$ on $\binom{n+H}{n}$ states, which a reader can check line by line. In base $10$ ($H = 4$) the table has $70$ states at $8$ digits, $126$ at $10$, $210$ at $12$, $330$ at $14$ and $495$ at $16$, against $24{,}310$, $92{,}378$ and $293{,}930$ digit multisets at $8$, $10$ and $12$ digits.

*Remark (base 2).* The results of this section hold in base $2$. There $H = 0$, so there is exactly one state, $(0, \dots, 0)$, whose string is $n$ ones followed by $n$ zeros. If the rule covers every gap, $T$ maps this state to itself, so condition (b) of Theorem 5.9 holds automatically and the criterion reduces to gap cover: in base $2$ a half-swap rule is universal if and only if it covers every gap. (Computed: this was also confirmed by complete enumeration of all half-swap rules for $n = 2, 3, 4, 5$; every rule that covers every gap is universal, and no other rule is.)

### The lifting theorem (b even)

**Definition 5.10 (class C).** Let $b$ be even. An oriented half-swap rule on $2n$ digits is *in class C* if

(S) $V(s^\rho) > 0$ for every state $\rho$;

(U) $T$ has an attracting fixed state $\tau$;

(C1) for every state $\rho$ with $\rho_1 \ge 1$, the state $T(\rho)$ contains a $0$.

A rule is in class C if one of its two orientations is. Its *seed data* are $\tau$, $m^* = V(s^\tau)$ and $N^* = m^* - 1$, written with $n$ digits. Here $m^*$ is a value of $V$, not of $|V|$; it is positive by (S), so $m^* = |V(s^\tau)|$.

By (S), $V(s^\rho) \ne 0$ on every state, so $T$ is defined on every state (Definition 5.8) even if the rule does not cover every gap. Class C does not ask for gap cover, and Theorem 5.13 does not need it: a class-C rule that fails gap cover is not universal itself (Theorem 5.9), but its lifts are. Condition (C1) says: if an image has no digit $0$ and no digit $b-1$ (all its deficits are at least $1$), then the next image has a $0$ and a $b-1$.

**Definition 5.11 (lifts).** Let $R$ be an oriented half-swap rule on $2n$ digits with pairs $(P_q, M_q)$. Its two *lifts* are oriented rules on $2n+2$ digits, with letters $s_0, \dots, s_{2n+1}$:

* *top lift*: for $q = 0, \dots, n-1$ the pair at place $q$ is $(P_q + 1, M_q + 1)$, and the pair at place $n$ is $(0, 2n+1)$;
* *bottom lift*: for $q = 0, \dots, n-1$ the pair at place $q+1$ is $(P_q + 1, M_q + 1)$, and the pair at place $0$ is $(2n+1, 0)$.

In both lifts the new largest letter $s_0$ and the new smallest letter $s_{2n+1}$ form the new pair, and the old rule acts on the $2n$ letters in between. In letter notation, the top lift puts the new largest letter first and the new smallest letter in the middle of word 1. The lifts depend on the orientation of $R$: the lifts of the reversed list of pairs are different rules, and they need not be universal. (Computed: for the seed of Example 5.16, neither lift of the reversed orientation is universal.)

In the next lemma and theorem, primes denote objects of the lifted rule: $T'$, $V'$, $N'$, $\tau'$, $m'^*$, $N'^*$. (Section 3 used a prime for the next state, $\rho'$; here the next state is written $T(\rho)$.) For a state $\rho$ of the old rule we write $m_\rho = V(s^\rho)$ and $N_\rho = m_\rho - 1$, with $n$ digits; $m_\rho$ is a value of $V$, positive under (S).

**Lemma 5.12 (one step of a lift).** *(Proven.)* Let $b$ be even, let $R$ be an oriented rule on $2n$ digits satisfying (S), and let $R'$ be one of its lifts. Let $\mu = (\mu_1 \le \dots \le \mu_{n+1})$ be a state on $2n+2$ digits. Put $x = \mu_1$, $\rho = (\mu_2, \dots, \mu_{n+1})$ and $A = b - 1 - 2x$. Then $1 \le A \le b-1$, $V'(s^\mu) > 0$, and:

* top lift: $V'(s^\mu) = b^n A + m_\rho$, and $N'$ is the digit $A$ followed by the $n$ digits of $N_\rho$;
* bottom lift: $V'(s^\mu) = b\, m_\rho - A$, and $N'$ is the $n$ digits of $N_\rho$ followed by the digit $b-1-A$.

In both cases
$$T'(\mu) = \{\varphi(\mu_1)\} \uplus T(\mu_2, \dots, \mu_{n+1}), \qquad \varphi(x) = r(b - 1 - 2x), \tag{$*$}$$
where $\uplus$ is union of multisets. Moreover $\varphi(0) = 0$.

*Proof.* By the definition of $s^\mu$, its letters are $s^\mu_{i-1} = b - 1 - \mu_i$ and $s^\mu_{2n+2-i} = \mu_i$ for $i = 1, \dots, n+1$. So $s^\mu_0 = b-1-x$ and $s^\mu_{2n+1} = x$. The inner letters $t_j = s^\mu_{j+1}$, $j = 0, \dots, 2n-1$, satisfy
$$t_{i-1} = s^\mu_i = b - 1 - \mu_{i+1} = b-1-\rho_i, \qquad t_{2n-i} = s^\mu_{2n+1-i} = \mu_{i+1} = \rho_i,$$
for $i = 1, \dots, n$. So the inner letters are exactly the letters of $s^\rho$ on $2n$ digits. The old pairs, shifted by one letter, read these inner letters, so their contribution is computed from $s^\rho$. Also $A = s^\mu_0 - s^\mu_{2n+1}$. Since $0 \le x \le H = (b-2)/2$, we have $1 \le A \le b-1$ (and $A$ is odd). By (S) and Lemma 5.2, $1 \le m_\rho \le b^n - 1$, so $0 \le N_\rho \le b^n - 2$ has $n$ digits, and by Lemma 5.6 the sorted deficits of the digits of $N_\rho$ form the state of $K(s^\rho)$, which is $T(\rho)$.

Top lift. The old pairs stay at places $0, \dots, n-1$ and contribute $m_\rho$; the new pair at place $n$ contributes $b^n (s^\mu_0 - s^\mu_{2n+1}) = b^n A$. So $V'(s^\mu) = b^n A + m_\rho > 0$, hence $m' = b^n A + m_\rho$ and
$$N' = m' - 1 = b^n A + N_\rho.$$
Since $0 \le N_\rho < b^n$ and $A$ is a digit, $N'$ is the digit $A$ followed by the $n$ digits of $N_\rho$.

Bottom lift. The old pairs move to places $1, \dots, n$ and contribute $b\, m_\rho$; the new pair $(2n+1, 0)$ at place $0$ contributes $s^\mu_{2n+1} - s^\mu_0 = -A$. So $V'(s^\mu) = b\, m_\rho - A \ge b - (b-1) > 0$, hence $m' = b\, m_\rho - A$ and
$$N' = m' - 1 = b\,(m_\rho - 1) + (b - 1 - A),$$
with $0 \le b-1-A \le b-2$. So $N'$ is the $n$ digits of $N_\rho$ followed by the digit $b-1-A$. (Also $N' \le b(b^n - 2) + b - 2 < b^{n+1}$, so $N'$ has $n+1$ digits.)

In both cases the digits of $N'$ are the digits of $N_\rho$ and one more digit, $A$ or $b-1-A$, and $r(A) = r(b-1-A)$. So the sorted deficits of $N'$, which form $T'(\mu)$ by Lemma 5.6, are $T(\rho)$ together with $r(A) = \varphi(x)$. Finally $\varphi(0) = r(b-1) = \min(b-1, 0) = 0$. $\blacksquare$

**Theorem 5.13 (lifting theorem).** *(Proven.)* Let $b$ be even and let $R$ be a rule on $2n$ digits in class C, oriented so that (S), (U), (C1) hold, with seed data $\tau$, $m^*$, $N^*$. Then each lift $R'$ of $R$ (Definition 5.11) covers every gap, is in class C on $2n+2$ digits with the orientation of Definition 5.11, and is universal. Its attracting fixed state is $\tau' = \{0\} \uplus \tau$, and its seed data are:

* top lift: $m'^* = (b-1)\, b^n + m^*$, that is, $N'^*$ is the digit $b-1$ followed by $N^*$;
* bottom lift: $m'^* = b\, m^* - (b-1)$, that is, $N'^* = b N^*$ is $N^*$ followed by the digit $0$.

The endpoint of $R'$ is $(b^{n+1} - 1)\, m'^*$.

*Proof.* We check the three conditions of Definition 5.10 for $R'$, then gap cover.

(S). By Lemma 5.12, $V'(s^\mu) > 0$ for every state $\mu$.

(C1). Let $\mu$ be a state with $\mu_1 \ge 1$. Then $\rho = (\mu_2, \dots, \mu_{n+1})$ has $\rho_1 = \mu_2 \ge \mu_1 \ge 1$, so $T(\rho)$ contains a $0$ by (C1) for $R$, and so does $T'(\mu)$ by $(*)$.

(U). Put $\tau' = \{0\} \uplus \tau$. Its smallest element is $0$, and removing it leaves $\tau$; so by $(*)$ and $\varphi(0) = 0$, $T'(\tau') = \{0\} \uplus T(\tau) = \tau'$. Now take any state $\mu$. If $\mu_1 \ge 1$, then $T'(\mu)$ contains a $0$, as just shown; so after at most one step the smallest deficit is $0$. Suppose $\mu_1 = 0$, and write $\mu = \{0\} \uplus \rho$. We show by induction on $k \ge 0$ that $T'^k(\mu) = \{0\} \uplus T^k(\rho)$. For $k = 0$ this is the definition. If $T'^k(\mu) = \{0\} \uplus T^k(\rho)$, its smallest element is $0$ and removing one copy of $0$ leaves $T^k(\rho)$, so $(*)$ gives $T'^{k+1}(\mu) = \{\varphi(0)\} \uplus T^{k+1}(\rho) = \{0\} \uplus T^{k+1}(\rho)$. By (U) for $R$ there is $k$ with $T^k(\rho) = \tau$, and then $T'^k(\mu) = \tau'$. So every state reaches $\tau'$.

Gap cover. The new pair has indices $0$ and $2n+1$, so it covers every gap $j = 0, \dots, 2n$.

By Theorem 5.9, $R'$ is universal with endpoint $(b^{n+1}-1)\,|V'(s^{\tau'})| = (b^{n+1}-1)\, m'^*$. At the state $\tau'$ we have $x = 0$, $A = b-1$ and $\rho = \tau$, so $m_\rho = m^*$. Lemma 5.12 gives, for the top lift, $m'^* = (b-1)\,b^n + m^*$ and $N'^* = (b-1)\,b^n + N^*$, the digit $b-1$ followed by $N^*$; for the bottom lift, $m'^* = b\, m^* - (b-1)$ and $N'^* = b\,m^* - b = b N^*$, which is $N^*$ followed by $0$. $\blacksquare$

**Corollary 5.14.** *(Proven.)* Let $b$ be even and let $R$ be a rule on $2n$ digits in class C, oriented so that (S), (U), (C1) hold, with seed data $N^*$. Applying $i$ top lifts and $j$ bottom lifts, in any order, with $i + j \ge 1$, gives a rule on $2(n+i+j)$ digits that is in class C and universal. Its endpoint $F$ is $N$ followed by its digit complement, where
$$N = (b-1)^i \; N^* \; 0^j,$$
that is, $i$ digits $b-1$, then the $n$ digits of $N^*$, then $j$ zeros. In particular, a rule in class C that covers every gap is universal itself (Theorem 5.9), and it yields a universal rule at every longer even length.

*Proof.* By Theorem 5.13 each lift is again in class C, so the lifts can be iterated, and each lifted rule is universal. By the same theorem, a top lift prepends the digit $b-1$ to $N^*$ and a bottom lift appends the digit $0$; these two operations on digit strings commute, so after $i$ top and $j$ bottom lifts in any order the seed data are $N = (b-1)^i N^* 0^j$, with $m = N + 1$. The endpoint is $(b^{n+i+j} - 1)\, m$, and by Lemma 5.6 its digits are those of $N$ followed by their complements. The last sentence follows from (U) and Theorem 5.9. $\blacksquare$

**Proposition 5.15 (step count).** *(Proven.)* Let $b$ be even and let $R$ be a rule on $2n$ digits in class C, oriented so that (S), (U), (C1) hold, and suppose every state of $R$ reaches $\tau$ in at most $D$ steps of $T$. Apply $i$ top lifts and $j$ bottom lifts in any order, where either $i + j \ge 1$, or $i + j = 0$ and $R$ covers every gap. Then every string that is not a repdigit reaches the endpoint $F$ of the resulting rule in at most $D + i + j + 2$ applications of $K$.

The condition on $i + j$ is needed: a class-C rule that misses a gap sends some non-repdigit to $0$ (Proposition 5.5), so it has no endpoint at all.

*Proof.* The resulting rule covers every gap: by Theorem 5.13 if $i + j \ge 1$, by hypothesis if $i + j = 0$. So every non-repdigit has a nonzero image (Proposition 5.5), and the rule is universal by Corollary 5.14 if $i + j \ge 1$ and by Theorem 5.9 if $i + j = 0$. For one lift, the proof of (U) in Theorem 5.13 shows that a state $\mu$ with $\mu_1 = 0$ reaches $\tau'$ in at most $D$ steps of $T'$ (since $T'^k(\mu) = \{0\} \uplus T^k(\rho)$), and a state with $\mu_1 \ge 1$ reaches a state with smallest element $0$ in one step. So every state of the lift reaches $\tau'$ in at most $D + 1$ steps. By induction, after $i + j$ lifts every state reaches the attracting fixed state in at most $D + i + j$ steps. For a non-repdigit string $s$, $K(s)$ has some state $\rho$ (one application); by the remark in the proof of Theorem 5.9, after at most $D + i + j$ further applications the image has the attracting fixed state as its state. Such an image has the letters of $F$ but need not equal $F$, so one more application may be needed. In total at most $D + i + j + 2$ applications. $\blacksquare$

**Example 5.16 (base 10).** *(The seed table is Computed; the lifted rules and endpoints then follow by Theorem 5.13 and Corollary 5.14, Proven.)* The rule $\mathtt{DHFBIJGECA} - \mathtt{JGECADHFBI}$ on $10$ digits has pairs $(P_q, M_q) = (8,0), (1,2), (5,4), (7,6), (3,9)$ at places $q = 0, \dots, 4$, so
$$\begin{aligned}
V &= (s_8 - s_0) + 10\,(s_1 - s_2) + 10^2 (s_5 - s_4) \\
  &\quad + 10^3 (s_7 - s_6) + 10^4 (s_3 - s_9).
\end{aligned}$$
It covers every gap: the pair $(8,0)$ covers gaps $0$ to $7$ and the pair $(3,9)$ covers gaps $3$ to $8$. Its table of $T$ on the $126$ states satisfies (S), (U) and (C1) with this orientation, with $\tau = (0,0,1,2,3)$, and every state reaches $\tau$ in at most $9$ steps. At $\tau$ the letters are $9,9,8,7,6,3,2,1,0,0$, so
$$m^* = -9 + 10 - 300 - 1000 + 70000 = 68701,$$
$N^* = 68700$ (whose deficits $3,1,2,0,0$ sort to $\tau$), and the endpoint is
$$F = 99999 \times 68701 = 6870031299.$$
By Theorem 5.13 the top lift $\mathtt{AEIGCJLKHFDB} - \mathtt{LKHFDBAEIGCJ}$ is universal on $12$ digits with endpoint $968700031299$, and the bottom lift $\mathtt{EIGCJLKHFDBA} - \mathtt{KHFDBAEIGCJL}$ is universal with endpoint $687000312999$. By Corollary 5.14, two top lifts give $99687000031299$ at $14$ digits, two bottom lifts give $68700003129999$, and one of each, in either order, gives $96870000312999$ (the two orders give different rules with the same endpoint). In general the endpoints are $9^i\, 68700\, 0^j$ followed by its complement, at $2(5+i+j)$ digits.

### Limits

* *Shape of the endpoints.* By Lemmas 5.2 and 5.6, every nonzero image of a half-swap rule, and so every endpoint, is a multiple of $b^n - 1$ of the form $N$ followed by its digit complement. Fixed points of any other shape are out of reach of this section. For example, Kaprekar's constant $6174$ at $4$ digits ($n = 2$) is not of this form: the block $61$ would have to be followed by its complement $38$, and $6138 \ne 6174$. So $6174$ is not the endpoint of any half-swap rule on $4$ digits in base $10$.
* *Seeds.* Seeds are found by search. There is no known recipe that produces a class-C rule for a given $N^*$. The lifts only add digits $b-1$ on the left of $N^*$ and digits $0$ on the right, so the endpoints reached from one seed form the family $(b-1)^i N^* 0^j$ and nothing else.
* *Odd bases.* Theorem 5.9, Definition 5.10, Lemma 5.12, Theorem 5.13 and their consequences are stated and proved for even $b$ only. Evenness enters in one place: $H = (b-2)/2 < b/2$, which gives Lemma 5.7 (the string of a state is never a repdigit) and the bound $1 \le A \le b-1$ in Lemma 5.12. For odd $b$ two things go wrong. First, put $\kappa = (b-1)/2$. The state with every $\rho_i = \kappa$ has as its string the repdigit $\kappa^{2n}$, which is its own mirror image, so Lemma 5.7 fails. On that state $V = 0$ for every rule (Lemma 5.3), so $T$ is not defined there, even for a rule that covers every gap. Second, the first image of a non-repdigit can be this repdigit: its value is $(b^n - 1)(b^n + 1)/2$, so this happens exactly when $m = (b^n + 1)/2$, and the repdigit then maps to $0$. It does happen for some rules: in base $3$ the rule $\mathtt{DABC} - \mathtt{BCDA}$ sends the string with digits $2, 2, 1, 0$ to $|25 - 65| = 40$, which is $1111$ in base $3$. (Lemma 3.8 excludes this for $R_n$.) As a result, the direction "universal implies (a) and (b)" of Theorem 5.9 fails as stated in odd bases, because $T$ is not defined on every state, while universal half-swap rules do exist in odd bases (Theorem 3.3). A criterion for odd bases would have to exclude $m = (b^n + 1)/2$ and restrict $T$ to the states other than $(\kappa, \dots, \kappa)$; we have not proved one. Also condition (S) of Definition 5.10 can never hold in an odd base, so class C as defined is empty there. Lemmas 5.2, 5.3, 5.6 and Proposition 5.5 hold in every base.
