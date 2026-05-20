# Sprint 9 results: n=12 complete witness pack

Date: 2026-05-21

Status: complete verified witness pack for the archived conjectural `S_12` present set.

## Commands

Sparse-tail pass:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python n12_witness_baseline.py
```

Low dense interval pass:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python n12_interval_witness_fill.py
```

Final dense interval completion:

```bash
/Users/siddhartha/Lossfunk/.venv/bin/python n12_complete_witness_pack.py
```

Outputs:

- `outputs/n12_tail_results.json`
- `outputs/n12_low_interval_fill_results.json`
- `outputs/n12_complete_witness_results.json`
- `outputs/n12_complete_witnesses.json`

## Result

The final combined witness pack verifies every value in the archived conjectural `S_12` present set.

Summary:

- conjectured spectrum size: 812 values including zero;
- total conjectured witnesses found: 812/812;
- missing conjectured values: none;
- values found outside the conjectured spectrum during these runs: 0;
- all reported witnesses verified exactly: yes.

The final covered range summary is:

`[0,738], [740,765], [767,769], [771,774], [776,777], [779,780], [783,786], [788,789], [792,793], 795, [797,798], [800,801], 805, 807, 810, 816, [818,819], 825, [832,833], 837, 840, 848, 864, 873, 882, 891, 896, 945, 972, 1024, 1053, 1215, 1458`.

## Interpretation

This handles the existence side of the archived conjecture:

- every conjectured present normalized value `s` has a stored 11 x 11 `(0,1)` block with `|det(block)| = s`;
- the corresponding 12 x 12 sign matrix verifies to `|det(R)| = 2048s`.

The remaining `n = 12` task is absence-side proof or certificate architecture for the 647 conjectured missing positive normalized values.
