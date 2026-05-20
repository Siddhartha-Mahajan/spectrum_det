#!/usr/bin/env python3
"""Reconcile order-13 BOOZ reproduction artifacts across sprints."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def display_path(path: Path, root: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError:
        return str(resolved)


def ranges(values: list[int]) -> list[str]:
    if not values:
        return []
    out: list[str] = []
    start = previous = values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
            continue
        out.append(str(start) if start == previous else f"[{start},{previous}]")
        start = previous = value
    out.append(str(start) if start == previous else f"[{start},{previous}]")
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stream",
        type=Path,
        default=None,
        help="Canonicalized candidate-class JSON to reconcile. Defaults to the sprint-7 long-run snapshot.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output report path. Defaults to outputs/order13_reconciliation.json.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sprint_dir = Path(__file__).resolve().parent
    root = sprint_dir.parents[1]

    n13_results = load_json(root / "agentic_sprints" / "sprint_3" / "outputs" / "n13_results.json")
    high_tail = {int(value) for value in n13_results["found_high_tail_values"]}

    if args.stream is None:
        stream_path = root / "agentic_sprints" / "sprint_7" / "outputs" / "flist_fix_full" / "canonical_classes.partial_latest.json"
    else:
        stream_path = args.stream if args.stream.is_absolute() else (Path.cwd() / args.stream)
    stream = load_json(stream_path)
    stream_values = {int(value) for value in stream["distinct_normalized_values"]}

    trace_path = root / "agentic_sprints" / "sprint_8" / "outputs" / "missing_witness_path_trace.json"
    trace = load_json(trace_path)
    trace_accepted = {int(value) for value in trace["accepted_values"]}

    covered_by_stream = high_tail & stream_values
    covered_by_trace_only = (high_tail & trace_accepted) - stream_values
    union_covered = covered_by_stream | covered_by_trace_only
    still_unaccounted = high_tail - union_covered

    report = {
        "known_high_tail_count": len(high_tail),
        "known_high_tail_values": sorted(high_tail),
        "candidate_stream": {
            "path": display_path(stream_path, root),
            "total_candidates": stream.get("total_candidates"),
            "candidate_classes": stream["unique_candidate_classes"],
            "distinct_normalized_value_count": stream["distinct_normalized_value_count"],
            "known_high_tail_covered_count": len(covered_by_stream),
            "known_high_tail_covered_values": sorted(covered_by_stream),
            "known_high_tail_missing_values": sorted(high_tail - covered_by_stream),
        },
        "path_trace_supplement": {
            "path": display_path(trace_path, root),
            "accepted_count": len(trace_accepted),
            "accepted_values": sorted(trace_accepted),
            "covered_by_trace_only_count": len(covered_by_trace_only),
            "covered_by_trace_only_values": sorted(covered_by_trace_only),
        },
        "reconciled_known_high_tail_coverage": {
            "covered_count": len(union_covered),
            "covered_fraction": f"{len(union_covered)}/{len(high_tail)}",
            "still_unaccounted_count": len(still_unaccounted),
            "still_unaccounted_values": sorted(still_unaccounted),
        },
        "booz_candidate_count_gap": {
            "paper_candidate_gram_count": 8321,
            "latest_local_candidate_classes": stream["unique_candidate_classes"],
            "remaining_count_gap": 8321 - int(stream["unique_candidate_classes"]),
            "interpretation": (
                "Known high-tail witness compatibility is reconciled, but the full BOOZ "
                "candidate-Gram enumeration count is not yet reproduced."
            ),
        },
        "range_summaries": {
            "stream_missing_known_high_tail": ranges(sorted(high_tail - covered_by_stream)),
            "still_unaccounted_after_trace": ranges(sorted(still_unaccounted)),
        },
    }

    output_path = args.output or (sprint_dir / "outputs" / "order13_reconciliation.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "known_high_tail": len(high_tail),
        "stream_coverage": len(covered_by_stream),
        "trace_only": len(covered_by_trace_only),
        "reconciled": report["reconciled_known_high_tail_coverage"],
        "candidate_count_gap": report["booz_candidate_count_gap"],
    }, indent=2))


if __name__ == "__main__":
    main()
