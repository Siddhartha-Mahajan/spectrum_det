#!/usr/bin/env python3
"""Canonicalize sprint-6 candidate Gram matrices up to row/column permutation.

The Gram matrix is treated as a complete weighted graph on n row vertices.
For exact weighted-graph canonicalization with pynauty, each off-diagonal edge
is replaced by an edge-vertex colored by its Gram value and connected to the two
incident row vertices. Row vertices form their own color class.
"""

from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import pynauty

Matrix = list[list[int]]


def gram_certificate(matrix: Matrix) -> bytes:
    order = len(matrix)
    edge_vertices: dict[tuple[int, int], int] = {}
    edge_color_classes: dict[int, set[int]] = defaultdict(set)
    adjacency: dict[int, list[int]] = {index: [] for index in range(order)}
    next_vertex = order

    for i in range(order):
        for j in range(i + 1, order):
            edge_vertex = next_vertex
            next_vertex += 1
            edge_vertices[(i, j)] = edge_vertex
            edge_color_classes[matrix[i][j]].add(edge_vertex)
            adjacency.setdefault(edge_vertex, [])
            adjacency[i].append(edge_vertex)
            adjacency[j].append(edge_vertex)
            adjacency[edge_vertex].extend([i, j])

    coloring = [set(range(order))]
    for value in sorted(edge_color_classes):
        coloring.append(edge_color_classes[value])

    graph = pynauty.Graph(
        number_of_vertices=next_vertex,
        directed=False,
        adjacency_dict=adjacency,
        vertex_coloring=coloring,
    )
    return pynauty.certificate(graph)


def summarize_candidates(input_path: Path, output_path: Path, progress_path: Path | None) -> dict[str, Any]:
    start = time.perf_counter()
    classes: dict[str, dict[str, Any]] = {}
    raw_matrix_cache: dict[str, str] = {}
    total = 0
    values: set[int] = set()

    with input_path.open() as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            total += 1
            matrix = item["matrix"]
            matrix_key = json.dumps(matrix, separators=(",", ":"))
            certificate_hex = raw_matrix_cache.get(matrix_key)
            if certificate_hex is None:
                certificate_hex = gram_certificate(matrix).hex()
                raw_matrix_cache[matrix_key] = certificate_hex
            value = int(item["normalized_determinant"])
            values.add(value)
            record = classes.setdefault(certificate_hex, {
                "count": 0,
                "normalized_values": set(),
                "example": item,
            })
            record["count"] += 1
            record["normalized_values"].add(value)

            if progress_path is not None and total % 500 == 0:
                progress_path.write_text(json.dumps({
                    "input": str(input_path),
                    "processed": total,
                    "unique_classes": len(classes),
                    "raw_matrix_cache_size": len(raw_matrix_cache),
                    "distinct_values": len(values),
                    "elapsed_seconds": time.perf_counter() - start,
                }, indent=2) + "\n")

    serializable_classes = []
    for certificate_hex, record in classes.items():
        serializable_classes.append({
            "certificate": certificate_hex,
            "count": record["count"],
            "normalized_values": sorted(record["normalized_values"]),
            "example": record["example"],
        })
    serializable_classes.sort(key=lambda record: (record["normalized_values"], record["certificate"]))

    output = {
        "input": str(input_path),
        "total_candidates": total,
        "unique_candidate_classes": len(classes),
        "distinct_normalized_values": sorted(values),
        "distinct_normalized_value_count": len(values),
        "raw_matrix_cache_size": len(raw_matrix_cache),
        "elapsed_seconds": time.perf_counter() - start,
        "classes": serializable_classes,
    }
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    if progress_path is not None:
        progress_path.write_text(json.dumps({
            "input": str(input_path),
            "processed": total,
            "unique_classes": len(classes),
            "raw_matrix_cache_size": len(raw_matrix_cache),
            "distinct_values": len(values),
            "elapsed_seconds": time.perf_counter() - start,
            "done": True,
        }, indent=2) + "\n")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--progress", type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.progress is not None:
        args.progress.parent.mkdir(parents=True, exist_ok=True)
    output = summarize_candidates(args.input, args.output, args.progress)
    print(json.dumps({key: value for key, value in output.items() if key != "classes"}, indent=2))


if __name__ == "__main__":
    main()
