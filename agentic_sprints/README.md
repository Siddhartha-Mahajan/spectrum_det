# Agentic sprints

Date: 2026-05-12

Each sprint folder should be self-contained and should try one strategy only.

A complete sprint folder should include:

- `strategies.md`: the single strategy being tested and why.
- runnable code or scripts for that strategy, if implementation is part of the sprint.
- `outputs/`: generated machine-readable outputs from the run.
- `results.md`: command run, result summary, interpretation, and limitations.

Current sprints:

- `sprint_1`: witness generation on the known n = 8 spectrum.
- `sprint_2`: fixed-Gram decomposition on known decomposable Grams and one inconsistent Gram.
- `sprint_3`: order-13 witness-side replication of the BOOZ high tail.
- `sprint_4`: BOOZ-style Gram proof pipeline, public-resource check, checkpointed supplied-Gram verification, and bounded candidate-minor profiling.
- `sprint_5`: native Orrick/BOOZ-style candidate-Gram generator prototype with exact determinant checks and checkpointed progress.
- `sprint_6`: paper-reproduction candidate-Gram generator attempt with BOOZ-congruent entries, active-block canonical diagnostics, and nauty-backed candidate canonicalization; not yet matching the 8321 order-13 paper count.
- `sprint_7`: witness-driven filter audit that found and fixed the sprint-6 `F`/`Gamma` update-order bug; patched diagnostics now cover 124/130 known high-tail values in the long-run snapshot.
- `sprint_8`: repaired order-13 generator reconciliation: path trace for the six stream-missing witnesses plus high-tail coverage accounting.
- `sprint_9`: complete n = 12 conjectural witness pack: sparse-tail search, dense-interval fill, and final exact verification for all 812 conjectured values.
- `sprint_10`: optimized order-13 reproduction generator: vectorized `IsLexMax` preserves capped candidate streams, gives a 1.35x speedup on the 200k-node benchmark, and completes an 8-worker full run in about 61 minutes; the BOOZ 8321 candidate count is still not reproduced.

The top-level `strategy_backlog.md` lists other possible strategies. It is not a sprint and should not mix experiments.
