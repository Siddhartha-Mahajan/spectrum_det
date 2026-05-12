# Sprint 3: order-13 witness-side replication

Date: 2026-05-12

## Strategy

Try one strategy: reproduce part of the BOOZ order-13 spectrum result on the witness/existence side.

BOOZ reports that heuristic search found witnesses for all normalized determinant values 0 through 2172, that 2173 is the first gap, and that candidate-Gram/decomposition work supplies the high-tail values above the gap.

This sprint does not attempt the full candidate-Gram proof. It asks whether a lightweight exact-verified witness search can recover order-13 examples, especially in the high tail of the published complete spectrum.

## Reduction used

For a first-row/first-column-normalized 13 x 13 {-1,1} matrix R, the lower-right 12 x 12 block corresponds to a 12 x 12 (0,1) matrix A. The normalized determinant value is

|det(R)| / 2^12 = |det(A)|.

So this sprint searches 12 x 12 (0,1) matrices and verifies every retained witness exactly.

## Experiment

Run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python n13_witness_replication.py --random-samples 200000 --target-restarts 80 --target-steps 220 --seed 20260512
```

The script:

- parses the archived complete n=13 spectrum from `../../web_sources/mds/spectrum13_complete.md`;
- confirms the first missing normalized value after the low interval is 2173;
- uses random sampling to recover easy low determinant witnesses;
- uses targeted bit-flip local search for every published high-tail value above 2173;
- attempts 2173 as a negative-control target with the same local-search style;
- verifies every found witness with exact Bareiss determinant arithmetic;
- writes machine-readable results and witnesses under `outputs/`.

## Success criteria

The sprint succeeds if it recovers a nontrivial subset of the published n=13 spectrum, especially high-tail values, and records misses honestly.

Full replication of the BOOZ proof would require candidate-Gram enumeration and decomposition certificates. That is outside this sprint.
