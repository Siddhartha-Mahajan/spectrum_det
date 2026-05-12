# Sprint 7: witness-driven canonical-filter audit

Date: 2026-05-12

## Strategy

Use the 130 known order-13 high-tail witnesses from sprint 3 as ground truth. Each witness is a decomposable order-13 sign matrix, so its row Gram matrix should occur in any complete BOOZ candidate-Gram enumeration with threshold `2173 * 2^12`.

Instead of running the entire candidate-Gram tree again, this sprint asks a sharper question: for each known witness Gram, is there any row permutation whose leading prefixes survive the structural and canonical filters used by the sprint-6 generator?

This isolates whether the mismatch is caused by:

- row/active-block ordering;
- block contiguity or block-order checks;
- premature or incorrect `IsLexMax` timing;
- final-block canonicalization;
- determinant/square/threshold tests.

## Paper clues being tested

From Orrick 2004, which BOOZ says their §3 Gram finder extends:

- the generator builds leading principal minors one row/column at a time;
- the allowed odd-order entries are congruent to `n mod 4`;
- lexicographically ordered matrices have contiguous blocks in descending lexicographic order;
- the active block contains the most recently added row/column;
- a new block begins when the new partial row is the minimal vector;
- `IsLexMax` is described as a block-canonical test, with text emphasizing completed blocks, while the algorithm text also says to test the active block after the KM bound passes;
- if a new block just started at index `r`, index `r + 1` is special and either the rest can be filled by minimal entries or `e_r` is set from the next non-minimal connection.

The arXiv source for 1112.4160 has only v1 and ancillary files for orders 19 and 37; no order-13 candidate list or original source code was found in the source package.

## Success criterion

A useful sprint result is not necessarily the full 8321 count. The sprint succeeds if it identifies which filter policy loses known decomposable witness Grams and provides concrete missing-value examples for repairing sprint 6.
