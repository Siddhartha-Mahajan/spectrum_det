# Sprint 5: native Orrick/BOOZ candidate-Gram generator

Date: 2026-05-12

## Strategy

Try one strategy: implement the candidate-Gram generator ourselves in a native language.

This sprint focuses only on the Gram-finding layer of the BOOZ order-13 proof. It does not do witness search and does not do fixed-Gram decomposition.

## Why native code

The Python profiler in sprint 4 showed that candidate principal-minor generation grows quickly. BOOZ says their programs were written in C and used GMP. This sprint starts a C++ implementation using exact integer arithmetic with `__int128`, which is sufficient for order 13 determinant comparisons in this prototype.

## Implemented algorithm pieces

`native_gram_generator.cpp` implements:

- odd-order canonical entry set `Phi`:
  - for n = 13, `Phi = {-11, -7, -3, 1}`;
- recursive construction from `M_1 = [n]`;
- Orrick-style `F` lists of accepted admissible vectors;
- `Gamma`/allowable-vector scanning from `F_{r-2}` plus two appended entries;
- positive-definiteness pruning using exact leading determinant signs;
- Kounias-Moyssiadis bound (BOOZ Theorem 1 equation 7) with `c = 1`;
- full-depth square determinant and threshold checks;
- JSON progress checkpointing;
- JSONL candidate output.

## Not implemented yet

This first native version does not yet implement:

- Orrick's full `IsLexMax` canonical block test;
- dynamic `e_r` block-start logic from Orrick's notes;
- BOOZ's Gram-equivalence canonicalization;
- enhanced n congruent 3 mod 4 bound, which is not relevant for n = 13 anyway;
- GMP or arbitrary precision beyond `__int128`.

Because canonicalization is incomplete, this generator is a prototype toward a full proof generator, not a finished replacement for BOOZ's 8321-class enumeration.

## Build

```bash
make
```

Equivalent direct command:

```bash
clang++ -O3 -std=c++17 native_gram_generator.cpp -o native_gram_generator
```

## Run

Bounded smoke run:

```bash
./native_gram_generator --order 13 --threshold-normalized 2173 --max-nodes 200000 --progress-every 25000 --output-dir outputs/smoke
```

Deeper bounded run:

```bash
./native_gram_generator --order 13 --threshold-normalized 2173 --max-nodes 5000000 --progress-every 100000 --output-dir outputs/deeper
```

## Success criteria

A useful sprint 5 run should:

- compile cleanly;
- produce progress JSON while running;
- reach deeper than the sprint-4 Python profiler under similar caps;
- report candidate/full-depth counts honestly;
- identify which missing BOOZ/Orrick pieces are needed next for proof-grade enumeration.
