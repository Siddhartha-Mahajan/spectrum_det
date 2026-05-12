# Sprint 7 results: witness-driven filter audit and F-list repair

Date: 2026-05-12

Status: major reproduction blocker found and fixed; full BOOZ count still not reproduced.

## Bottom line

Sprint 7 found the concrete bug that made sprint 6 undercount: the generator updated `F_{r-1}` after `IsLexMax`, but Orrick's algorithm adds a KM/gamma-passing vector `f` to `F_{r-1}` before the active-block `IsLexMax` test.

That matters because `F` is also used to construct later `Gamma` lists. If a vector passes the determinant-bound/gamma test but fails lexmax as a branch root, it can still be needed as an admissible vector in future sibling gamma lists. Sprint 6 was starving those future lists.

After patching this in `../sprint_6/paper_reproduction_generator.cpp`, order-13 coverage improved sharply:

- old sprint-6 strict full run: 2055 nauty classes, 75/130 known high-tail values covered;
- patched 200k-node run: 247 classes, 85/130 known high-tail values covered;
- patched 2M-node run: 870 classes, 123/130 known high-tail values covered;
- patched long-run snapshot: 1429 classes, 124/130 known high-tail values covered.

The BOOZ target remains 8321 candidate Gram matrices, so this is not yet a complete paper reproduction.

## Paper/source search

See `paper_source_findings.md`.

The useful findings were:

- arXiv `1112.4160` has only v1.
- The arXiv source package was downloaded to `paper_pdfs/sources/arxiv_1112_4160/`.
- The source/ancillary bundle contains paper TeX and order-19/order-37 data, not order-13 candidate Grams or the Gram-finder source.
- The live ANU maxdet page exposes order folders for 19, 26, 27, 29, 33, and 37, not order 13.
- Orrick's older `mypage.iu.edu/~worrick/talks.html` hostname did not resolve here.
- Orrick 2004 §3.2 gives the crucial `F`-list update order.

## Witness audit

Command:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python audit_witness_filters.py --output canonical_audit_all.json
```

Output:

- `outputs/canonical_audit_all.json`

Result:

- all 130 known high-tail witness Grams have a canonical ordering that passes row/block/lexmax filters under both tested row policies and all tested lex modes;
- this falsified the earlier hypothesis that strict active-block `IsLexMax` was directly rejecting known decomposable Grams;
- since sprint 6 still missed many values, the next suspect was not final canonicalization but generator state used by the gamma/KM layer.

## Generator patch

Patched file:

- `../sprint_6/paper_reproduction_generator.cpp`

Change:

- move `working_lists[next_size - 1].push_back(vector)` to immediately after `passes_bound(...)` succeeds and before the active-block `IsLexMax` branch-pruning check.

This matches Orrick 2004 §3.2:

1. run gamma/KM bound;
2. if it passes, add `f` to `F_{r-1}`;
3. then run `IsLexMax` and recurse only if it passes.

## Patched runs

### 200k nodes

Command:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 200000 --progress-every 50000 --output-dir ../sprint_7/outputs/flist_fix_200k
```

Canonicalization:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python canonicalize_candidates.py --input ../sprint_7/outputs/flist_fix_200k/candidates.jsonl --output ../sprint_7/outputs/flist_fix_200k/canonical_classes.json
```

Result:

- nodes tested: 200000
- candidates/classes: 247
- distinct normalized values: 96
- known high-tail coverage: 85/130

### 2M nodes

Command:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 2000000 --progress-every 250000 --output-dir ../sprint_7/outputs/flist_fix_2m
```

Result:

- nodes tested: 2000000
- candidates/classes: 870
- distinct normalized values: 146
- known high-tail coverage: 123/130
- missing known high-tail values at this cutoff: `2271, 2307, 2316, 2336, 2360, 2592, 2916`

### Long strict run snapshot

Command started:

```bash
./paper_reproduction_generator --order 13 --threshold-normalized 2173 --max-nodes 0 --progress-every 500000 --output-dir ../sprint_7/outputs/flist_fix_full
```

The run was intentionally stopped after it became clear it was a long multi-hour branch. It was still CPU-bound and had reached the latest checkpoint:

- nodes tested: 5000000
- candidates at checkpoint: 1397
- elapsed at checkpoint: about 2461 seconds

A later candidate-stream snapshot was canonicalized:

- `outputs/flist_fix_full/candidates.partial_latest.jsonl`
- `outputs/flist_fix_full/canonical_classes.partial_latest.json`

Snapshot result:

- candidates/classes: 1429
- distinct normalized values: 151
- known high-tail coverage: 124/130
- missing known high-tail values in this snapshot: `2271, 2307, 2316, 2336, 2360, 2916`

No generator or canonicalizer process was left running after the stop.

## Interpretation

This sprint materially improves reproduction confidence. The earlier undercount was not just a vague canonicalization mismatch; it was a specific state-update error in the `F`/`Gamma` machinery.

However, the patched generator is now slower because the corrected `F` lists enlarge gamma search. It has not yet reproduced the paper's 8321 candidate count. The next implementation work should target performance and the remaining six missing witness values in the long-run snapshot.

## Next step

Add a direct witness-path instrumentation mode to the C++ generator: feed it the canonical order of a missing witness Gram, then report at which exact recursive level the generator's live `F`, `Gamma`, `e_r`, or bound state diverges from the witness path. The Python audit shows the static row/block/lex tests pass, so the remaining gap is dynamic search-state behavior.
