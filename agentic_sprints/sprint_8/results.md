# Sprint 8 results: order-13 repaired-generator reconciliation

Date: 2026-05-21

Status: known order-13 high-tail witness compatibility is fully reconciled; the full BOOZ candidate count is still not locally reproduced.

## Commands

Trace the six missing known high-tail witness paths:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python witness_path_trace.py
```

Reconcile trace coverage with the patched candidate stream:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python reconcile_order13.py
```

Outputs:

- `outputs/missing_witness_path_trace.json`
- `outputs/order13_reconciliation.json`

## Result

The patched sprint-7 stream covers 124 of the 130 known BOOZ order-13 high-tail witness values.

The six missing values were:

`2271, 2307, 2316, 2336, 2360, 2916`.

All six canonical witness paths were accepted by the repaired generator logic. They were not rejected by active-block structure, row order, block order, positive definiteness, the KM/gamma bound, or active-block `IsLexMax`.

Reconciled status:

- known high-tail values: 130;
- covered by latest patched stream: 124;
- accepted by path trace only: 6;
- still unaccounted known high-tail values: 0.

## Remaining gap

This sprint does not reproduce the full BOOZ paper count of 8321 candidate Gram matrices. The latest local canonical stream has 1429 classes, leaving a count gap of 6892 classes.

The next order-13 task is not another witness audit. It is a full patched generator run to completion, with enough checkpointing or runtime budget to determine whether the local generator reaches BOOZ's 8321 candidate count.
