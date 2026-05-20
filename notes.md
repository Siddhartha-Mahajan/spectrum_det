# Running notes: determinant spectrum exploration

Date: 2026-05-12

## User request
- Read exploration sprint PDF in this folder.
- Research the determinant spectrum problem for 12x12 {-1,1} matrices.
- Create a detailed problem.md with gathered context only; do not try to solve the problem.
- Create paper_pdfs/ containing PDFs and Markdown/text extractions for relevant papers.
- Report any paper that cannot be downloaded.
- User follow-up: keep these running notes; focus especially on https://arxiv.org/abs/1112.4160.

## Sprint PDF facts extracted
- Target problem: determine the complete set of possible absolute determinant values for 12x12 matrices with every entry in {-1,1}.
- Hadamard bound for n=12: max determinant is 12^6 = 2,985,984.
- Determinants are multiples of 2^(n-1)=2^11=2048, so the normalized positive spectrum has at most 2,985,984 / 2048 = 1458 positive values.
- Literature status stated in sprint: determinant spectrum solved for all n<12 and n=13; n=12 remains unsolved/conjectural.
- Standard approach in the sprint: search Gram matrices G = A A^T, prune by PSD constraints, then decompose candidate Gram matrices into {-1,1} matrices.
- Claimed obstruction for n=12: because n is even, row dot products can be zero; many zeros weaken constraints and the Gram-matrix search branches aggressively.
- Candidate AI/agentic directions mentioned in sprint: SAT+CAS architecture; inject mod-4 parity constraints like G_ij congruent to -2(r_i+r_j) mod 4.

## Web facts collected so far
- Maxdet archived site defines determinant spectrum for {-1,1} matrices as values of |det R_n| / 2^(n-1) over all n x n {-1,1} matrices.
- Maxdet archived site says spectra are known through n=11 and n=13, with conjectures up to n=22.
- Maxdet archived spectrum page says n<=7 has all integers between 0 and max normalized determinant; n=8 has gaps found by Metropolis, Stein, and Wells.
- Maxdet archived n=12 page is titled a conjectured spectrum; visible tail includes values ending at 1458.
- Maxdet archived n=13 page is marked complete and was recently proved complete by Brent, Orrick, Osborn, and Zimmermann.
- ArXiv 1112.4160 is "Maximal determinants and saturated D-optimal designs of orders 19 and 37" by Richard P. Brent, William Orrick, Judy-anne Osborn, Paul Zimmermann.
- Abstract of arXiv 1112.4160: uses two-step computation: search candidate Gram matrices, then decompose them; also finds complete determinant spectrum for {-1,1} matrices of order 13.

## Archived n=12 conjecture parsed
- Archived present normalized spectrum for n=12: {[0,738], [740,765], [767,769], [771,774], [776,777], [779,780], [783,786], [788,789], [792,793], 795, [797,798], [800,801], 805, 807, 810, 816, [818,819], 825, [832,833], 837, 840, 848, 864, 873, 882, 891, 896, 945, 972, 1024, 1053, 1215, 1458}.
- Parsed as normalized values in [0,1458], the conjecture contains 812 values including zero, 811 positive values, and 647 missing positive values.
- Conjectural missing normalized values: {739, 766, 770, 775, 778, [781,782], 787, [790,791], 794, 796, 799, [802,804], 806, [808,809], [811,815], 817, [820,824], [826,831], [834,836], [838,839], [841,847], [849,863], [865,872], [874,881], [883,890], [892,895], [897,944], [946,971], [973,1023], [1025,1052], [1054,1214], [1216,1457]}.
- To recover unnormalized determinants, multiply normalized values by 2048.

## Problem.md rewrite notes
- Rewrote problem.md on 2026-05-12 so it reads as an agent handoff brief instead of an exploration log.
- Kept in problem.md: problem statement, objective, normalization, current conjectural target, difficulty summary, short history, recommended starting point, and key local files.
- Kept in notes.md: detailed BOOZ mechanics, runtime/scale evidence, n=14 context, paper collection status, blocked-download details, and raw parsing notes.

## Cache cleanup notes
- Cleaned paper_pdfs on 2026-05-12 into paper_pdfs/pdfs/ and paper_pdfs/mds/.
- Kept PDFs: BOOZ 2011 arXiv 1112.4160, Orrick 2004/2005 order-15 paper, Zivkovic 2005/2006 small (0,1) matrix classification, Craigen 1990 range paper, and Komlos 1967 determinant paper.
- Kept Markdown notes/extractions: BOOZ, Orrick order-15, Zivkovic, Craigen, Komlos, and Metropolis NOT_DOWNLOADED.
- Removed from active cache as nonessential for getting started: BOOZ arXiv source dump, Orrick switching operations, Orrick D-optimal enumeration, Orrick-Solomon order 4k+1 paper, Orrick-Solomon-Dowdeswell-Smith lower-bound paper.
- Cleaned web_sources into web_sources/mds/ and kept only spectrum_main.md, spectrum12_conjectured.md, and spectrum13_complete.md.
- Removed archived HTML and the n=14 conjecture page from active cache; n=14 was useful during exploration but not needed for the first agent handoff.

