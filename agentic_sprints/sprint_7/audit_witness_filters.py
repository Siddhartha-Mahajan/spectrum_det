#!/usr/bin/env python3
"""Audit sprint-6 candidate-Gram filters against known order-13 witnesses."""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from pathlib import Path
from typing import Any

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
        [sum(sign_matrix[row_index][column] * sign_matrix[col_index][column] for column in range(size)) for col_index in range(size)]
        for row_index in range(size)
    ]


def positive_mod(value: int, modulus: int) -> int:
    result = value % modulus
    return result if result >= 0 else result + modulus


def phi_congruent(order: int) -> list[int]:
    values = [value for value in range(1 - order, order) if positive_mod(value - order, 4) == 0]
    return sorted(values, key=lambda value: (abs(value), value))


def compare_vectors_abs(left: list[int], right: list[int]) -> int:
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


def partial_row(matrix: Matrix, row_index: int, length: int) -> list[int]:
    return matrix[row_index][:length]


def compare_matrices_abs_lex(left: Matrix, right: Matrix) -> int:
    shared = min(len(left), len(right))
    for row_index in range(1, shared):
        comparison = compare_vectors_abs(partial_row(left, row_index, row_index), partial_row(right, row_index, row_index))
        if comparison != 0:
            return comparison
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1
    return 0


def is_row_ordered_current(matrix: Matrix) -> bool:
    size = len(matrix)
    for earlier in range(size - 1):
        for later in range(earlier + 1, size):
            earlier_prefix = partial_row(matrix, earlier, earlier + 1)
            later_prefix = partial_row(matrix, later, earlier + 1)
            if compare_vectors_abs(earlier_prefix, later_prefix) <= 0:
                return False
    return True


def is_row_ordered_prefix_ge(matrix: Matrix) -> bool:
    size = len(matrix)
    for earlier in range(1, size - 1):
        for later in range(earlier + 1, size):
            earlier_prefix = partial_row(matrix, earlier, earlier)
            later_prefix = partial_row(matrix, later, earlier)
            if compare_vectors_abs(earlier_prefix, later_prefix) < 0:
                return False
    return True


def is_row_ordered_prefix_strict(matrix: Matrix) -> bool:
    size = len(matrix)
    for earlier in range(1, size - 1):
        for later in range(earlier + 1, size):
            earlier_prefix = partial_row(matrix, earlier, earlier)
            later_prefix = partial_row(matrix, later, earlier)
            if compare_vectors_abs(earlier_prefix, later_prefix) <= 0:
                return False
    return True


def build_submatrix(gram: Matrix, ordering: list[int]) -> Matrix:
    return [[gram[row_index][col_index] for col_index in ordering] for row_index in ordering]


def compute_blocks(matrix: Matrix, minimal: int) -> tuple[list[tuple[int, int]], bool, list[list[int]]]:
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

    groups = sorted(groups_by_root.values(), key=lambda group: group[0])
    intervals: list[tuple[int, int]] = []
    contiguous = True
    for group in groups:
        start = group[0]
        end = group[-1]
        if end - start + 1 != len(group):
            contiguous = False
        intervals.append((start, end))
    return intervals, contiguous, groups


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


def leading_signature(block: Matrix, permutation: list[int], leading_size: int) -> list[int]:
    signature: list[int] = []
    for row_index in range(1, leading_size):
        for col_index in range(row_index):
            signature.append(block[permutation[row_index]][permutation[col_index]])
    return signature


def make_pair_permutation(size: int, first: int, second: int) -> list[int]:
    return [first, second] + [item for item in range(size) if item != first and item != second]


def is_identity(permutation: list[int]) -> bool:
    return all(index == value for index, value in enumerate(permutation))


def is_lexmax_block(block: Matrix, permutation_cap: int) -> tuple[bool, bool, int]:
    size = len(block)
    if size <= 1:
        return True, False, 1

    current: set[tuple[int, ...]] = set()
    best_signature: list[int] | None = None
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
    if not any(is_identity(list(permutation)) for permutation in current):
        return False, False, len(current)

    seen = len(current)
    for leading_size in range(3, size + 1):
        next_set: set[tuple[int, ...]] = set()
        best_signature = None
        for permutation_tuple in current:
            permutation = list(permutation_tuple)
            for swap_position in range(leading_size - 1, size):
                candidate = permutation[:]
                candidate[leading_size - 1], candidate[swap_position] = candidate[swap_position], candidate[leading_size - 1]
                signature = leading_signature(block, candidate, leading_size)
                comparison = 1 if best_signature is None else compare_vectors_abs(signature, best_signature)
                if best_signature is None or comparison > 0:
                    next_set.clear()
                    best_signature = signature
                if comparison >= 0:
                    next_set.add(tuple(candidate))
        seen += len(next_set)
        if len(next_set) > permutation_cap:
            return True, True, seen
        if not any(is_identity(list(permutation)) for permutation in next_set):
            return False, False, seen
        current = next_set
    return True, False, seen


