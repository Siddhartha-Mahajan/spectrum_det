# Paper and source findings for BOOZ order-13 reproduction

Date: 2026-05-12

## arXiv versions

The arXiv page for `1112.4160` lists only `v1`, submitted 2011-12-18. No later arXiv revision is available.

The source package was downloaded to:

- `paper_pdfs/sources/arxiv_1112_4160/source.tar`
- `paper_pdfs/sources/arxiv_1112_4160/extracted/`

The source package contains the paper TeX and ancillary files for orders 19 and 37, including `G1-19.tex`, `G2-19.tex`, `G-37.tex`, `s19d833.txt`, `s37allsofar.txt`, `s37classes.txt`, and conversion utilities. It does not contain an order-13 candidate-Gram list or the original Gram-finding source code.

The TeX source repeats the published order-13 counts:

- lower gap: `2173 * 2^12`;
- Gram-finding lower bound: `d_min = 2173 * 2^12`;
- candidate Gram matrices: `8321`;
- decomposable candidate Grams: `1643`;
- distinct high-tail determinants from decompositions: `130`.

## Public website check

The live ANU page is available at:

- `https://maths-people.anu.edu.au/~brent/maxdet/`

A copy of the index was saved to:

- `agentic_sprints/sprint_7/web_sources/anu_maxdet_index.html`

Visible data links include order folders for 19, 26, 27, 29, 33, and 37, plus `compressed-format.txt`, `convert.c`, and `unconvert.c`. There is no visible order-13 folder or candidate file on that page.

The historical Indiana maxdet URLs redirect to the Bloomington site rather than the old maxdet content. Orrick's `mypage.iu.edu/~worrick/talks.html` hostname did not resolve from this environment, so the determinant-spectrum talk referenced by the paper could not be retrieved here.

## Algorithm clues from Orrick 2004

The important implementation detail was in Orrick's §3.2 algorithm:

1. Build candidate `M_r` from an admissible vector `f`.
2. If `r < n`, run the gamma/KM bound test.
3. If the gamma/KM test passes, add `f` to `F_{r-1}`.
4. Then test the active block with `IsLexMax`.
5. Recurse only if `IsLexMax` passes.

Sprint 6 had step 3 after step 4, which made future `Gamma_r` lists too small. This was the root cause of the large undercount.

## Confirmed local fix

`paper_reproduction_generator.cpp` was patched so KM-passing vectors are added to the working `F` list before lexmax pruning. This matches Orrick's text and immediately improves order-13 coverage:

- old strict full run: 2055 classes, 75/130 known high-tail values covered;
- patched 200k-node run: 247 classes, 85/130 known high-tail values covered;
- patched 2M-node run: 870 classes, 123/130 known high-tail values covered;
- patched in-progress full snapshot at 1419 classes: 124/130 known high-tail values covered.

The patched full run is much slower because the corrected `F` lists enlarge the gamma search space.
