# Sprint 9: complete n = 12 conjectural witness pack

Date: 2026-05-21

## What This Sprint Is

Sprint 9 moves from order 13 back to the actual target problem: the conjectured determinant spectrum for `n = 12`.

The goal here is witness-side only: find exact `{ -1, 1 }` matrices for every determinant value that the archived maxdet page claims is present.

## Main Files

- `n12_witness_baseline.py`: baseline witness search.
- `n12_interval_witness_fill.py`: interval fill pass.
- `n12_complete_witness_pack.py`: final completion and verification pass.
- `outputs/n12_complete_witnesses.json`: verified witness library.
- `outputs/n12_complete_witness_results.json`: final summary.

## Result

The sprint found and verified witnesses for all 812 conjectured present normalized values, including zero.

Final output summary:

- found conjectured count: 812;
- missing conjectured count: 0;
- total witness count: 812;
- all reported witnesses verified: true.

## Current Meaning

The presence side of the archived `n = 12` conjecture is now locally reproducible.

This does not prove the conjectured spectrum, because the hard half is the absence side: proving that the 647 conjectured missing positive normalized values cannot occur.

## Next

The next serious `n = 12` sprint should target exclusion/certificate architecture for the 647 missing values.