def global_lexmax_order(gram: Matrix) -> tuple[list[int], int, bool]:
    size = len(gram)
    states: list[tuple[list[int], set[int]]] = [([], set(range(size)))]
    truncated = False
    max_states = 200000
    for depth in range(size):
        best_signature: list[int] | None = None
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


def row_policy_function(name: str):
    if name == "current":
        return is_row_ordered_current
    if name == "prefix-ge":
        return is_row_ordered_prefix_ge
    if name == "prefix-strict":
        return is_row_ordered_prefix_strict
    raise ValueError(f"unknown row policy {name}")


def should_test_lex(prefix_size: int, order: int, lex_mode: str, starts_new_block: bool, interval_count: int) -> tuple[bool, int]:
    if lex_mode == "none":
        return False, -1
    if prefix_size == order:
        return True, interval_count - 1
    if lex_mode == "always":
        return True, interval_count - 1
    if lex_mode == "closed" and starts_new_block and interval_count >= 2:
        return True, interval_count - 2
    return False, -1


def audit_single_ordering(
    gram: Matrix,
    ordering: list[int],
    order: int,
    threshold: int,
    row_policy: str,
    lex_mode: str,
    permutation_cap: int,
) -> dict[str, Any]:
    row_ordered = row_policy_function(row_policy)
    minimal = 1 if order % 4 == 1 else -1
    for prefix_size in range(2, order + 1):
        current_matrix = build_submatrix(gram, ordering[: prefix_size - 1])
        current_intervals, _, _ = compute_blocks(current_matrix, minimal)
        active_start = current_intervals[-1][0]
        new_index = ordering[prefix_size - 1]
        vector = [gram[new_index][existing] for existing in ordering[: prefix_size - 1]]
        if any(vector[index] != minimal for index in range(active_start)):
            return {"passes": False, "first_failure": "active_block", "prefix_size": prefix_size}
        candidate_matrix = build_submatrix(gram, ordering[:prefix_size])
        if not row_ordered(candidate_matrix):
            return {"passes": False, "first_failure": f"row_order_{row_policy}", "prefix_size": prefix_size}
        candidate_intervals, contiguous, _ = compute_blocks(candidate_matrix, minimal)
        if not contiguous:
            return {"passes": False, "first_failure": "block_contiguity", "prefix_size": prefix_size}
        if not blocks_descending(candidate_matrix, candidate_intervals):
            return {"passes": False, "first_failure": "block_order", "prefix_size": prefix_size}
        determinant = det_bareiss(candidate_matrix)
        if determinant <= 0:
            return {"passes": False, "first_failure": "positive_definite", "prefix_size": prefix_size}
        starts_new_block = all(value == minimal for value in vector)
        test_lex, interval_index = should_test_lex(prefix_size, order, lex_mode, starts_new_block, len(candidate_intervals))
        if test_lex:
            start, end = candidate_intervals[interval_index]
            block = submatrix_interval(candidate_matrix, start, end)
            lexmax, inconclusive, seen = is_lexmax_block(block, permutation_cap)
            if inconclusive:
                return {"passes": False, "first_failure": "lexmax_inconclusive", "prefix_size": prefix_size, "permutations_seen": seen}
            if not lexmax:
                return {"passes": False, "first_failure": f"lexmax_{lex_mode}", "prefix_size": prefix_size, "block_size": len(block)}
        if prefix_size == order:
            square, determinant, normalized = determinant_summary(candidate_matrix, order)
            if not square:
                return {"passes": False, "first_failure": "full_not_square", "prefix_size": prefix_size}
            if normalized < threshold:
                return {"passes": False, "first_failure": "full_below_threshold", "prefix_size": prefix_size, "normalized": normalized}
    return {"passes": True, "first_failure": "none", "prefix_size": order}


