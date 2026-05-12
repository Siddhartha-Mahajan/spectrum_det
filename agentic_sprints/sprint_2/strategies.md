# Sprint 2: fixed-Gram decomposition

Date: 2026-05-12

## Strategy

Try the fixed-Gram decomposition strategy as a separate sprint.

Given a candidate Gram matrix G, decide whether there exists a {-1,1} matrix R such that

G = R R^T.

This sprint does not enumerate candidate Grams and does not try to prove determinant values absent. It only tests the decomposition subproblem on known decomposable Grams and a deliberately inconsistent Gram.

## Experiment

The script `decompose_gram.py`:

- represents sign rows as bit words;
- precomputes dot products by Hamming distance;
- fixes the first row of R to all +1 for Grams generated from first-row-normalized matrices;
- backtracks over row candidates constrained by G_ij;
- verifies any recovered matrix by recomputing R R^T exactly.

Run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python decompose_gram.py
```

## Test cases

- n = 8 Sylvester Hadamard Gram.
- n = 8 random normalized sign matrix Gram.
- n = 12 random normalized sign matrix Gram.
- n = 8 deliberately inconsistent perturbed Gram.

## Success criteria

The sprint succeeds if the decomposer:

- finds decompositions for the known decomposable Grams;
- verifies each recovered decomposition exactly;
- rejects the deliberately inconsistent Gram;
- records node counts and runtimes for comparison with later SAT or CP-SAT encodings.

## Interpretation

If this works cleanly, fixed-Gram decomposition is a viable component to reuse later. It still needs a separate candidate-Gram generator before it can prove anything about the n = 12 spectrum.
