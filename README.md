# spectrum_det

Date: 2026-05-12

## What this repository is

This repository is a working research and experimentation archive for the determinant-spectrum problem for 12 x 12 `{ -1, 1 }` matrices.

The main long-term goal is to determine the exact normalized spectrum

`S_12 = { |det(R)| / 2^11 : R is a 12 x 12 { -1, 1 } matrix }`.

The work here is not limited to direct attacks on `n = 12`. A large part of the repository is devoted to reproducing the Brent, Orrick, Osborn, Zimmermann order-13 pipeline, because that is the closest completed proof architecture and the best local model for how a certificate-quality `n = 12` solution may need to look.

In practice, the repository now contains four things:

1. problem framing and literature notes for the `n = 12` task;
2. a curated cache of relevant papers, extracted notes, and web snapshots;
3. self-contained agentic sprints that each test one strategy;
4. order-13 BOOZ reproduction machinery used as a prerequisite for later `n = 12` work.

## Current status in one page

- The target problem is still open here: `S_12` is not proved.
- The archived maxdet page gives a conjectured normalized spectrum for `n = 12` with 812 values including zero.
- The nearest completed odd-order result is `n = 13`, proved by Brent, Orrick, Osborn, and Zimmermann.
- Sprint 3 reproduced the witness side of the BOOZ `n = 13` theorem: all 130 published high-tail values above the first gap were found and verified.
- Sprint 6 built a native C++ candidate-Gram generator and nauty-backed canonicalizer, but initially undercounted badly.
- Sprint 7 found the main bug in that generator: `F_{r-1}` must be updated before active-block `IsLexMax`, not after it.
- After the sprint 7 patch, the strict order-13 reproduction run improved from 75/130 to 124/130 known high-tail values in the long-run snapshot.
- The BOOZ order-13 paper count of 8321 candidate Gram matrices is still not fully reproduced.
- The best current next step is a dynamic witness-path instrumentation sprint for the six remaining missing high-tail values.

## Main top-level files and folders

| Path | Purpose |
| --- | --- |
| `problem.md` | Focused agent handoff for the actual `n = 12` determinant-spectrum problem. |
| `notes.md` | Running detailed notes, literature findings, sprint history, and download status. |
| `exploration_sprint_determinant_spectrum_problem.pdf` | Original exploration brief that kicked off the repo work. |
| `paper_pdfs/` | Curated local paper cache: PDFs, extracted markdown, and downloaded source bundles. |
| `web_sources/` | Saved web pages and spectrum tables from the archived maxdet material. |
| `agentic_sprints/` | Self-contained strategy folders. Each sprint tries one idea and leaves runnable code, outputs, and a result note. |

## The actual problem this repo is trying to solve

The target problem is:

> Determine exactly which normalized values `s` in `{0, 1, ..., 1458}` occur as `|det(R)| / 2048` for 12 x 12 `{ -1, 1 }` matrices `R`.

Equivalent facts used throughout the repo:

- Hadamard gives `|det(R)| <= 12^6 = 2,985,984`.
- Every 12 x 12 `{ -1, 1 }` determinant is divisible by `2^11 = 2048`.
- So `S_12` is a subset of `{0, 1, ..., 1458}`.
- Presence needs a witness matrix.
- Absence needs a proof or at least a certificate architecture that could be independently checked.

The working conjectural target set for `n = 12` was parsed from the archived maxdet page and recorded in `problem.md` and `notes.md`.

## What has been collected

### 1. Problem framing and project notes

| Path | Collected content |
| --- | --- |
| `exploration_sprint_determinant_spectrum_problem.pdf` | Original project framing, motivation, and constraints. |
| `problem.md` | Clean agent-ready problem statement, objective, status, and recommended start path. |
| `notes.md` | Detailed cumulative log of all findings and sprint work. |

### 2. Papers kept in the active cache

The repository intentionally keeps a lean but useful paper set. These are the papers and extracted notes currently kept as active local context.

