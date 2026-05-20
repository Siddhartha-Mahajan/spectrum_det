#!/usr/bin/env python3
"""Run sharded optimized order-13 reproduction workers and merge outputs."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def write_summary(output_dir: Path, workers: int, processes: list[subprocess.Popen[bytes]], start: float) -> dict[str, Any]:
    worker_summaries = []
    totals = {
        "nodes_tested": 0,
        "recursion_calls": 0,
        "gamma_tests": 0,
        "lexmax_checks": 0,
        "lexmax_permutations_seen": 0,
        "candidates_written": 0,
        "candidate_lines": 0,
        "shard_skipped": 0,
    }

    for index in range(workers):
        worker_dir = output_dir / f"worker_{index:02d}"
        progress = load_json(worker_dir / "progress.json")
        candidate_lines = count_lines(worker_dir / "candidates.jsonl")
        summary = {
            "worker": index,
            "pid": processes[index].pid if index < len(processes) else None,
            "returncode": processes[index].poll() if index < len(processes) else None,
            "candidate_lines": candidate_lines,
            "progress": progress,
        }
        worker_summaries.append(summary)
        for key in totals:
            if key == "candidate_lines":
                totals[key] += candidate_lines
            else:
                totals[key] += int(progress.get(key, 0) or 0)

    report = {
        "workers": workers,
        "elapsed_seconds": time.perf_counter() - start,
        "all_done": all(process.poll() is not None for process in processes),
        "all_ok": all(process.poll() == 0 for process in processes),
        "totals": totals,
        "worker_summaries": worker_summaries,
    }
    (output_dir / "parallel_progress.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def merge_candidates(output_dir: Path, workers: int) -> None:
    merged_path = output_dir / "candidates.jsonl"
    with merged_path.open("w") as merged:
        for index in range(workers):
            candidate_path = output_dir / f"worker_{index:02d}" / "candidates.jsonl"
            if not candidate_path.exists():
                continue
            with candidate_path.open() as handle:
                for line in handle:
                    if line.strip():
                        merged.write(line)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 8))
    parser.add_argument("--shard-depth", type=int, default=10)
    parser.add_argument("--max-nodes", type=int, default=0)
    parser.add_argument("--progress-every", type=int, default=250000)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/parallel_full_20260521"))
    parser.add_argument("--binary", type=Path, default=Path("./optimized_reproduction_generator"))
    parser.add_argument("--poll-seconds", type=float, default=30.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    binary = args.binary.resolve()
    if not binary.exists():
        raise SystemExit(f"binary not found: {binary}")

    processes: list[subprocess.Popen[bytes]] = []
    start = time.perf_counter()
    for index in range(args.workers):
        worker_dir = output_dir / f"worker_{index:02d}"
        worker_dir.mkdir(parents=True, exist_ok=True)
        command = [
            str(binary),
            "--order", "13",
            "--threshold-normalized", "2173",
            "--max-nodes", str(args.max_nodes),
            "--progress-every", str(args.progress_every),
            "--shard-count", str(args.workers),
            "--shard-index", str(index),
            "--shard-depth", str(args.shard_depth),
            "--output-dir", str(worker_dir),
        ]
        log_path = worker_dir / "worker.log"
        log_handle = log_path.open("wb")
        process = subprocess.Popen(command, stdout=log_handle, stderr=subprocess.STDOUT)
        processes.append(process)

    try:
        while True:
            report = write_summary(output_dir, args.workers, processes, start)
            totals = report["totals"]
            print(json.dumps({
                "elapsed_seconds": round(report["elapsed_seconds"], 1),
                "all_done": report["all_done"],
                "nodes_tested": totals["nodes_tested"],
                "candidate_lines": totals["candidate_lines"],
                "gamma_tests": totals["gamma_tests"],
            }), flush=True)
            if report["all_done"]:
                break
            time.sleep(args.poll_seconds)
    except KeyboardInterrupt:
        for process in processes:
            if process.poll() is None:
                process.terminate()
        raise

    report = write_summary(output_dir, args.workers, processes, start)
    if not report["all_ok"]:
        raise SystemExit("one or more workers failed; inspect worker_*/worker.log")
    merge_candidates(output_dir, args.workers)
    final = write_summary(output_dir, args.workers, processes, start)
    final["merged_candidate_lines"] = count_lines(output_dir / "candidates.jsonl")
    (output_dir / "parallel_summary.json").write_text(json.dumps(final, indent=2) + "\n")
    print(json.dumps({
        "done": True,
        "elapsed_seconds": round(final["elapsed_seconds"], 1),
        "merged_candidate_lines": final["merged_candidate_lines"],
        "totals": final["totals"],
    }, indent=2))


if __name__ == "__main__":
    main()
