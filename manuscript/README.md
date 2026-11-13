# Rebuilding the A027182 note

`note.tex` is the main source. It contains its bibliography and needs no external
figures or bibliography database. `metadata.json` records the title, abstract,
creators, stable note identifier, revision, covered problems and CC BY 4.0 license.

## Build

Use **Tectonic 0.17.0**:

```sh
tectonic --untrusted note.tex
```

An initial build needs access to Tectonic's standard TeX bundle. Alternatively,
use a normal LaTeX installation providing `geometry`, `amsmath`, `amssymb`,
`amsthm` and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded, so BibTeX is not required.

## Reproduce the checks

Python 3 with its standard library is sufficient:

```sh
python3 verify.py --bfile b027182.txt --prefixes sequence-prefixes.json --output check.json
```

The default bound is 400. The check constructs the defining triangle directly,
compares the convolution and all four companion closed forms, checks the five
recurrences on their stated domains through that bound, matches 126 terms
retrieved from the five OEIS entries on 1 November 2026, matches the 22 archived
A027182 b-file terms, and verifies twelve exact polynomial/operator identities.
`verification.json` is the expected output at the default bound. A finite
prefix comparison corroborates the complete all-index proofs in the note.

## Sources and proof scope

The five conjectures are in the FORMULA sections of
[A027182](https://oeis.org/A027182), [A027171](https://oeis.org/A027171),
[A027174](https://oeis.org/A027174), [A027175](https://oeis.org/A027175) and
[A027179](https://oeis.org/A027179), each attributed to R. J. Mathar on
6 May 2026. Krause's recorded closed forms and the Stephan--Krause row-sum
formula are credited in the note. All OEIS access dates are 1 November 2026.

The A027182 written proof corresponds to
[`MatharA027182SelfConvolution.lean`](https://github.com/the-omega-institute/trureturing/blob/494f471b70d9470db92b4dbc07a309d78ca59ec7/D5/S1/Recurrence/MatharA027182SelfConvolution.lean)
at commit `494f471b70d9470db92b4dbc07a309d78ca59ec7`. The declaration
`D5.S1.Recurrence.MatharA027182SelfConvolution.result` states the A027182
recurrence for `n >= 6`; the four companion corollaries have written proofs
and exact arithmetic checks.

`provenance.json` records the scientific source identities and precise scope.
`MANIFEST.json` lists each packaged member's size and SHA256 digest, excluding
the manifest itself. PDF byte reproducibility is not asserted: compilation
timestamps can differ even when page text and rendered pixels agree.

## License

The note is licensed under the
[Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/)
(`CC BY 4.0`, metadata identifier `cc-by-4.0`).
