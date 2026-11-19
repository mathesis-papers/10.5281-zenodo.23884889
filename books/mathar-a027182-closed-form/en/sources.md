# Evidence, sources and contributions

This explanation follows version 4 of *Proof of Mathar's conjecture on OEIS A027182: a closed form and the six-term recurrence*, by Haobo Ma and Wenlin Zhang. The exact version DOI is [10.5281/zenodo.23884890](https://doi.org/10.5281/zenodo.23884890); [10.5281/zenodo.23884889](https://doi.org/10.5281/zenodo.23884889) is the concept DOI for the work. The paper and this explanation use CC BY 4.0. Haobo Ma is affiliated with ChronoAI Pte Ltd, Singapore; Wenlin Zhang with the National University of Singapore and ChronoAI Pte Ltd, Singapore.

## Scope of the argument and formal evidence

The public theorem in the [Lean source file](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S1/Recurrence/MatharA027182SelfConvolution.lean) proves the A027182 recurrence for every $n\ge6$, using the same triangle and convolution definitions as the manuscript. The source is identical at the paper’s recorded revision and the book’s pin. Our [separate recurrence statement](proof.md#mathar-recurrence) cites it exactly. A private helper proof of the closed form does not make the whole paper one public theorem; the full closed form and three companion corollaries are presented with their manuscript proofs.

The paper also reports finite arithmetic comparisons through $n=400$. These can help detect errors; conclusions for every index rest on the written arguments or an exactly matching Lean theorem. We have not rerun the programs supplied with the manuscript.

| Remaining public scope | Shared contribution link |
|---|---|
| All-index closed form in the main theorem; retain the existing recurrence proof | [A027182 closed form](https://github.com/the-omega-institute/trureturing-requests/issues/253) |
| Middle-entry recurrences for A027171 and A027175 | [Two middle entries](https://github.com/the-omega-institute/trureturing-requests/issues/254) |
| Near-middle recurrence for A027174 | [Near-middle entry](https://github.com/the-omega-institute/trureturing-requests/issues/255) |
| Half-row recurrence for A027179 | [Half-row sum](https://github.com/the-omega-institute/trureturing-requests/issues/256) |

These results have proofs in the manuscript and await the public formalization scope specified above. Contributors coordinate a precise scope on the corresponding request, work on a focused branch in their own fork, and submit directly to trureturing `dev` under the [upstream contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). After acceptance, the public statement must still be compared with the source definitions, quantifiers and boundaries before updating this book’s citations. GitHub activity does not constitute a platform verification receipt or award points.

## Who posed the problems and supplied the formulas?

Clark Kimberling introduced the [A027170](https://oeis.org/A027170) triangle and [A027182](https://oeis.org/A027182). R. J. Mathar recorded the five recurrence conjectures addressed here on 6 May 2026. Christian Krause recorded the [A027171](https://oeis.org/A027171) closed form on 10 May 2026 and the [A027174](https://oeis.org/A027174) and [A027175](https://oeis.org/A027175) formulas on 11 May. The paper uses these formulas to prove their recurrences while retaining their original attribution. The parity decomposition for [A027179](https://oeis.org/A027179) is credited to Mathar. Ralf Stephan recorded the [A027178](https://oeis.org/A027178) row-sum formula in 2004; the OEIS credits Krause with a proof in 2026. These dates and attributions follow the OEIS records cited in version 4.

For general algorithms deriving recurrences for binomial sums, see A. Bostan, P. Lairez and B. Salvy, *Multiple binomial sums*, Journal of Symbolic Computation **80** (2017), 351–386, [doi:10.1016/j.jsc.2016.04.002](https://doi.org/10.1016/j.jsc.2016.04.002). The mechanism here is a direct evaluation using row symmetry, followed by a shifted operator calculation.
