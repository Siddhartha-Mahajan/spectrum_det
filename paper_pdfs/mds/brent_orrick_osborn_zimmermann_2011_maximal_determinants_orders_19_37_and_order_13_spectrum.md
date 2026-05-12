# Extracted text: brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.pdf

Source PDF: brent_orrick_osborn_zimmermann_2011_maximal_determinants_orders_19_37_and_order_13_spectrum.pdf

Pages: 28



## Page 1

arXiv:1112.4160v1  [math.CO]  18 Dec 2011
Maximal Determinants and Saturated D-optimal
Designs of Orders 19 and 37
Richard P. Brent
Mathematical Sciences Institute,
Australian National University,
Canberra, ACT 0200, Australia
maxdet@rpbrent.com
William Orrick
Department of Mathematics,
Indiana University,
Bloomington, IN 47405, USA
worrick@indiana.edu
Judy-anne Osborn
University of Newcastle,
Callaghan, NSW 2308, Australia
Judy-anne.Osborn@anu.edu.au
Paul Zimmermann
INRIA Nancy – Grand Est,
Villers-l` es-Nancy, France
Paul.Zimmermann@inria.fr
October 1, 2018
Abstract
A saturated D-optimal design is a {+1, − 1} square matrix of given
order with maximal determinant. We search for saturated D-optim al
designs of orders 19 and 37, and ﬁnd that known matrices due to
Smith, Cohn, Orrick and Solomon are optimal. For order 19 we ﬁnd all
inequivalent saturated D-optimal designs with maximal determinant ,
230 × 72 × 17, and conﬁrm that the three known designs comprise a
complete set. For order 37 we prove that the maximal determinant
is 2 39 × 336, and ﬁnd a sample of inequivalent saturated D-optimal
designs. Our method is an extension of that used by Orrick to resolv e
the previously smallest unknown order of 15; and by Chadjipantelis,
Kounias and Moyssiadis to resolve orders 17 and 21. The method is a
two-step computation which ﬁrst searches for candidate Gram ma trices
and then attempts to decompose them. Using a similar method, we
also ﬁnd the complete spectrum of determinant values for {+1, − 1}
matrices of order 13.
1 Introduction
The Maximal Determinant problem of Hadamard [12, 22] asks fo r the largest
possible determinant of an n× n matrix whose entries are drawn from the set
{+1, − 1}. We are only interested in the absolute value of the determin ant,
since we can always change the sign of the determinant by chan ging the sign
of a row. The problem in its full generality has been open sinc e ﬁrst posed by
1



## Page 2

Hadamard [12], and has applications to areas such as Experim ental Design
and Coding Theory.
We could equally well consider {0, 1} matrices. There is a well-known
mapping [25] from {0, 1}(n− 1)× (n− 1) matrices to {+1, − 1}n× n matrices which
multiplies the determinant by ( − 2)n− 1, and vice versa. To avoid confusion
we only consider {+1, − 1} matrices. Their determinants are always divisible
by 2 n− 1, thanks to the correspondence with {0, 1} matrices. Thus, it is
convenient to let Dn denote max |det(R)|, where the maximum is over all
{+1, − 1}n× n matrices R, and dn = Dn/ 2n− 1.
There is an extensive literature on the Maximal Determinant problem,
which splits into four cases, according to the value of n mod 4. A general
upper bound of
Dn ≤ nn/ 2 (1)
on the maximal determinant applies to all the four cases, but is not achiev-
able unless n = 1 , 2, or n ≡ 0 mod 4. The conjecture that this bound is
always achievable when n ≡ 0 (mod 4) is known as the Hadamard Conjec-
ture, and has been the subject of much investigation, see for exam ple [11, 13].
Smaller upper bounds are known for each of the other three equ ivalence
classes modulo four.
A bound which holds for all odd orders, and which is known to be sharp
for an inﬁnite sequence of orders congruent to 1 (mod 4), is
Dn ≤
√
(n − 1)n− 1(2n − 1), (2)
due independently to Ehlich [9] and Barba [1]. A smaller uppe r bound, due
to Ehlich [10], applies only in the case n ≡ 3 (mod 4):
Dn ≤
√
(n − 3)n− s(n − 3 + 4r)u(n + 1 + 4r)v
(
1 − ur
n− 3+4r − v(r+1)
n+1+4r
)
.
(3)
Here s = 3 for n = 3 (and the factor ( n − 3)(n− s) is interpreted as 1 in this
case), s = 5 for n = 7, s = 6 for 11 ≤ n ≤ 59, s = 7 for n ≥ 63, r = ⌊n/s ⌋,
v = n − rs, and u = s − v. The complicated form of the bound (3) as
compared with (2) is indicative of the extra diﬃculties whic h often seem to
arise when n ≡ 3 (mod 4). The bound (3) is sharp when n = 3; it is not
known if it is sharp for any n > 3.
In this work we settle the smallest hitherto unresolved case of n = 19.
This case has remained open despite higher orders (for examp le, 21) being
solved by similar methods, mainly because the use of (2) and i ts generali-
sation when the Gram matrix has a ﬁxed block—see Theorem 1—is much
more eﬀective in pruning the search tree than are (3) and its ge neralisations.
All orders congruent to 3 mod 4 and larger than 19 are currentl y open.
In this paper we only consider odd orders. The smallest unres olved
orders which are congruent to 1 mod 4 are n = 29 , 33 and 37. Of these,
2



## Page 3

we resolve n = 37, and improve the upper bounds for n = 29 , 33. For a
summary, see Table 1 in §7.
Our method is structurally similar to that used for n = 15 by Orrick [18],
and by earlier authors for n = 17 in [17] and n = 21 in [4]. There are two
essential steps, Gram ﬁnding and decomposition. In the case s we consider,
decomposition by hand would be tedious for n = 19, and infeasible for
larger orders. Thus, we implement a back-tracking computer search to deal
with this second step, describing such an algorithm for the ﬁ rst time in the
literature.
Our Gram-ﬁnding algorithm is discussed in §3, and our decomposition
algorithms in §4. The results for order 19 are described in §5, and for
order 37 in §6. In §7 we give some new upper and lower bounds for various
odd orders. For orders n = 29, 33, 45, 49, 53 and 57 we have not been able
to determine Dn precisely, but we have reduced the gap between the known
upper and lower bounds. Finally, in §8 we also ﬁnd the complete spectrum
of determinant values for {+1, − 1} matrices of order 13. Previously, the
spectrum was only known for orders up to 11.
2 Deﬁnitions
Z denotes the integers, and N1 the positive integers. The following deﬁ-
nitions are largely taken from [18], to which we refer for fur ther technical
deﬁnitions.
Deﬁnition 1. A design is an m × n matrix with entries drawn from the set
{+1, − 1}. If m = n the design is called saturated. If the absolute value of
the determinant of the saturated design is maximal for its or der, the design
is called D-optimal.
In this paper we consider saturated D-optimal designs of odd order. It is
convenient to consider “normalized” designs, leading to th e next deﬁnition:
Deﬁnition 2. A vector with elements in {+1, − 1} is parity normalized iﬀ
it has an even number of positive elements. A design is parity normalized
iﬀ all its rows and columns are parity normalized.
It is easy to show, as in [9, Lemmas 3.1, 3.2], that any saturat ed design
of odd order can be converted to a unique parity normalized ma trix by a
series of negations of rows and columns.
If R1 is a design, then any signed permutation of the rows and colum ns
of R1 gives another design R2, which we can regard as equivalent to the
original design since |det(R1)| = |det(R2)|. We can also change the signs
of any rows and/or columns of without changing more than the s ign of
the determinant. This suggests the following deﬁnition, in which a signed
permutation matrix is a permutation of the rows or columns of a diagonal
matrix diag( ± 1, ± 1, . . . , ± 1).
3



## Page 4

Deﬁnition 3. Two designs R and S are Hadamard equivalent iﬀ S = P RQ
for some pair of signed permutation matrices (P, Q ).
Deﬁnition 4. If R is a design, then G = RRT is called the Gram matrix
of R, and H = RT R is called the dual Gram matrix of R.
Deﬁnition 5. Two symmetric matrices G1 and G2 are Gram equivalent iﬀ
G1 = P G2P T for some signed permutation matrix P .
Deﬁnition 6. Let dmin > 0 and let Mn,p be the set of square matrices M ,
of order p, 1 ≤ p ≤ n, satisfying properties 1–3 below.
1. M is symmetric and positive deﬁnite;
2. Mi,i = n;
3. Mi,j ≡ n (mod 4) .
A matrix M ∈ M n,p is called a candidate principal minor . If, further-
more, n = p and the following additional properties 4–5 hold:
4. det(M ) = d2 for d ∈ Z;
5. d ≥ dmin;
then M is called a candidate Gram matrix .
It is clear that Properties 1, 2, 4 and 5 of candidate Gram matr ices are
satisﬁed by all Gram matrices. Furthermore, Property 3 of ca ndidate Gram
matrices holds for Gram matrices G = RRT if R is assumed to be parity
normalized.
4



## Page 5

3 Gram-ﬁnding Algorithm
We summarize our Gram-ﬁnding algorithm below. The method is essentially
that described in greater detail in [18]. We search for candi date Gram
matrices whose determinant is greater than or equal to a posi tive parameter
d2
min.
1. Set r = 1 and start from the candidate principal minor M1 = (n).
2. Increment r. Build a list of admissible vectors f , and allowable vec-
tors γ (for details see [18]).
3. For each possible lexicographically maximal matrix Mr− 1 of order r− 1,
and each admissible vector f , construct the matrix
Mr =
[ Mr− 1 f
f T n
]
. (4)
If r = n,
(a) if det( Mr) = d2 ≥ d2
min, output the candidate Gram matrix Mr.
If r < n ,
(b) evaluate
d =
⏐
⏐
⏐
⏐
Mr γ
γT 1
⏐
⏐
⏐
⏐ (5)
for each allowable vector γ, looking for a “good d”, namely d
such that the function ur in Theorem 1 satisﬁes ur(1, d ) ≥ d2
min.
If a good d is found, try to extend Mr by recursively calling the
algorithm (starting at step 2).
Pruning at step 3(b) of the above algorithm relies on the foll owing Theo-
rem, originally used by Moyssiadis and Kounias [17] to ﬁnd a m aximal Gram
matrix of order n = 17. Our version below contains a sharper bound (9)
applicable when n ≡ 3 (mod 4).
5



## Page 6

Theorem 1. [Enhanced Kounias & Moyssiadis] Let M =
[ Mr B
BT A
]
be a
symmetric, positive deﬁnite matrix of order n with elements taken from a set
Φ whose members are greater than or equal in magnitude to some n umber
c, 0 < c ≤ n. Here Mr is a candidate principal minor of order r ≤ n, and
A is a square matrix of order n − r, with diagonal elements Ai,i = n. The
columns of the r × (n− r) matrix B are taken from some set Γr ⊆ Φr. Deﬁne
d∗ and γ∗ by
d∗ =
⏐
⏐
⏐
⏐
Mr γ∗
γ∗ T c
⏐
⏐
⏐
⏐ = max
γ ∈ Γr
⏐
⏐
⏐
⏐
Mr γ
γT c
⏐
⏐
⏐
⏐ . (6)
Then
det(M ) ≤ ur(c, d ∗), (7)
where
ur(c, d ) = ( n − c)n− r− 1 [(n − c) det(Mr) + (n − r) max(0, d )] .
Furthermore, if n ≡ 3 (mod 4) , then the following bounds apply:
det(M ) ≤ (n − 1)n− r det(Mr) + (8)
[(n − 1)n− r − (n − 3)n− r − (n − r)(n − 3)n− r− 1] max(0, d ∗)
and, assuming det Mr > (n − 3) det Mr− 1,
det(M ) ≤ max
k
max
b1,...,b k∈ N1
b1+... +bk=n− r
max
γ ∗
1 ,...,γ ∗
k ∈ Γr
det





Mr
γ∗
1jT
b1 · · · γ∗
kjT
bk
jb1γ∗
1
T (n − 3)Ib1 + 3Jb1 · · · − Jb1,b k
.
.
.
.
.
. . . . .
.
.
jbk γ∗
k
T
− Jbk,b 1 · · · (n − 3)Ibk + 3Jbk




 (9)
where Mr− 1 is the principal (r − 1)-by-(r − 1) minor of Mr, ja is the column
vector of dimension a whose elements all equal 1, Ja,b is the a-by-b matrix
whose elements all equal 1, and Ja = Ja,a .
Proof. For a proof of inequalities (7) and (8) we refer to [18, Theore m 3.1
and Corollary 3.3]. A proof of (9) is sketched in the Appendix .
The bound (9) is sharp and therefore potentially much more po werful
than (7) or (8). Unfortunately, the multidimensional searc h for the optimal
set of block sizes ( b1, . . . , b k), and the optimal set of vectors, {γ∗
j } is expen-
sive. We therefore restricted its use to the situation where the non-diagonal
elements of the last column of Mr all equal − 1. This allows us to assume
that all γ∗
j consist entirely of elements − 1, and we are left only with the
search for the optimal partition. Much of the computation as sociated with
the latter search need only be done once. The use of (9) result ed in an
approximately 15% improvement in running time.
6



## Page 7

4 Decomposition Algorithm
The output of the program described in the previous section i s a list L
of candidate Gram matrices, complete in the sense that it con tains one
representative of each Gram equivalence class with determi nant ≥ d2
min for
a given bound dmin. We need to determine if any G ∈ L decomposes as
a product G = RRT for some square {+1, − 1} matrix R. This section
describes several algorithms for carrying out this task.
For each candidate G this involves a (possibly large) combinatorial search.
It may be regarded as searching a tree, where each level of the tree corre-
sponds to one row of the matrix R. At level k we know k − 1 rows of R and
try to ﬁnd a k-th row satisfying the constraints. Each node at the k-th level
corresponds to one possible choice of the k-th row of R, given the preceding
rows. If G = RRT has solutions, then the solution matrices, R, correspond
to nodes at level n of the tree. In principle our procedure may generate
many Hadamard-equivalent solutions. We prune the tree so as to limit the
number of duplicate solutions produced.
The search algorithm relies on a family of constraints. The z eroth mem-
ber of the family is a special case which can be implemented wi th a single
Gram matrix and we call this constraint the single-Gram constraint. The
rest of the family require both the Gram matrix G = RRT and the dual
Gram matrix H = RT R and we call these Gram-pair constraints.
Our decomposition algorithm diﬀers from that described in [1 8] in several
respects. First, it builds up R by rows, instead of by rows and columns
simultaneously. Second, it uses more general Gram-pair con straints (see (14)
with j ≥ 2 below).
For clarity, we ﬁrst describe a version of the algorithm whic h uses only
the single-Gram constraint.
4.1 Decomposition using only the single-Gram constraint
Denote the elements of G by gi,j for i, j = 1 , .., n , and the rows of R by ri
for i = 1, . . . , n . Then the constraint RRT = G is equivalent to
rirT
j = gi,j (10)
for 1 ≤ i ≤ j ≤ n. The search tree is created by application of these
constraints. An outline of the basic algorithm is as follows . The main work
is done by a recursive procedure search(k) which searches an (implicit)
subtree at level k, where the root is at level 1.
7



## Page 8

Algorithm using the single-Gram constraint, version 1
1. Initialize level k = 1, ﬁrst row r1 = (1, 1, . . . , 1) and R = r1.
2. Call search(k).
3. Output “no solution” and halt.
4. search(k): If k = n, output the solution R and halt. Otherwise incre-
ment k. Find all solutions rk ∈ { +1, − 1}n of the (under-determined)
set of simultaneous linear equations:





r1
r2
.
.
.
rk− 1




 rT
k =





g1,k
g2,k
.
.
.
gk− 1,k





For each solution rk, append rk to R and call search(k) recursively
to search the relevant subtree. Return to the caller (i.e. ba cktrack).
We justify the choice of the ﬁrst row in the above algorithm by observing
that G = RRT is invariant under a signed permutation of columns of R, i.e.
R ↦→ RP for any signed permutation matrix P .
The above algorithm considers a large number of equivalent p artial so-
lution matrices R, and is impractical for all but very small orders. We can
obtain a vastly more eﬃcient algorithm by imposing an orderi ng constraint
on the +1’s and − 1’s in row-vectors. We do this by deﬁning the concept
of “framings” and a new set of associated variables called “f rame variables”
which we use in Step 4 instead of rk. We ﬁrst deﬁne these terms, and then
give an improved version of the algorithm.
At each level k, we create a partition of the indices {1, . . . , n } into frames,
where a frame is a nonempty contiguous set of indices; and the collection
of frames is called a framing. A framing of size m is deﬁned by a frame-
widths vector w = ( w1, . . . , w m) ∈ Nm
1 , ∑ wi = n, where wi is the size of
the i-th frame. At level 1 the framing consists of a single frame {1, . . . , n }
with frame-width vector w = ( n). At each subsequent level, the framing
is a reﬁnement of the framing from the previous level. We use t he framing
at level k − 1 to deﬁne the frame variables that we use at level k in the
following algorithm. The frame variable xi gives the number of +1 entries
in the k-th row of R, considering only the column indices given by the i-th
frame. Thus, the number of − 1 entries is wi − xi and the sum of the entries
is 2 xi − wi (see equation (11)).
8



## Page 9

Algorithm using the single-Gram constraint, version 2
1. Initialize the level k = 1, the frame-size m = 1 and the frame-width-
vector w = ( w1) = ( n). Set q1 = (+1) and Q = q1. [In the course
of the algorithm, qi is a column vector of size k − 1 or k, and Q is a
matrix whose columns depend on the qi. Also, w may be thought of
as a vector of weights corresponding to the columns of Q.]
2. Call search(k).
3. Output “no solution” and halt.
4. search(k): If k = n, output the solution Q and halt [here m = n].
Otherwise increment k.
Deﬁne integer variables x1, x 2, . . . , x m. Find all solutions to the fol-
lowing integer programming problem:
Q





2x1 − w1
2x2 − w2
.
.
.
2xm − wm




 =





g1,k
g2,k
.
.
.
gk− 1,k




 (11)
subject to
0 ≤ xi ≤ wi for 1 ≤ i ≤ m. (12)
For each solution, update w and Q as follows:
(a) Let w := (x1, w 1 − x1, x 2, w 2 − x2, . . . , x m, w m − xm).
(b) Recall that Q = ( q1, q 2, ..., q m) is a matrix of column vectors qi,
each of length k − 1. Update Q to a k × 2m matrix as follows:
Q :=
[ q1 q1 q2 q2 · · · qm qm
+1 − 1 +1 − 1 · · · +1 − 1
]
.
(c) Compress Q by removing all columns which correspond to zeros
in w.
(d) Compress w by removing all zero entries.
(e) Set m := length(w).
Call search(k) recursively to search the relevant subtree. When all
solutions have been processed, return to the caller (i.e. ba cktrack).
In procedure search(k) of version 2 we use Gaussian elimination with col-
umn pivoting in order to ﬁnd a ( k − 1) × (k − 1) nonsingular minor of Q
(this is always possible, since the Gram matrix G is positive deﬁnite). We
then solve for the corresponding k − 1 basic variables in terms of the re-
maining m − k + 1 non-basic variables. The non-basic variables are chosen
9



## Page 10

exhaustively as integers in the appropriate intervals give n by (12); the basic
variables are then determined uniquely (as real numbers). I f the non-basic
variables are not in Z or violate the bounds (12), the solution is discarded.
It is preferable to choose as non-basic variables the variab les with the small-
est upper bounds wi, provided that the resulting ( k − 1) × (k − 1) minor is
nonsingular. A heuristic for accomplishing this is to weigh t the columns in
proportion to the bounds wi before performing the Gaussian elimination.
We illustrate an iteration of the algorithm with an example. Consider
the case n = 7 and the candidate Gram matrix (here and elsewhere we may
abbreviate “ − 1” by “ − ”):
G =










7 3 − − − − −
3 7 − − − − −
− − 7 3 − − −
− − 3 7 − − −
− − − − 7 3 −
− − − − 3 7 −
− − − − − − 7










.
Suppose we are at level k = 3 in the search. At this stage the search
tree has not branched yet, so there is just one matrix Q:
Q =


1 1 1 1
1 1 − −
1 − 1 −


Associated with Q is the frame-widths vector (at depth 3) which is
w = (2, 3, 1, 1).
We comment that, translated into the language of the algorit hm in version 1,
Q and w together correspond to a 3 × 7 matrix R:


r1
r2
r3

 =


1 1 1 1 1 1 1
1 1 1 1 1 − −
1 1 − − − 1 −

 .
To ﬁnd the next row of Q, we deﬁne 4 (= m = |w|) new variables x1, x 2, x 3, x 4.
The interpretation is that x1 represents the number of “+1”s in the ﬁrst
w1 = 2 entries of row 4, x2 represents the number of “+1”s in the next
w2 = 3 entries of row 4, as so on. We use the constraints imposed by
g1, 4, g 2, 4, g 3, 4, giving the linear system


1 1 1 1
1 1 − −
1 − 1 −






2x1 − 2
2x2 − 3
2x3 − 1
2x4 − 1



 =


−
−
3

 .
10



## Page 11

The two integer solutions which satisfy this system as well a s the bounds
0 ≤ x1 ≤ 2, 0 ≤ x2 ≤ 3, 0 ≤ x3 ≤ 1, 0 ≤ x4 ≤ 1 given by equation (12) are
(x1, x 2, x 3, x 4) = (1 , 1, 1, 0) and (2 , 0, 0, 1). These generate two children in
the search tree, with Q and w as follows:
Q =




1 1 1 1 1 1
1 1 1 1 − −
1 1 − − 1 −
1 − 1 − 1 −



 with w = (1, 1, 1, 2, 1, 1);
and
Q =




1 1 1 1
1 1 − −
1 − 1 −
1 − − 1



 with w = (2, 3, 1, 1).
The ﬁrst Q leads to a solution; the second does not.
4.2 Decomposition using Gram-pair constraints
The algorithm (version 2) outlined in §4.1, using only the single-Gram con-
straint, quickly becomes infeasible due to the size of the se arch space. It
can be improved by noting that, since the list L is complete, it must include
a matrix H Gram-equivalent to RT R. By permuting columns of R, we can
assume that H = RT R. This relation allows us to prune the search more
eﬃciently than if we did not know H.
Recall that the characteristic polynomial of a square matri x A is the
monic polynomial P (λ) = det( λI − A). Since H = RT G(RT )− 1, the matrices
G and H are similar, so they have the same characteristic polynomia l.
Thus, the reﬁned strategy is to consider each pair ( G, H ) ∈ L 2, such that
G and H have the same characteristic polynomial, and try to ﬁnd R such
that G = RRT , H = RT R. If we have considered ( G, H ) there is no need
to consider ( H, G ) since this would correspond to the dual solution RT .
More precisely, consider the constraint
Gj+1 = (RRT )j+1 = R(RT R)jRT = RH jRT . (13)
We say that the degree of such a constraint is j + 1, since the elements of
G (not R) occur with degree j + 1. The case j = 0 corresponds to the
single-Gram constraint considered in §4.1. For j = 1 we get the degree 2
constraint
G2 = RHR T
considered in [18]. The use of Gram-pair constraints with j > 1 is a new
element of our algorithm. In principle, we could get diﬀerent constraints for
j = 0, 1, . . . , n − 1. For j ≥ n the Cayley-Hamilton theorem implies that we
get nothing new.
11



## Page 12

To apply Gram-pair constraints for pruning when only the ﬁrs t k− 1 rows
of R are known, partition the matrices appearing in (13) into cor responding
blocks:
R =
[ R1
R2
]
, G j+1 =
[ G1, 1(j + 1) G1, 2(j + 1)
G2, 1(j + 1) G2, 2(j + 1)
]
, H j =
[ H1, 1(j) H1, 2(j)
H2, 1(j) H2, 2(j)
]
say, where R1 has k − 1 (known) rows. Then we can use the constraints
G1, 1(j + 1) = R1H1, 1(j)RT
1 (14)
since it only involves the known rows of R. The matrices Gj+1 and H j need
only be computed once.
Observe that H1, 1(j) for j ≥ 2 depends on all the entries in H. This
suggests that (14) with j ≥ 2 may be more eﬀective for pruning than the
“degree 2” case j = 1. In practice, we found that it was worthwhile to
use (14) with both j = 1 and j = 2, but not with j > 2.
When using Gram-pair constraints for pruning, we can no long er assume
that the ﬁrst row of R is (1 , 1, . . . , 1). The algorithm (version 2) of §4.1 has
to be modiﬁed so step 1 starts with level k = 0, Q empty, and a frame-widths
vector w which is compatible with H, in the sense that H is invariant under
permutations of rows (and corresponding columns) within ea ch frame. For
example, if we take H = G in the example of order 7 above, we can choose
w = (2, 2, 2, 1) as the initial frame-widths vector.
We remark that we used three variants of the decomposition al gorithm
outlined in this subsection. One variant attempts to ﬁnd a de composition
or (by failing to do so) to prove that a decomposition of a give n pair ( G, H )
does not exist. A second variant ﬁnds all possible decomposi tions, up to
Hadamard equivalence. The output typically includes many s olutions that
are Hadamard equivalent, so we use McKay’s program nauty [15] to remove
all but one representative of each equivalence class after t ransforming the
problem to a graph isomorphism problem [14]. A third variant is nondeter-
ministic and attempts to traverse the search tree by choosin g one or more
children randomly at each node. This variant is useful in diﬃ cult cases
where the deterministic variants take too long (see §6.2 for an example).
4.3 Proving indecomposability using the Hasse–Minkowski
criterion
A complementary approach to the decomposition problem, or, more prop-
erly, to proofs of indecomposability, makes use of the Hasse –Minkowski the-
orem on rational equivalence of quadratic forms. The use of t his theorem
has a long history in design theory, originating with its use by Bruck and
Ryser in their proof of their nonexistence result for certai n ﬁnite projective
planes [3]. Tamura recently applied the theorem to the quest ion of decom-
posability of candidate Gram matrices with block structure [27].
12



## Page 13

Theorem 2. Let A and B be symmetric, nonsingular rational matrices
of the same dimension. Then there exists a rational matrix R such that
B = RART if and only if
1. det A/det B is a rational square, and
2. the p-signatures of A and B agree for all primes p and for p = − 1.
The criterion is implemented by ﬁnding rational matrices U and V such
that U AUT and V BV T are diagonal—this can always be done—and then by
comparing the p-signatures of the resulting matrices for all primes dividi ng
any of the diagonal elements. The p-signature of a diagonal form is deﬁned
in [7, Chapter 15, §5.1].
The application of this theorem is as follows: there is no dec omposition
of the form RRT = G, RT R = H if there is a j ≥ 0 for which Gj+1 fails to be
rationally equivalent to H j or for which H j+1 fails to be rationally equivalent
to Gj. As was the case in the application of the Gram-pair constrai nt in
back-tracking search, we need only check the criterion for j < n .
The Hasse–Minkowski criterion is sometimes a competitive a lternative
to the backtracking algorithm in ruling out the existence of a decomposition.
On certain Gram matrix pairs for which the back-tracking sea rch ruled out
a decomposition only after exploring the search tree to grea t depth, the
Hasse–Minkowski criterion ruled out any decomposition wit h a relatively
fast computation. In most cases, however, back-tracking se arch is the much
faster method, especially when rational equivalence fails only for large j,
in which case the large-integer arithmetic needed to implem ent the Hasse–
Minkowski criterion can become prohibitively expensive. F urthermore, in a
small number of cases, the Hasse–Minkowski theorem fails en tirely to rule
out a decomposition where backtracking search succeeds. It is surprising
that this occurs relatively infrequently, as the existence of a decomposition
with R rational would appear to be a far milder constraint than the e xistence
of a decomposition with R a {+1, − 1} matrix.
5 The Maximal Determinant for Order 19
For order 19, known designs due to Smith [26], Cohn [6] and Orr ick and
Solomon [24] are D-optimal, as we now show.
Theorem 3. The maximal determinant of {+1, − 1} order 19 matrices is
230 × 72 × 17 = 833 × 46 × 218. (15)
There are precisely three corresponding equivalence classe s of saturated D-
optimal designs with representatives R1, R 2 and R3 indicated in Figure 2.
There are two corresponding (Gram equivalence classes of ) Gr am matrices,
G1 = R1RT
1 = RT
1 R1 and G2 = R2RT
2 = RT
2 R2 = R3RT
3 = RT
3 R3 – see
Figure 1.
13



## Page 14

Proof. A computational proof of Theorem 3 is described in §§5.1–5.2.
Remark 1. The maximal determinant given by (15) is smaller by a factor
17/
√
304 ≈ 0. 975 than the Ehlich bound (3) for n = 19.
5.1 Candidate Gram-ﬁnding for order 19
In the algorithm described in §3 we used dmin = 833 × 46 × 218 since {+1, − 1}
matrices with this determinant were known to exist. Our cand idate Gram-
ﬁnding program took 826 hours 1 to ﬁnd nine equivalence classes of candidate
Gram matrices and to rule out any others.
For the nine candidate Gram matrices G, the values of
√
det(G)/ 230
were 840 (ﬁve times), 836 . 0625 (once), 836 (once), and 833 (twice). The
matrices are available from the website [2].
G1 =

















n 3 3 3 3 3 3 − − − − − − − − − − − −
3 n 3 3 − − − − − − − − − − − − − − −
3 3 n 3 − − − − − − − − − − − − − − −
3 3 3 n − − − − − − − − − − − − − − −
3 − − − n 3 3 − − − − − − − − − − − −
3 − − − 3 n 3 − − − − − − − − − − − −
3 − − − 3 3 n − − − − − − − − − − − −
− − − − − − − n 3 3 − − − − − − − − −
− − − − − − − 3 n 3 − − − − − − − − −
− − − − − − − 3 3 n − − − − − − − − −
− − − − − − − − − − n 3 3 − − − − − −
− − − − − − − − − − 3 n 3 − − − − − −
− − − − − − − − − − 3 3 n − − − − − −
− − − − − − − − − − − − − n 3 3 − − −
− − − − − − − − − − − − − 3 n 3 − − −
− − − − − − − − − − − − − 3 3 n − − −
− − − − − − − − − − − − − − − − n 3 3
− − − − − − − − − − − − − − − − 3 n 3
− − − − − − − − − − − − − − − − 3 3 n

















G2 =

















n − − 3 − − 3 − − 3 − − − − − − − − −
− n 3 3 − − − − − − − − − − − − − − −
− 3 n 3 − − − − − − − − − − − − − − −
3 3 3 n − − − − − − − − − − − − − − −
− − − − n 3 3 − − − − − − − − − − − −
− − − − 3 n 3 − − − − − − − − − − − −
3 − − − 3 3 n − − − − − − − − − − − −
− − − − − − − n 3 3 − − − − − − − − −
− − − − − − − 3 n 3 − − − − − − − − −
3 − − − − − − 3 3 n − − − − − − − − −
− − − − − − − − − − n 3 3 − − − − − −
− − − − − − − − − − 3 n 3 − − − − − −
− − − − − − − − − − 3 3 n − − − − − −
− − − − − − − − − − − − − n 3 3 − − −
− − − − − − − − − − − − − 3 n 3 − − −
− − − − − − − − − − − − − 3 3 n − − −
− − − − − − − − − − − − − − − − n 3 3
− − − − − − − − − − − − − − − − 3 n 3
− − − − − − − − − − − − − − − − 3 3 n

















Figure 1: Optimal Gram matrices for n = 19. Here “ − ” stands for “ − 1”.
1 Computer times mentioned here and below are for a single 2.3G Hz Opteron processor.
In cases where the search could easily be parallelised, we so metimes used several processors
running in parallel. Our candidate Gram-ﬁnding program act ually took 188 hours using
several processors, each operating on part of the search tre e. Our programs were written
in C and used the GMP package to perform multiple-precision a rithmetic.
14



## Page 15

5.2 Decomposition for order 19
Our decomposition program found that seven of the candidate Gram matri-
ces were indecomposable, but the last two decomposed (as exp ected). The
running time was only 0.85 sec. Nevertheless, it would be ext remely tedious
to attempt to replicate the search by hand, since it involves visiting about
1400 nodes in the search trees.
The nine matrices have distinct characteristic polynomial s, so we only
had to consider the case G = RRT = H = RT R. Only the two candidate
Gram matrices with smallest determinant were decomposable , and these de-
composed in three ways, giving three Hadamard classes of des igns (maxdet
matrices) of order 19. See Figure 1 for the Gram matrices (not e that they
diﬀer only in the ﬁrst row and column), and Figure 2 for two of th e three
designs. The third design R3 can be obtained from R2 by a switching oper-
ation, as indicated in Figure 2.
A variant of our decomposition program exhaustively search es for all
possible decompositions (up to equivalence) of a given pair (G, H ). Run-
ning this program on ( G1, G 1) gave 110592 matrices in 36 seconds. Using
McKay’s program nauty [14, 15], we veriﬁed that they were all equivalent
to R1. Similarly, on ( G2, G 2) we obtained 3456 matrices in 3 seconds, and
nauty veriﬁed that 1728 were equivalent to R2, and the remaining 1728 were
equivalent to R3. Thus, there are precisely three inequivalent designs with
maximal determinant.
6 The Maximal Determinant for Order 37
The case of order 37 was handled in much the same way as order 19 . Al-
though 37 is much larger than 19, we have 37 ≡ 1 mod 4, and typically the
cases 1 mod 4 are easier than the cases 3 mod 4 (as one can see fro m the
summary at [22]). This is partly because Theorem 1 gives a sha rper bound
when n ≡ 1 mod 4.
We established that, for order 37, a known design, found prev iously by
Orrick and Solomon [21], is D-optimal. The design is not uniq ue, but the
corresponding Gram matrix is (up to equivalence).
Theorem 4. The maximal determinant of {+1, − 1} order 37 matrices is
72 × 917 × 236 = 2 39 × 336. (16)
A representative R of one equivalence class of saturated D-optimal designs is
indicated in Figure 4. The corresponding Gram matrix is G = RRT = RT R
as shown in Figure 3. Moreover, G is unique, up to equivalence.
15



## Page 16

R1 =
















+ − − − − − − + + + + + + + + + + + +
− + − − − − − − − − − + + − + + − + +
− − + − − − − − − − + − + + − + + − +
− − − + − − − − − − + + − + + − + + −
− − − − + − − + + + + − − − + − − − +
− − − − − + − + + + − + − − − + + − −
− − − − − − + + + + − − + + − − − + −
+ + + + − − − − + + + − − − − + − + −
+ + + + − − − + − + − + − + − − − − +
+ + + + − − − + + − − − + − + − + − −
+ + − − − + + + − − + − − + + + − − −
+ − + − + − + − + − − + − + + + − − −
+ − − + + + − − − + − − + + + + − − −
+ + − − + + − − + − − − − + − − + + +
+ − + − − + + − − + − − − − + − + + +
+ − − + + − + + − − − − − − − + + + +
+ + − − + − + − − + + + + − − − + − −
+ − + − + + − + − − + + + − − − − + −
+ − − + − + + − + − + + + − − − − − +
















R2 =
















− + + − + + − + + − − − − − − − − − −
+ − − − ⊕ ⊖ + − + + − − − ⊕ ⊖ + + − −
+ − − − ⊖ ⊕ + + − + − − − ⊖ ⊕ + − + −
− − − + + + + + + + − − − + + − − − +
+ − + + − − − − + + + − − − − − − + +
+ + − + − − − + − + − + − − − − + − +
− + + + − − + + + + − − + − − − + + −
+ − + + − + + − − − − + + + − − − − −
+ + − + + − + − − − + − + − + − − − −
− + + + + + + − − + + + − − − + − − −
− − − − ⊖ ⊕ − − + + + + + ⊖ ⊕ − + − −
− − − − ⊕ ⊖ − + − + + + + ⊕ ⊖ − − + −
− − − − − − + + + − + + + − − + − − +
− − + + − − − + − − + − − + + + + − −
− + − + − − − − + − − + − + + + − + −
− + + − − − − − − + − − + + + + − − +
− + − − − + + − − − + − − + − − + + +
− − + − + − + − − − − + − − + − + + +
− − − + + + − − − − − − + − − + + + +
















Figure 2: Two inequivalent saturated D-optimal designs of o rder 19. Here
“− ” stands for “ − 1” and “+” stands for “+1”. A third inequivalent design
R3 is the same as R2 except that the circled entries have their signs reversed
(this is an example of “switching”, see Orrick [19]).
16



## Page 17

Remark 2. The maximal determinant given by (16) is smaller by a factor
8/
√
73 ≈ 0. 936 than the Ehlich-Barba bound (2) for n = 37.
G =










37 5 5 5 5 5 5 5 5 5 1 ... 1
5 37 1 1 1 1 1 1 1 1 1 ... 1
5 1 37 1 1 1 1 1 1 1 1 ... 1
5 1 1 37 1 1 1 1 1 1 1 ... 1
5 1 1 1 37 1 1 1 1 1 1 ... 1
5 1 1 1 1 37 1 1 1 1 1 ... 1
5 1 1 1 1 1 37 1 1 1 1 ... 1
5 1 1 1 1 1 1 37 1 1 1 ... 1
5 1 1 1 1 1 1 1 37 1 1 ... 1
5 1 1 1 1 1 1 1 1 37 1 ... 1
1 1 1 1 1 1 1 1 1 1 37 ... 1.
.
. .
.
. .
.
. .
.
. .
.
. .
.
. .
.
. .
.
. .
.
. .
.
. .
.
. ... .
.
.
1 1 1 1 1 1 1 1 1 1 1 ... 37










Figure 3: The optimal Gram matrix for n = 37. All omitted entries are 1.
The matrix R in Figure 4 was constructed by Orrick and Solomon from
a doubly 3-normalized Hadamard matrix of order 36. There are at least 78
(and probably many more) inequivalent designs, as we discus s below.
6.1 Candidate Gram matrices for order 37
Our backtracking program with bound dmin = 2 39336 (93.6% of the Ehlich-
Barba bound) took 77 hours to ﬁnd 807 candidate Gram matrices . These
had 284 distinct determinants ∆ 2 in the range ∆ / (239332) ∈ [81, 85]. The
candidate Gram matrices are available from the website [2].
6.2 Decomposition for order 37
We applied our decomposition program to all pairs ( G, H ) of candidate
Gram matrices where G and H had the same characteristic polynomial.
There were 489 diﬀerent characteristic polynomials, and 152 8 pairs ( G, H )
to consider. The decomposition algorithm took 257 seconds t o show that
806 of the candidate Gram matrices did not decompose (in no ca se could
more than two rows of R be constructed).
For the remaining candidate, which was in fact equivalent to the Gram
matrix G shown in Figure 3, the program was stopped after running for 1 47
hours and exploring about 1 . 7 × 108 nodes (reaching level 26 of the tree).
A variant of our decomposition program uses a randomised sea rch – at
each node of the tree being searched, we choose to explore one (or sometimes
two) children selected uniformly at random. Using this rand omised search
program we can decompose G, in fact we have now found 39 solutions.
Finding one solution takes on average about 125 hours. By als o considering
duals, we get 78 solutions. Some (but not all) of these can be o btained
from a Hadamard matrix of order 36, in the same way as the matri x R
17



## Page 18

of Figure 4. Since all 78 solutions are inequivalent, we expe ct that many
more inequivalent solutions exist. The known solutions are available from
the website [2].
R =




































+ − − − − − − − − − + + + + + + + + + + + + + + + + + + + + + + + + + + +
− − − − + + + + + + − − − − − − − − − + + + + + + + + + + + + + + + + + +
− − − − + + + + + + + + + + + + + + + − − − − − − − − − + + + + + + + + +
− − − − + + + + + + + + + + + + + + + + + + + + + + + + − − − − − − − − −
− + + + + + − + − − + + − + + + + − − + − + + − + − + + + + + + − + + − −
− + + + + + − − − + − + + + − + − + + + − − + + − + + + − − − + + + + + +
− + + + + − + − + − + + + − + + − − + − + + − + + + + − + + − − + + + + −
− + + + − + − + + − + − + − + − + + + + + − + + − + + − + + + + − − − + +
− + + + − − + + − + + − + + + − + + − − + + − + + + − + − − + + + + + − +
− + + + − − + − + + − + − + − + + + + + + + + − + − − + + + + − + − − + +
+ − + + − + − + + + + − + + − + − − + − + − + − + + − + + + − + + − + − −
+ − + + − + + − + + + − − − + + + − + − − + + − − + + + − − + − − + + + +
+ − + + − + + + + − − + + − + − − + + + − + − − + − + + + − − + + + − − +
+ − + + + − − + + + − − + + + + + − − + + − − + − − + + + − + − + + − + −
+ − + + + − − + + + − + − + + − − + + − − + + + + + − − − + + + − + − + −
+ − + + + − + + − + + + + − − − + + − − − − + + + − + + + + − − − − + + +
+ − + + + + + − − + + + + − + + − − − + + + + + − − − − − + + + + − − − +
+ − + + + + + − + − + + − + − − + + − + + − − − + + + − − − + + + − + + −
+ − + + + + + + − − − − − + − + + + + + + + − + − + − − + + − − − + + − +
+ + − + − + − + + + + − − + + + − + − + − + − + + − + − − + − − + − + + +
+ + − + − + + + − + − + + − + + − + − + + − + − + + − − + − + − − + + + −
+ + − + − + + + − + + + − + − − + − + − + + + + − − + − + − − + + + − + −
+ + − + + − + − + + − − + + + − + − + + + − + − + − + − − + − + − + + − +
+ + − + + − + + + − + − + − − + + + − + − + + − − + − + − + − + + + − + −
+ + − + + − + + + − + + − + + − − − + + − − + + − + − + + − + − + − + − +
+ + − + + + − − + + + + + + − − − + − − + + − − − + + + + + + − − + − − +
+ + − + + + − + + − − + + − − + + − + − + + − + + − − + − − + + − − + + +
+ + − + + + + − − + − − − − + + + + + − − − − + + + + + + + + + + − − − −
+ + + − + + − − + + + − + − − − + + + + − + + + + − − − + − + − + + + − −
+ + + − + − + + − + + − + + − + − − + + − + − − + + + − + − + + − − − + +
+ + + − + − − + + + − + − − + + + + − − + + + − − + + − + − − + + − + − +
+ + + − − + + + + − − + + + − + + − − − − − + + + + + − − + + − + + − − +
+ + + − − + + − + + − + + + + − + − − + − + − + − + − + + + − + − − + + −
+ + + − − − + + + + + + − − − + − + + + + − − + − − + + − + + + − + + − −
+ + + − + + − + − + + + − − + − + − + + + − − − + + − + − + − − + + − + +
+ + + − + + + − + − + − − + + + − + − − + − + + + − − + + − − + − + − + +
+ + + − + + + + − − − − + + + − − + + − + + + − − − + + − + + − + − + + −




































Figure 4: A saturated D-optimal design of order 37, construc ted by Orrick
and Solomon. Here “ − ” stands for “ − 1” and “+” stands for “+1”.
7 Improved Bounds for Various Orders
Recall that dn is the maximal determinant for order n, divided by the known
factor 2n− 1. Table 1 summarises the best known upper and lower bounds on
dn for orders n = 19, 29, 33, 37, 45, 49, 53, 57 (we omit n = 25, 41, 61 because
for these orders the Ehlich-Barba bound (2) is attained). Th e ﬁgures in
parentheses are the ratios of the entries to the Ehlich-Barb a bound (for
n ≡ 1 mod 4) or the Ehlich bound (for n ≡ 3 mod 4), rounded to three
decimals.
For n = 19 and n = 37, the upper and lower bounds are equal, and thus
optimal ( dn = u = ℓ in these cases). In the other cases the upper bounds
are unattainable, so dn ∈ [ℓ, u ). In all cases the upper bounds are new,
18



## Page 19

and for n = 45 the lower bound is new (the previous best lower bound was
83 × 1121).
The last column gives the number of equivalence classes of ca ndidate
Gram matrices G with det( G) ≥ (2n− 1u)2.
order n lower bound ℓ upper bound u Gram count
19 833 × 46 (0. 975) 833 × 46 (0. 975) 9
29 320 × 712 (0. 865) 329 × 712 (0. 889) 9587
33 441 × 814 (0. 855) 470 × 814 (0. 911) 13670
37 8 × 918 (0. 936) 8 × 918 (0. 936) 807
45 89 × 1121 (0. 858) 99 × 1121 (0. 953) 1495
49 96 × 1223 (0. 812) 114 × 1223 (0. 965) 168
53 105 × 1325 (0. 788) 129 × 1325 (0. 968) 220
57 133 × 1427 (0. 894) 145 × 1427 (0. 974) 128
Table 1: Bounds on the (scaled) maximal determinant dn
7.1 Discussion
Let k = ⌊n/ 4⌋. From the summary at [22] we observe that, in the cases
k ≤ 3 where d4k+3 is known precisely, d4k+3 is divisible by k2k− 1. However,
our result for n = 19 shows that this pattern does not continue, for d19 is
not divisible by 4 7.
In all cases where d4k+1 is known precisely ( k ≤ 6 and k = 10, 15, 28, . . . ),
d4k+1 is divisible by k2k− 1. This is easily seen to be true if the Ehlich-Barba
bound (2) is attainable ( d4k+1 is divisible by k2k in such cases), but it is also
true for k = 2, 4, 5, where the Ehlich-Barba bound is not attainable.
For n = 29, we ruled out 9587 candidate Gram matrices to show that
d29 < 329× 712. If d29 is divisible by 7 13, then we must have d29 = 322× 712 =
46 × 713, since this is the only multiple of 7 13 in the allowable interval
[320× 712, 329× 712). However, all attempts to construct an example of order
29 with |det |/ 228 > 320 × 712, using hill-climbing or constructions based on
Hadamard matrices of order 28, have failed. Thus, the plausi ble conjecture
that d4k+1 is divisible by k2k− 1 may well be false. An attempt to reduce the
upper bound u to 322 × 712 is underway but may not be feasible with our
current resources – so far we have generated 16683 candidate Gram matrices
(taking about two processor-years) but estimate that there are about 220000
in all.
For n = 33 we ruled out 13670 candidate Gram matrices to establish a n
upper bound of u = 470 × 814. It is unlikely that we can reduce u much
further without improvements in the candidate Gram-ﬁnding program, since
it took about two processor-years to generate the candidate s for u = 470,
though only about six hours to show that none of them decompos e.
19



## Page 20

For n = 45, the new lower bound of 89 × 1121 was established by a
construction using a doubly 3-normalized Hadamard matrix o f order 44.
Details will appear elsewhere.
8 The Spectrum for Order 13
The spectrum Sn of the determinant function for {+1, − 1} matrices is de-
ﬁned to be the set of values taken by |det(Rn)|/ 2n− 1 as Rn ranges over
all n × n {+1, − 1} matrices. For 2 ≤ n ≤ 7, the spectrum includes all
integers between 0 and dn. The spectrum for n = 8 was ﬁrst computed
by Metropolis, Stein, and Wells [16], who found that gaps occ ur, in fact
S8 = {0, 1, . . . , 18, 20, 24, 32}. A (non-computer-based) proof of the exis-
tence of gaps was later given by Craigen [8]. At present, the s pectrum is
known for n ≤ 11 and (given here for the ﬁrst time) for n = 13. The results
for n = 9 are due to ˇZivkovi´ c [28] (and, independently, Charalambides [5]),
those for n = 10 are due to ˇZivkovi´ c [28], and those for n = 11 are due to
Orrick [18]. The spectra for n ≤ 11, and conjectured spectra for n = 12
and 14 ≤ n ≤ 17, may be found at [23]. Here we give only the spectrum
for n = 13, using the notation a..b as a shorthand to represent the interval
{x ∈ Z : a ≤ x ≤ b}.
Theorem 5. The spectrum for order 13 is
S13 = {0.. 2172, 2174.. 2185, 2187.. 2196, 2199.. 2202, 2205, 2208, 2210, 2211,
2214.. 2218, 2220.. 2226, 2228, 2229, 2230, 2232, 2233, 2235, 2238, 2240, 2241,
2243.. 2245, 2247, 2248, 2250, 2253, 2256, 2258.. 2260, 2262, 2264, 2265, 2267,
2268, 2271, 2272, 2274, 2277, 2280, 2283, 2286, 2288, 2292, 2295, 2296, 2304,
2307, 2312, 2313, 2316, 2319, 2320, 2322, 2325, 2328, 2331, 2334, 2336, 2340,
2343, 2344, 2349, 2352, 2355, 2360, 2361, 2367, 2368, 2370, 2373, 2376, 2385,
2394, 2400, 2403, 2406, 2421, 2430, 2432, 2439, 2457, 2472, 2484, 2496, 2511,
2520, 2538, 2560, 2583, 2592, 2619, 2646, 2673, 2835, 2916, 3159, 3645}.
Proof. The proof is computational. Using a heuristic algorithm des cribed
in [20, pg. 34], we found examples of order 13 matrices with al l 2173 deter-
minants 0, 1 × 212, 2 × 212, . . . , 2172 × 212. The ﬁrst “gap” was at 2173 × 212.
We ran the Gram-ﬁnding program of §3 with lower bound dmin = 2173 × 212.
It produced 8321 candidate Gram matrices in 73 minutes. We th en ran the
decomposition program of §4 which found (in 48 seconds) that 1643 of the
candidate Gram matrices decomposed, giving 130 distinct de terminants in
the range [2174 , 3645]. These are listed in the statement of the theorem.
Appendix: Proof of new bound (9) in Theorem 1
The proof is a generalisation Ehlich’s proof [9] of the bound (3) on the
maximal determinant, which applies in the case n ≡ 3 (mod 4). Ehlich’s
20



## Page 21

proof shows the following.
(1) The candidate principal minor of maximal determinant ha s non-diagonal
elements equal to either − 1 or 3.
(2) It is a block matrix , which means that the non-diagonal 3s occur in
square blocks along the diagonal.
(3) In the case that the candidate principal minor is a candid ate Gram
matrix, that is, its size is n, the number of blocks is s, with u blocks of
size ⌊n/s ⌋ and v blocks of size ⌊n/s ⌋+ 1, where s, u, and v are deﬁned
following (3).
We generalise this to the case where the candidate principal minor contains
a ﬁxed principal submatrix Mr. If such a candidate principal minor of
maximal determinant is written as
[ Mr B
BT A
]
,
then our result, assuming the hypothesis det Mr > (n − 3) det Mr− 1, is
that A satisﬁes properties (1) and (2) above, and the submatrices o f B
corresponding to blocks of A consist of repeated columns. The generalisation
of (3) depends on Mr and is not unique in general.
From now on, we take n ≡ 3 (mod 4) and n > 3. Deﬁne
Cm = {Cm|Cm = (cij), c ij = cji, C m is pos. def. , c ii = n,
cij ≡ n (mod 4) , i, j = 1 . . . m } . (17)
and
Em = {Em|Em ∈ Cm and the leading r × r submatrix of Em is Mr}. (18)
Deﬁne C ∗
m and E∗
m (which may not be unique) by the conditions
det C ∗
m = max{det Cm|Cm ∈ Cm},
det E∗
m = max{det Em|Em ∈ Em}.
The ﬁrst thing Ehlich proves (Theorem 2.1) is that det C ∗
m > (n −
3) det C ∗
m− 1 for 2 ≤ m ≤ n. To explain the use of this theorem, we ﬁrst
introduce a notation. If Cm ∈ Cm then deﬁne ˜Cm be the matrix that results
from replacing the last diagonal element of Cm by 3, i.e. ˜Cm = (˜cij) where
˜cij =
{
3 if i = j = m
cij otherwise.
21



## Page 22

Expanding det C ∗
m by minors on its last row, we ﬁnd
det C ∗
m − det ˜C ∗
m = (n − 3) det Cm− 1 ≤ (n − 3) det C ∗
m− 1 (19)
where Cm− 1 is the leading ( m − 1) × (m − 1) submatrix of C ∗
m. (Note that
˜C ∗
m is the result of applying the tilde operation to C ∗
m.) The theorem then
implies that det ˜C ∗
m > 0 and therefore that ˜C ∗
m is positive deﬁnite. This
becomes important in later proofs when evaluating determin ants that arise
as the result of column operations.
For the generalization to our case, we appear to need the extr a condition
det ˜Mr > 0. This cannot be expected to hold in general. Consider for
example,
M2 =
[ 11 7
7 11
]
(20)
for which det ˜M2 < 0. For now, we leave it as a question for empirical
study whether the condition holds often enough in practical searches for the
following considerations to be useful.
Theorem 6. Let 1 ≤ r ≤ m, let Mr ∈ Cr, and let det ˜Mr > 0. Then the
set of elements Em ∈ Em for which det ˜Em > 0 is non-empty.
Proof. We prove the theorem by induction on m. For the base case, m = r,
the matrix Mr ∈ Er satisﬁes det ˜Mr > 0 by assumption. Now assume that
the theorem holds for all Ek with r ≤ k ≤ m. We want to show that it holds
for Em+1. Let Em be an element of Em for which det ˜Em > 0, and write
this element as
Em =
[ Cm− 1 γ
γT n
]
. (21)
Form the matrix
Em+1 =


Cm− 1 γ γ
γT n 3
γT 3 n

 . (22)
Subtracting column m from column m + 1 and expanding by minors on
column m + 1 we ﬁnd that det Em+1 = (n − 3) det Em + (n − 3) det ˜Em. Both
terms are positive, which means that det Em+1 is positive, and therefore
that Em+1 is positive deﬁnite and hence an element of Em+1. By a similar
computation det ˜Em+1 = ( n − 3) det ˜Em > 0. Therefore Em+1 is a suitable
element.
Theorem 7. Let 1 ≤ r < m , let Mr ∈ Cr, and let det ˜Mr > 0. Then
det E∗
m > (n − 3) det E∗
m− 1.
22



## Page 23

Proof. When m = r + 1 we write
Mr =
[ Cr− 1 γ
γT n
]
(23)
and deﬁne
Er+1 =


Cr− 1 γ γ
γT n 3
γT 3 n

 . (24)
From the proof of the previous theorem we know that Er+1 ∈ Er+1 and
det ˜Er+1 > 0. Now det E∗
r+1 ≥ det Er+1 = (n − 3) det Mr + (n − 3) det ˜Mr >
(n − 3) det Mr = (n − 3) det E∗
r .
We now proceed by induction. Assume that det E∗
m > (n − 3) det E∗
m− 1.
Write
E∗
m =
[ Em− 1 γ
γT n
]
(25)
and deﬁne
Em+1 =


Em− 1 γ γ
γT n 3
γT 3 n

 . (26)
Now det Em+1 = ( n − 3) det E∗
m + ( n − 3) det ˜E∗
m. Note that det E∗
m =
(n − 3) det Em− 1 + det ˜E∗
m ≤ (n − 3) det E∗
m− 1 + det ˜E∗
m. From the induction
hypothesis, it follows that det ˜E∗
m > 0, and so det Em+1 > (n− 3) det E∗
m.
This proof contains the proof of an important corollary:
Corollary 8. Let 1 ≤ r ≤ m, let Mr ∈ Cr, and let det ˜Mr > 0. Then
det ˜E∗
m > 0.
We now generalize Ehlich’s Theorem 2.2. Again we need the ass umption
that det ˜Mr > 0.
Theorem 9. Let 1 ≤ r ≤ m, let Mr ∈ Cr, and let det ˜Mr > 0. Write
E∗
m =
[ Mr B
BT A
]
,
where A = (aij) and B = (bij) satisfy the conditions in the deﬁnition of Em.
Then for i ̸= j we have aij = − 1 or 3.
Proof. When m = r or r + 1 the statement is vacuously true. So we assume
m ≥ r + 2. Suppose there is an element aij = c ̸= − 1 or 3 for i ̸= j. Then
|c| > 3. We may assume that the element is positioned so that i = m − 1,
j = m, so that we may write
E∗
m =


Em− 2 α β
α T n c
β T c n

 .
23



## Page 24

By interchanging the last two rows and last two columns, if ne cessary, we
may assume that
det
[ Em− 2 α
α T n
]
≤ det
[ Em− 2 β
β T n
]
.
We now claim that the matrix
Em =


Em− 2 β β
β T n 3
β T 3 n


has larger determinant than E∗
m, a contradiction. To establish the claim,
evaluate both determinants:
det E∗
m = (n − 3) det
[ Em− 2 α
α T n
]
+ det ˜E∗
m
det Em = (n − 3) det
[ Em− 2 β
β T n
]
+ det ˜Em
By Corollary 8, ˜E∗
m is positive deﬁnite. Symmetric row and column opera-
tions do not aﬀect positive deﬁniteness, so we get
det ˜E∗
m = det



Em− 2 α β
α T n c
β T c 3


 = det



Em− 2 β α − c
3 β
β T 3 0
α T − c
3 β T 0 n − c2
3



≤
(
n − c2
3
)
det
[
Em− 2 β
β T 3
]
.
We evaluate det ˜Em by subtracting column m from column m − 1 and doing
expansion by minors on column m − 1 to obtain
det ˜Em = (n − 3) det
[ Em− 2 β
β T 3
]
.
Since |c|> 3 we have det ˜E∗
m < det ˜Em and therefore det E∗
m < det Em.
Now we want to generalize Ehlich’s Theorem 2.3. First a usefu l lemma
about block matrices. (See Ehlich’s paper for the formal deﬁ nition of block.)
Lemma 10. A symmetric matrix A = ( aij) with diagonal elements n is a
block matrix if and only if its non-diagonal elements are all − 1 or 3 and for
any i ̸= j such that aij = 3 the columns i and j diﬀer only in their ith and
jth elements.
24



## Page 25

Proof. If A is a block matrix, the statement is clearly true. For the conv erse,
let ( i, j ) be the position of one of the 3s of A. Deﬁne i1 = j, i2 = i, and let
{i2, i 3, . . . , i p} be the set of all indices h for which ahj = 3. Let 2 ≤ k ≤ p.
Then aikj = 3 means that the ith
k element of column j is 3. Let 1 ≤ ℓ ≤ p,
ℓ ̸= k. Then since columns iℓ and j agree in their ith
k element we have
aikiℓ = 3 for all k ̸= ℓ.
For an index h / ∈ { i1, . . . , i p} we have ahj = − 1. But since columns j
and iℓ, 1 ≤ ℓ ≤ p, agree in their hth element, we have ahiℓ = − 1 for all
1 ≤ ℓ ≤ p. Therefore the set of indices {i1, . . . , i p} forms a block. Hence
every one of the 3s in A lies in a block, and A is a block matrix.
Now for the generalization of Ehlich’s Theorem 2.3.
Theorem 11. Let 1 ≤ r ≤ m, let Mr ∈ Cr, and let det ˜Mr > 0. Write
E∗
m =
[ Mr B
BT A
]
,
where A = (aij) and B = (bij) satisfy the conditions in the deﬁnition of Em.
If for some i ̸= j, aij = 3, then columns i and j of B are equal and columns
i and j of A are equal except for their ith and jth elements.
Proof. By Theorem 9 we know that the non-diagonal elements of A are − 1
or 3. As before, the theorem is vacuously true if m = r or m = r + 1.
Assume m ≥ r + 2 and let A have an element 3, say in position ( m − 1, m ).
Write
E∗
m =




Mr B1 βm− 1 βm
BT
1 A1 α m− 1 α m
β T
m− 1 α T
m− 1 n 3
β T
m α T
m 3 n



 .
We assume, as we may (by swapping the last two rows and last two columns
if necessary), that
det


Mr B1 βm− 1
BT
1 A1 α m− 1
β T
m− 1 α T
m− 1 n

 ≤ det


Mr B1 βm
BT
1 A1 α m
β T
m α T
m n

 .
Our goal is now to show that βm− 1 = βm and α m− 1 = α m. Suppose that
this is not the case. We claim that det Em > det E∗
m where
Em =




Mr B1 βm βm
BT
1 A1 α m α m
β T
m α T
m n 3
β T
m α T
m 3 n



 .
Write
det E∗
m = (n − 3) det


Mr B1 βm− 1
BT
1 A1 α m− 1
β T
m− 1 α T
m− 1 n

 + det ˜E∗
m
25



## Page 26

and
det Em = (n − 3) det


Mr B1 βm
BT
1 A1 α m
β T
m α T
m n

 + det ˜Em.
The ﬁrst term on the right in det E∗
m is no larger than the ﬁrst term on the
right in det Em, and we will see that the second term of det E∗
m is strictly
smaller than the second term of det Em. By subtracting row and column
m of ˜Em from row and column m − 1 of ˜Em and expanding by minors on
column m − 1 we ﬁnd that
det ˜Em = (n − 3) det


Mr B1 βm
BT
1 A1 α m
β T
m α T
m 3

 .
On the other hand, using Corollary 8, which implies that ˜E∗
m is positive
deﬁnite, and evaluating the determinant as we did for det ˜Em, we ﬁnd that
det ˜E∗
m < (n − 3) det


Mr B1 βm
BT
1 A1 α m
β T
m α T
m 3

 .
This follows because α m− 1 − α m and βm− 1 − βm, which together form the
ﬁrst m − 2 elements of column m − 1 in the expansion by minors, are not
both zero.
Corollary 12. The matrix A in Theorem 11 is a block matrix.
Proof. We have proved in Theorems 9 and 11 that both of the conditions
needed in Lemma 10 for A to be a block matrix hold.
Our conclusion is that, when det ˜Mr > 0, the maximal determinant
completion E∗
m of Mr takes a form where A is a block matrix with some
number k of blocks whose sizes we will denote b1, b2, . . . , bk, and where
B =
[
B1 . . . B k
]
with each of the matrices Bj a rank-1 matrix consisting
of a column β ∗
j repeated bj times. This establishes (9).
Acknowledgements
We gratefully acknowledge support from the Australian Rese arch Council,
the ARC Centre of Excellence for Mathematics and Statistics of Complex
Systems (MASCOS), and INRIA via the ANU-INRIA Associate Tea m ANC.
26



## Page 27

References
[1] G. Barba, Intorno al teorema di Hadamard sui determinant i a valore
massimo Giorn. Mat. Battaglini 71 (1933), 70–86.
[2] R. P. Brent, W. P. Orrick, J. H. Osborn and P. Zimmermann, S ome D-
optimal designs of orders 19 and 37, http://wwwmaths.anu.edu.au/
~brent/maxdet/
[3] R. H. Bruck and H. J. Ryser, The nonexistence of certain ﬁn ite projec-
tive planes Canadian J. Math. 1 (1949) 88–93.
[4] T. Chadjipantelis, S. Kounias and C. Moyssiadis, The max imum deter-
minant of 21 × 21 (+1 , − 1)-matrices and D-optimal designs, J. Statist.
Plann. Inference 16, 2 (1987), 167–178.
[5] A. Charalambides, personal communication to W. Orrick, 2005.
[6] J. H. E. Cohn, Almost D-optimal designs, Utilitas Math. 57 (2000),
121–128.
[7] N. J. A. Sloane and J. H. Conway, Sphere Packings, Lattices
and Groups, volume 290 of Grundlehren der Mathematischen Wi s-
senschaften, Springer, New York–Berlin–Heidelberg, 3rd edition, 1998 .
[8] R. Craigen, The range of the determinant function on the s et of n × n
(0, 1)-matrices, J. Combin. Math. Combin. Comput. 8 (1990), 161–171.
[9] H. Ehlich, Determinantenabsch¨ atzungen f¨ ur bin¨ are Matrizen, Math. Z.
83 (1964), 123–132.
[10] H. Ehlich, Determinantenabsch¨ atzungen f¨ ur bin¨ areMatrizen mit n ≡
3 mod 4, Math. Z. 84 (1964), 438–447.
[11] A. V. Geramita and J. Seberry, Orthogonal Designs: Quadratic Forms
and Hadamard Matrices , Marcel Dekker, New York, 1979.
[12] J. Hadamard, R´ esolution d’une question relative aux d ´ eterminants,
Bull. des Sci. Math. 17 (1893), 240–246.
[13] K. J. Horadam, Hadamard Matrices and their Applications , Princeton
University Press, 2007.
[14] B. D. McKay, Hadamard equivalence via graph isomorphis m, Discrete
Mathematics 27 (1979), 213–214.
[15] B. D. McKay, nauty, http://cs.anu.edu.au/~bdm/nauty/.
27



## Page 28

[16] N. Metropolis, Spectra of determinant values in (0 , 1) matrices. In A.
O. L. Atkin and B. J. Birch, editors, Computers in Number Theory:
Proceedings of the Science Research Atlas Symposium No. 2 he ld at
Oxford, 18–23 August, 1969 , Academic Press, London, 1971, 271–276.
[17] C. Moyssiadis and S. Kounias, The exact D-optimal ﬁrst o rder satu-
rated design with 17 observations, J. Statist. Plann. Inference 7 (1982),
13–27.
[18] W. P. Orrick, The maximal {− 1, 1}-determinant of order 15, Metrika
62 (2005), 195–219.
[19] W. P. Orrick, Switching operations for Hadamard matric es, SIAM J.
Discrete Math. 22 (2008), 31–50.
[20] W. P. Orrick, Range and distribution of determinants of binary matri-
ces, invited talk presented at the Maximal Determinant Workshop held
at the Australian National University, 17 May 2010. Availab le from
http://mypage.iu.edu/~worrick/talks.html.
[21] W. P. Orrick and B. Solomon, Large-determinant sign mat rices of order
4k + 1, Discrete Math. 307 (2007), 226–236.
[22] W. P. Orrick and B. Solomon, The Hadamard maximal determinant
problem, http://www.indiana.edu/~maxdet/.
[23] W. P. Orrick and B. Solomon, Spectrum of the determinant function ,
http://www.indiana.edu/~maxdet/spectrum.html.
[24] W. P. Orrick and B. Solomon, Conjectured 19 × 19 {− 1, +1} matri-
ces of maximal determinant , 15 May 2003. http://www.indiana.edu/
~maxdet/d19.html.
[25] J. H. Osborn, The Hadamard Maximal Determinant Problem , Hon-
ours thesis, University of Melbourne, 2002. Available from http://
wwwmaths.anu.edu.au/~osborn/publications/pubsall.html.
[26] W. D. Smith, Studies in Computational Geometry Motivated by Mesh
Generation, PhD dissertation, Princeton University, 1988.
[27] H. Tamura, D-optimal designs and group divisible desig ns, J. Combin.
Des. 14 (2006), 451–462.
[28] M. ˇZivkovi´ c, Classiﬁcation of small (0, 1) matrices, Linear Algebra Appl.
414 (2006), 1, 310–346.
28
