#!/usr/bin/env python3
"""BOOZ-style Gram proof pipeline prototype for order 13.

This script verifies and decomposes Gram matrices induced by sprint-3 witnesses,
and separately profiles a bounded candidate-principal-minor generator. It is not
a complete replacement for BOOZ's optimized Gram-finding program.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DecompositionResult:
    status: str
    nodes: int
    elapsed_seconds: float
    reason: str | None
    matrix: list[list[int]] | None


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


def block01_to_sign_matrix(block: list[list[int]]) -> list[list[int]]:
    size = len(block)
    matrix = [[1 for _ in range(size + 1)] for _ in range(size + 1)]
    for i, row in enumerate(block):
        for j, value in enumerate(row):
            matrix[i + 1][j + 1] = -1 if value else 1
    return matrix


def parity_normalize_rows(matrix: list[list[int]]) -> list[list[int]]:
    """Flip rows so each row sum is congruent to n mod 4."""
    n = len(matrix)
    normalized = []
    for row in matrix:
        row_sum = sum(row)
        if (row_sum - n) % 4 == 0:
            normalized.append(row[:])
        else:
            normalized.append([-value for value in row])
    return normalized


def gram(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    return [[sum(matrix[i][k] * matrix[j][k] for k in range(n)) for j in range(n)] for i in range(n)]


def word_to_row(word: int, order: int) -> list[int]:
    return [1 if (word >> j) & 1 else -1 for j in range(order)]


def dot_words(a: int, b: int, order: int) -> int:
    return order - 2 * (a ^ b).bit_count()


def validate_candidate_gram(g: list[list[int]], threshold_normalized: int = 2173) -> dict[str, object]:
    n = len(g)
    errors: list[str] = []
    if any(len(row) != n for row in g):
        errors.append("not square")
        return {"valid": False, "errors": errors}

    for i in range(n):
        if g[i][i] != n:
            errors.append(f"diagonal {i} is {g[i][i]}, expected {n}")
        for j in range(n):
            if g[i][j] != g[j][i]:
                errors.append(f"not symmetric at ({i},{j})")
            if (g[i][j] - n) % 4 != 0:
                errors.append(f"entry ({i},{j}) violates mod-4 condition")

    leading_minors = []
    for k in range(1, n + 1):
        value = det_bareiss([row[:k] for row in g[:k]])
        leading_minors.append(value)
        if value <= 0:
            errors.append(f"leading principal minor {k} is not positive")
            break

    determinant = det_bareiss(g)
    root = math.isqrt(abs(determinant))
    square_determinant = determinant >= 0 and root * root == determinant
    if not square_determinant:
        errors.append("determinant is not a nonnegative square")

    normalized = root // (1 << (n - 1)) if square_determinant else None
    if square_determinant and root % (1 << (n - 1)) != 0:
        errors.append("sqrt(det(G)) is not divisible by 2^(n-1)")
    if normalized is not None and normalized < threshold_normalized:
        errors.append("normalized determinant below threshold")

    return {
        "valid": not errors,
        "errors": errors,
        "determinant": determinant,
        "sqrt_determinant": root if square_determinant else None,
        "normalized_determinant": normalized,
        "leading_minors": leading_minors,
    }


def validate_gram_shape_for_decomposition(g: list[list[int]]) -> str | None:
    n = len(g)
    if any(len(row) != n for row in g):
        return "Gram is not square"
    for i in range(n):
        if g[i][i] != n:
            return f"Diagonal entry {i} is {g[i][i]}, expected {n}"
        for j in range(n):
            if g[i][j] != g[j][i]:
                return f"Gram is not symmetric at ({i},{j})"
            if abs(g[i][j]) > n:
                return f"Entry ({i},{j}) has magnitude > n"
            if (g[i][j] - n) % 2 != 0:
                return f"Entry ({i},{j}) has invalid parity"
    return None


def decompose_first_row_normalized(g: list[list[int]], max_nodes: int | None = None) -> DecompositionResult:
    start = time.perf_counter()
    shape_error = validate_gram_shape_for_decomposition(g)
    if shape_error is not None:
        return DecompositionResult("invalid", 0, time.perf_counter() - start, shape_error, None)

    n = len(g)
    all_ones = (1 << n) - 1
    all_words = list(range(1 << n))
    candidates: list[list[int]] = []
    for i in range(n):
        if i == 0:
            row_candidates = [all_ones]
        else:
            row_candidates = [word for word in all_words if dot_words(all_ones, word, n) == g[0][i]]
        if not row_candidates:
            return DecompositionResult("unsat", 0, time.perf_counter() - start, f"No candidates for row {i}", None)
        candidates.append(row_candidates)

    assigned: list[int | None] = [None for _ in range(n)]
    assigned[0] = all_ones
    nodes = 0
    aborted = False

    def choose_row() -> int | None:
        best_index = None
        best_count = 10**18
        for i in range(n):
            if assigned[i] is not None:
                continue
            count = 0
            for candidate in candidates[i]:
                if all(assigned[j] is None or dot_words(candidate, assigned[j], n) == g[i][j] for j in range(n)):
                    count += 1
            if count < best_count:
                best_count = count
                best_index = i
            if count == 0:
                return i
        return best_index

    def search() -> bool:
        nonlocal nodes, aborted
        if max_nodes is not None and nodes >= max_nodes:
            aborted = True
            return False
        row_index = choose_row()
        if row_index is None:
            return True
        for candidate in candidates[row_index]:
            if max_nodes is not None and nodes >= max_nodes:
                aborted = True
                return False
            nodes += 1
            if all(assigned[j] is None or dot_words(candidate, assigned[j], n) == g[row_index][j] for j in range(n)):
                assigned[row_index] = candidate
                if search():
                    return True
                assigned[row_index] = None
        return False

    found = search()
    elapsed = time.perf_counter() - start
    if aborted:
        return DecompositionResult("aborted", nodes, elapsed, f"Stopped at max_nodes={max_nodes}", None)
    if not found:
        return DecompositionResult("unsat", nodes, elapsed, "Search exhausted", None)
    matrix = [word_to_row(word, n) for word in assigned if word is not None]
    return DecompositionResult("sat", nodes, elapsed, None, matrix)


def unique_witness_grams(witness_path: Path) -> dict[str, dict[str, object]]:
    payload = json.loads(witness_path.read_text())
    unique: dict[tuple[tuple[int, ...], ...], dict[str, object]] = {}
    for key, item in payload.items():
        value = int(key)
        if value < 2174:
            continue
        sign_matrix = parity_normalize_rows(block01_to_sign_matrix(item["block01"]))
        g = gram(sign_matrix)
        gram_key = tuple(tuple(row) for row in g)
        unique.setdefault(gram_key, {"normalized_values": [], "gram": g, "source_matrix": sign_matrix})
        unique[gram_key]["normalized_values"].append(value)
    return {str(index): data for index, data in enumerate(unique.values(), start=1)}


def run_supplied_gram_verifier(
    witness_path: Path,
    output_dir: Path,
    verify_limit: int | None,
    max_decompose_nodes: int | None,
) -> dict[str, object]:
    grams = unique_witness_grams(witness_path)
    gram_items = list(grams.items())
    if verify_limit is not None:
        gram_items = gram_items[:verify_limit]
    records = []
    determinant_values = set()
    total_decomposition_nodes = 0
    start = time.perf_counter()
    progress_path = output_dir / "supplied_gram_progress.json"

    for index, (gram_id, data) in enumerate(gram_items, start=1):
        g = data["gram"]
        source_matrix = data["source_matrix"]
        validation = validate_candidate_gram(g)
        decomposition = decompose_first_row_normalized(g, max_decompose_nodes)
        total_decomposition_nodes += decomposition.nodes
        recovered_value = validation.get("normalized_determinant")
        if isinstance(recovered_value, int):
            determinant_values.add(recovered_value)
        records.append({
            "gram_id": gram_id,
            "normalized_values_from_witnesses": sorted(data["normalized_values"]),
            "validation_valid": validation["valid"],
            "validation_errors": validation["errors"],
            "normalized_determinant_from_gram": recovered_value,
            "source_decomposition_verified": gram(source_matrix) == g,
            "decomposition_status": decomposition.status,
            "decomposition_nodes": decomposition.nodes,
            "decomposition_verified": decomposition.matrix is not None and gram(decomposition.matrix) == g,
            "decomposition_elapsed_seconds": decomposition.elapsed_seconds,
        })
        progress = {
            "source": str(witness_path),
            "available_unique_gram_count": len(grams),
            "requested_gram_count": len(gram_items),
            "completed_gram_count": index,
            "valid_candidate_gram_count_so_far": sum(1 for record in records if record["validation_valid"]),
            "decomposed_count_so_far": sum(1 for record in records if record["decomposition_status"] == "sat"),
            "aborted_decomposition_count_so_far": sum(1 for record in records if record["decomposition_status"] == "aborted"),
            "recovered_distinct_determinant_count_so_far": len(determinant_values),
            "total_decomposition_nodes_so_far": total_decomposition_nodes,
            "elapsed_seconds_so_far": time.perf_counter() - start,
            "last_record": records[-1],
        }
        progress_path.write_text(json.dumps(progress, indent=2) + "\n")

    elapsed = time.perf_counter() - start
    output = {
        "source": str(witness_path),
        "available_unique_gram_count": len(grams),
        "requested_gram_count": len(gram_items),
        "valid_candidate_gram_count": sum(1 for record in records if record["validation_valid"]),
        "decomposed_count": sum(1 for record in records if record["decomposition_status"] == "sat"),
        "aborted_decomposition_count": sum(1 for record in records if record["decomposition_status"] == "aborted"),
        "recovered_distinct_determinants": sorted(determinant_values),
        "recovered_distinct_determinant_count": len(determinant_values),
        "total_decomposition_nodes": total_decomposition_nodes,
        "elapsed_seconds": elapsed,
        "records": records,
    }
    (output_dir / "supplied_gram_verification.json").write_text(json.dumps(output, indent=2) + "\n")
    return output


def profile_candidate_minor_generation(order: int, max_depth: int, max_generated: int) -> dict[str, object]:
    if order % 4 == 1:
        allowed = list(range(2 - order, 2, 4))
    elif order % 4 == 3:
        allowed = list(range(2 - order, 4, 4))
    else:
        allowed = [value for value in range(-order, order + 1) if (value - order) % 4 == 0]
    threshold = (2173 * (1 << 12)) ** 2 if order == 13 else 1
    start = time.perf_counter()
    frontier = [([[order]], det_bareiss([[order]]))]
    levels = [{"level": 1, "frontier": 1, "accepted": 1, "tested": 1, "pruned_pd": 0, "pruned_hadamard_bound": 0}]
    total_tested = 1
    stopped_by_cap = False

    for level in range(2, max_depth + 1):
        next_frontier = []
        tested = 0
        accepted = 0
        pruned_pd = 0
        pruned_hadamard = 0
        for matrix, _determinant in frontier:
            r = len(matrix)
            for vector in itertools.product(allowed, repeat=r):
                tested += 1
                total_tested += 1
                candidate = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
                candidate.append(list(vector) + [order])
                determinant = det_bareiss(candidate)
                if determinant <= 0:
                    pruned_pd += 1
                    continue
                remaining = order - level
                if determinant * (order ** remaining) < threshold:
                    pruned_hadamard += 1
                    continue
                next_frontier.append((candidate, determinant))
                accepted += 1
                if total_tested >= max_generated:
                    stopped_by_cap = True
                    break
            if stopped_by_cap:
                break
        levels.append({
            "level": level,
            "frontier": len(next_frontier),
            "accepted": accepted,
            "tested": tested,
            "pruned_pd": pruned_pd,
            "pruned_hadamard_bound": pruned_hadamard,
        })
        frontier = next_frontier
        if stopped_by_cap or not frontier:
            break

    return {
        "order": order,
        "allowed_offdiagonal_entries": allowed,
        "max_depth_requested": max_depth,
        "max_generated": max_generated,
        "stopped_by_cap": stopped_by_cap,
        "total_tested": total_tested,
        "final_frontier_size": len(frontier),
        "levels": levels,
        "elapsed_seconds": time.perf_counter() - start,
        "is_complete_gram_enumeration": False,
        "why_not_complete": "This bounded profiler lacks BOOZ allowable-vector generation, equivalence canonicalization, and the enhanced Kounias-Moyssiadis pruning needed for a complete 8321-candidate order-13 enumeration.",
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    root = Path(__file__).resolve().parents[2]
    witness_path = root / "agentic_sprints" / "sprint_3" / "outputs" / "n13_witnesses.json"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    supplied = run_supplied_gram_verifier(witness_path, output_dir, args.verify_limit, args.max_decompose_nodes)
    if args.skip_profiler:
        profiler = {
            "skipped": True,
            "total_tested": 0,
            "final_frontier_size": 0,
            "stopped_by_cap": False,
            "why_not_complete": "Profiler skipped for this run.",
        }
    else:
        profiler = profile_candidate_minor_generation(13, args.max_depth, args.max_generated)
        (output_dir / "candidate_minor_profile.json").write_text(json.dumps(profiler, indent=2) + "\n")

    summary = {
        "is_full_booz_replication": False,
        "supplied_gram_available_unique_count": supplied["available_unique_gram_count"],
        "supplied_gram_requested_count": supplied["requested_gram_count"],
        "supplied_gram_decomposed_count": supplied["decomposed_count"],
        "supplied_gram_aborted_decomposition_count": supplied["aborted_decomposition_count"],
        "recovered_distinct_determinant_count": supplied["recovered_distinct_determinant_count"],
        "candidate_minor_profile_total_tested": profiler["total_tested"],
        "candidate_minor_profile_final_frontier_size": profiler["final_frontier_size"],
        "candidate_minor_profile_stopped_by_cap": profiler["stopped_by_cap"],
        "blocker": profiler["why_not_complete"],
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-generated", type=int, default=20_000)
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--verify-limit", type=int, default=None)
    parser.add_argument("--max-decompose-nodes", type=int, default=None)
    parser.add_argument("--skip-profiler", action="store_true")
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    print(json.dumps(run(args), indent=2))


if __name__ == "__main__":
    main()
