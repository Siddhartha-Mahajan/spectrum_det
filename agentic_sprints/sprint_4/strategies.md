# Sprint 4: BOOZ-style Gram-enumeration proof pipeline

Date: 2026-05-12

## Strategy

Try one strategy: build the candidate-Gram proof layer needed for the BOOZ order-13 theorem.

BOOZ's order-13 proof has two computational pieces:

1. Witnesses for normalized determinants 0 through 2172.
2. A complete candidate-Gram enumeration above the first gap 2173, followed by decomposition of those candidate Grams.

Sprint 3 reproduced a witness-side subset by finding exact witnesses for every published high-tail value. Sprint 4 focuses on the proof layer: candidate Gram validation, decomposition, and a bounded Gram-generation profiler.

## What a full proof needs

For order 13 and threshold d_min = 2173 * 2^12, a full BOOZ replication would need:

- a complete list of candidate Gram matrices, one per Gram-equivalence class, with det(G) >= d_min^2;
- verification that each candidate has diagonal 13, off-diagonal entries congruent to 13 mod 4, positive definiteness, and square determinant;
- decomposition/refutation of every candidate Gram;
- confirmation that decomposable Grams yield exactly the 130 published high-tail normalized determinants.

BOOZ reports 8321 candidate Grams and 1643 decomposable candidates.

## Experiment in this sprint

The script `gram_proof_pipeline.py` does three things:

1. It turns sprint-3 witnesses into decomposable Gram matrices and verifies the candidate-Gram conditions.
2. It decomposes those Grams with the sprint-2 fixed-Gram decomposer as an end-to-end verifier for a supplied Gram list.
3. It runs a bounded principal-minor generator/profiler using BOOZ/Orrick candidate entry rules to measure branching and pruning pressure.

The script writes partial progress after every supplied Gram, so long runs can be interrupted without losing the current state.

This is not expected to regenerate all 8321 BOOZ candidate Grams in pure Python. The purpose is to establish the verification pipeline and quantify the missing full generator.

## Run

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python gram_proof_pipeline.py --max-generated 20000 --max-depth 6
```

## Success criteria

- Verify all unique Grams induced by sprint-3 high-tail witnesses.
- Decompose those Grams and recover their normalized determinant values.
- Produce a profiling report for candidate principal-minor generation.
- State clearly whether the run is a full proof or a partial proof-pipeline attempt.

## Limitation

The public BOOZ/Brent page linked from the paper currently provides compressed-format utilities and candidate-Gram data for orders 19 and 37, but not the Gram-finding C/GMP source and not an order-13 candidate-Gram directory. A direct check of the likely `order13/` URL returned HTTP 404.

That does not make a native implementation impossible. It means sprint 4 is a proof-pipeline and profiling sprint, while a later sprint should implement the full BOOZ/Orrick Gram-finding algorithm in C/C++/Rust with exact arithmetic.
