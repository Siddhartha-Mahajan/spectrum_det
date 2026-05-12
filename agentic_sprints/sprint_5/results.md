# Sprint 5 results: native Orrick/BOOZ candidate-Gram generator

Date: 2026-05-12

Status: implemented and smoke-tested.

Artifacts:

- `native_gram_generator.cpp`
- `Makefile`
- `outputs/km_200k/progress.json`
- `outputs/km_200k/candidates.jsonl`

## Build

Command:

```bash
make
```

Result: clean build with Apple clang/C++ in C++17 mode.

## Main bounded run

Command:

```bash
./native_gram_generator --order 13 --threshold-normalized 2173 --max-nodes 200000 --progress-every 25000 --output-dir outputs/km_200k
```

Summary from `outputs/km_200k/progress.json`:

- nodes tested: 200000
- recursion calls: 5659
- maximum depth reached: 13
- stopped by cap: true
- elapsed time: about 85.6 seconds
- high-threshold candidate Grams written: 0
- candidate output file lines: 0

Level summary:

| level | tested | accepted | pruned PD | pruned KM-bound |
| --- | ---: | ---: | ---: | ---: |
| 2 | 3 | 2 | 0 | 1 |
| 3 | 12 | 5 | 3 | 4 |
| 4 | 60 | 12 | 24 | 24 |
| 5 | 204 | 27 | 79 | 98 |
| 6 | 612 | 81 | 222 | 309 |
| 7 | 2216 | 296 | 763 | 1157 |
| 8 | 11144 | 936 | 3868 | 6340 |
| 9 | 47920 | 1838 | 16696 | 29386 |
| 10 | 88605 | 1053 | 28380 | 59172 |
| 11 | 27084 | 1183 | 7816 | 18085 |
| 12 | 20476 | 225 | 5753 | 14498 |
| 13 | 1664 | 0 | 443 | 0 |

At full depth, the bounded run tested 1664 leaves. Of those, 443 failed positive definiteness, 1213 had nonsquare Gram determinant or failed divisibility, and 8 square/divisible determinants were below the normalized threshold 2173.

## Interpretation

The sprint now has a working native Orrick/BOOZ-style generator prototype with checkpointed progress. It implements the main admissible-vector and allowable-vector recursion structure and the Kounias-Moyssiadis upper-bound prune.

This is not yet a proof-grade reproduction of the BOOZ order-13 enumeration. The run did not enumerate all candidate Gram equivalence classes, and it did not reproduce the 8321 BOOZ candidates. The missing proof-critical pieces are still Orrick's full `IsLexMax` block canonicalization, dynamic block `e_r` logic, and a stronger/faster exact implementation of the allowable-vector bound.

## Implementation note

An initial smoke version passed only the current accepted vector down each branch. That made the search tree unrealistically tiny. The corrected version accumulates accepted sibling admissible vectors in the current recursive context before recursing, matching the intended `F_r` list behavior more closely.
