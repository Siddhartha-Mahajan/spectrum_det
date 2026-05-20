# Sprint 8: repaired order-13 generator reconciliation

Date: 2026-05-21

## What This Sprint Is

Sprint 8 reconciles the repaired order-13 generator against known BOOZ high-tail witnesses.

Sprint 7 found the important `F`/`Gamma` update-order bug. Sprint 8 checks whether the patched logic is compatible with all 130 known high-tail determinant values, even when the candidate stream itself does not yet contain all of them.

## Main Files

- `witness_path_trace.py`: traces canonical witness paths through the repaired generator logic.
- `reconcile_order13.py`: combines stream coverage with path-trace coverage.
- `outputs/missing_witness_path_trace.json`: path-trace results for the six missing values from the sprint-7 stream.
- `outputs/order13_reconciliation.json`: reconciled status report.

## Result

The sprint-7 patched candidate stream covered 124/130 known high-tail determinant values.

The remaining six values were:

```text
2271, 2307, 2316, 2336, 2360, 2916
```

Sprint 8 showed that all six survive the repaired generator path checks. They are not rejected by:

- active-block structure;
- row ordering;
- block ordering;
- positive definiteness;
- KM/gamma bound;
- active-block `IsLexMax`.

## Current Meaning

Known witness compatibility is reconciled: 130/130.

The full BOOZ candidate count is not reconciled: BOOZ reports 8321 candidate Gram matrices, while local generated streams remain below that.

## Next

Do not spend more time proving that the known witnesses can pass some ordering. That is done.

The next order-13 task is to find the remaining generator-semantics mismatch that explains the missing candidate classes.
