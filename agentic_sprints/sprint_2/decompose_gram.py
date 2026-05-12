#!/usr/bin/env python3
"""Fixed-Gram decomposition experiment.

Given a Gram matrix G from a first-row-normalized sign matrix, search for a
{-1,1} matrix R with first row all +1 and G = R R^T.
"""

from __future__ import annotations

import json
import random
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


def hadamard(order: int) -> list[list[int]]:
    if order == 1:
        return [[1]]
    half = hadamard(order // 2)
    return [row + row for row in half] + [row + [-value for value in row] for row in half]


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


def random_normalized_sign_matrix(order: int, rng: random.Random) -> list[list[int]]:
    matrix = [[1 for _ in range(order)] for _ in range(order)]
    for i in range(1, order):
        for j in range(1, order):
            matrix[i][j] = 1 if rng.randrange(2) else -1
    return matrix


def gram(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    return [[sum(matrix[i][k] * matrix[j][k] for k in range(n)) for j in range(n)] for i in range(n)]


def determinant_normalized(matrix: list[list[int]]) -> int:
    n = len(matrix)
    return abs(det_bareiss(matrix)) // (1 << (n - 1))


def word_to_row(word: int, order: int) -> list[int]:
    return [1 if (word >> j) & 1 else -1 for j in range(order)]


def row_to_word(row: list[int]) -> int:
    word = 0
    for j, value in enumerate(row):
        if value == 1:
            word |= 1 << j
    return word


def dot_words(a: int, b: int, order: int) -> int:
    return order - 2 * (a ^ b).bit_count()


def validate_gram_shape(g: list[list[int]]) -> str | None:
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


def decompose_first_row_normalized(g: list[list[int]]) -> DecompositionResult:
    start = time.perf_counter()
    shape_error = validate_gram_shape(g)
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
        nonlocal nodes
        row_index = choose_row()
        if row_index is None:
            return True
        for candidate in candidates[row_index]:
            nodes += 1
            if all(assigned[j] is None or dot_words(candidate, assigned[j], n) == g[row_index][j] for j in range(n)):
                assigned[row_index] = candidate
                if search():
                    return True
                assigned[row_index] = None
        return False

    found = search()
    elapsed = time.perf_counter() - start
    if not found:
        return DecompositionResult("unsat", nodes, elapsed, "Search exhausted", None)
    matrix = [word_to_row(word, n) for word in assigned if word is not None]
    return DecompositionResult("sat", nodes, elapsed, None, matrix)


def verify_decomposition(g: list[list[int]], matrix: list[list[int]] | None) -> bool:
    return matrix is not None and gram(matrix) == g


def make_inconsistent_gram(base: list[list[int]]) -> list[list[int]]:
    bad = [row[:] for row in base]
    n = len(bad)
    bad[0][1] = n
    bad[1][0] = n
    if n > 2 and bad[0][2] == bad[1][2]:
        replacement = bad[0][2] + 2 if bad[0][2] <= n - 2 else bad[0][2] - 2
        bad[1][2] = replacement
        bad[2][1] = replacement
    return bad


def result_to_dict(name: str, source_matrix: list[list[int]] | None, g: list[list[int]], result: DecompositionResult) -> dict[str, object]:
    verified = verify_decomposition(g, result.matrix)
    return {
        "case": name,
        "order": len(g),
        "source_normalized_determinant": determinant_normalized(source_matrix) if source_matrix is not None else None,
        "gram_determinant": det_bareiss(g),
        "status": result.status,
        "nodes": result.nodes,
        "elapsed_seconds": result.elapsed_seconds,
        "reason": result.reason,
        "verified_decomposition": verified,
        "matrix": result.matrix,
    }


def run_experiment(output_dir: Path) -> dict[str, object]:
    rng = random.Random(20260512)
    cases: list[tuple[str, list[list[int]] | None, list[list[int]]]] = []

    h8 = normalize_sign_matrix(hadamard(8))
    cases.append(("n8_sylvester_hadamard", h8, gram(h8)))

    random8 = random_normalized_sign_matrix(8, rng)
    cases.append(("n8_random_normalized", random8, gram(random8)))

    random12 = random_normalized_sign_matrix(12, rng)
    cases.append(("n12_random_normalized", random12, gram(random12)))

    cases.append(("n8_inconsistent_perturbation", None, make_inconsistent_gram(gram(random8))))

    results = []
    for name, source_matrix, g in cases:
        result = decompose_first_row_normalized(g)
        results.append(result_to_dict(name, source_matrix, g, result))

    summary = {
        "seed": 20260512,
        "cases": results,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "decomposition_results.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    summary = run_experiment(Path("outputs"))
    compact = [
        {
            "case": case["case"],
            "status": case["status"],
            "nodes": case["nodes"],
            "verified_decomposition": case["verified_decomposition"],
            "elapsed_seconds": case["elapsed_seconds"],
            "reason": case["reason"],
        }
        for case in summary["cases"]
    ]
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