## Agentic sprint notes
- Created agentic_sprints/README.md on 2026-05-12 to make the sprint rule explicit: one sprint folder should try one strategy only and contain its own strategy note, code, outputs, and result note.
- Moved the broad strategy menu into agentic_sprints/strategy_backlog.md; it is not a sprint.
- Refocused sprint_1 on witness generation for the known n=8 spectrum. The run found witnesses for every known normalized S_8 value {0,1,2,...,18,20,24,32}; outputs are in agentic_sprints/sprint_1/outputs/.
- Created sprint_2 for fixed-Gram decomposition. The run decomposed n=8 Hadamard, n=8 random, and n=12 random Grams, and rejected a deliberately inconsistent n=8 Gram; outputs are in agentic_sprints/sprint_2/outputs/.
- Created sprint_3 for order-13 witness-side replication. It found all 130 published high-tail values above the first gap 2173 and verified witnesses exactly; outputs are in agentic_sprints/sprint_3/outputs/.
- Created sprint_4 for the BOOZ-style Gram proof pipeline. It found that the public Brent/BOOZ page has compressed-format utilities and order-19/order-37 candidate data, but no linked order-13 directory and no published Gram-finding C/GMP source at the checked URLs. It now writes partial progress during supplied-Gram runs.
- Sprint_4 supplied-source verification validated all 130 high-tail Grams induced by sprint_3 witnesses and verified their source decompositions. A bounded independent decomposer sample hit the node cap, and the bounded principal-minor profiler hit its generation cap at depth 5.
- Created sprint_5 for a native Orrick/BOOZ-style candidate-Gram generator prototype. It implements C++ exact Bareiss determinants with `__int128`, odd-order Phi, recursive F/Gamma admissible-vector structure, Kounias-Moyssiadis bound pruning, JSON progress checkpoints, and JSONL candidate output. A 200000-node n=13 run reached depth 13 in about 85.6 seconds, wrote progress to agentic_sprints/sprint_5/outputs/km_200k/progress.json, and found no high-threshold candidates before the cap.
- Created sprint_6 for a paper-reproduction candidate-Gram generator attempt. It adds BOOZ-congruent n=13 entries `[1, -3, 5, -7, 9, -11]`, active-block canonical diagnostics, dynamic/constant `e_r` modes, KM/Hadamard bound modes, and a `pynauty`-backed weighted-Gram canonicalizer. The completed strict run produced 2057 candidate lines / 2055 nauty permutation classes, not BOOZ's 8321; it covered 75 of the 130 known sprint-3 high-tail values. An interrupted no-lexmax diagnostic produced 12245 raw lines and covered 102/130 values, confirming the unresolved issue is exact canonical generation rather than native arithmetic or the BOOZ-congruent value set.
- Created sprint_7 for a witness-driven filter audit and deeper paper/source search. The arXiv source package for 1112.4160 has only v1 and order-19/order-37 ancillary data, not order-13 candidate Grams or source. The key algorithm clue came from Orrick 2004 §3.2: after the gamma/KM bound passes, vector `f` is added to `F_{r-1}` before active-block `IsLexMax`. Sprint 6 had this update after lexmax, starving later `Gamma` lists. Patching `paper_reproduction_generator.cpp` improved strict-run diagnostics from 75/130 known high-tail values to 123/130 at 2M nodes and 124/130 in a long-run snapshot with 1429 candidate classes. The BOOZ 8321 count is still not reproduced.

## Need to do next
- Done this pass: problem.md drafted and later rewritten into a focused agent brief; BOOZ details folded into notes; Zivkovic/Craigen/Komlos downloaded or extracted; paper and web caches cleaned into lean subfolders; Metropolis remains not downloaded; sprint_1 through sprint_7 now contain runnable experiments or proof-pipeline artifacts.
- Superseded by 2026-05-21 continuation: sprint_8 completed repaired order-13 generator reconciliation; sprint_9 completed the `n = 12` conjectural witness pack. The next serious step is absence-side certificate architecture for `n = 12`.

