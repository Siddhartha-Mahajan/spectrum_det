# Sprint 10: optimized order-13 reproduction generator

Date: 2026-05-21

## What This Sprint Is

Sprint 10 is an optimization and parallelization sprint for the order-13 BOOZ candidate-Gram generator.

It is not a new mathematical method. It keeps the sprint-6/sprint-7 reconstructed generator semantics and tries to make the same search run faster and more observably.

## Main Files

- `optimized_reproduction_generator.cpp`: optimized C++ generator.
- `run_parallel_reproduction.py`: launches deterministic sharded workers and merges outputs.
- `adjugate_incremental_experiment.cpp`: exact determinant/adjugate experiment kept as a negative result.
- `outputs/bench_200k_vector_lexmax/`: capped optimized benchmark.
- `outputs/parallel_full_20260521/`: completed 8-worker full run.
- `results.md`: detailed run results.

## Current Best Result

The 8-worker optimized run completed in about 61 minutes.

It produced:

- 2701 raw candidate lines;
- 2626 canonical candidate classes;
- 102 distinct normalized determinant values;
- 86/130 direct coverage of the known BOOZ high-tail determinant values.

This is faster than the killed single-process baseline, but it still does not reproduce the BOOZ paper count of 8321 candidate Gram matrices.

## What Worked

The useful speedup was changing active-block `IsLexMax` from `std::set<Vec>` to vector accumulation plus `sort`/`unique`.

On a 200k-node benchmark:

- baseline: 21.8835 s;
- optimized: 16.2072 s;
- speedup: 1.35x;
- candidate output: byte-identical.

## What Did Not Work

The adjugate/incremental determinant idea is mathematically exact, but the current cofactor implementation is slower than Bareiss recomputation at order 13.

MPS/GPU is not a good fit for this exact integer branch-and-bound workload.

## Current Bottleneck

Runtime is no longer the main blocker. The current blocker is still generator semantics: the reconstructed generator is missing BOOZ-admissible candidate branches.

Next step: use the 40 still-unaccounted high-tail values in `outputs/parallel_full_20260521/order13_reconciliation.json` as branch-level regression tests.
