#!/usr/bin/env python3
"""Fill a bounded interval of conjectured n=12 witness values."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np

SPRINT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SPRINT_DIR))

from n12_witness_baseline import (  # noqa: E402
    add_witness,
    block01_to_sign_matrix,
    compress_ranges,
    parse_spectrum12,
    target_search,
    verify_witnesses,
)

Matrix = list[list[int]]


def load_seed_witnesses(path: Path) -> dict[int, Matrix]:
    payload = json.loads(path.read_text())
    return {int(value): item["block01"] for value, item in payload.items()}


def run(args: argparse.Namespace) -> dict[str, Any]:
    sprint_dir = Path(__file__).resolve().parent
    root = sprint_dir.parents[1]
    targets = parse_spectrum12(root / "web_sources" / "mds" / "spectrum12_conjectured.md")
    interval_targets = sorted(value for value in targets if args.min_target <= value <= args.max_target)
    witnesses = load_seed_witnesses(sprint_dir / "outputs" / "n12_tail_witnesses.json")
    all_seen = set(witnesses)
    rng = np.random.default_rng(args.seed)
    target_stats: dict[str, dict[str, int | bool]] = {}
    start = time.perf_counter()

    for _ in range(args.random_samples):
        block = rng.integers(0, 2, size=(11, 11), dtype=np.int8)
        value = add_witness(witnesses, block, targets)
        all_seen.add(value)
        if all(value in witnesses for value in interval_targets):
            break

    missing_after_sampling = [value for value in interval_targets if value not in witnesses]
    for target in missing_after_sampling:
        block, stats = target_search(target, 11, rng, args.target_restarts, args.target_steps, args.kicks)
        target_stats[str(target)] = stats
        if block is not None:
            value = add_witness(witnesses, block, targets)
            all_seen.add(value)

    interval_found = sorted(value for value in interval_targets if value in witnesses)
    interval_missing = sorted(value for value in interval_targets if value not in witnesses)
    contradiction_candidates = sorted(value for value in all_seen if value not in targets)
    verified = verify_witnesses({value: witnesses[value] for value in sorted(witnesses)})
    elapsed = time.perf_counter() - start

    output_dir = sprint_dir / "outputs"
    output_dir.mkdir(exist_ok=True)
    witness_payload = {
        str(value): {
            "normalized_value": value,
            "block01": witnesses[value],
            "sign_matrix": block01_to_sign_matrix(witnesses[value]),
        }
        for value in sorted(witnesses)
    }
    (output_dir / "n12_witnesses_extended.json").write_text(json.dumps(witness_payload, indent=2) + "\n")

    result = {
        "seed": args.seed,
        "min_target": args.min_target,
        "max_target": args.max_target,
        "interval_target_count": len(interval_targets),
        "random_samples": args.random_samples,
        "target_restarts": args.target_restarts,
        "target_steps": args.target_steps,
        "kicks": args.kicks,
        "seed_witness_count": len(load_seed_witnesses(sprint_dir / "outputs" / "n12_tail_witnesses.json")),
        "total_witness_count": len(witnesses),
        "interval_found_count": len(interval_found),
        "interval_missing_count": len(interval_missing),
        "interval_found_ranges": compress_ranges(interval_found),
        "interval_missing_values": interval_missing,
        "interval_missing_ranges": compress_ranges(interval_missing),
        "contradiction_candidate_count": len(contradiction_candidates),
        "contradiction_candidates": contradiction_candidates,
        "target_search_stats": target_stats,
        "all_reported_witnesses_verified": all(verified.values()),
        "elapsed_seconds": elapsed,
    }
    (output_dir / "n12_interval_fill_results.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260522)
    parser.add_argument("--min-target", type=int, default=0)
    parser.add_argument("--max-target", type=int, default=300)
    parser.add_argument("--random-samples", type=int, default=150000)
    parser.add_argument("--target-restarts", type=int, default=20)
    parser.add_argument("--target-steps", type=int, default=120)
    parser.add_argument("--kicks", type=int, default=4)
    return parser.parse_args()


def main() -> None:
    result = run(parse_args())
    print(json.dumps({
        "interval": [result["min_target"], result["max_target"]],
        "interval_found_count": result["interval_found_count"],
        "interval_missing_count": result["interval_missing_count"],
        "total_witness_count": result["total_witness_count"],
        "contradiction_candidate_count": result["contradiction_candidate_count"],
        "all_reported_witnesses_verified": result["all_reported_witnesses_verified"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
