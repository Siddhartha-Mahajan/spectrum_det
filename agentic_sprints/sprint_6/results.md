# Sprint 6 results: paper-level Orrick/BOOZ candidate-Gram reproduction

Date: 2026-05-12

Status: substantial reproduction machinery built, but the BOOZ paper count is not reproduced yet.

Sprint 7 update: the main sprint-6 undercount diagnosis below is superseded. Sprint 7 found a concrete `F`/`Gamma` state-update bug: KM-passing vectors must be added to `F_{r-1}` before active-block `IsLexMax` pruning, as in Orrick 2004 §3.2. After patching `paper_reproduction_generator.cpp`, a 2M-node run covered 123/130 known high-tail values, compared with 75/130 in the old strict full run.

## Bottom line

We were not at paper-reproduction level after sprint 5, and sprint 6 still does not reach it.

The BOOZ target is 8321 order-13 candidate Gram matrices at threshold `2173 * 2^12`. The completed strict sprint-6 generator run produced 2057 candidate lines, which nauty canonicalization reduced to 2055 permutation classes. It covers 75 of the 130 known high-tail determinant values from sprint 3.

So sprint 6 is a strong implementation step, not a completed reproduction of the paper.

## Built artifacts

- `paper_reproduction_generator.cpp`: native C++ Orrick/BOOZ-style candidate-Gram generator.
- `canonicalize_candidates.py`: nauty-backed weighted-Gram canonicalizer.
- `Makefile`: C++ build target.
- `outputs/full_attempt/`: completed strict generator run.
- `outputs/diagnostic_skip_lexmax_full/`: interrupted no-lexmax diagnostic stream.
- `outputs/diagnostic_final_lexmax_full/`: interrupted final-only lexmax diagnostic stream.

Additional local dependency installed into the existing venv:

```bash
uv pip install --python .venv/bin/python pynauty
```

## Implemented in the generator

- BOOZ-congruent off-diagonal value set for n = 13: `[1, -3, 5, -7, 9, -11]`.
- Restricted Orrick Phi diagnostic mode: `[1, -3, -7, -11]`.
- Exact Bareiss determinant arithmetic in C++ using `__int128`.
- Recursive admissible-vector `F` lists and allowable-vector `Gamma` scans.
- Kounias-Moyssiadis determinant-bound pruning.
- Dynamic `e_r` mode and constant-`e_r` diagnostic mode.
- Active-block structure tracking from non-minimal entries.
- Block-order and row-order filters.
- Orrick-style `IsLexMax` active-block check.
- Diagnostic lexmax modes: `always`, `closed`, `final`, and `none`.
- JSON progress checkpoints and JSONL candidate output.

## Completed strict run

Command:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 0 --progress-every 500000 --output-dir outputs/full_attempt
```

This was run before the explicit `lexmax_mode` field was added; behavior corresponds to active-block lexmax checking at every accepted extension, now exposed as `--lexmax-mode always`.

Summary from `outputs/full_attempt/progress.json` and `outputs/full_attempt/candidates.jsonl`:

- nodes tested: 5945497
- recursion calls: 983988
- gamma tests: 152843985
- lexmax checks: 1073722
- candidates written: 2057
- nauty permutation classes: 2055
- distinct normalized determinant values: 86
- known high-tail sprint-3 values covered: 75 / 130
- elapsed time: about 643 seconds
- stopped by cap: false

This is below the BOOZ paper target of 8321 candidate Gram matrices.

## Diagnostics

### Restricted Phi

The narrow Orrick-order-15-style Phi set `[1, -3, -7, -11]` is not sufficient for order-13 spectrum reproduction. Known sprint-3 witness Grams use off-diagonal value `5`, and the restricted-Phi run produced only 74 candidate lines.

### No lexmax

An interrupted no-lexmax diagnostic produced a much larger raw stream:

- raw candidate lines: 12245
- nauty permutation classes in the interrupted prefix: 703
- distinct normalized determinant values: 115
- known high-tail sprint-3 values covered: 102 / 130

This confirms that lexmax/canonical generation is the key unresolved layer, but the run was stopped before normal completion and is not a proof artifact.

### Final-only lexmax

An interrupted final-only lexmax diagnostic produced:

- raw candidate lines: 3516
- nauty permutation classes in the interrupted prefix: 374
- distinct normalized determinant values: 101
- known high-tail sprint-3 values covered: 91 / 130

This did not close the gap either.

### Hadamard and constant emax

Hadamard-bound-only and constant-`e_r` diagnostics did not point to those layers as the primary cause of the 2057 vs 8321 mismatch. The main unresolved issue remains exact BOOZ/Orrick canonical generation.

## Public-data sweep

The public BOOZ/maxdet site still exposes compressed-format utilities and candidate data for orders such as 19 and 37, but not an order-13 candidate list or the original Gram-finding source. The root page lists data folders for orders 19, 26, 27, 29, 33, and 37, not 13.

## Interpretation

Sprint 6 gets us much closer to the paper machinery than sprint 5: the generator is native, checkpointed, uses the BOOZ-congruent value set, has canonical/block diagnostics, and has independent nauty canonicalization.

But it is not paper-level yet. The exact missing piece is a faithful reconstruction of BOOZ/Orrick canonical generation. Our active-block `IsLexMax` policy over-prunes relative to the paper count, while disabling it creates an incomplete/duplicated stream that needs a different exhaustive strategy.

## Next concrete step

The best next sprint is not more blind running. It should isolate canonical generation against known decomposable order-13 witness Grams:

1. Take the 130 sprint-3 high-tail witness Grams.
2. For each, find a parity/sign/permutation normalization that should place it in Orrick/BOOZ canonical form.
3. Check exactly which generator filter rejects the missing witness values.
4. Repair that filter before attempting another full 8321-count run.
