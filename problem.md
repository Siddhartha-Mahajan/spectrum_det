# Determinant spectrum problem for 12 x 12 {-1,1} matrices

Date: 2026-05-12

## Problem statement

Determine the complete determinant spectrum of 12 x 12 matrices with entries in {-1,1}.

Let R range over all 12 x 12 {-1,1} matrices. The object of interest is the set of possible absolute determinant values |det(R)|. It is standard to normalize by the universal divisibility factor 2^(n-1):

S_n = { |det(R)| / 2^(n-1) : R is an n x n {-1,1} matrix }.

For this problem, determine S_12 exactly.

## Objective

A complete solution should establish, for every integer s in {0,1,...,1458}, whether there exists a 12 x 12 {-1,1} matrix R such that

|det(R)| = 2048 s.

For values that are present, one explicit matrix is enough as a witness. For values that are absent, the solution needs a proof or independently checkable certificate that no such matrix exists.

## Basic facts

- Hadamard's inequality gives |det(R)| <= 12^6 = 2,985,984.
- Every 12 x 12 {-1,1} determinant is divisible by 2^11 = 2048.
- Therefore S_12 is a subset of {0,1,...,1458}.
- The normalized maximum 1458 corresponds to the Hadamard bound 2,985,984.
- Row dot products have the form 12 - 2h, where h is a Hamming distance. Since n = 12 is even, zero row dot products are possible.

The main structured object is the Gram matrix G = R R^T. For a 12 x 12 {-1,1} matrix R, G is symmetric positive semidefinite, has diagonal entries 12, has integer off-diagonal entries in {-12,-10,...,10,12}, and det(G) = det(R)^2.

## Current status

The determinant spectrum is known for all orders n < 12 and for n = 13. The order n = 12 case is still listed as conjectural in the archived maxdet spectrum tables.

The archived conjectured normalized spectrum for n = 12 is:

{[0,738], [740,765], [767,769], [771,774], [776,777], [779,780], [783,786], [788,789], [792,793], 795, [797,798], [800,801], 805, 807, 810, 816, [818,819], 825, [832,833], 837, 840, 848, 864, 873, 882, 891, 896, 945, 972, 1024, 1053, 1215, 1458}.

This conjecture contains 812 normalized values including zero, so it predicts 811 positive values present and 647 positive values absent.

The conjectured missing positive normalized values are:

{739, 766, 770, 775, 778, [781,782], 787, [790,791], 794, 796, 799, [802,804], 806, [808,809], [811,815], 817, [820,824], [826,831], [834,836], [838,839], [841,847], [849,863], [865,872], [874,881], [883,890], [892,895], [897,944], [946,971], [973,1023], [1025,1052], [1054,1214], [1216,1457]}.

Treat this conjecture as a target map, not as a proof.

## Why n = 12 is difficult

The search space of all 12 x 12 sign matrices has size 2^144 before equivalences, so direct enumeration is not the right starting point.

The best-known completed nearby proof is the n = 13 spectrum result of Brent, Orrick, Osborn, and Zimmermann. Their method separates the problem into two stages: enumerate candidate Gram matrices, then test whether each candidate decomposes as G = R R^T for a {-1,1} matrix R.

The n = 12 case is not just a smaller copy of n = 13. Because n is even, row dot products can be zero. This allows many nearly orthogonal row configurations and may weaken pruning in Gram-matrix search. Any adaptation of odd-order Gram constraints from the literature needs to be checked carefully for even order.

## Historical context

- For n <= 7, the normalized {-1,1} determinant spectrum contains every integer from 0 to the normalized maximum.
- n = 8 is the first order with gaps; Metropolis, Stein, and Wells computed its spectrum.
- Craigen later gave a non-computer proof that gaps exist in determinant spectra.
- Zivkovic classified small (0,1) determinant ranges and is credited for results corresponding to {-1,1} orders n = 9 and n = 10.
- Orrick's order-15 maximal determinant paper is credited for the n = 11 spectrum.
- Brent, Orrick, Osborn, and Zimmermann proved the complete n = 13 spectrum.
- The archived maxdet site leaves n = 12 as conjectural.

The standard relation with (0,1) matrices shifts the order by one: an m x m (0,1) determinant corresponds to an (m+1) x (m+1) {-1,1} determinant after multiplication by 2^m.

## Recommended starting point for an agent

Start from the structured search formulation, not raw matrix enumeration.

1. Read the exploration sprint PDF in this folder for the project motivation and constraints.
2. Use the conjectured spectrum above as the target checklist.
3. Read arXiv:1112.4160, especially Sections 2-4 and 8, for the candidate-Gram/decomposition pipeline and the completed n = 13 spectrum proof.
4. Work separately on existence and nonexistence: present values need witnesses; missing values need exhaustive or certifiable exclusion.
5. Before using an odd-order theorem or pruning rule, verify that it remains valid for n = 12.

Useful local files:

- notes.md: running research notes, source log, detailed BOOZ notes, download status, and extra context.
- exploration_sprint_determinant_spectrum_problem.pdf: original sprint document.
- paper_pdfs/mds/brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.md: extracted text of the main reference.
- paper_pdfs/pdfs/brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.pdf: PDF of the main reference.
- web_sources/mds/spectrum12_conjectured.md: archived conjectured n = 12 spectrum source.
- agentic_sprints/README.md: structure for self-contained one-strategy sprints.
- agentic_sprints/sprint_1/results.md: witness-generation experiment on the known n = 8 spectrum.
- agentic_sprints/sprint_2/results.md: fixed-Gram decomposition experiment on known decomposable cases.
- agentic_sprints/sprint_3/results.md: order-13 witness-side replication; all 130 published high-tail values found and verified.
- agentic_sprints/sprint_4/results.md: BOOZ-style Gram proof-pipeline progress and public-resource check.
- agentic_sprints/sprint_5/results.md: native Orrick/BOOZ-style candidate-Gram generator prototype with checkpointed progress.
- agentic_sprints/sprint_6/results.md: paper-reproduction candidate-Gram generator attempt; includes BOOZ-congruent native generator, nauty canonicalization, and current blocker against reproducing the 8321 order-13 count.
- agentic_sprints/sprint_7/results.md: witness-driven filter audit; identifies and patches the sprint-6 `F`/`Gamma` update-order bug, and records patched-run coverage up to 124/130 known order-13 high-tail values.
- agentic_sprints/sprint_8/results.md: repaired order-13 generator reconciliation; all 130 known high-tail witnesses are accounted for by stream coverage plus path trace, while the full 8321 BOOZ candidate count remains open.
- agentic_sprints/sprint_9/results.md: complete n = 12 conjectural witness pack; verifies all 812 conjectured present values.
- agentic_sprints/sprint_10/results.md: optimized order-13 generator fork; vectorized `IsLexMax` gives a 1.35x speedup on a 200k-node benchmark with byte-identical candidate output, and the full 8-worker run finishes in about 61 minutes while still undercounting BOOZ.

## Scope notes

- Do not assume the archived n = 12 conjecture is correct without proof.
- Do not import BOOZ's odd-order assumptions blindly into the even-order n = 12 case.
- Do not begin with brute-force enumeration over all 2^144 matrices.
- This document is a problem brief. Detailed literature notes, blocked downloads, and exploratory observations are in notes.md.
