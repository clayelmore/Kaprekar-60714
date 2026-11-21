# Literature check: is the all-lengths, all-bases rule new? (2026-11-21)

Method: two search engines, six queries, five sources read through targeted extraction. One further read
(Nuez 2021, arXiv 2110.15123) was blocked by a credit limit; its claim below rests on one engine's excerpt plus
my own arithmetic. This is a short search, not a systematic review. "Not found" is not "does not exist".

## What is already published

| Source | What it does | Overlap with this audit |
|---|---|---|
| Smarandache 2010, arXiv 1005.3235 | Defines f(a) = \|P1(a) - P2(a)\| for two arbitrary permutations of the digits. Examples and open questions only; no theorems. | The general framework (word 1 - word 2) is not new. |
| Peterson and Pulapaka 2008, "The Kaprekar Routine and Other Digit Games" (doi 10.25891/8ajq-ax45) | All 15 rearrangement types for 3 digits in an arbitrary base. Types (132,312) and (213,231) have a constant in every EVEN base and a 2-cycle in every odd base, like the classical routine. | Arbitrary-base proofs for modified rules exist at length 3. None of their rules works in odd bases. |
| Nuez 2021, arXiv 2110.15123 (and Symmetry 14(1):37) | A variant: sort descending, exchange only the two extreme digits, subtract. The result depends only on (largest - smallest), and 4 9...9 5 is fixed for every length > 2 in base 10. | A modified rule with a constant at every length already exists. It ignores every digit except the two extremes. |
| Thakur 2019, "Kaprekar phenomena" | Classical routine, any base B and length D. Constants for D = 5, 7, 9 only in special bases; for a fixed base only finitely many lengths can have a constant. | Confirms the classical routine cannot give an all-lengths law. No modified rules. |
| Kay and Downes-Ward 2024, arXiv 2408.12257 | Classifies fixed points and cycles of the classical routine in even bases. | Classical only. |
| Prichett, Ludington, Lapenta 1981 | 495 and 6174 are the only base-10 constants of the classical routine. | Classical only. |
| Savic 2026 (Zenodo 20101402, preprint) | Adds a constant k_n at each step so every length has a fixed point; checked to 7 digits. | A different modification (not a rearrangement). |

## What I did not find

* The half-swap rule, the fixed-middle rule, or the endpoint (b-1)(b^h - 1); searches for 8991 and 89991 in this
  context returned nothing relevant.
* Any rearrangement rule proved to have one constant in every base >= 3, odd bases included, at any length >= 4.
* 146070 or 60714 as constants of a rearrangement rule.
* A census of all rearrangement rules by length, or the finding that a fraction of a percent of them have constants.

## Assessment

* Not new: the idea of subtracting two arbitrary rearrangements; that a modified rule can have a constant at
  every length (Nuez's extreme-swap rule does, in base 10, by ignoring all but two digits).
* Apparently new, on this search: a rule family with one constant at every length >= 6 in every base >= 3 with an
  explicit formula; the pairing argument for odd lengths; 146070 for all lengths >= 6; the census counts.
* The Nuez example sharpens the "is it cheating" question: constants are easy to force when digits cancel. The
  extreme-swap rule uses 2 letters out of L; the half-swap rule uses all L (even) or L-1 (odd), but its endpoint
  (b-2)(b-1)...(b-1)1 is made almost entirely of the top digit, so it sits at the low-complexity end.

## Smarandache 2010, read in full (added later the same day)

Five pages, no theorems. Two points that change the comparison above:
* His permutations act on the digits AS WRITTEN, not on the sorted digits: with P1 = (2,3,1), P2 = (1,3,2),
  125 -> |251 - 152| = 099 -> |990 - 099| = 891 -> |918 - 819| = 099, a 2-cycle. The rules in this audit sort
  first. So his operator is a neighbor of ours, not the same one. The sorted version for three digits is
  Peterson and Pulapaka 2008.
* His open question 3 is "In what conditions one reaches a constant, not a cycle?" and question 1 asks for the
  longest number of iterations. He gives no answer to either. Our theorems are answers to the sorted-digit
  version of question 3 (a family that always reaches a constant) and question 1 (step bounds).
