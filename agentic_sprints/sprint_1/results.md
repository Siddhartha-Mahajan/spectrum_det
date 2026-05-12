# Sprint 1 results: witness generation on n = 8

Date: 2026-05-12

Status: completed.

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python witness_search.py --n 8 --samples 120000 --restarts 80 --steps 1200 --seed 20260512
```

Outputs:

- outputs/n8_results.json
- outputs/n8_witnesses.json

## Result summary

- Known target spectrum: {0,1,2,...,18,20,24,32}.
- Found all known normalized values.
- Missing known values after random sampling: {17,18,20,24}.
- Targeted local search then found 17, 18, 20, and 24.
- Every reported witness verified exactly by Bareiss determinant checks.
- No extra normalized values outside the known spectrum were observed.
- Runtime for this run: about 1.55 seconds.

## Search details

Random sampling evaluated 120000 random 7 x 7 (0,1) blocks and found:

{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,32}.

Targeted local search filled the remaining values:

- 17: found after 405 exact determinant evaluations.
- 18: found after 175 exact determinant evaluations.
- 20: found after 183 exact determinant evaluations.
- 24: found after 350 exact determinant evaluations.

## Interpretation

Witness generation is useful for the existence side of the spectrum problem. On n = 8, a simple exact-arithmetic sampler plus local bit-flip search recovered witnesses for every known present value quickly.

This sprint does not prove absence of missing values. It should not be used as evidence that values outside the observed set are impossible.
