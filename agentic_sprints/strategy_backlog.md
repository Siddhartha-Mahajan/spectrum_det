# Agentic sprint backlog

Date: 2026-05-12

Each sprint should try one strategy and leave behind runnable code, outputs, and a short result note. This file is only a backlog; it is not itself a sprint.

## Candidate sprint lanes

- Witness generation: find explicit matrices for present determinant values.
- Candidate Gram enumeration: enumerate possible G = R R^T for target determinants.
- Fixed-Gram decomposition: decide whether a given Gram decomposes as R R^T.
- SAT or CP-SAT decomposition: encode fixed-Gram decomposition as Boolean or pseudo-Boolean constraints.
- Meet-in-the-middle row-set search: assemble compatible rows using precomputed dot-product tables.
- Arithmetic filters: measure determinant, PSD, modular, and invariant-factor filters.
- Certificate architecture: design checkable records for negative results.
- Agentic division of labor: separate literature extraction, math audit, implementation, experiment, and certificate checking.

## Active sprint folders

- sprint_1: witness-generation experiment on the known n = 8 spectrum.
- sprint_2: fixed-Gram decomposition experiment on known decomposable small cases.
- sprint_3: order-13 witness-side replication.
- sprint_4: BOOZ-style Gram proof pipeline and bounded candidate-minor profiling.
- sprint_5: native Orrick/BOOZ-style candidate-Gram generator prototype.
- sprint_6: paper-reproduction candidate-Gram generator attempt with canonicalization diagnostics; currently reaches 2055 nauty classes, not BOOZ's 8321.
- sprint_7: witness-driven canonical-filter audit; found and patched the `F`/`Gamma` update-order bug, improving patched-run coverage to 124/130 known high-tail values in the long-run snapshot.
- sprint_8: repaired order-13 generator reconciliation; known high-tail compatibility is 130/130 after combining stream coverage with direct path tracing, while the full 8321 candidate-Gram count remains open locally.
- sprint_9: complete n = 12 conjectural witness pack; found and verified all 812 conjectured present values.
- sprint_10: optimized order-13 generator fork; vectorized `IsLexMax` gives a 1.35x speedup on a 200k-node benchmark with byte-identical candidate output.

## Suggested next sprint

- future sprint: start exclusion/certificate architecture for the 647 conjectured missing positive `n = 12` values. Witness search is complete; the next hard problem is nonexistence.
