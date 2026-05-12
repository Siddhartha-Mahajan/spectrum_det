# Sprint 4 results: BOOZ-style Gram proof pipeline

Date: 2026-05-12

Status: partial proof-pipeline progress, not a full BOOZ proof replication.

## Public BOOZ resources checked

BOOZ reference [2] points to:

https://maths-people.anu.edu.au/~brent/maxdet/

The current public page provides:

- `booz_public_resources/convert.c`: C utility for compressed Gram format.
- `booz_public_resources/unconvert.c`: C utility for reading compressed Gram format.
- `booz_public_resources/compressed-format.txt`: format description.
- `booz_public_resources/order19_s19d833.txt`: the 9 order-19 candidate Grams.
- `booz_public_resources/order37_n37b648-r111.txt`: the 807 order-37 candidate Grams.

The current public page does not expose the BOOZ Gram-finding C/GMP source. The paper says their programs were written in C and used GMP, but the linked site publishes data and format utilities, not the optimized Gram-finding program itself.

A direct check of the likely order-13 directory returned 404:

```text
https://maths-people.anu.edu.au/~brent/maxdet/order13/ -> HTTP 404
```

So the right statement is not that a native implementation is impossible. It is that the exact BOOZ optimized Gram-finding program and the order-13 8321-candidate output list are not currently public at the cited URLs I checked. Recreating them means implementing the algorithm ourselves.

## Stuck-run fix

`gram_proof_pipeline.py` now writes incremental progress:

- `outputs/supplied_gram_progress.json` after each supplied Gram.
- `outputs/supplied_gram_verification.json` after a supplied-Gram run completes.
- `outputs/candidate_minor_profile.json` after the bounded generator profiler completes.
- `outputs/summary.json` for the latest run summary.

It also supports:

```bash
--verify-limit N
--max-decompose-nodes N
--skip-profiler
--output-dir PATH
```

This makes future long runs interruptible and inspectable.

## Supplied high-tail Gram verification

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python gram_proof_pipeline.py --max-decompose-nodes 0 --skip-profiler --output-dir outputs/supplied_source_verification
```

Result:

- Available unique high-tail Grams from sprint 3 witnesses: 130.
- Requested Grams: 130.
- Candidate-Gram validation passed: 130 / 130.
- Distinct recovered normalized determinants: 130 / 130.
- Source decomposition verified: 130 / 130.

This verifies that the sprint-3 high-tail witnesses induce valid BOOZ-style candidate Grams and directly decompose those Grams. This is still not a gap proof, because it only checks Grams supplied by witnesses.

## Independent backtracking decomposer progress

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python gram_proof_pipeline.py --verify-limit 20 --max-decompose-nodes 200000 --skip-profiler
```

Result:

- Requested Grams: 20.
- Candidate-Gram validation passed: 20 / 20.
- Independent generic decomposer hit the 200000-node cap on all 20.
- Total decomposition nodes: 4000000.
- Elapsed time: about 6.36 seconds.

Interpretation: candidate-Gram validation is cheap, but the generic decomposer needs better ordering, frame variables, Gram-pair constraints, or direct certificate input. BOOZ's decomposition method is more specialized than the simple row-word backtracker here.

## Bounded Gram-generation profiler

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python gram_proof_pipeline.py --verify-limit 0 --max-generated 20000 --max-depth 8
```

Result:

- Order: 13.
- Orrick/BOOZ Phi entries used: {-11, -7, -3, 1}.
- Total candidate principal minors tested before cap: 20033.
- Final frontier size at cap: 1441.
- Stopped by cap: yes.
- Deepest completed level: 5.

Level summary:

| Level | Tested | Accepted/frontier | Pruned PD | Pruned bound |
| --- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 4 | 4 | 0 | 0 |
| 3 | 64 | 26 | 20 | 18 |
| 4 | 1664 | 385 | 894 | 385 |
| 5 | 18300 | 1441 | 14409 | 2450 |

Interpretation: even with the canonical Phi entry set, a naive principal-minor generator grows quickly. A full proof-grade generator needs BOOZ/Orrick's allowable-vector lists, lexicographic maximality/canonical block logic, and enhanced Kounias-Moyssiadis pruning.

## What remains for a full proof

A full order-13 gap proof still needs either:

1. The original BOOZ Gram-finding source or their 8321 order-13 candidate-Gram list, neither of which was found at the public URLs checked; or
2. A new implementation of the BOOZ/Orrick Gram-finding algorithm, preferably in C/C++/Rust with GMP or another exact integer backend.

The next sprint should be a native candidate-Gram generator sprint. It should focus only on implementing the Orrick algorithm: Phi/admissible vectors, allowable gamma vectors, lexicographic maximality, determinant-bound pruning, and checkpointed output.
