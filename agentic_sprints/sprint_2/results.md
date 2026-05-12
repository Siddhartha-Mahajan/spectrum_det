# Sprint 2 results: fixed-Gram decomposition

Date: 2026-05-12

Status: completed.

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python decompose_gram.py
```

Output:

- outputs/decomposition_results.json

## Result summary

The fixed-Gram decomposer represents rows as bit words, fixes the first row to all +1, and searches row candidates constrained by pairwise dot products.

| Case | Status | Nodes | Verified | Runtime |
| --- | --- | ---: | --- | ---: |
| n8_sylvester_hadamard | sat | 128 | yes | 0.0007 s |
| n8_random_normalized | sat | 125 | yes | 0.0006 s |
| n12_random_normalized | sat | 15084 | yes | 0.0448 s |
| n8_inconsistent_perturbation | unsat | 71 | expected no witness | 0.0002 s |

## Interpretation

The fixed-Gram decomposition subproblem is very approachable on these small controlled cases. The n = 12 random decomposable Gram was recovered quickly, which is encouraging for using this as a component.

This sprint does not enumerate candidate Grams. It can only answer: given this G, can we find R with G = R R^T? A future nonexistence sprint still needs a complete candidate-Gram generation or certificate layer.