## 2026-05-21 continuation notes
- Created sprint_8 for repaired order-13 generator reconciliation. It includes dynamic witness-path tracing of the six order-13 high-tail values missing from the sprint-7 long-run snapshot: `2271, 2307, 2316, 2336, 2360, 2916`.
- Sprint_8 result: all six canonical witness paths are accepted by the patched sprint-6 generator logic. None are rejected by active-block structure, row ordering, block ordering, positive definiteness, KM/gamma bound, or active-block `IsLexMax`. The patched candidate stream covers 124/130 known high-tail witness values, and the remaining 6 are accounted for by path trace, giving 130/130 known high-tail compatibility.
- Remaining order-13 gap: BOOZ reports 8321 candidate Gram matrices; the latest local canonical stream has 1429 classes. Full paper-level candidate enumeration is still not reproduced.
- Created sprint_9 for direct `n = 12` witness search via 11 x 11 `(0,1)` blocks. It combines sparse-tail search, low dense interval fill, and final dense interval completion.
- Current `n = 12` witness status: complete for the archived conjectural present set. `agentic_sprints/sprint_9/outputs/n12_complete_witnesses.json` contains verified witnesses for all 812 conjectured values including zero.
- Current `n = 12` proof status: absence side remains open. The next serious sprint should target exclusion/certificate architecture for the 647 conjectured missing positive normalized values, not more witness search.
- Created sprint_10 for order-13 generator optimization while the full sprint_8 reproduction run continues. The useful optimization replaces `std::set<Vec>` inside active-block `IsLexMax` with vector accumulation plus `sort`/`unique`; this keeps the 200k-node candidate stream byte-identical and improves that benchmark from 21.8835 s to 16.2072 s. An exact adjugate/incremental-determinant experiment was recorded but is slower with the current cofactor implementation.
- Sprint_10 full optimized run status: killed the slow single-process baseline and ran `run_parallel_reproduction.py` with 8 deterministic shards at shard depth 10. The run completed in 3662.1 seconds, tested 35,366,382 nodes, performed 4,213,266,303 gamma tests, wrote 2701 raw candidate lines, and canonicalized to 2626 candidate classes with 102 distinct normalized determinant values. Reconciliation gives 86/130 direct known high-tail coverage, 90/130 after the sprint-8 path-trace supplement, and a remaining count gap of 5695 classes versus the BOOZ paper's 8321 candidate count. Conclusion: runtime is much better, but exact generator semantics are still wrong or incomplete.

## BOOZ / arXiv 1112.4160 details
- Full title: Richard P. Brent, William P. Orrick, Judy-anne Osborn, Paul Zimmermann, "Maximal Determinants and Saturated D-optimal Designs of Orders 19 and 37" (arXiv:1112.4160).
- Scope: odd orders only; proves maximal determinants for n=19 and n=37, improves bounds for n=29,33,45,49,53,57, and gives the complete determinant spectrum for n=13.
- Normalization: D_n is max |det(R)| over n x n {-1,1} matrices; d_n = D_n / 2^(n-1). The determinant spectrum S_n is the set of |det(R_n)| / 2^(n-1).
- Candidate Gram matrix definition in BOOZ: symmetric positive definite; diagonal entries n; off-diagonal entries congruent to n mod 4; full candidate also has square determinant d^2 and d >= d_min.
- The congruence condition in BOOZ is stated for parity-normalized odd-order designs. For the n=12 problem, parity normalization and congruence behavior need to be handled carefully because n is even.
- Gram-finding pipeline: recursively extend candidate principal minors M_r by admissible vectors; prune partial matrices using allowable vectors gamma and enhanced Kounias-Moyssiadis determinant bounds.
- BOOZ Theorem 1 gives a determinant upper bound for completions of a fixed principal minor. They use a sharper bound for n congruent 3 mod 4; the paper says the sharp bound gave roughly 15% runtime improvement in their setting.
- Decomposition pipeline: take a complete list L of candidate Gram matrices up to Gram equivalence, then test whether some G decomposes as G = R R^T for a square {-1,1} matrix R.
- Decomposition is a row-building backtracking tree. The naive single-Gram constraint solves r_i r_j^T = g_ij; the improved version uses framings/frame variables to quotient repeated column patterns.
- Gram-pair constraints: since a complete list L should include a matrix H Gram-equivalent to R^T R, BOOZ considers pairs (G,H) with the same characteristic polynomial and tries to solve G = R R^T, H = R^T R.
- BOOZ uses constraints G^(j+1) = R H^j R^T. They found j=1 and j=2 useful, but j>2 not worth it in practice.
- BOOZ also discusses Hasse-Minkowski/rational quadratic-form equivalence as an indecomposability certificate; useful in some hard pairs but usually slower than backtracking.
- Order 13 proof: heuristic examples covered normalized determinants 0..2172; first gap was 2173. Gram-finding with d_min = 2173 * 2^12 produced 8321 candidate Gram matrices in 73 minutes. Decomposition took 48 seconds; 1643 candidates decomposed, giving 130 distinct determinants in [2174,3645].
- For n=13, BOOZ gives complete S_13 with max normalized determinant 3645. The archived maxdet site labels n=13 complete and n=12 conjectured.
- BOOZ compute scale examples: n=19 candidate search 826 single-processor hours for 9 Gram classes; n=37 candidate search 77 hours for 807 candidate Grams, then decomposition ruled out 806 quickly, while finding actual decompositions of the surviving Gram required randomized long runs.
- BOOZ section 7 notes n=29 candidate generation took about two processor-years for one upper-bound push and estimated about 220000 candidates for a tighter attempted bound. This is useful evidence for combinatorial explosion of the Gram search pipeline.

