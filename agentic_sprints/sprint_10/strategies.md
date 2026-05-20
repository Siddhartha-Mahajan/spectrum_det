# Sprint 10: optimized order-13 reproduction generator

Date: 2026-05-21

## Strategy

Keep the paper-reproduction search semantics from sprint 6, but reduce overhead in the hot canonical-pruning path.

This sprint does not change the Gram search definition, admissible values, determinant threshold, KM bound, block rules, or `F`/`Gamma` state update. It only changes implementation details that should preserve the enumerated candidate stream.

Tested optimization ideas:

1. Replace `std::set<Vec>` in active-block `IsLexMax` with vector accumulation followed by `sort`/`unique`.
2. Avoid allocation of row-prefix and block-submatrix temporaries in row/block comparisons.
3. Try an exact adjugate/incremental-determinant experiment as a possible replacement for repeated determinant recomputation.

## Success Criterion

- The optimized generator must produce byte-identical `candidates.jsonl` against the baseline on capped reproduction runs.
- It should improve wall-clock time on a nontrivial capped run without weakening any paper-reproduction filters.

## Notes

Apple MPS is not a good fit for this sprint. The workload is exact integer branch-and-bound over tiny dependent matrices, with early exits and mutable search state. Moving this to MPS would require approximate floating-point tensor code and would not preserve the exact paper-reproduction semantics.
