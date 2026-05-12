# Sprint 1: witness generation on the known n = 8 spectrum

Date: 2026-05-12

## Strategy

Try the witness-generation strategy on order n = 8, where the normalized determinant spectrum is known:

S_8 = {0,1,2,...,18,20,24,32}.

The goal is not to prove the spectrum. The goal is to see whether a simple exact-arithmetic search can recover explicit witnesses for known present values before attempting any n = 12 witness search.

## Reduction used

Every {-1,1} matrix can be sign-normalized so that its first row and first column are all +1. In that form, the remaining (n-1) x (n-1) block can be represented as a (0,1) matrix A, where 1 means the sign entry is -1.

For n = 8, the normalized determinant value is exactly |det(A)| for a 7 x 7 (0,1) matrix A.

This sprint searches 7 x 7 (0,1) blocks and converts any found block into an 8 x 8 sign-matrix witness.

## Experiment

Run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python witness_search.py --n 8 --samples 120000 --restarts 80 --steps 1200 --seed 20260512
```

The script:

- samples random 7 x 7 (0,1) blocks;
- seeds the search with a Sylvester Hadamard witness for normalized value 32;
- uses targeted bit-flip local search for known values not found by random sampling;
- verifies every reported witness with exact Bareiss determinants;
- writes JSON output under outputs/.

## Success criteria

A successful sprint finds explicit witnesses for all known S_8 values, or records which values were missed and how much search was attempted.

## Interpretation

If this works for n = 8, the witness-generation lane is viable as an existence-side tool. It still says nothing about missing values; absence needs a separate proof or certificate strategy.
