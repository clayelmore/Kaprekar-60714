## Rules and notation

Fix a base $b \geq 2$ and a length $L \geq 2$. A *string* is a sequence of $L$ digits in base $b$, leading zeros allowed; it is identified with the integer it represents, which lies in $[0, b^L)$. Places are numbered from the least significant, place $0$, to the most significant, place $L-1$. For a string $x$ write $s_0 \geq s_1 \geq \dots \geq s_{L-1}$ for its digits sorted in descending order. We call $s_i$ *letter* $i$ and, when displaying rules, write the letters as $\mathtt{A} = s_0$, $\mathtt{B} = s_1$, and so on. A *repdigit* is a string with $s_0 = s_{L-1}$.

**Definition 2.1.** *A* rule *of length $L$ is an ordered pair $(\alpha, \beta)$ of distinct bijections from the letters $\{0, \dots, L-1\}$ to the places $\{0, \dots, L-1\}$. It acts on strings by*
$$K(x) \;=\; \Bigl|\, \sum_{i=0}^{L-1} b^{\alpha(i)} s_i \;-\; \sum_{i=0}^{L-1} b^{\beta(i)} s_i \,\Bigr| \;=\; \Bigl|\, \sum_{i=0}^{L-1} c_i\, s_i \,\Bigr|, \qquad c_i = b^{\alpha(i)} - b^{\beta(i)}.$$
*The two sums are* word 1 *and* word 2*. A rule is displayed by writing each word as a string of letters, most significant place first.*

The classical routine of Kaprekar is $\mathtt{ABCD} - \mathtt{DCBA}$ at $L = 4$ and $b = 10$: sort the digits, subtract the reversal. Each word is an integer in $[0, b^L)$, so $K(x)$ is again a string of length $L$. Since $K(x)$ depends on $x$ only through its sorted digits, the orbit of $x$ is determined by its digit multiset, and all enumerations below run over multisets. The definition of a rule does not mention $b$: the same pair of words can be read in every base, and the question of this paper is what happens when it is.

Because $\sum_i c_i = 0$, every repdigit maps to $0$, and $0$ is a repdigit. The interesting inputs are the others.

**Definition 2.2.** *A rule is* universal *in base $b$ if there is a string $F \neq 0$ with $K(F) = F$ such that every string that is not a repdigit reaches $F$ under iteration of $K$. Here "reaches" allows zero steps: $F$ reaches itself. The value $F$ is the* endpoint*, or* constant*, of the rule.*

Kaprekar's theorem is that $\mathtt{ABCD} - \mathtt{DCBA}$ is universal in base $10$ with endpoint $6174$.

It is often convenient to pass from digits to gaps. Put $g_j = s_j - s_{j+1} \geq 0$ for $0 \leq j \leq L-2$, and $C_j = c_0 + c_1 + \dots + c_j$. Summation by parts, with $\sum_i c_i = 0$, gives
$$K(x) \;=\; \Bigl|\, \sum_{j=0}^{L-2} C_j\, g_j \,\Bigr|.$$
We call $C_j$ the *weight* of gap $j$.

**Lemma 2.3.** *(Proven.) Let a rule of length $L$ be given, in base $b$.*

*(a) $K(x)$ is a multiple of $b - 1$ for every string $x$.*

*(b) If $K(F) = F$, then $F$ is the absolute difference of two arrangements of its own digits, namely its two words.*

*(c) If some gap weight $C_j$ is $0$, the rule is not universal.*

*Proof.* (a) Each $c_i$ is a difference of two powers of $b$, and $b^k \equiv 1 \pmod{b-1}$. (b) Both words of $F$ are arrangements of the digits of $F$, and $K(F)$ is the absolute value of their difference. (c) Let $x$ be the string whose sorted digits are $j+1$ ones followed by $L-1-j$ zeros. Since $0 \leq j \leq L-2$, it is not a repdigit. Its only nonzero gap is $g_j = 1$, so $K(x) = |C_j| = 0$, and $0$ is fixed. So $x$ never reaches a nonzero endpoint. $\blacksquare$

Part (c) is the only general obstruction used below. Parts (a) and (b) limit which numbers can be endpoints at all: in base $10$ an endpoint is a multiple of $9$ that equals one arrangement of its digits minus another.