| PDF | Markdown extraction | Why it is here |
| --- | --- | --- |
| `paper_pdfs/pdfs/brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.pdf` | `paper_pdfs/mds/brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.md` | Main BOOZ reference. Complete order-13 spectrum proof and candidate-Gram/decomposition pipeline. |
| `paper_pdfs/pdfs/orrick_2004_maximal_pm1_determinant_order_15.pdf` | `paper_pdfs/mds/orrick_2004_maximal_pm1_determinant_order_15.md` | Precursor Gram-finding algorithm. Critical for `IsLexMax`, block structure, and `F`/`Gamma` semantics. |
| `paper_pdfs/pdfs/zivkovic_2005_classification_small_01_matrices.pdf` | `paper_pdfs/mds/zivkovic_2005_classification_small_01_matrices.md` | Small `(0,1)` determinant-range context corresponding to nearby `{ -1, 1 }` orders. |
| `paper_pdfs/pdfs/craigen_1990_range_determinant_function_01_matrices.pdf` | `paper_pdfs/mds/craigen_1990_range_determinant_function_01_matrices.md` | Gap existence context and determinant-spectrum history. |
| `paper_pdfs/pdfs/komlos_1967_on_determinant_of_01_matrices.pdf` | `paper_pdfs/mds/komlos_1967_on_determinant_of_01_matrices.md` | Older determinant background and asymptotic context. |

### 3. Papers or sources not fully available

| Path | Status |
| --- | --- |
| `paper_pdfs/mds/metropolis_1971_spectra_determinant_values_01_matrices_NOT_DOWNLOADED.md` | Metadata note only. The proceedings item could not be downloaded from the reachable sources in this environment. |

### 4. Downloaded paper/source bundles

Later sprints also collected source-level material for BOOZ itself.

| Path | What it contains |
| --- | --- |
| `paper_pdfs/sources/arxiv_1112_4160/source.tar` | The arXiv source package for `1112.4160`. |
| `paper_pdfs/sources/arxiv_1112_4160/extracted/` | Extracted TeX and ancillary files. This includes order-19 and order-37 data files and conversion utilities, but not an order-13 candidate-Gram list or the original Gram-finder source. |

### 5. Web snapshots and archived spectrum data

| Path | What was collected |
| --- | --- |
| `web_sources/mds/spectrum_main.md` | Archived maxdet spectrum overview. |
| `web_sources/mds/spectrum12_conjectured.md` | Archived conjectured `n = 12` spectrum. |
| `web_sources/mds/spectrum13_complete.md` | Archived complete `n = 13` spectrum. |

### 6. Public BOOZ/maxdet artifacts mirrored into sprints

Sprint 4 and sprint 7 pulled down the publicly visible order-19/order-37 files and related utilities that were still exposed on the live maxdet pages.

Important local copies include:

- `agentic_sprints/sprint_4/booz_public_resources/compressed-format.txt`
- `agentic_sprints/sprint_4/booz_public_resources/convert.c`
- `agentic_sprints/sprint_4/booz_public_resources/unconvert.c`
- `agentic_sprints/sprint_4/booz_public_resources/order19_s19d833.txt`
- `agentic_sprints/sprint_4/booz_public_resources/order37_n37b648-r111.txt`
- `agentic_sprints/sprint_7/web_sources/anu_maxdet_index.html`

These were useful for confirming what public data still exists and what is missing.

## What has been done

The repository is organized as one-strategy sprints. The sprint rule is documented in `agentic_sprints/README.md`.

### Sprint summary table

| Sprint | Main files | What it did | Main outcome |
| --- | --- | --- | --- |
| `sprint_1` | `witness_search.py`, `results.md`, `outputs/` | Checked witness generation on a known solved case, `n = 8`. | Recovered all known normalized `S_8` values, confirming the basic witness workflow. |
| `sprint_2` | `decompose_gram.py`, `results.md`, `outputs/` | Tested fixed-Gram decomposition on known decomposable and inconsistent examples. | Successfully decomposed valid Grams and rejected an inconsistent one. |
| `sprint_3` | `n13_witness_replication.py`, `results.md`, `outputs/` | Reproduced the witness side of the BOOZ order-13 high tail. | Found and exactly verified all 130 published high-tail determinant values above the first gap. |
| `sprint_4` | `gram_proof_pipeline.py`, `results.md`, `outputs/`, `booz_public_resources/` | Built a BOOZ-style proof pipeline and checked public source/data availability. | Verified supplied witness-induced high-tail Grams and confirmed public order-13 Gram-finder source/data was not available at checked URLs. |
| `sprint_5` | `native_gram_generator.cpp`, `Makefile`, `results.md`, `outputs/` | Built a first native Orrick/BOOZ-style candidate-Gram generator. | Useful prototype, but not yet proof-grade or paper-level. |
| `sprint_6` | `paper_reproduction_generator.cpp`, `canonicalize_candidates.py`, `results.md`, `outputs/` | Attempted paper-level BOOZ order-13 candidate-Gram reproduction. | Built serious machinery, but initial strict run only reached 2055 nauty classes and covered 75/130 known high-tail values. |
| `sprint_7` | `audit_witness_filters.py`, `paper_source_findings.md`, `results.md`, `outputs/` | Audited witness Grams against sprint-6 filters and searched the paper/source trail for exact generator semantics. | Found the critical `F_{r-1}` update-order bug and patched sprint 6. Patched runs improved to 124/130 known high-tail values in the long-run snapshot. |