## BOOZ bibliography entries relevant to this task
- Metropolis 1971: N. Metropolis, "Spectra of determinant values in (0,1) matrices", in Computers in Number Theory, Academic Press, 1971, pp. 271-276. First computed n=8 spectrum/gaps.
- Craigen 1990: R. Craigen, "The range of the determinant function on the set of n x n (0,1)-matrices", J. Combin. Math. Combin. Comput. 8 (1990), 161-171. Non-computer proof that gaps exist.
- Zivkovic 2006: M. Zivkovic, "Classification of small (0,1) matrices", Linear Algebra Appl. 414 (2006), 310-346; arXiv math/0511636. Gives n=9 and n=10 spectrum/classification results per BOOZ.
- Orrick 2005: W. P. Orrick, "The maximal {-1,1}-determinant of order 15", Metrika 62 (2005), 195-219; arXiv math/0401179. Gives n=11 spectrum per BOOZ and is the precursor Gram-finding method.
- Orrick 2010 talk: "Range and distribution of determinants of binary matrices", Maximal Determinant Workshop, ANU, 17 May 2010; cited for heuristic low-determinant examples in the n=13 proof.

## Download status updates
- Downloaded and extracted Zivkovic 2005/2006 arXiv paper to paper_pdfs/pdfs/zivkovic_2005_classification_small_01_matrices.pdf and paper_pdfs/mds/zivkovic_2005_classification_small_01_matrices.md.
- User added Craigen 1990 PDF; renamed/extracted to paper_pdfs/pdfs/craigen_1990_range_determinant_function_01_matrices.pdf and paper_pdfs/mds/craigen_1990_range_determinant_function_01_matrices.md. Removed the obsolete Craigen NOT_DOWNLOADED note.
- User added Komlos 1967 PDF; renamed/extracted to paper_pdfs/pdfs/komlos_1967_on_determinant_of_01_matrices.pdf and paper_pdfs/mds/komlos_1967_on_determinant_of_01_matrices.md.
- Metropolis 1971 could not be downloaded: Internet Archive has the proceedings, but it is access-restricted and OCR/PDF derivatives are private; direct DjVu text download returned HTTP 401. Added a NOT_DOWNLOADED markdown note in paper_pdfs/mds/.

## Zivkovic paper notes
- Zivkovic works with A_n, the set of n x n (0,1) matrices, and D_n = {|det A| : A in A_n}. This is related to {-1,1} order n+1 determinants by the standard bordering map det(B) = 2^n det(A).
- Zivkovic states Craigen showed D_n is the interval {1,...,d_n} for n <= 6 but not for n = 7, because a_8 = 41 < d_8 = 56; Zivkovic confirms/suggests a_9 = 103.
- Table 2 in Zivkovic gives D_8 = {0-40, 42, 44, 45, 48, 56} and D_9 = {0-102, 104, 105, 108, 110, 112, 116, 117, 120, 125, 128, 144}; these align with the maxdet archived spectra after accounting for the (0,1) vs {-1,1} order shift.

## Paper collection status
The active paper cache is intentionally lean. It keeps the references needed to understand the n=12 determinant-spectrum task and start a first technical sprint:
- Kept downloaded/extracted: 1112.4160 Brent--Orrick--Osborn--Zimmermann, maximal determinants orders 19 and 37; includes complete order-13 spectrum and the main candidate-Gram/decomposition pipeline.
- Kept downloaded/extracted: math/0401179 Orrick, maximal {-1,1}-determinant of order 15; precursor Gram-finding method and n=11 spectrum reference.
- Kept downloaded/extracted: math/0511636 Zivkovic, classification of small (0,1) matrices; small-order determinant-range context.
- Kept downloaded/extracted: Craigen 1990, range of determinant function on n x n (0,1)-matrices; non-computer proof that gaps exist.
- Kept downloaded/extracted: Komlos 1967, on the determinant of (0,1) matrices; asymptotic nonsingularity context.
- Kept as blocked-download note: Metropolis 1971; see NOT_DOWNLOADED note in paper_pdfs/mds/.
- Removed from active cache after initial exploration: math/0507515, math/0511141, math/0311292, and math/0304410, because they are peripheral to a first n=12 spectrum sprint.
