# Sprint 6: paper-level Orrick/BOOZ candidate-Gram reproduction

Date: 2026-05-12

## Strategy

Try one strategy: make the native candidate-Gram generator paper-faithful enough to reproduce the order-13 BOOZ Gram-finding stage.

Sprint 5 established a native determinant-pruned recursive search, but it was not yet at the level of reproducing the paper. Sprint 6 adds the proof-critical canonical search mechanics from Orrick's Section 3.

## Target from the paper

BOOZ reports that for order 13, with

```text
d_min = 2173 * 2^12
```

the Gram-finding program produced 8321 candidate Gram matrices in 73 minutes. Decomposition then found 1643 decomposable candidates giving 130 high-tail determinant values.

This sprint targets the first stage: candidate Gram generation. Decomposition is not part of this sprint.

## Implemented additions over sprint 5

`paper_reproduction_generator.cpp` adds:

- Orrick absolute-value lexicographic ordering for `Phi`;
- default BOOZ candidate-Gram entry set: all off-diagonal values congruent to `n mod 4`, ordered by absolute value;
- diagnostic `--phi-mode restricted` for the narrower Orrick order-15 sequence;
- canonical minimal element handling;
- active-block tracking from non-minimal connectivity;
- block-form/contiguous-block validation;
- row lex-order validation;
- descending block-order validation;
- Orrick-style `IsLexMax` for the active block;
- diagnostic lexmax policies: `always` (default), `closed`, `final`, and `none`/`--skip-lexmax`;
- dynamic `e_r` updates when a new block begins and the next row joins it;
- Kounias-Moyssiadis allowable-vector pruning with the current `e_r` bound;
- explicit stats for structure, block-order, lexmax, determinant, and bound pruning;
- checkpointed JSON progress and JSONL candidate output.

## Still not covered by this sprint

This sprint still does not implement the BOOZ decomposition stage, Gram-pair constraints, Hasse-Minkowski certificates, or the order-13 high-tail witness search. Those were covered separately in sprints 3 and 4.

## Build

```bash
make
```

## Smoke run

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 200000 --progress-every 25000 --output-dir outputs/smoke
```

## Fuller reproduction attempt

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 0 --progress-every 500000 --output-dir outputs/full_attempt
```

`--max-nodes 0` means no node cap. If the run is too slow for this machine, use a cap and record the frontier/status honestly.

Restricted-Phi diagnostic:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --phi-mode restricted --max-nodes 0 --output-dir outputs/restricted_phi
```

No-lexmax diagnostic:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --lexmax-mode none --max-nodes 0 --progress-every 500000 --output-dir outputs/diagnostic_skip_lexmax_full
```

## Success criteria

- Paper-level target: 8321 order-13 candidate Gram matrices before decomposition.
- Sprint-level minimum: all canonical-search pieces compile and run, progress is checkpointed, and output states clearly whether the 8321 target was reached or what remains different.
