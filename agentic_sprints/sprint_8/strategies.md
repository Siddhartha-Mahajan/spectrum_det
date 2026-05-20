# Sprint 8: order-13 repaired-generator reconciliation

Date: 2026-05-21

## Strategy

Consolidate the order-13 BOOZ reproduction work after the `F`/`Gamma` update-order repair.

This sprint has three parts:

1. Trace the six high-tail witness values still missing from the patched sprint-7 candidate stream:
   `2271, 2307, 2316, 2336, 2360, 2916`.
2. Check whether those witnesses are rejected by the live repaired generator path or merely absent because the long run was stopped before reaching the relevant branches.
3. Reconcile stream coverage, traced-witness coverage, and the remaining gap to BOOZ's reported 8321 candidate Gram matrices.

## Success criterion

Produce a single order-13 status artifact that separates:

- known high-tail witness compatibility;
- current candidate-stream coverage;
- the still-unreproduced full candidate-Gram enumeration count.