def candidate_sort_key(gram: Matrix, prefix: list[int], candidate: int) -> tuple[int, ...]:
    return tuple(abs(gram[candidate][previous]) for previous in prefix)


def search_surviving_ordering(
    gram: Matrix,
    order: int,
    threshold: int,
    row_policy: str,
    lex_mode: str,
    permutation_cap: int,
    max_states: int,
) -> dict[str, Any]:
    row_ordered = row_policy_function(row_policy)
    minimal = 1 if order % 4 == 1 else -1
    counters: Counter[str] = Counter()
    start = time.perf_counter()
    visited = 0

    def dfs(prefix: list[int], remaining: set[int]) -> list[int] | None:
        nonlocal visited
        if visited >= max_states:
            counters["state_cap"] += 1
            return None
        visited += 1
        if len(prefix) == order:
            matrix = build_submatrix(gram, prefix)
            square, _, normalized = determinant_summary(matrix, order)
            if not square:
                counters["full_not_square"] += 1
                return None
            if normalized < threshold:
                counters["full_below_threshold"] += 1
                return None
            return prefix

        if prefix:
            current_matrix = build_submatrix(gram, prefix)
            current_intervals, _, _ = compute_blocks(current_matrix, minimal)
            active_start = current_intervals[-1][0]
        else:
            active_start = 0

        candidates = sorted(remaining, key=lambda item: candidate_sort_key(gram, prefix, item), reverse=True)
        for candidate in candidates:
            vector = [gram[candidate][existing] for existing in prefix]
            if any(vector[index] != minimal for index in range(active_start)):
                counters["active_block"] += 1
                continue
            next_prefix = prefix + [candidate]
            candidate_matrix = build_submatrix(gram, next_prefix)
            prefix_size = len(next_prefix)
            if prefix_size >= 2 and not row_ordered(candidate_matrix):
                counters[f"row_order_{row_policy}"] += 1
                continue
            intervals, contiguous, _ = compute_blocks(candidate_matrix, minimal)
            if not contiguous:
                counters["block_contiguity"] += 1
                continue
            if not blocks_descending(candidate_matrix, intervals):
                counters["block_order"] += 1
                continue
            determinant = det_bareiss(candidate_matrix)
            if determinant <= 0:
                counters["positive_definite"] += 1
                continue
            starts_new_block = bool(prefix) and all(value == minimal for value in vector)
            test_lex, interval_index = should_test_lex(prefix_size, order, lex_mode, starts_new_block, len(intervals))
            if test_lex:
                start_index, end_index = intervals[interval_index]
                block = submatrix_interval(candidate_matrix, start_index, end_index)
                lexmax, inconclusive, _ = is_lexmax_block(block, permutation_cap)
                if inconclusive:
                    counters["lexmax_inconclusive"] += 1
                    continue
                if not lexmax:
                    counters[f"lexmax_{lex_mode}"] += 1
                    continue
            next_remaining = set(remaining)
            next_remaining.remove(candidate)
            found = dfs(next_prefix, next_remaining)
            if found is not None:
                return found
        return None

    found_ordering = dfs([], set(range(order)))
    elapsed = time.perf_counter() - start
    return {
        "found": found_ordering is not None,
        "ordering": found_ordering if found_ordering is not None else [],
        "visited_states": visited,
        "hit_state_cap": visited >= max_states,
        "elapsed_seconds": elapsed,
        "prune_counts": dict(counters.most_common()),
    }


def load_sprint6_values(root: Path) -> set[int]:
    path = root / "agentic_sprints" / "sprint_6" / "outputs" / "full_attempt" / "canonical_classes.json"
    if not path.exists():
        return set()
    payload = json.loads(path.read_text())
    return set(payload.get("distinct_normalized_values", []))


def summarize_offdiagonal_values(matrix: Matrix) -> list[int]:
    values = set()
    for row_index in range(len(matrix)):
        for col_index in range(row_index + 1, len(matrix)):
            values.add(matrix[row_index][col_index])
    return sorted(values, key=lambda value: (abs(value), value))


