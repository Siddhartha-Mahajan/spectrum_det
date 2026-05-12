# Sprint 3 results: order-13 witness-side replication

Date: 2026-05-12

Status: completed.

Command run:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python n13_witness_replication.py --random-samples 200000 --target-restarts 80 --target-steps 220 --gap-restarts 80 --seed 20260512
```

Outputs:

- outputs/n13_results.json
- outputs/n13_witnesses.json

## Result summary

- Parsed BOOZ/maxdet complete n=13 spectrum size: 2303 normalized values.
- Low interval: 0 through 2172.
- First gap after low interval: 2173.
- Published high-tail values above 2173: 130.
- Random 12 x 12 (0,1) sampling found 217 low-interval witnesses and no high-tail witnesses.
- Targeted bit-flip local search found all 130 published high-tail values.
- The 2173 negative-control search did not find a witness; nearest value found was 2172, distance 1.
- Every retained target witness was verified exactly with Bareiss determinant arithmetic.
- Runtime for the recorded run: about 52.1 seconds.

## Interpretation

This reproduces the witness/existence side of the BOOZ order-13 theorem for the high tail: every published high-tail determinant value has an explicit verified 12 x 12 (0,1) block, hence a normalized 13 x 13 {-1,1} determinant witness.

This is not the full BOOZ proof. It does not prove 2173 or any other missing high-tail value absent. The missing-value proof requires the candidate-Gram enumeration/decomposition layer.
