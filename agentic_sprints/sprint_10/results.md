# Sprint 10 results: optimized order-13 reproduction generator

Date: 2026-05-21

Status: vectorized `IsLexMax` is faster and preserves the candidate stream on capped tests. The 8-worker full optimized run completed, but still does not reproduce BOOZ's 8321 candidate count.

## Build

```bash
make
```

This builds:

- `optimized_reproduction_generator`

The Makefile also has a native/LTO target:

```bash
make optimized_reproduction_generator_native
```

In the first small benchmark, the native/LTO binary was not faster, so the normal `-O3` build is the current default.

## Commands

Baseline:

```bash
../sprint_6/paper_reproduction_generator \
  --order 13 \
  --threshold-normalized 2173 \
  --max-nodes 200000 \
  --progress-every 100000 \
  --output-dir outputs/bench_200k_original_now
```

Optimized:

```bash
./optimized_reproduction_generator \
  --order 13 \
  --threshold-normalized 2173 \
  --max-nodes 200000 \
  --progress-every 100000 \
  --output-dir outputs/bench_200k_vector_lexmax
```

Equivalence check:

```bash
cmp -s outputs/bench_200k_original_now/candidates.jsonl \
       outputs/bench_200k_vector_lexmax/candidates.jsonl
```

`cmp` returned zero: candidate output is byte-identical for the 200k-node benchmark.

## Benchmark Result

| generator | nodes | candidates | elapsed |
| --- | ---: | ---: | ---: |
| baseline sprint-6 | 200000 | 247 | 21.8835 s |
| sprint-10 optimized | 200000 | 247 | 16.2072 s |

Speedup: `1.35x` on this capped run.

The search statistics match exactly:

- recursion calls: 24672;
- gamma tests: 2093008;
- lexmax checks: 41891;
- lexmax permutations seen: 5082760.

## Full Parallel Run

After killing the slow single-process baseline run, I ran the optimized generator with deterministic sharding:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python run_parallel_reproduction.py \
  --workers 8 \
  --shard-depth 10 \
  --max-nodes 0 \
  --progress-every 250000 \
  --output-dir outputs/parallel_full_20260521 \
  --poll-seconds 30
```

The run completed cleanly:

| metric | value |
| --- | ---: |
| wall time | 3662.1 s |
| workers | 8 |
| tested nodes | 35366382 |
| gamma tests | 4213266303 |
| lexmax checks | 6846241 |
| raw candidate lines | 2701 |
| canonical candidate classes | 2626 |
| distinct normalized determinant values | 102 |
| direct known high-tail coverage | 86/130 |
| coverage after adding sprint-8 path-trace supplement | 90/130 |
| remaining BOOZ count gap | 5695 classes |

Outputs:

- `outputs/parallel_full_20260521/parallel_summary.json`
- `outputs/parallel_full_20260521/candidates.jsonl`
- `outputs/parallel_full_20260521/canonical_classes.json`
- `outputs/parallel_full_20260521/order13_reconciliation.json`
- `outputs/parallel_full_20260521/worker_*/`

## Interpretation

The infrastructure side is now much better:

- the slow single-process run was replaced by a deterministic 8-worker run;
- candidate streams can be merged and canonicalized cleanly;
- progress is visible through `parallel_progress.json`;
- a completed full run takes about one hour on this machine.

But the math-reproduction side is still not solved:

- BOOZ reports 8321 order-13 candidate Gram matrices above the threshold;
- the best current optimized run gives 2626 canonical classes;
- the stream covers 86 of the 130 published high-tail determinant values directly.

So the current blocker is not runtime anymore. It is still a semantic mismatch in the reconstructed generator: some BOOZ admissible branches are being pruned or never generated.

## What Helped

`IsLexMax` previously stored active permutations in `std::set<Vec>`. That pays tree-balancing and allocator overhead for many small permutation lists. The optimized version accumulates permutations in a vector, then calls `sort`/`unique`. This preserves exact set semantics but reduces overhead.

The row/block allocation trim is included, but the measured win appears to come mainly from the `IsLexMax` data-structure change.

## Negative Result

`adjugate_incremental_experiment.cpp` records an exact-algebra attempt:

- use `det([[M,v],[v^T,n]]) = n det(M) - v^T adj(M)v`;
- use the same adjugate identity for KM gamma augmentations.

It produced identical search statistics, but was slower in the early benchmarks because computing adjugates by cofactors costs more than the determinant work saved at order 13. A faster fraction-free adjugate/inverse routine could make this idea worth revisiting.

## Next

The next optimization should not be another blind speed pass. It should target exact generator semantics:

- compare BOOZ/Orrick's `IsLexMax` block handling against the current active-block implementation;
- test whether the `shard_depth = 10` split changes traversal only, not accepted set, against a smaller complete search;
- build a witness-guided branch replay for the 40 still-unaccounted high-tail values from `order13_reconciliation.json`;
- consider a dynamic task queue only after the semantic gap is fixed.
