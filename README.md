# Proof of Mathar's conjecture on OEIS A027182: a closed form and the six-term recurrence

**Authors:** Haobo Ma, Wenlin Zhang

We prove the recurrence for A027182 stated as a conjecture by R. J. Mathar (OEIS A027182, FORMULA section, 6 May 2026) for all n >= 6, by evaluating the middle coefficient of the square of each A027170 row polynomial. Row symmetry reduces the convolution to five binomial sums, and a shifted second-order recurrence gives the six-term recurrence. The same central-binomial identity proves Mathar's conjectured recurrences for A027171, A027174 and A027175; a parity decomposition also proves his seven-term recurrence for the half-row sums A027179.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23884890](https://doi.org/10.5281/zenodo.23884890)
- Concept DOI: [https://doi.org/10.5281/zenodo.23884889](https://doi.org/10.5281/zenodo.23884889)
- License: CC-BY-4.0
- Version: 4
- Mathesis record: [mathar-a027182-closed-form](https://mathesis-omega-research.apps.chrono-ai.fun/papers/mathar-a027182-closed-form?version=4)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Proof of Mathar's conjecture on OEIS A027182: a closed form and the six-term recurrence. Mathesis, version 4. https://doi.org/10.5281/zenodo.23884890

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/494f471b70d9470db92b4dbc07a309d78ca59ec7/D5/S1/Recurrence/MatharA027182SelfConvolution.lean) | No public receipt |
| Corollary (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/494f471b70d9470db92b4dbc07a309d78ca59ec7/D5/S1/Recurrence/MatharA027182SelfConvolution.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/494f471b70d9470db92b4dbc07a309d78ca59ec7/D5/S1/Recurrence/MatharA027182SelfConvolution.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/494f471b70d9470db92b4dbc07a309d78ca59ec7/D5/S1/Recurrence/MatharA027182SelfConvolution.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23884889/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23884889/mathar-a027182-closed-form/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23884889/mathar-a027182-closed-form/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23884889/mathar-a027182-closed-form/slides/) ([sources](books/mathar-a027182-closed-form/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23884889/mathar-a027182-closed-form/films/) ([sources](books/mathar-a027182-closed-form/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23884889/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `main-formula` | special case | `D5/S1/Recurrence/MatharA027182SelfConvolution.result` |
| `middle-entries` | none | — |
| `near-middle` | none | — |
| `half-row` | none | — |
| `mathar-recurrence` | same | `D5/S1/Recurrence/MatharA027182SelfConvolution.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/mathar-a027182-closed-form/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