def audit_witnesses(args: argparse.Namespace) -> dict[str, Any]:
    sprint_dir = Path(__file__).resolve().parent
    root = sprint_dir.parents[1]
    witness_path = root / "agentic_sprints" / "sprint_3" / "outputs" / "n13_witnesses.json"
    witnesses = json.loads(witness_path.read_text())
    sprint6_values = load_sprint6_values(root)
    selected_values = sorted(int(value) for value in witnesses if int(value) > args.threshold)
    if args.values:
        requested = {int(value) for value in args.values.split(",") if value.strip()}
        selected_values = [value for value in selected_values if value in requested]
    if args.limit:
        selected_values = selected_values[: args.limit]

    results: list[dict[str, Any]] = []
    failure_counter: Counter[str] = Counter()
    found_counter: Counter[str] = Counter()
    for value in selected_values:
        block = witnesses[str(value)]["block01"]
        sign_matrix = block01_to_sign_matrix(block)
        normalized_sign_matrix = parity_normalize_odd(sign_matrix)
        gram = gram_matrix(normalized_sign_matrix)
        square, gram_determinant, normalized = determinant_summary(gram, args.order)
        canonical_order, canonical_ties, canonical_truncated = global_lexmax_order(gram)
        canonical_matrix = build_submatrix(gram, canonical_order)
        canonical_blocks, canonical_contiguous, canonical_groups = compute_blocks(canonical_matrix, 1)
        value_result: dict[str, Any] = {
            "value": value,
            "present_in_sprint6_strict_values": value in sprint6_values,
            "verified_square_gram": square,
            "normalized_from_gram": normalized,
            "gram_determinant": str(gram_determinant),
            "offdiagonal_values": summarize_offdiagonal_values(gram),
            "canonical_ordering": canonical_order,
            "canonical_tie_count": canonical_ties,
            "canonical_truncated": canonical_truncated,
            "canonical_block_sizes": [end - start + 1 for start, end in canonical_blocks],
            "canonical_blocks_contiguous": canonical_contiguous,
            "canonical_group_sizes_raw": [len(group) for group in canonical_groups],
            "canonical_path": {},
            "search": {},
        }
        for row_policy in args.row_policies.split(","):
            row_policy = row_policy.strip()
            if not row_policy:
                continue
            for lex_mode in args.lex_modes.split(","):
                lex_mode = lex_mode.strip()
                if not lex_mode:
                    continue
                key = f"{row_policy}/{lex_mode}"
                path_result = audit_single_ordering(
                    gram,
                    canonical_order,
                    args.order,
                    args.threshold,
                    row_policy,
                    lex_mode,
                    args.permutation_cap,
                )
                value_result["canonical_path"][key] = path_result
                if path_result["passes"]:
                    found_counter[f"canonical:{key}"] += 1
                else:
                    failure_counter[f"canonical:{key}:{path_result['first_failure']}"] += 1
                if args.search:
                    search_result = search_surviving_ordering(
                        gram,
                        args.order,
                        args.threshold,
                        row_policy,
                        lex_mode,
                        args.permutation_cap,
                        args.max_states,
                    )
                    value_result["search"][key] = search_result
                    if search_result["found"]:
                        found_counter[f"search:{key}"] += 1
                    else:
                        top_reason = next(iter(search_result["prune_counts"]), "none")
                        failure_counter[f"search:{key}:{top_reason}"] += 1
        results.append(value_result)

    summary = {
        "order": args.order,
        "threshold": args.threshold,
        "values_checked": selected_values,
        "value_count": len(selected_values),
        "sprint6_strict_value_coverage_in_checked_set": sum(1 for value in selected_values if value in sprint6_values),
        "row_policies": [policy.strip() for policy in args.row_policies.split(",") if policy.strip()],
        "lex_modes": [mode.strip() for mode in args.lex_modes.split(",") if mode.strip()],
        "search_enabled": args.search,
        "max_states": args.max_states,
        "found_counter": dict(found_counter.most_common()),
        "failure_counter": dict(failure_counter.most_common()),
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
    parser.add_argument("--row-policies", default="current,prefix-ge")
    parser.add_argument("--lex-modes", default="always,closed,final,none")
    parser.add_argument("--permutation-cap", type=int, default=2000000)
    parser.add_argument("--max-states", type=int, default=200000)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--values", default="")
    parser.add_argument("--search", action="store_true")
    parser.add_argument("--output", default="witness_filter_audit.json")
    return parser.parse_args()


def main() -> None:
    summary = audit_witnesses(parse_args())
    print(json.dumps({
        "value_count": summary["value_count"],
        "sprint6_coverage": summary["sprint6_strict_value_coverage_in_checked_set"],
        "found_counter": summary["found_counter"],
        "top_failures": dict(list(summary["failure_counter"].items())[:20]),
    }, indent=2))


if __name__ == "__main__":
    main()
