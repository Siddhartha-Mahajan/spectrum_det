#!/usr/bin/env python3
"""Witness baseline for the conjectured n=12 determinant spectrum.

After normalizing the first row and column of a 12 x 12 sign matrix to +1,
the lower-right 11 x 11 (0,1) block has determinant equal to the normalized
sign determinant.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

import numpy as np


Matrix = list[list[int]]


def det_bareiss(matrix: Matrix) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    working = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = column
        while pivot < size and working[pivot][column] == 0:
            pivot += 1
        if pivot == size:
            return 0
        if pivot != column:
            working[column], working[pivot] = working[pivot], working[column]
            sign = -sign
        pivot_value = working[column][column]
        for row_index in range(column + 1, size):
            for col_index in range(column + 1, size):
                working[row_index][col_index] = (
                    working[row_index][col_index] * pivot_value
                    - working[row_index][column] * working[column][col_index]
                ) // previous
        previous = pivot_value
        for row_index in range(column + 1, size):
            working[row_index][column] = 0
        for col_index in range(column + 1, size):
            working[column][col_index] = 0
    return sign * working[size - 1][size - 1]


def fast_abs_det(block: np.ndarray) -> int:
    return abs(int(round(float(np.linalg.det(block)))))


def exact_abs_det(block: np.ndarray) -> int:
    return abs(det_bareiss(block.astype(int).tolist()))


def parse_spectrum12(path: Path) -> set[int]:
    text = path.read_text()
    data = text.split("Conjectured spectrum for n=12", 1)[1].split("Back to", 1)[0]
    values: set[int] = set()
    for start, end in re.findall(r"\[(\d+),\s*(\d+)\]", data):
        values.update(range(int(start), int(end) + 1))
    data_without_ranges = re.sub(r"\[\d+,\s*\d+\]", " ", data)
    for token in data_without_ranges.split():
        if token.isdigit():
            values.add(int(token))
    return values


def block01_to_sign_matrix(block: Matrix) -> Matrix:
    size = len(block)
    matrix = [[1 for _ in range(size + 1)] for _ in range(size + 1)]
    for row_index, row in enumerate(block):
        for col_index, value in enumerate(row):
            matrix[row_index + 1][col_index + 1] = -1 if value else 1
    return matrix


def sign_matrix_to_block01(matrix: Matrix) -> Matrix:
    return [[1 if value == -1 else 0 for value in row[1:]] for row in matrix[1:]]


def paley_hadamard_12() -> Matrix:
    q = 11
    residues = {(x * x) % q for x in range(1, q)}
    core: Matrix = []
    for i in range(q):
        row = []
        for j in range(q):
            if i == j:
                row.append(-1)
            else:
                row.append(1 if ((i - j) % q) in residues else -1)
        core.append(row)
    return [[1] * (q + 1)] + [[1] + row for row in core]


def add_witness(
    witnesses: dict[int, Matrix],
    block: np.ndarray,
    allowed: set[int] | None = None,
) -> int:
    exact_value = exact_abs_det(block)
    if allowed is None or exact_value in allowed:
        witnesses.setdefault(exact_value, block.astype(int).tolist())
    return exact_value


def target_search(
    target: int,
    size: int,
    rng: np.random.Generator,
    restarts: int,
    steps: int,
    kicks: int,
) -> tuple[np.ndarray | None, dict[str, int | bool]]:
    best_distance = 10**9
    best_value = -1
    evaluations = 0

    for restart in range(restarts):
        block = rng.integers(0, 2, size=(size, size), dtype=np.int8)
        value = fast_abs_det(block)
        evaluations += 1
        distance = abs(value - target)
        if distance < best_distance:
            best_distance = distance
            best_value = value
        if value == target and exact_abs_det(block) == target:
            return block, {
                "found": True,
                "restart": restart,
                "step": 0,
                "evaluations": evaluations,
                "best_distance": 0,
                "best_value": target,
            }

        for step in range(1, steps + 1):
            best_position = None
            best_candidate_value = value
            best_candidate_distance = distance

            for row_index in range(size):
                for col_index in range(size):
                    block[row_index, col_index] ^= 1
                    candidate_value = fast_abs_det(block)
                    evaluations += 1
                    candidate_distance = abs(candidate_value - target)
                    block[row_index, col_index] ^= 1
                    if candidate_distance < best_candidate_distance:
                        best_candidate_distance = candidate_distance
                        best_candidate_value = candidate_value
                        best_position = (row_index, col_index)

            if best_position is None:
                for _ in range(kicks):
                    row_index = int(rng.integers(0, size))
                    col_index = int(rng.integers(0, size))
                    block[row_index, col_index] ^= 1
                value = fast_abs_det(block)
                evaluations += 1
                distance = abs(value - target)
            else:
                row_index, col_index = best_position
                block[row_index, col_index] ^= 1
                value = best_candidate_value
                distance = best_candidate_distance

            if distance < best_distance:
                best_distance = distance
                best_value = value
            if value == target and exact_abs_det(block) == target:
                return block, {
                    "found": True,
                    "restart": restart,
                    "step": step,
                    "evaluations": evaluations,
                    "best_distance": 0,
                    "best_value": target,
                }

    return None, {
        "found": False,
        "restart": restarts,
        "step": steps,
        "evaluations": evaluations,
        "best_distance": best_distance,
        "best_value": best_value,
    }


def verify_witnesses(witnesses: dict[int, Matrix]) -> dict[str, bool]:
    verified = {}
    for value, block in witnesses.items():
        block_det = abs(det_bareiss(block))
        sign_matrix = block01_to_sign_matrix(block)
        sign_det = abs(det_bareiss(sign_matrix))
        verified[str(value)] = block_det == value and sign_det == (1 << 11) * value
    return verified


def compress_ranges(values: list[int]) -> list[str]:
    if not values:
        return []
    ranges = []
    start = previous = values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
            continue
        ranges.append(str(start) if start == previous else f"[{start},{previous}]")
        start = previous = value
    ranges.append(str(start) if start == previous else f"[{start},{previous}]")
    return ranges


def run(args: argparse.Namespace) -> dict[str, Any]:
    sprint_dir = Path(__file__).resolve().parent
    root = sprint_dir.parents[1]
    targets = parse_spectrum12(root / "web_sources" / "mds" / "spectrum12_conjectured.md")
    tail_targets = sorted(value for value in targets if value > args.tail_threshold)
    rng = np.random.default_rng(args.seed)
    witnesses: dict[int, Matrix] = {}
    all_seen: set[int] = set()
    target_stats: dict[str, dict[str, int | bool]] = {}

    start = time.perf_counter()

    hadamard_block = np.array(sign_matrix_to_block01(paley_hadamard_12()), dtype=np.int8)
    add_witness(witnesses, hadamard_block, targets)
    all_seen.add(exact_abs_det(hadamard_block))

    for _ in range(args.random_samples):
        block = rng.integers(0, 2, size=(11, 11), dtype=np.int8)
        value = add_witness(witnesses, block, targets)
        all_seen.add(value)

    missing_tail_after_sampling = [value for value in tail_targets if value not in witnesses]
    for target in missing_tail_after_sampling:
        block, stats = target_search(target, 11, rng, args.target_restarts, args.target_steps, args.kicks)
        target_stats[str(target)] = stats
        if block is not None:
            value = add_witness(witnesses, block, targets)
            all_seen.add(value)

    found_targets = sorted(set(witnesses) & targets)
    found_tail = sorted(value for value in found_targets if value > args.tail_threshold)
    missing_tail = sorted(set(tail_targets) - set(found_tail))
    contradiction_candidates = sorted(value for value in all_seen if value not in targets)
    verified = verify_witnesses({value: witnesses[value] for value in found_targets})
    elapsed = time.perf_counter() - start

    output_dir = sprint_dir / "outputs"
    output_dir.mkdir(exist_ok=True)
    witness_payload = {
        str(value): {
            "normalized_value": value,
            "block01": witnesses[value],
            "sign_matrix": block01_to_sign_matrix(witnesses[value]),
        }
        for value in found_targets
    }
    (output_dir / "n12_witnesses.json").write_text(json.dumps(witness_payload, indent=2) + "\n")

    result = {
        "seed": args.seed,
        "conjectured_spectrum_size": len(targets),
        "tail_threshold": args.tail_threshold,
        "tail_target_count": len(tail_targets),
        "random_samples": args.random_samples,
        "target_restarts": args.target_restarts,
        "target_steps": args.target_steps,
        "kicks": args.kicks,
        "found_target_count": len(found_targets),
        "found_tail_count": len(found_tail),
        "missing_tail_count": len(missing_tail),
        "found_target_values": found_targets,
        "found_tail_values": found_tail,
        "missing_tail_values": missing_tail,
        "found_target_ranges_preview": compress_ranges(found_targets)[:80],
        "found_tail_ranges": compress_ranges(found_tail),
        "missing_tail_ranges": compress_ranges(missing_tail),
        "contradiction_candidate_count": len(contradiction_candidates),
        "contradiction_candidates": contradiction_candidates,
        "target_search_stats": target_stats,
        "verified": {str(value): verified[str(value)] for value in found_targets},
        "all_reported_witnesses_verified": all(verified.values()),
        "elapsed_seconds": elapsed,
    }
    (output_dir / "n12_results.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260521)
    parser.add_argument("--random-samples", type=int, default=100000)
    parser.add_argument("--target-restarts", type=int, default=35)
    parser.add_argument("--target-steps", type=int, default=160)
    parser.add_argument("--kicks", type=int, default=4)
    parser.add_argument("--tail-threshold", type=int, default=738)
    return parser.parse_args()


def main() -> None:
    result = run(parse_args())
    print(json.dumps({
        "found_target_count": result["found_target_count"],
        "found_tail_count": result["found_tail_count"],
        "missing_tail_count": result["missing_tail_count"],
        "contradiction_candidate_count": result["contradiction_candidate_count"],
        "all_reported_witnesses_verified": result["all_reported_witnesses_verified"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
