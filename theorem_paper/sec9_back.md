## Methods and provenance

All enumerations run over digit multisets, since a rule reads its input only through the sorted digits; there are $\binom{L+b-1}{L}$ multisets of length $L$ in base $b$. The checks of Section 6 that concern Theorems 3.3, 4.16, 5.9, and 5.13 were written from the statements as printed in this paper, separately from the programs used when the proofs were first found. The examples of Section 7 were re-run for this paper, except the six-digit range $3$ to $80$ and the statement about sampling in bases $97$, $200$, and $640$, which are quoted. The census counts of Section 6 (the half-swap family in base $10$, the counts across bases, the test of $400$ class-C rules, and the sampled targets) are quoted from the project's November 2026 computations and were not re-run for this paper, apart from the rows for $4$, $6$, and $8$ digits of the base-$10$ table, which were reproduced by direct enumeration. Source code and outputs are linked from the project page, <https://arbolinea.com/60714/>.

The literature search behind the statement of novelty in the introduction was made in November 2026 with general web search engines (including searches of arXiv and Zenodo), the OEIS, and papers fetched from the online archives of the *Fibonacci Quarterly* and the *Journal of Integer Sequences*. It did not include zbMATH, MathSciNet, or a citation search of the papers of Young and of Peterson and Pulapaka, which is where an extension of Young's rule to $2n$ digits would most likely be found. The sequence $9(10^n - 1)$ is OEIS A086580; its entry has no comment on Kaprekar-type maps.

## Acknowledgments {.unnumbered}

The searches, enumerations, proofs, and checks were developed in collaboration with AI models (Anthropic's Claude and OpenAI's ChatGPT), used as research instruments. Several intermediate claims were withdrawn when verification contradicted them; one of them, that the length-$8$ extension of $\mathtt{EABDFC} - \mathtt{DFCEAB}$ is universal in every base, is the subject of Section 7. The questions, the direction, and the responsibility for the results are the author's.

## References {.unnumbered}

- E. Chen, K. Ono, R. E. Schwartz, and D. S. Thakur, Four-digit Kaprekar dynamics in odd bases, *J. Integer Seq.* 29 (2026), Article 26.4.7.
- K. E. Eldridge and S. Sagong, The determination of Kaprekar convergence and loop convergence of all three-digit numbers, *Amer. Math. Monthly* 95 (1988), 105-112.
- J. Fukuta and R. J. Chapman, An absorbing 4-digit number, *Amer. Math. Monthly* 100 (1993), 955-956.
- H. Hanslik, E. Hetmaniok, I. Sobstyl, M. Pleszczy`\'n`{=latex}ski, and R. Witu`\l{}`{=latex}a, Orbits of the Kaprekar's transformations: some introductory facts, *Zeszyty Nauk. Politech. `\'S`{=latex}l`\k{a}`{=latex}skiej Mat. Stosow.* 5 (2015), 5-34.
- H. Hasse and G. D. Prichett, The determination of all four-digit Kaprekar constants, *J. Reine Angew. Math.* 299/300 (1978), 113-124.
- D. R. Kaprekar, Another solitaire game, *Scripta Math.* 15 (1949), 244-245.
- D. R. Kaprekar, An interesting property of the number 6174, *Scripta Math.* 21 (1955), 304.
- A. Kay and K. Downes-Ward, Fixed points and cycles of the Kaprekar transformation: 1. Odd bases, *J. Integer Seq.* 25 (2022), Article 22.6.7.
- A. Kay and K. Downes-Ward, Fixed points and cycles of the Kaprekar transformation: 2. Even bases, arXiv:2408.12257 (2024).
- F. Nuez, Parametric transformation functions in the Kaprekar routine (I), arXiv:2110.15123 (2021).
- N. Perry, Complete classification of decimal repdigit-shifted Kaprekar maps, preprint, Zenodo (2026), doi:10.5281/zenodo.24251808.
- K. Peterson and H. Pulapaka, The Kaprekar routine and other digit games for undergraduate exploration, *J. Math. Sci.: Collaborative Explorations* 10 (2008), 143-156.
- V. Polukhin, Linear structure of the image of the Kaprekar routine, symmetric sums, and a census of attractors, preprint, Zenodo (2026), doi:10.5281/zenodo.24444706.
- G. D. Prichett, A. L. Ludington, and J. F. Lapenta, The determination of all decadic Kaprekar constants, *Fibonacci Quart.* 19 (1981), 45-52.
- F. Smarandache, Generalization and alternatives of Kaprekar's routine, arXiv:1005.3235 (2010).
- A. L. Young, The switch, subtract, reorder routine, *Fibonacci Quart.* 33 (1995), 432-440.