### More detail by sprint

#### Sprint 1

- Purpose: sanity-check witness generation on a solved small spectrum.
- Output: exact witnesses for the known `n = 8` values.
- Why it matters: established a reliable existence-side workflow before touching `n = 12` or `n = 13`.

#### Sprint 2

- Purpose: sanity-check the decomposition side on fixed Grams.
- Output: decomposition results for valid examples plus one deliberate negative example.
- Why it matters: gave a local tool for reasoning about `G = R R^T` style constraints.

#### Sprint 3

- Purpose: reproduce the published order-13 high-tail witnesses.
- Key result: all 130 published values above 2173 were recovered and verified exactly.
- Why it matters: the BOOZ existence side is real and locally reproducible in this repo.

#### Sprint 4

- Purpose: build the beginnings of a BOOZ-style proof pipeline and verify what public supporting data still exists.
- Key result: public order-19/order-37 artifacts still exist, but no order-13 candidate-Gram list or source code was found in the checked public locations.
- Why it matters: this narrowed the problem from "find the public BOOZ code" to "reconstruct the BOOZ generator ourselves".

#### Sprint 5

- Purpose: implement the generator ourselves in native code.
- Key implementation features: exact Bareiss determinants with `__int128`, recursive admissible-vector handling, KM-style bound checks, checkpointing, JSONL candidate output.
- Key limitation: the generator was still missing enough canonical-generation fidelity to be considered paper-level.

#### Sprint 6

- Purpose: push from prototype to paper-reproduction attempt for BOOZ order 13.
- Added: BOOZ-congruent entry set `[1, -3, 5, -7, 9, -11]`, canonicalization modes, `pynauty` canonicalizer, more diagnostics, and many output streams.
- Initial strict result: 2057 candidate lines, 2055 nauty classes, 86 determinant values, 75/130 known high-tail values covered.
- Interpretation at the time: canonical-generation mismatch, but the exact cause was still unclear.

#### Sprint 7

- Purpose: use the 130 known high-tail witness Grams as ground truth.
- Witness-audit finding: all 130 witness Grams admit canonical orderings that pass the static row/block/lexmax filters.
- Source-search finding: Orrick 2004 section 3.2 says `f` is added to `F_{r-1}` after the gamma/KM bound passes and before the active-block `IsLexMax` test.
- Bug fixed: sprint 6 had been updating `F_{r-1}` after lexmax pruning, which starved later `Gamma` lists.
- Patched reproduction status:
  - 200k nodes: 247 classes, 85/130 coverage.
  - 2M nodes: 870 classes, 123/130 coverage.
  - long-run snapshot: 1429 classes, 124/130 coverage.

## Important technical findings so far

### Findings about the real `n = 12` task

- `n = 12` is harder than a naive "smaller than 13" story suggests.
- Even order means row dot products can be zero, which weakens some of the odd-order structure that BOOZ exploits.
- The archived conjecture is a target map, not a proof.
- A serious `n = 12` solution is likely to need both witness-side and exclusion-side machinery.

### Findings about BOOZ order-13 reproduction

- The full congruent off-diagonal set for `n = 13` is required: `[1, -3, 5, -7, 9, -11]`.
- Restricted odd-order Phi like `[1, -3, -7, -11]` is not enough for the order-13 spectrum stage.
- Static row/block/lexmax checks were not the main reason sprint 6 undercounted.
- The main undercount bug was dynamic search-state behavior in the admissible-vector lists.
- Correct `F`/`Gamma` state handling improves reproduction sharply, but makes the run slower because the gamma search becomes larger.
- The paper-level target of 8321 candidate Gram matrices is still open in this repo.

## Current best picture of the order-13 BOOZ reproduction

What is reproduced:

- the witness side of the high tail;
- a native C++ candidate-Gram generator;
- a nauty-backed canonicalizer for candidate streams;
- the main hidden generator bug found through paper reading plus witness audits.

