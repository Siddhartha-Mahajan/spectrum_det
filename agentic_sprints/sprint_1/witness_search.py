#!/usr/bin/env python3
"""Witness-generation experiment for the order-8 determinant spectrum.

This script searches 7 x 7 (0,1) blocks. After sign normalization, the
absolute determinant of such a block is the normalized determinant of the
corresponding 8 x 8 {-1,1} matrix.
"""

from __future__ import annotations

import argparse
import json
import random
import time
from pathlib import Path


KNOWN_SPECTRA = {
    8: set(range(19)) | {20, 24, 32},
}


def det_bareiss(matrix: list[list[int]]) -> int:
    """Return the exact determinant of a square integer matrix."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = k
        while pivot < n and a[pivot][k] == 0:
            pivot += 1
        if pivot == n:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[n - 1][n - 1]


def hadamard(order: int) -> list[list[int]]:
    if order == 1:
        return [[1]]
    half = hadamard(order // 2)
    top = [row + row for row in half]
    bottom = [row + [-value for value in row] for row in half]
    return top + bottom


def normalize_sign_matrix(matrix: list[list[int]]) -> list[list[int]]:
    normalized = [row[:] for row in matrix]
    n = len(normalized)
    for i in range(n):
        if normalized[i][0] == -1:
            normalized[i] = [-value for value in normalized[i]]
    for j in range(n):
        if normalized[0][j] == -1:
            for i in range(n):
                normalized[i][j] *= -1
    return normalized


def sign_matrix_to_block01(matrix: list[list[int]]) -> list[list[int]]:
    normalized = normalize_sign_matrix(matrix)
    return [[1 if value == -1 else 0 for value in row[1:]] for row in normalized[1:]]


def block01_to_sign_matrix(block: list[list[int]]) -> list[list[int]]:
    m = len(block)
    matrix = [[1 for _ in range(m + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(m):
            matrix[i + 1][j + 1] = -1 if block[i][j] else 1
    return matrix


def random_block(size: int, rng: random.Random) -> list[list[int]]:
    return [[rng.randrange(2) for _ in range(size)] for _ in range(size)]


def normalized_value_from_block(block: list[list[int]]) -> int:
    return abs(det_bareiss(block))


def add_witness(witnesses: dict[int, list[list[int]]], block: list[list[int]]) -> int:
    value = normalized_value_from_block(block)
    witnesses.setdefault(value, [row[:] for row in block])
    return value


def local_search_target(
    size: int,
    target: int,
    rng: random.Random,
    restarts: int,
    steps: int,
) -> tuple[list[list[int]] | None, dict[str, int]]:
    best_distance = 10**9
    best_value = -1
    evaluations = 0

    for _ in range(restarts):
        block = random_block(size, rng)
        value = normalized_value_from_block(block)
        evaluations += 1
        distance = abs(value - target)
        if distance < best_distance:
            best_distance = distance
            best_value = value
        if value == target:
            return block, {"evaluations": evaluations, "best_distance": 0, "best_value": value}

        for step in range(steps):
            i = rng.randrange(size)
            j = rng.randrange(size)
            block[i][j] ^= 1
            candidate_value = normalized_value_from_block(block)
            evaluations += 1
            candidate_distance = abs(candidate_value - target)
            temperature_accept = step < steps // 3 and rng.random() < 0.015
            if candidate_distance <= distance or temperature_accept:
                value = candidate_value
                distance = candidate_distance
            else:
                block[i][j] ^= 1
            if distance < best_distance:
                best_distance = distance
                best_value = value
            if value == target:
                return block, {"evaluations": evaluations, "best_distance": 0, "best_value": value}

    return None, {"evaluations": evaluations, "best_distance": best_distance, "best_value": best_value}


def verify_witnesses(order: int, witnesses: dict[int, list[list[int]]]) -> dict[int, bool]:
    factor = 1 << (order - 1)
    verified = {}
    for value, block in witnesses.items():
        sign_matrix = block01_to_sign_matrix(block)
        sign_det = abs(det_bareiss(sign_matrix))
        block_det = abs(det_bareiss(block))
        verified[value] = block_det == value and sign_det == factor * value
    return verified


def run_experiment(order: int, samples: int, restarts: int, steps: int, seed: int, output_dir: Path) -> dict[str, object]:
    if order not in KNOWN_SPECTRA:
        raise ValueError(f"No known spectrum configured for order {order}")

    rng = random.Random(seed)
    size = order - 1
    known = KNOWN_SPECTRA[order]
    witnesses: dict[int, list[list[int]]] = {}
    target_stats: dict[str, dict[str, int | bool]] = {}

    if order == 8:
        add_witness(witnesses, sign_matrix_to_block01(hadamard(8)))

    start = time.perf_counter()
    samples_evaluated = 0
    for _ in range(samples):
        add_witness(witnesses, random_block(size, rng))
        samples_evaluated += 1
        if known.issubset(witnesses):
            break

    after_sampling = sorted(known & witnesses.keys())
    missing_after_sampling = sorted(known - witnesses.keys())

    for target in missing_after_sampling:
        block, stats = local_search_target(size, target, rng, restarts, steps)
        stats["found"] = block is not None
        if block is not None:
            add_witness(witnesses, block)
        target_stats[str(target)] = stats

    elapsed = time.perf_counter() - start
    verified = verify_witnesses(order, {value: witnesses[value] for value in known & witnesses.keys()})
    found_known = sorted(known & witnesses.keys())
    missing_known = sorted(known - witnesses.keys())

    output_dir.mkdir(parents=True, exist_ok=True)
    witness_payload = {
        str(value): {
            "normalized_value": value,
            "block01": witnesses[value],
            "sign_matrix": block01_to_sign_matrix(witnesses[value]),
        }
        for value in found_known
    }
    (output_dir / f"n{order}_witnesses.json").write_text(json.dumps(witness_payload, indent=2) + "\n")

    result = {
        "order": order,
        "seed": seed,
        "samples_requested": samples,
        "samples_evaluated": samples_evaluated,
        "restarts_per_missing_target": restarts,
        "steps_per_restart": steps,
        "known_spectrum": sorted(known),
        "found_known_values": found_known,
        "missing_known_values": missing_known,
        "extra_values_seen": sorted(set(witnesses) - known),
        "found_after_sampling": after_sampling,
        "missing_after_sampling": missing_after_sampling,
        "target_search_stats": target_stats,
        "verified": {str(value): verified[value] for value in sorted(verified)},
        "all_reported_witnesses_verified": all(verified.values()),
        "elapsed_seconds": elapsed,
    }
    (output_dir / f"n{order}_results.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--samples", type=int, default=120_000)
    parser.add_argument("--restarts", type=int, default=80)
    parser.add_argument("--steps", type=int, default=1_200)
    parser.add_argument("--seed", type=int, default=20260512)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    result = run_experiment(args.n, args.samples, args.restarts, args.steps, args.seed, args.output_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
