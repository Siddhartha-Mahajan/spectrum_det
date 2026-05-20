#!/usr/bin/env python3
"""Trace known order-13 witness Grams through the patched sprint-6 generator.

This is not a full generator. It follows one canonical witness path and, at
each prefix, enumerates the same sibling candidate vectors that the C++ search
would enumerate at that frame. That is enough to distinguish a live
F/Gamma/bound rejection from an unfinished long run.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from pathlib import Path
from typing import Any

Matrix = list[list[int]]
Vec = list[int]


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


def block01_to_sign_matrix(block: Matrix) -> Matrix:
    size = len(block)
    matrix = [[1 for _ in range(size + 1)] for _ in range(size + 1)]
    for row_index, row in enumerate(block):
        for col_index, value in enumerate(row):
            matrix[row_index + 1][col_index + 1] = -1 if value else 1
    return matrix


def parity_normalize_odd(matrix: Matrix) -> Matrix:
    normalized = [row[:] for row in matrix]
    size = len(normalized)
    for row_index in range(size):
        negative_count = sum(1 for value in normalized[row_index] if value < 0)
        if negative_count % 2 == 0:
            normalized[row_index] = [-value for value in normalized[row_index]]
    for col_index in range(size):
        negative_count = sum(1 for row_index in range(size) if normalized[row_index][col_index] < 0)
        if negative_count % 2 == 0:
            for row_index in range(size):
                normalized[row_index][col_index] *= -1
    return normalized


def gram_matrix(sign_matrix: Matrix) -> Matrix:
    size = len(sign_matrix)
    return [
        [
            sum(
                sign_matrix[row_index][column] * sign_matrix[col_index][column]
                for column in range(size)
            )
            for col_index in range(size)
        ]
        for row_index in range(size)
    ]


def positive_mod(value: int, modulus: int) -> int:
    result = value % modulus
    return result if result >= 0 else result + modulus


def phi_congruent(order: int) -> list[int]:
    values = [value for value in range(1 - order, order) if positive_mod(value - order, 4) == 0]
    return sorted(values, key=lambda value: (abs(value), value))


def allowed_values(phi: list[int], emax: int) -> list[int]:
    return [value for value in phi if abs(value) <= emax]


def compare_vectors_abs(left: Vec, right: Vec) -> int:
    shared = min(len(left), len(right))
    for index in range(shared):
        left_abs = abs(left[index])
        right_abs = abs(right[index])
        if left_abs < right_abs:
            return -1
        if left_abs > right_abs:
            return 1
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1
    return 0


def vector_sort_key(vector: Vec) -> tuple[int, ...]:
    return tuple(abs(value) for value in vector)


def append_vectors_from_prefixes(prefixes: list[Vec], values: list[int]) -> list[Vec]:
    out: list[Vec] = []
    for prefix in prefixes:
        for value in values:
            out.append(prefix + [value])
    return sorted(out, key=vector_sort_key)


def partial_row(matrix: Matrix, row_index: int, length: int) -> Vec:
    return matrix[row_index][:length]


def compare_matrices_abs_lex(left: Matrix, right: Matrix) -> int:
    shared = min(len(left), len(right))
    for row_index in range(1, shared):
        comparison = compare_vectors_abs(
            partial_row(left, row_index, row_index),
            partial_row(right, row_index, row_index),
        )
        if comparison != 0:
            return comparison
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1
    return 0


def is_row_lex_ordered(matrix: Matrix) -> bool:
    size = len(matrix)
    for earlier in range(size - 1):
        for later in range(earlier + 1, size):
            earlier_prefix = partial_row(matrix, earlier, earlier + 1)
            later_prefix = partial_row(matrix, later, earlier + 1)
            if compare_vectors_abs(earlier_prefix, later_prefix) <= 0:
                return False
    return True


def extend_matrix(matrix: Matrix, vector: Vec, order: int) -> Matrix:
    size = len(matrix)
    candidate = [[order for _ in range(size + 1)] for _ in range(size + 1)]
    for row_index in range(size):
        for col_index in range(size):
            candidate[row_index][col_index] = matrix[row_index][col_index]
    for row_index in range(size):
        candidate[row_index][size] = vector[row_index]
        candidate[size][row_index] = vector[row_index]
    return candidate


def augment_with_gamma(matrix: Matrix, gamma: Vec, c_value: int) -> Matrix:
    size = len(matrix)
    augmented = [[c_value for _ in range(size + 1)] for _ in range(size + 1)]
    for row_index in range(size):
        for col_index in range(size):
            augmented[row_index][col_index] = matrix[row_index][col_index]
    for row_index in range(size):
        augmented[row_index][size] = gamma[row_index]
        augmented[size][row_index] = gamma[row_index]
    return augmented


def compute_blocks(matrix: Matrix, minimal: int) -> tuple[list[tuple[int, int]], bool]:
    size = len(matrix)
    parent = list(range(size))

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for row_index in range(size):
        for col_index in range(row_index + 1, size):
            if matrix[row_index][col_index] != minimal:
                union(row_index, col_index)

    groups_by_root: dict[int, list[int]] = {}
    for index in range(size):
        groups_by_root.setdefault(find(index), []).append(index)

    intervals: list[tuple[int, int]] = []
    contiguous = True
    for group in sorted(groups_by_root.values(), key=lambda values: values[0]):
        start = group[0]
        end = group[-1]
        if end - start + 1 != len(group):
            contiguous = False
        intervals.append((start, end))
    return intervals, contiguous


def submatrix_interval(matrix: Matrix, start: int, end: int) -> Matrix:
    return [row[start : end + 1] for row in matrix[start : end + 1]]


def blocks_descending(matrix: Matrix, intervals: list[tuple[int, int]]) -> bool:
    for index in range(1, len(intervals)):
        previous_start, previous_end = intervals[index - 1]
        current_start, current_end = intervals[index]
        previous_block = submatrix_interval(matrix, previous_start, previous_end)
        current_block = submatrix_interval(matrix, current_start, current_end)
        if compare_matrices_abs_lex(previous_block, current_block) < 0:
            return False
    return True


def leading_signature(block: Matrix, permutation: Vec, leading_size: int) -> Vec:
    signature: Vec = []
    for row_index in range(1, leading_size):
        for col_index in range(row_index):
            signature.append(block[permutation[row_index]][permutation[col_index]])
    return signature


def make_pair_permutation(size: int, first: int, second: int) -> Vec:
    return [first, second] + [item for item in range(size) if item != first and item != second]


def is_identity(permutation: Vec) -> bool:
    return all(index == value for index, value in enumerate(permutation))


def is_lexmax_block(block: Matrix, permutation_cap: int) -> tuple[int, int]:
    size = len(block)
    if size <= 1:
        return 1, 1

    current: set[tuple[int, ...]] = set()
    best_signature: Vec | None = None
    for first in range(size):
        for second in range(size):
            if first == second:
                continue
            permutation = make_pair_permutation(size, first, second)
            signature = leading_signature(block, permutation, 2)
            comparison = 1 if best_signature is None else compare_vectors_abs(signature, best_signature)
            if best_signature is None or comparison > 0:
                current.clear()
                best_signature = signature
            if comparison >= 0:
                current.add(tuple(permutation))
    seen = len(current)
    if not any(is_identity(list(permutation)) for permutation in current):
        return 0, seen

    for leading_size in range(3, size + 1):
        next_set: set[tuple[int, ...]] = set()
        best_signature = None
        for permutation_tuple in current:
            permutation = list(permutation_tuple)
            for swap_position in range(leading_size - 1, size):
                candidate = permutation[:]
                candidate[leading_size - 1], candidate[swap_position] = (
                    candidate[swap_position],
                    candidate[leading_size - 1],
                )
                signature = leading_signature(block, candidate, leading_size)
                comparison = 1 if best_signature is None else compare_vectors_abs(signature, best_signature)
                if best_signature is None or comparison > 0:
                    next_set.clear()
                    best_signature = signature
                if comparison >= 0:
                    next_set.add(tuple(candidate))
        seen += len(next_set)
        if len(next_set) > permutation_cap:
            return 2, seen
        if not any(is_identity(list(permutation)) for permutation in next_set):
            return 0, seen
        current = next_set
    return 1, seen


def all_minimal(vector: Vec, minimal: int) -> bool:
    return all(value == minimal for value in vector)


def has_good_gamma(
    order: int,
    phi: list[int],
    threshold_det: int,
    matrix: Matrix,
    det_matrix: int,
    gamma_prefixes: list[Vec],
    emax: int,
    counter: Counter[str],
) -> bool:
    size = len(matrix)
    remaining = order - size
    if remaining <= 0:
        return True
    multiplier = (order - 1) ** (order - size - 1)
    n_minus_c = order - 1
    values = allowed_values(phi, emax)
    for prefix in gamma_prefixes:
        for e1 in values:
            for e2 in values:
                gamma = prefix + [e1, e2]
                counter["gamma_tests"] += 1
                d_value = det_bareiss(augment_with_gamma(matrix, gamma, 1))
                positive_d = d_value if d_value > 0 else 0
                upper_bound = multiplier * (n_minus_c * det_matrix + remaining * positive_d)
                if upper_bound >= threshold_det:
                    return True
    return False


def determinant_summary(gram: Matrix, order: int) -> tuple[bool, int, int]:
    determinant = det_bareiss(gram)
    if determinant < 0:
        return False, determinant, -1
    root = math.isqrt(determinant)
    if root * root != determinant:
        return False, determinant, -1
    divisor = 1 << (order - 1)
    if root % divisor != 0:
        return False, determinant, -1
    return True, determinant, root // divisor


def next_emax_after_accept(current: Matrix, vector: Vec, current_emax: int, active_start: int, minimal: int) -> int:
    current_size = len(current)
    active_size = current_size - active_start
    if active_size == 1 and not all_minimal(vector, minimal):
        return abs(vector[-1])
    return current_emax


def global_lexmax_order(gram: Matrix) -> tuple[list[int], int, bool]:
    size = len(gram)
    states: list[tuple[list[int], set[int]]] = [([], set(range(size)))]
    truncated = False
    max_states = 200000
    for _depth in range(size):
        best_signature: Vec | None = None
        next_states: list[tuple[list[int], set[int]]] = []
        for prefix, remaining in states:
            for candidate in remaining:
                signature = [gram[candidate][previous] for previous in prefix]
                comparison = 1 if best_signature is None else compare_vectors_abs(signature, best_signature)
                if best_signature is None or comparison > 0:
                    next_states.clear()
                    best_signature = signature
                if comparison >= 0:
                    new_remaining = set(remaining)
                    new_remaining.remove(candidate)
                    next_states.append((prefix + [candidate], new_remaining))
        if len(next_states) > max_states:
            next_states = next_states[:max_states]
            truncated = True
        states = next_states
    return states[0][0], len(states), truncated


def build_submatrix(gram: Matrix, ordering: list[int]) -> Matrix:
    return [[gram[row_index][col_index] for col_index in ordering] for row_index in ordering]


def load_reference_values(root: Path) -> set[int]:
    candidates = [
        root / "agentic_sprints" / "sprint_7" / "outputs" / "flist_fix_full" / "canonical_classes.partial_latest.json",
        root / "agentic_sprints" / "sprint_7" / "outputs" / "flist_fix_2m" / "canonical_classes.json",
        root / "agentic_sprints" / "sprint_6" / "outputs" / "full_attempt" / "canonical_classes.json",
    ]
    for path in candidates:
        if path.exists():
            payload = json.loads(path.read_text())
            return {int(value) for value in payload.get("distinct_normalized_values", [])}
    return set()


def trace_value(
    value: int,
    witness: dict[str, Any],
    args: argparse.Namespace,
    reference_values: set[int],
) -> dict[str, Any]:
    order = args.order
    phi = phi_congruent(order)
    minimal = phi[0]
    threshold_det = (args.threshold * (1 << (order - 1))) ** 2
    sign_matrix = parity_normalize_odd(block01_to_sign_matrix(witness["block01"]))
    gram = gram_matrix(sign_matrix)
    square, gram_det, normalized = determinant_summary(gram, order)
    ordering, ordering_ties, ordering_truncated = global_lexmax_order(gram)
    target_matrix = build_submatrix(gram, ordering)

    f_lists: list[list[Vec]] = [[] for _ in range(order + 1)]
    f_lists[0].append([])
    emax = order - 2
    prefix_matrix: Matrix = [[order]]
    level_traces: list[dict[str, Any]] = []
    global_counter: Counter[str] = Counter()

    for next_size in range(2, order + 1):
        if args.verbose:
            print(f"trace value={value} prefix={next_size}", flush=True)
        current_blocks, current_contiguous = compute_blocks(prefix_matrix, minimal)
        if not current_contiguous:
            return {
                "value": value,
                "status": "rejected",
                "failure": "current_prefix_block_contiguity",
                "prefix_size": next_size - 1,
                "level_traces": level_traces,
            }
        active_start = current_blocks[-1][0]
        target_vector = target_matrix[next_size - 1][: next_size - 1]
        values = allowed_values(phi, emax)
        candidate_vectors = append_vectors_from_prefixes(f_lists[next_size - 2], values)
        working_lists = [[item[:] for item in level] for level in f_lists]

        level: dict[str, Any] = {
            "prefix_size": next_size,
            "emax_before": emax,
            "f_list_sizes_before": [len(level_items) for level_items in f_lists[: next_size]],
            "target_vector": target_vector,
            "candidate_vector_count": len(candidate_vectors),
            "target_position": None,
            "prior_vectors_that_passed_bound": 0,
            "prior_vectors_that_passed_lexmax": 0,
            "prior_bound_checks_attempted": 0,
            "prior_prune_counts": {},
        }
        prior_counter: Counter[str] = Counter()
        target_seen = False

        for position, vector in enumerate(candidate_vectors):
            is_target = vector == target_vector
            if is_target:
                target_seen = True
                level["target_position"] = position

            if any(vector[index] != minimal for index in range(active_start)):
                if is_target:
                    level["target_failure"] = "active_block"
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                prior_counter["active_block"] += 1
                continue

            candidate = extend_matrix(prefix_matrix, vector, order)
            if not is_row_lex_ordered(candidate):
                if is_target:
                    level["target_failure"] = "row_order"
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                prior_counter["row_order"] += 1
                continue

            candidate_blocks, contiguous = compute_blocks(candidate, minimal)
            if not contiguous:
                if is_target:
                    level["target_failure"] = "block_contiguity"
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                prior_counter["block_contiguity"] += 1
                continue
            if not blocks_descending(candidate, candidate_blocks):
                if is_target:
                    level["target_failure"] = "block_order"
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                prior_counter["block_order"] += 1
                continue

            determinant = det_bareiss(candidate)
            if determinant <= 0:
                if is_target:
                    level["target_failure"] = "positive_definite"
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                prior_counter["positive_definite"] += 1
                continue

            if next_size == order:
                full_square, _, full_normalized = determinant_summary(candidate, order)
                if not full_square:
                    if is_target:
                        level["target_failure"] = "full_not_square"
                        level_traces.append(level)
                        return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                    prior_counter["full_not_square"] += 1
                    continue
                if full_normalized < args.threshold:
                    if is_target:
                        level["target_failure"] = "full_below_threshold"
                        level["full_normalized"] = full_normalized
                        level_traces.append(level)
                        return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                    prior_counter["full_below_threshold"] += 1
                    continue
                active_interval = candidate_blocks[-1]
                block = submatrix_interval(candidate, active_interval[0], active_interval[1])
                lexmax, seen = is_lexmax_block(block, args.permutation_cap)
                if lexmax == 0:
                    if is_target:
                        level["target_failure"] = "lexmax"
                        level["lexmax_permutations_seen"] = seen
                        level_traces.append(level)
                        return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces)
                    prior_counter["lexmax"] += 1
                    continue
                if is_target:
                    level["target_failure"] = "none"
                    level["full_normalized"] = full_normalized
                    level["lexmax_permutations_seen"] = seen
                    level["prior_prune_counts"] = dict(prior_counter)
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "accepted", level_traces, global_counter)
                prior_counter["full_candidate_before_target"] += 1
                continue

            if (
                not is_target
                and args.max_prior_bound_checks > 0
                and level["prior_bound_checks_attempted"] >= args.max_prior_bound_checks
            ):
                prior_counter["prior_bound_skipped_by_cap"] += 1
                continue

            level["prior_bound_checks_attempted"] += 1
            if not has_good_gamma(order, phi, threshold_det, candidate, determinant, f_lists[next_size - 2], emax, global_counter):
                if is_target:
                    level["target_failure"] = "km_gamma_bound"
                    level["prior_prune_counts"] = dict(prior_counter)
                    level_traces.append(level)
                    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces, global_counter)
                prior_counter["km_gamma_bound"] += 1
                continue

            working_lists[next_size - 1].append(vector)
            if not is_target:
                level["prior_vectors_that_passed_bound"] += 1

            starts_new_block = all_minimal(vector, minimal)
            if args.lexmax_mode == "always" or (
                args.lexmax_mode == "closed" and starts_new_block and len(candidate_blocks) >= 2
            ):
                interval = candidate_blocks[-1]
                if args.lexmax_mode == "closed":
                    interval = candidate_blocks[-2]
                block = submatrix_interval(candidate, interval[0], interval[1])
                lexmax, seen = is_lexmax_block(block, args.permutation_cap)
                if lexmax == 0:
                    if is_target:
                        level["target_failure"] = "lexmax"
                        level["lexmax_permutations_seen"] = seen
                        level["prior_prune_counts"] = dict(prior_counter)
                        level_traces.append(level)
                        return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces, global_counter)
                    prior_counter["lexmax"] += 1
                    continue

            if is_target:
                child_emax = next_emax_after_accept(prefix_matrix, vector, emax, active_start, minimal)
                level["target_failure"] = "none"
                level["emax_after"] = child_emax
                level["f_list_sizes_after"] = [len(level_items) for level_items in working_lists[: next_size + 1]]
                level["prior_prune_counts"] = dict(prior_counter)
                level_traces.append(level)
                f_lists = working_lists
                emax = child_emax
                prefix_matrix = candidate
                break

            level["prior_vectors_that_passed_lexmax"] += 1

        if not target_seen:
            level["target_failure"] = "target_vector_not_in_candidate_list"
            level["prior_prune_counts"] = dict(prior_counter)
            level_traces.append(level)
            return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "rejected", level_traces, global_counter)

    return finish_trace(value, square, gram_det, normalized, ordering, ordering_ties, ordering_truncated, reference_values, "accepted", level_traces, global_counter)


def finish_trace(
    value: int,
    square: bool,
    gram_det: int,
    normalized: int,
    ordering: list[int],
    ordering_ties: int,
    ordering_truncated: bool,
    reference_values: set[int],
    status: str,
    level_traces: list[dict[str, Any]],
    counter: Counter[str] | None = None,
) -> dict[str, Any]:
    last_level = level_traces[-1] if level_traces else {}
    return {
        "value": value,
        "status": status,
        "present_in_sprint7_reference_stream": value in reference_values,
        "verified_square_gram": square,
        "normalized_from_gram": normalized,
        "gram_determinant": str(gram_det),
        "canonical_ordering": ordering,
        "canonical_tie_count": ordering_ties,
        "canonical_truncated": ordering_truncated,
        "failure_prefix_size": last_level.get("prefix_size"),
        "failure": last_level.get("target_failure", "none" if status == "accepted" else "unknown"),
        "gamma_tests": 0 if counter is None else counter["gamma_tests"],
        "level_traces": level_traces,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    sprint_dir = Path(__file__).resolve().parent
    root = sprint_dir.parents[1]
    witnesses = json.loads((root / "agentic_sprints" / "sprint_3" / "outputs" / "n13_witnesses.json").read_text())
    reference_values = load_reference_values(root)
    if args.values:
        values = [int(item) for item in args.values.split(",") if item.strip()]
    else:
        values = [2271, 2307, 2316, 2336, 2360, 2916]

    start = time.perf_counter()
    results = []
    for value in values:
        if args.verbose:
            print(f"starting value={value}", flush=True)
        results.append(trace_value(value, witnesses[str(value)], args, reference_values))

    summary = {
        "order": args.order,
        "threshold": args.threshold,
        "lexmax_mode": args.lexmax_mode,
        "values": values,
        "accepted_values": [item["value"] for item in results if item["status"] == "accepted"],
        "rejected_values": [item["value"] for item in results if item["status"] != "accepted"],
        "failure_counts": dict(Counter(item["failure"] for item in results).most_common()),
        "elapsed_seconds": time.perf_counter() - start,
        "results": results,
    }
    output_dir = sprint_dir / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / args.output
    output_path.write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=13)
    parser.add_argument("--threshold", type=int, default=2173)
    parser.add_argument("--values", default="")
    parser.add_argument("--lexmax-mode", choices=["always", "closed"], default="always")
    parser.add_argument("--permutation-cap", type=int, default=2000000)
    parser.add_argument("--max-prior-bound-checks", type=int, default=0)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--output", default="missing_witness_path_trace.json")
    return parser.parse_args()


def main() -> None:
    summary = run(parse_args())
    print(json.dumps({key: value for key, value in summary.items() if key != "results"}, indent=2))


if __name__ == "__main__":
    main()
