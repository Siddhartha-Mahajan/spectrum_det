#!/usr/bin/env python3
"""Order-13 witness-side replication experiment.

Searches 12 x 12 (0,1) matrices. By the standard normalization, each exact
absolute determinant is a normalized determinant value for a 13 x 13 {-1,1}
matrix with first row and column normalized.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

import numpy as np


def det_bareiss(matrix: list[list[int]]) -> int:
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


def fast_abs_det(block: np.ndarray) -> int:
    return abs(int(round(float(np.linalg.det(block)))))


def exact_abs_det(block: np.ndarray) -> int:
    return abs(det_bareiss(block.astype(int).tolist()))


def block01_to_sign_matrix(block: list[list[int]]) -> list[list[int]]:
    size = len(block)
    matrix = [[1 for _ in range(size + 1)] for _ in range(size + 1)]
    for i, row in enumerate(block):
        for j, value in enumerate(row):
            matrix[i + 1][j + 1] = -1 if value else 1
    return matrix


def parse_spectrum13(path: Path) -> set[int]:
    text = path.read_text()
    data = text.split("Spectrum for n=13", 1)[1].split("Back to", 1)[0]
    values: set[int] = set()
    for start, end in re.findall(r"\[(\d+),\s*(\d+)\]", data):
        values.update(range(int(start), int(end) + 1))
    data_without_ranges = re.sub(r"\[\d+,\s*\d+\]", " ", data)
    for token in data_without_ranges.split():
        if token.isdigit():
            values.add(int(token))
    return values


def add_witness(witnesses: dict[int, list[list[int]]], block: np.ndarray, allowed: set[int] | None = None) -> int:
    value = exact_abs_det(block)
    if allowed is None or value in allowed:
        witnesses.setdefault(value, block.astype(int).tolist())
    return value


def random_sampling(size: int, samples: int, rng: np.random.Generator, targets: set[int]) -> tuple[dict[int, list[list[int]]], int]:
    witnesses: dict[int, list[list[int]]] = {}
    for _ in range(samples):
        block = rng.integers(0, 2, size=(size, size), dtype=np.int8)
        value = fast_abs_det(block)
        if value in targets:
            add_witness(witnesses, block, targets)
    return witnesses, samples


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

            for i in range(size):
                for j in range(size):
                    block[i, j] ^= 1
                    candidate_value = fast_abs_det(block)
                    evaluations += 1
                    candidate_distance = abs(candidate_value - target)
                    block[i, j] ^= 1
                    if candidate_distance < best_candidate_distance:
                        best_candidate_distance = candidate_distance
                        best_candidate_value = candidate_value
                        best_position = (i, j)

            if best_position is None:
                for _ in range(kicks):
                    i = int(rng.integers(0, size))
                    j = int(rng.integers(0, size))
                    block[i, j] ^= 1
                value = fast_abs_det(block)
                evaluations += 1
                distance = abs(value - target)
            else:
                i, j = best_position
                block[i, j] ^= 1
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


def verify_witnesses(witnesses: dict[int, list[list[int]]]) -> dict[str, bool]:
    verified = {}
    for value, block in witnesses.items():
        exact_value = abs(det_bareiss(block))
        sign_matrix = block01_to_sign_matrix(block)
        sign_det = abs(det_bareiss(sign_matrix))
        verified[str(value)] = exact_value == value and sign_det == (1 << 12) * value
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


def run(args: argparse.Namespace) -> dict[str, object]:
    root = Path(__file__).resolve().parents[2]
    spectrum_path = root / "web_sources" / "mds" / "spectrum13_complete.md"
    targets = parse_spectrum13(spectrum_path)
    low_interval = set(range(2173))
    high_tail = sorted(targets - low_interval)
    rng = np.random.default_rng(args.seed)
    start = time.perf_counter()

    witnesses, samples_evaluated = random_sampling(12, args.random_samples, rng, targets)
    found_after_sampling = set(witnesses)

    target_stats: dict[str, dict[str, int | bool]] = {}
    for target in high_tail:
        if target in witnesses:
            continue
        block, stats = target_search(target, 12, rng, args.target_restarts, args.target_steps, args.kicks)
        target_stats[str(target)] = stats
        if block is not None:
            add_witness(witnesses, block, targets)

    negative_controls: dict[str, dict[str, int | bool]] = {}
    for target in args.negative_controls:
        block, stats = target_search(target, 12, rng, args.gap_restarts, args.target_steps, args.kicks)
        if block is not None:
            add_witness(witnesses, block, None)
        negative_controls[str(target)] = stats

    verified = verify_witnesses({value: witnesses[value] for value in witnesses if value in targets})
    elapsed = time.perf_counter() - start
    found_targets = sorted(set(witnesses) & targets)
    found_high_tail = sorted(set(witnesses) & set(high_tail))
    missed_high_tail = sorted(set(high_tail) - set(found_high_tail))

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    witness_payload = {
        str(value): {
            "normalized_value": value,
            "block01": witnesses[value],
        }
        for value in found_targets
    }
    (output_dir / "n13_witnesses.json").write_text(json.dumps(witness_payload, indent=2) + "\n")

    result = {
        "seed": args.seed,
        "spectrum_size": len(targets),
        "low_interval_size": len(low_interval),
        "high_tail_size": len(high_tail),
        "first_gap_after_low_interval": min(set(range(max(targets) + 1)) - targets),
        "random_samples_requested": args.random_samples,
        "random_samples_evaluated": samples_evaluated,
        "found_target_count": len(found_targets),
        "found_low_count": len(set(found_targets) & low_interval),
        "found_high_tail_count": len(found_high_tail),
        "missed_high_tail_count": len(missed_high_tail),
        "found_after_sampling_count": len(found_after_sampling),
        "found_after_sampling_low_count": len(found_after_sampling & low_interval),
        "found_after_sampling_high_count": len(found_after_sampling & set(high_tail)),
        "found_high_tail_values": found_high_tail,
        "missed_high_tail_values": missed_high_tail,
        "found_low_ranges_preview": compress_ranges(sorted(set(found_targets) & low_interval))[:40],
        "target_search_stats": target_stats,
        "negative_controls": negative_controls,
        "all_target_witnesses_verified": all(verified.values()),
        "verified_count": len(verified),
        "elapsed_seconds": elapsed,
    }
    (output_dir / "n13_results.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--random-samples", type=int, default=200_000)
    parser.add_argument("--target-restarts", type=int, default=80)
    parser.add_argument("--gap-restarts", type=int, default=80)
    parser.add_argument("--target-steps", type=int, default=220)
    parser.add_argument("--kicks", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20260512)
    parser.add_argument("--negative-controls", type=int, nargs="*", default=[2173])
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    result = run(args)
    compact = {
        "found_target_count": result["found_target_count"],
        "found_low_count": result["found_low_count"],
        "found_high_tail_count": result["found_high_tail_count"],
        "missed_high_tail_count": result["missed_high_tail_count"],
        "negative_controls": result["negative_controls"],
        "all_target_witnesses_verified": result["all_target_witnesses_verified"],
        "elapsed_seconds": result["elapsed_seconds"],
    }
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