What is not yet reproduced:

- the full BOOZ count of 8321 candidate Gram matrices;
- the full decomposition-side confirmation of the published 130-value high tail from our own fully reproduced candidate list;
- the original public order-13 candidate-Gram data or source, because no such public file was found in the reachable locations.

## Repository layout in more detail

```text
spectrum_det/
  README.md
  problem.md
  notes.md
  exploration_sprint_determinant_spectrum_problem.pdf
  agentic_sprints/
    README.md
    strategy_backlog.md
    sprint_1/
    sprint_2/
    sprint_3/
    sprint_4/
    sprint_5/
    sprint_6/
    sprint_7/
  paper_pdfs/
    pdfs/
    mds/
    sources/
  web_sources/
    mds/
```

## How to navigate this repository quickly

If you only need the big picture:

1. Read `problem.md`.
2. Read `agentic_sprints/README.md`.
3. Read `agentic_sprints/sprint_7/results.md`.
4. Read `notes.md` only if you need the detailed history.

If you want the latest technical frontier:

1. Read `agentic_sprints/sprint_6/results.md`.
2. Read `agentic_sprints/sprint_7/results.md`.
3. Inspect `agentic_sprints/sprint_6/paper_reproduction_generator.cpp`.
4. Inspect `agentic_sprints/sprint_7/audit_witness_filters.py`.

If you want the paper corpus first:

1. Start with the BOOZ PDF and markdown extraction.
2. Then read Orrick 2004.
3. Then look at the archived `n = 12` and `n = 13` spectrum pages.

## Environment and tooling used in the repo

The work so far used:

- an existing Python virtual environment at `.venv`;
- `uv` for package installation into that environment when needed;
- `pynauty` for fast candidate canonicalization in sprint 6;
- `clang++` for the native C++ generator builds;
- exact Bareiss determinant arithmetic in both Python and C++;
- JSON and JSONL outputs for machine-readable experiment records.

Important sprint-local build or run surfaces include:

- `agentic_sprints/sprint_5/Makefile`
- `agentic_sprints/sprint_6/Makefile`
- `agentic_sprints/sprint_6/requirements.txt`

## Most important generated artifacts

The repo includes a large number of outputs. The most important ones to know about are:

| Path | Why it matters |
| --- | --- |
| `agentic_sprints/sprint_3/outputs/n13_witnesses.json` | Exact witness library for the published order-13 high tail. |
| `agentic_sprints/sprint_4/outputs/` | Early BOOZ-style verification pipeline outputs. |
| `agentic_sprints/sprint_6/outputs/full_attempt/` | Original strict reproduction attempt that undercounted. |
| `agentic_sprints/sprint_6/outputs/diagnostic_*` | Canonicalization and pruning diagnostics from the pre-fix generator. |
| `agentic_sprints/sprint_7/outputs/canonical_audit_all.json` | Witness-filter audit showing all 130 witness Grams pass the static filter layer. |
| `agentic_sprints/sprint_7/outputs/flist_fix_2m/` | Best clean patched diagnostic cutoff so far. |
| `agentic_sprints/sprint_7/outputs/flist_fix_full/` | Partial artifacts from the longer patched run. |

## What is blocked or incomplete

- The Metropolis 1971 source paper is still not locally downloaded.
- No public order-13 BOOZ candidate-Gram list was found.
- No public BOOZ order-13 Gram-finding source code was found.
- The older Orrick IU talk page cited by the paper did not resolve from this environment.
- The full 8321 BOOZ candidate-Gram count is still not reproduced here.

## Recommended next step from the current state

The best next sprint is already identified in `agentic_sprints/strategy_backlog.md`:

- add dynamic witness-path instrumentation for the six remaining missing high-tail values in the patched long-run snapshot: `2271, 2307, 2316, 2336, 2360, 2916`;
- feed their canonical witness-Gram orderings into the live C++ generator;
- log the first exact divergence in `F`, `Gamma`, `e_r`, or bound state.

That is the narrowest known path from the current state toward a genuine BOOZ order-13 reproduction, and it is the best immediate precursor to any serious `n = 12` exclusion-side work.

## If you are starting fresh in this repo

Read these in order:

1. `README.md`
2. `problem.md`
3. `agentic_sprints/README.md`
4. `agentic_sprints/sprint_7/results.md`
5. `notes.md`

That sequence gives the problem statement, the repo map, the sprint structure, the current technical frontier, and the detailed research log.