# Sprint 9: n=12 complete witness pack

Date: 2026-05-21

## Strategy

Build a verified witness pack for the full archived conjectural `S_12` present set.

With first row and first column normalized to `+1`, every 12 x 12 sign matrix corresponds to an 11 x 11 `(0,1)` block. The absolute determinant of that block is exactly the normalized determinant value `|det(R)| / 2^11`.

This sprint combines the earlier witness-search passes into one larger workflow:

1. sparse-tail search for all conjectured values above 738;
2. low dense interval fill for `[0,300]`;
3. dense interval completion for `[301,738]`;
4. exact verification of every stored witness against the corresponding 12 x 12 sign determinant.

## Success criterion

Produce a single combined witness file containing all 812 conjectured normalized `n = 12` values, with exact verification.
