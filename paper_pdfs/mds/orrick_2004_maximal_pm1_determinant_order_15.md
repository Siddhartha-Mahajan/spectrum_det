# Extracted text: orrick_2004_maximal_pm1_determinant_order_15.pdf

Source PDF: orrick_2004_maximal_pm1_determinant_order_15.pdf

Pages: 30



## Page 1

arXiv:math/0401179v1  [math.CO]  15 Jan 2004
THE MAXIMAL {− 1, 1}-DETERMINANT OF ORDER 15
W. P. ORRICK
Abstract. We study the question of ﬁnding the maximal determinant of matrice s of
odd order with entries ± 1. The most general upper bound on the maximal determi-
nant, due to Barba, can only be achieved when the order is the sum o f two consecutive
squares. It is conjectured that the bound is always attained in suc h cases. Apart from
these, only in orders 3, 7, 9, 11, 17 and 21 has the maximal value bee n established. In
this paper we conﬁrm the results for these orders, and add order 15 to the list. We follow
previous authors in exhaustively searching for candidate Gram mat rices having deter-
minant greater than or equal to the square of a known lower bound on the maximum.
We then attempt to decompose each candidate as the product of a {− 1, 1}-matrix and
its transpose. For order 15 we ﬁnd four candidates, all of Ehlich blo ck form, two having
determinant (105 ·35 ·214)2 and the others determinant (108 ·35 ·214)2. One of the former
decomposes (in an essentially unique way) while the remaining three do not. This result
proves a conjecture made independently by W. D. Smith and J. H. E. Cohn. We also use
our method to compute improved upper bounds on the maximal dete rminant in orders
29, 33, and 37, and to establish the range of the determinant func tion of {− 1, 1}-matrices
in orders 9 and 11.
1. Introduction
Under the conditions that its elements are real and bounded in magn itude, what is the
largest determinant that a square matrix can have? By rescaling we may ﬁx the bound
on the magnitude of the elements to 1, and because of linearity of th e determinant in
its rows and columns, we lose nothing by restricting the entries to th e set {− 1, 1}. For
Rn ∈ { n × n matrices with entries ± 1}, Hadamard [Ha] showed that
det Rn ≤ nn/2 (1.1)
and that equality can only hold when n = 1, 2 or n ≡ 0 mod 4. It is not known whether
equality always does hold in such cases, but Paley [Pa] conjectured that it does, and
the lowest order for which the question is unresolved is n = 428. For other orders more
stringent bounds have been established. Barba [Ba] showed that w hen n is odd the bound
is
det Rn ≤
√
2n − 1 ( n − 1)(n− 1)/2 := B(n). (1.2)
Date: October 30, 2018.
1991 Mathematics Subject Classiﬁcation. Primary 05B30, 05B20, 62K05.
Key words and phrases. Maximal determinant, D-optimal design.
1



## Page 2

2 W. P. ORRICK
This bound is an integer only when n is the sum of two consecutive squares, and it is
believed that equality holds whenever this is the case. However, eve n for orders as low
as 85 = 6 2 + 7 2 this has not been proved. When n ≡ 2 mod 4, the bound, derived
independently by Ehlich [Eh1] and Wojtas [Wo], is
det Rn ≤ 2(n − 1)(n − 2)(n− 2)/2. (1.3)
The bound has been shown to be attainable only if n − 1 is the sum of two squares [Eh1],
and again it is believed to hold in all such cases. The lowest order for wh ich the question
has not been settled is n = 138 [FKS].
We say that a bound is tight when it is achieved inﬁnitely often. All three of the above
bounds have been shown constructively to be tight [Br, Sp, KKS]. Th e bound (1.2) is
actually tight only for n ≡ 1 mod 4. For n ≡ 3 mod 4 Ehlich [Eh2] proved the stricter
bound
det Rn ≤ (n − 3)(n− s)/2(n − 3 + 4r)u/2(n + 1 + 4r)v/2
√
1 − ur
n − 3 + 4r − v(r + 1)
n + 1 + 4r (1.4)
where s = 5 for n = 7, s = 5 or 6 for n = 11, s = 6 for 15 ≤ n ≤ 59 and s=7 for n ≥ 63
and where r =
⌊ n
s
⌋
, n = rs + v and u = s − v. This bound is not integral for n ≤ 59. For
n ≥ 63 Cohn [Co2] has shown that it is integral only when n = 112 t2 ± 28t + 7 for some
integer t, but even in these cases, it is not known whether the bound is ever a ttained.
Denote by md( n) the maximal determinant attained by any member of the set of
n × n {− 1, 1}-matrices and deﬁne md(n) := md( n)/2n− 1. The latter is the “normalized”
maximal determinant function where the factor 2 n− 1 common to all n× n {− 1, 1}-matrices
has been removed.
When a determinant is found that attains the relevant one of the ab ove bounds, it is
immediate that md( n) is just the bound itself, but when the upper bound is not attained,
ﬁnding md( n) can be exceedingly diﬃcult. To date, the only orders in this categor y for
which md( n) is known are 3, 7 [Wi], 9 [EZ], 11 (Ehlich, as reported in [GK]), 17 [MK]
and 21 [CKM]. This leaves, for n ≤ 30, orders 15, 19, 22, 23, 27, and 29 unresolved. The
sequence of maximal determinants for 1 ≤ n ≤ 14 is
n 1 2 3 4 5 6 7 8 9 10 11 12 13 14
md(n) 1 1 1 2 3 5 9 32 56 144 320 1458 3645 9477 .
In this paper, we settle the case n = 15. This means the above sequence can be extended
up to n = 18:
n 15 16 17 18
md(n) 25515 131072 327680 1114112 .
Our method of proof follows that of Ehlich (reported in [GK]), Moyss iadis and Kou-
nias [MK] and Chadjipantelis, Kounias and Moyssiadis [CKM], and relies o n an intensive
computer search. Compared with all other orders in which md( n) has been determined, a
considerably greater (but still modest) amount of computer powe r is required for n = 15.



## Page 3

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 3
The value 25515 was conjectured to be the maximum by Warren D. Sm ith [Sm] and
independently by John H. E. Cohn [Co1, Co2].
In addition to this result for n = 15, we conﬁrm the known values of md( n) for all
odd n ≤ 21 excluding, of course, n = 19. We are also able to report improved upper
bounds on the maximal determinants for matrices of orders 29, 33 , and 37. Furthermore,
we establish the range of the determinant function for matrices of orders 9 and 11.
2. Some properties of matrices
While we are here mainly interested in the case n = 15, we also would like to conﬁrm
existing results in other orders and to say as much as possible about other open cases.
On the other hand, even orders (the lowest interesting case is n = 22) require a somewhat
diﬀerent approach, owing primarily to the absence of a canonical no rmalization (see be-
low). Hence we will describe an algorithm that works for odd orders g enerally. For the
remainder of this paper we take n to be an odd positive number.
2.1. Equivalences of {− 1, 1}-matrices. Negating some set of rows and some set of
columns of a matrix changes its determinant by at most a sign. Two ma trices related
to each other by such negations are considered to be equivalent. I t is advantageous to
restrict our attention to a single canonical representative of eac h equivalence class:
Deﬁnition. A vector of odd length with elements in the set {− 1, 1} is parity normalized
if it has an even number of positive elements. A matrix of odd order wit h elements in
{− 1, 1} is parity normalized all its rows and columns are.
Lemma 2.1. Any {− 1, 1}-matrix of odd order may be converted to a unique parity nor-
malized matrix by a series of negations of rows and columns.
Proof. Begin by negating all rows containing an even number of entries − 1. Since the
number of rows is odd, the matrix now contains an odd number of neg ative entries. Thus
the number of columns containing an even number of negative entrie s must be even.
Negating these gives the desired matrix, which is clearly unique. □
Permuting a set of rows and a set of columns of a matrix also preserv es its determinant
up to a sign.
Deﬁnition. Two {− 1, 1}-matrices R and S are Hadamard equivalent if S = P RQ for
some pair of signed permutation matrices ( P, Q).
Note that we have omitted a third determinant preserving operatio n, transposition, in
our notion of equivalence. Henceforth, we take {− 1, 1}-matrices to be parity normalized.
On the other hand, transforming a given matrix into a canonical rep resentative of the
same class under full Hadamard equivalence is computationally expen sive, so we do not
attempt to impose a canonical ordering on the rows and columns of a matrix.



## Page 4

4 W. P. ORRICK
2.2. Gram matrices. Let Mr(R) be the Gram matrix of the rows of R,
Mr(R) = RRT. (2.1)
Mr(R) is unchanged under negation and permutation of the columns of R. Likewise let
Mc(R) be the Gram matrix of the columns of R,
Mc(R) = RTR. (2.2)
Mc(R) is unchanged under negation or permutation of the rows of R. Both Mr(R) and
Mc(R) are symmetric, have diagonal elements equal to n, and, assuming R nonsingular,
are positive deﬁnite. They have the same determinant, which must b e a perfect square.
Furthermore, they have identical characteristic equations. This follows from the following
lemma.
Lemma 2.2. Let A and B be square matrices. Then det(AB − λI) = det( BA − λI).
Proof. If B is invertible, the result follows immediately by multiplying the right-hand side
of the equation on the left by det B and on the right by det B− 1, and then combining
determinants. If B is not invertible, consider B′ = B − xI. Since B′ is invertible for all
but ﬁnitely many x, we have, in the generic case, that det( AB′− λI) = det( B′A − λI). As
this is a polynomial identity in x, it must be true for all x and for x = 0 in particular. □
Since Gram matrices are symmetric, we will often have occasion to ta lk about operations
that act on rows and columns simultaneously in the same way. We will th erefore refer to
such operations as, for example, permuting the indices of M.
When R is parity normalized, the elements of Mr(R) and Mc(R) are necessarily con-
gruent to n mod 4. Under permutation of the rows of R, the indices of Mr(R) undergo
the same permutation. Under permutation of the columns of R, the indices of Mc(R)
undergo the same permutation.
The search method we employ requires the generation of a set of ca ndidate matrices
which are potentially Gram matrices of {− 1, 1}-matrices. We are interested in {− 1, 1}-
matrices whose determinant equals or exceeds some threshold, dmin in magnitude. For a
given n, this threshold is usually chosen to be the best known lower bound on md(n). To
be a candidate, a matrix M must possess the properties of Mr(R) and Mc(R) described
above and must have determinant greater than or equal to d2
min. The set of such candidates
is the set M□
n (dmin) whose deﬁnition is made precise below.
Deﬁnition. We denote by Mn,p be the set of p × p matrices M having the following
properties:
(1) M is symmetric and positive deﬁnite;
(2) the diagonal elements of M are all equal to n;
(3) the elements of M are integers congruent to n mod 4.
The set Mn,p(dmin) is the subset of Mn,p whose elements satisfy the additional requirement
(4) det M ≥ d2
min.



## Page 5

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 5
We deﬁne Mn = Mn,n and Mn(dmin) = Mn,n(dmin). Finally, let M□
n (dmin) be the subset
of Mn(dmin) whose elements satisfy
(5) det M = perfect square.
Positive deﬁniteness implies that the oﬀ-diagonal elements of M are less than n in
absolute value.
Just as for {− 1, 1}-matrices, there is a notion of equivalence for candidate Gram ma-
trices. Negation will not be considered because the congruence pr operty modulo 4 that
we have imposed on the matrix elements already ﬁxes the signs.
Deﬁnition. Two matrices, M1, M2 ∈ M n,p, are equivalent if one can be obtained from
the other by a permutation of indices. The equivalence class of M will be denoted EM .
Deﬁnition. An element of a matrix M ∈ M n,p is minimal if its magnitude is the smallest
allowed value. If n ≡ 1 mod 4 the minimal element is 1; if n ≡ 3 mod 4 the minimal
element is − 1. The minimal vector of length k is the vector of length k, all of whose
elements are minimal.
Deﬁnition. A set of indices A ⊆ { 1, . . . , p} is a block of M ∈ M n,p if, for every pair ( i, j)
with i ∈ A and j ∈ { 1, . . . , p} \ A, the matrix element Mi,j is minimal, and if no proper
subset of A has this property.
Remark. The blocks of any matrix M ∈ M n,p are disjoint, and there is a unique decom-
position of the full set of indices {1, . . . , p} into blocks.
Deﬁnition. A set of indices A ⊆ { 1, . . . , p} is contiguous if for any i, k ∈ A and j ∈
{1, . . . , n}, i < j < k implies j ∈ A.
Deﬁnition. A matrix M ∈ M n,p has block form if all of its blocks are contiguous.
We will also use the term “block” to refer to the sub-matrix obtained by removing all
rows and columns whose indices are not in the block.
Deﬁnition. The partial row Pr,k(M) with M ∈ M n,p and 1 ≤ r, k ≤ p is the k-
dimensional vector formed by taking the ﬁrst k components of row r of M.
Notation. For integers a and b we use a < a b to indicate that |a| < |b|, with similar
notation for other inequality signs. For integer vectors u and v, u <a v indicates that u
is lexicographically less than v where comparison of individual vector elements is made
using <a.
Deﬁnition. A matrix M ∈ M n,p is lexicographically ordered if its rows are in descending
lexicographic order, according to the ordering <a.
Since each row of M is dominated by its diagonal element, this deﬁnition is equivalent
to the criterion that, for all pairs of indices 1 ≤ i < j ≤ p, the partial rows satisfy
Pi,i− 1(M) >a Pj,i− 1(M).
Lemma 2.3. A lexicographically ordered matrix M ∈ M n,p, has block form.



## Page 6

6 W. P. ORRICK
Proof. Assume the contrary. Then there is at least one pair of blocks, ( A, B), whose
indices are interleaved. Assume the lowest index in A to be less than the lowest index
j in B. Then A is partitioned into two subsets: A<j of indices less than j and A>j of
indices greater than j. There exists i ∈ A<j and k ∈ A>j such that Mi,k is non-minimal,
since otherwise A<j and A>j would be separate blocks.
By the lexicographic ordering of M we have Pj,j− 1(M) ≥ a Pk,j − 1(M). However, all
entries of Pj,j− 1(M) are minimal since j is the smallest index in its block, whereas Mk,i =
Mi,k is non-minimal — a contradiction. □
Notation. Let M1 ∈ M n,p1 and M2 ∈ M n,p2 We say that M1 <a M2 if either
(1) there exists an index k such that 1 ≤ k ≤ min(p1, p2), Pi,i− 1(M1) = Pi,i− 1(M2) for
all i < k , and Pk,k− 1(M1) <a Pk,k− 1(M2), or
(2) p1 < p 2 and Pi,i− 1(M1) = Pi,i− 1(M2) for all i ≤ p1.
Clearly the blocks of a lexicographically ordered matrix (considered a s sub-matrices)
are themselves lexicographically ordered.
There may be many lexicographically ordered matrices equivalent to a given matrix.
Because <a is a total ordering and Mn,p is ﬁnite, any subset of Mn,p has a greatest
element.
Deﬁnition. A matrix M ∈ M n,p is lexicographically maximal if it is the greatest element
of EM under the ordering <ay.
Trivially, a matrix that is lexicographically maximal is lexicographically ord ered. The
proof of the following is straightforward.
Lemma 2.4. A matrix M ∈ M n,p is lexicographically maximal if and only if all its blocks
(considered as sub-matrices) are lexicographically maximal and are arranged in descending
lexicographic order along the diagonal.
In Section 3, we present a backtracking algorithm to generate a list containing a canon-
ical representative of each equivalence class in Mn(dmin). The canonical representative
of an equivalence class is taken to be its lexicographically maximal eleme nt. The algo-
rithm builds up matrices by augmenting the leading sub-matrix, one ro w and column per
iteration, and is so designed that any sub-matrix M ∈ M n,p, constructed at stage p, is
automatically in block form with lexicographically ordered blocks in desc ending lexico-
graphic order along the diagonal. To ensure that only canonical mat rices are produced
in the end, there is a check, performed at the completion of any bloc k, that the block
is lexicographically maximal. In the event that it is not, the sub-matrix is discarded.
To carry out this check, the following simple procedure, while not opt imal, proved to be
adequate.
2.3. Procedure IsLexMax. The procedure returns True if the block cannot be trans-
formed into some lexicographically greater block by permutation of in dices, and returns
False otherwise. It is perhaps simpler to consider how to put a block into its lexico-
graphically maximal order. There is at least one permutation that ac complishes this. If



## Page 7

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 7
the set of all such permutations includes the identity, then our rou tine is to return True,
otherwise False.
Let the block be of size p ≥ 2. The procedure goes as follows: we ﬁrst ﬁnd the set, P2, of
permutations that produce the lexicographically maximal 2 × 2 leading sub-matrix. Since
this is accomplished by placing a maximal oﬀ-diagonal element into the ( 1, 2) position, the
set P2 can contain permutations of three types, depending on the initial lo cations of the
maximal elements: the identity, if a maximal element already was in the (1, 2) position;
a single swap, if a maximal element occurred in a position with an index (r ow or column)
1 or 2; a pair of swaps, if a maximal element occurred in a position with n either index
equal to 1 or 2.
Now, given the set Pk of permutations that produce the maximal k × k leading sub-
matrix, 2 ≤ k ≤ p − 1, we produce the set Pk+1. We do this by composing each per-
mutation in Pk with each single swap ( k + 1, j), j > k + 1, that produces the maximal
(k + 1) × (k + 1) leading sub-matrix (if any exists), and with the identity, if the lea ding
(k + 1) × (k + 1) sub-matrix already is maximal. The permutations so produced ar e the
elements of Pk+1. It is in fact unnecessary to consider all possible swaps, since some
indices in the set {k + 2, . . . , p} may be equivalent (under permutation of indices) to each
other due to the structure of the matrix. Thus we need only consid er one index from each
equivalence class.
This process is iterated until either
(1) a set Pk does not contain the identity, in which case we terminate the proced ure
and return False, or
(2) we have produced Pp. If it contains the identity, we return True, otherwise False.
Notice that multiplying all elements of the set Pp by the inverse of any one of them
produces the automorphism group of the block.
3. Finding candidate Gram matrices
We perform a backtracking search, based on the methods of Moys siadis and Kou-
nias [MK] and Chadjipantelis, Kounias and Moyssiadis [CKM], to determin e the set
M□
n (dmin). Starting from the 1 × 1 matrix,
(n)
, candidate matrices are built up by
symmetrically appending one row and column at a time, until size n is reached or no con-
tinuation is possible. At this stage, the program returns to the mos t recent sub-matrix
from which there is a possible continuation that has not yet been trie d, and resumes the
search from there. Proceeding exhaustively in this manner, until t he entire search tree has
been explored, the program terminates with a complete list of candid ate Gram matrices.
Naturally, the search tree is vast, and various methods must be us ed to prune it. The
value d2
min bounds the space we need to explore. In practice, a theorem of Mo yssiadis and
Kounias, described below, provides a criterion for removing branch es of the search tree
at an early stage. However, the size of the search space grows ra pidly as dmin is lowered,
so there is a practical limit to how low the threshold can be set.



## Page 8

8 W. P. ORRICK
A second method to reduce the size of the search is to impose lexicog raphic maximality
of the matrices. This means that all but one of the branches conta ining a set of equivalent
matrices are removed. There are two aspects to this pruning. The ﬁrst is that only
lexicographically ordered matrices whose blocks are in descending lex icographic order
along the diagonal are generated. Speciﬁcally, there is an active block , namely the block
containing the index of the most recently added row and column. A ne w block begins in
index j whenever Pj,j− 1(M) is a minimal vector. The row and column vector appended to
the current sub-matrix must have non-minimal elements only within t he active block, and
must be lexicographically less than the preceding row and column. (Th e ﬁrst criterion is
actually redundant.) Furthermore, a comparison is made of the act ive block (considered
as a sub-matrix) and the previous block, and the continuation is disa llowed if it would
cause the blocks to be incorrectly ordered.
However, as discussed in Section 2.2, this alone does not guarantee that the matrix ob-
tained is lexicographically maximal. To enforce maximality, the active blo ck is subjected
to the test IsLexMax, described in Section 2.3, and the continuation is disallowed if the
test fails. This test can be extremely time-consuming, although it imp roved the eﬃciency
of the algorithm for the cases considered here. For higher orders , it may be better to omit
it, or, better, to carry it out more eﬃciently, perhaps using the me thods of [McK].
3.1. The theorem of Moyssiadis and Kounias.
Theorem 3.1. Let M =
(
Dr B
BT A
)
be a symmetric, positive deﬁnite matrix of order
m with elements taken from the set Φ whose members are greater or equal in magnitude
to some positive number c. Here Dr and A are square matrices and the order of Dr is
r ≤ m ≤ n. The diagonal elements of A are equal to n. The columns of the r × (m − r)
matrix B are taken from some set Γr ⊆ Φr.
Deﬁne d∗ and γ∗ by
d∗ =
⏐
⏐
⏐
⏐
Dr γ∗
γ∗T c
⏐
⏐
⏐
⏐ = max
γ∈ Γr
⏐
⏐
⏐
⏐
Dr γ
γT c
⏐
⏐
⏐
⏐ (3.1)
and deﬁne
ur(d) := ( n − c)m− r− 1 [(n − c) det Dr + (m − r) max(0, d)] . (3.2)
Then
det M ≤ ur(d∗) (3.3)
For the convenience of the reader, we will reproduce the proof of Moyssiadis and Kounias
below. First we point out two slight modiﬁcations of their original stat ement of the
theorem.
• The columns of B and the vector γ are taken to be members of Γ r ⊆ Φr rather
than of Φ r itself. This is needed in a practical implementation of the algorithm
where lexicographic ordering is enforced.



## Page 9

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 9
• We do not require d∗ ≥ 0 but replace d by max(0 , d) in the bound (3.2). This is
necessary in the case n ≡ 3 mod 4 since, in contrast to the case n ≡ 1 mod 4, d∗
is often negative.
Proof. By subdivision of the matrices A and B we rewrite M as


Dr B1 γ
BT
1 A1 δ
γT δT n


where γ ∈ Γr and δ is a column vector of length m − r − 1. Using the expansion by minors
on the last column of M we obtain
det M = (n − c)
⏐
⏐
⏐
⏐
Dr B1
BT
1 A1
⏐
⏐
⏐
⏐ +
⏐
⏐
⏐
⏐
⏐
⏐
Dr B1 γ
BT
1 A1 δ
γT δT c
⏐
⏐
⏐
⏐
⏐
⏐
.
Note that the ﬁrst term is an ( m − 1) × (m − 1) determinant that satisﬁes the hypotheses
of the theorem. Denote the array in the second term by
M . Either det M ≤ 0 or M is
positive deﬁnite in which case we have
det M = c
⏐
⏐
⏐
⏐
Dr − 1
c γγ T B1 − 1
c γδ T
BT
1 − 1
c δγ T A1 − 1
c δδ T
⏐
⏐
⏐
⏐ ≤ c
⏐
⏐Dr − 1
c γγ T⏐
⏐ ·
⏐
⏐A1 − 1
c δδ T⏐
⏐ .
The ﬁrst factor is bounded above by d∗, and the second, being the determinant of a
positive deﬁnite matrix whose diagonal entries are less than or equa l to n − c, is bounded
above by ( n − c)m− r− 1. Hence
det
M ≤ (n − c)m− r− 1 max(0, d∗).
By induction, using this bound and (3.1) we obtain (3.3). □
Corollary 3.2. Let M be an m × m symmetric, positive deﬁnite matrix whose diagonal
elements are less than or equal to some positive number n and whose oﬀ-diagonal elements
are greater than or equal to some positive number c in magnitude. Then
det M ≤ (n − c)m + mc(n − c)m− 1
Proof. Since M is positive deﬁnite, its determinant can only increase if we replace all
diagonal elements with the upper bound, n. Now apply Theorem (3.1) with r = 0 to this
revised matrix. □
In the n ≡ 1 mod 4 case our search algorithm will make use of Theorem (3.1) direc tly
(with c = 1 and m = n). In the n ≡ 3 mod 4 case we strengthen the theorem as follows:
Corollary 3.3. Let M =
(
Dr B
BT A
)
satisfy the conditions of Theorem (3.1) with m =
n ≡ 3 mod 4 and furthermore let M ∈ M n,n. Then
det M ≤ (n − 1)n− r det Dr +
[
(n − 1)n− r − (n − 3)n− r − (n − r)(n − 3)n− r− 1]
max(0, d∗).



## Page 10

10 W. P. ORRICK
Proof. We apply Corollary 3.2 to the matrix A′
1 := A1 − 1
c δδ T in the proof of Theorem 3.1
to obtain a bound on det M which is sharper than (3.1). Because all elements of both
A1 and δ are congruent to 3 modulo 4, it follows that the diagonal elements of A′
1 are
bounded above by n − 1 and the magnitude of the oﬀ-diagonal elements is bounded below
by 2. Therefore
det A′
1 ≤ (n − 3)m− r− 1 + 2(m − r − 1)(n − 3)m− r− 2
and det
M is bounded above by the product of this bound and max(0 , d∗). Applying the
induction step, we ﬁnd that the coeﬃcient of max(0 , d∗) in the bound on det M becomes
the sum
n− r− 1∑
j=0
(n − 1)n− r− 1− j[(n − 3)j + 2j(n − 3)j− 1].
Evaluating this sum gives the stated result. □
3.2. The algorithm. Let the set of allowed matrix elements be
Φ =
{
{1, − 3, . . . ,2 − n} if n ≡ 1 mod 4
{− 1, 3, . . . ,2 − n} if n ≡ 3 mod 4
and denote the determinant threshold (for {− 1, 1}-matrices) as dmin. The threshold for
candidate Gram matrices is then d2
min.
We carry out the following recursive procedure.
(1) Initialize variables.
r := 1 order of current sub-matrix
M1 :=
(n)
the initial sub-matrix
F0 := (()) the list of vectors (Here () is the null vector.)
e1 := n − 2 the magnitude of the maximum allowed matrix element
(2) (Beginning of the recursive step) Increment r. Build the list of vectors, ˜Fr− 1, by
appending to every vector in the list Fr− 2 each e ∈ Φ satisfying |e| ≤ emax. The
construction is carried out in such a way that ˜Fr− 1 will always be in ascending
lexicographic order (according to the ordering <a). Initialize Fr− 1 to the null
list. Build the list Γ r by appending to every vector in Fr− 2 all possible 2-vectors,
(e1, e2) ∈ Φ2 satisfying |e1|, |e2| ≤ er− 1.
(3) For each vector f in ˜Fr− 1 construct the matrix
Mr =
(
Mr− 1 f
f T n
)
.
If r = n then
(a) If det Mr ≥ d2
min and is a perfect square, then run the procedure IsLexMax
on the ﬁnal block of Mr. If it returns True then print out the matrix.



## Page 11

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 11
(b) Return to the calling procedure.
If r < n go to step (4).
(4) For each γ ∈ Γr evaluate
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
⏐
until a d is found such that the bound in Theorem 3.1 or Corollary 3.3 equals or
exceeds d2
min, or until the list Γ r is exhausted. If the list was exhausted without
ﬁnding such a d, then Mr is discarded, and we continue in step (3) with the
next vector f . Otherwise, add f to the list Fr− 1. Then test the active block for
lexicographic maximality using IsLexMax. If it passes, recursively begin again at
step (2), otherwise continue in step (3) with the next vector f .
Notes:
(a) If a new block started with index r, then index r + 1 is very important. It must be
the case that all components of the vector f ∈ ˜Fr that forms the initial segment
of row and column r + 1 are minimal except possibly the rth. If this component is
minimal as well, then the entire remainder of the matrix Mn will be ﬁlled in with
minimal elements, and we can proceed directly to the check of the pe rfect-square
condition as in step (3). If component r is non-minimal, we set
er equal to its
absolute value.
(b) No attempt has been made to improve the eﬃciency of IsLexMax by keeping track
of the automorphisms of the blocks of Dr as they are built. This may be necessary
to extend to method to higher orders in the n ≡ 3 mod 4 case.
(c) No attempt has been made to improve the eﬃciency of step (4) b y using facts about
the form of the optimal form of γ. Moyssiadis and Kounias [MK], for example,
in their analysis of n = 17 were able to predict when a component would equal
1 which avoided the need to check the entire list Γ r. This condition occurs much
less frequently in the case n ≡ 3 mod 4.
4. Order by order list of candidate Gram matrices
We state known results for all odd orders up to n = 21 and for selected higher orders.
First we introduce a few standard types of matrices that arise rep eatedly.
Notation. The matrix Jp,q is the p × q matrix with all elements equal to 1. We deﬁne
Jp := Jp,p.
Barba’s bound is attained by the determinant of a {− 1, 1}-matrix, R, if and only if
Mr(R) = Mc(R) = ( n − 1)In + Jn. This occurs in orders 1, 5, 13, 25, and 41, among
others, and we will have nothing more to say about these orders. N o other candidate
Gram matrix can have a determinant as large as Barba’s bound, but w hen n ≡ 1 mod 4
it is not unusual to ﬁnd candidate Gram matrices of high determinant which diﬀer only
slightly from the the matrix ( n − 1)In + Jn. Typically the oﬀ-diagonal entries diﬀer from
1 in only one or two rows and columns.



## Page 12

12 W. P. ORRICK
Notation. If v is a vector of length n − 1 then S(v) denotes the matrix
(
n v T
v (n − 1)In− 1 + Jn− 1
)
Notation. If v and w are vectors of length n − 2 then D(a; v; w) denotes the matrix


n a v T
a n w T
v w (n − 1)In− 2 + Jn− 2


For n ≡ 3 mod 4 deﬁne
Deﬁnition. An Ehlich block matrix is a matrix of the form
B(v1, v2, . . . , vk) := ( n − 3)In − Jn + 4




Jv1 0 . . . 0
0 Jv2
.
.
. . . .
0 0 . . . J vk




with ∑vj = n, or in other words, a matrix with diagonal elements equal to n, square
blocks along the diagonal whose oﬀ-diagonal elements are equal to 3, and all other oﬀ-
diagonal elements − 1.
In low orders, n ≡ 3 mod 4, most large-determinant candidate Gram matrices are
closely related to Ehlich block matrices. When an element a of a vector is repeated k
times consecutively, it will be convenient to denote this sequence by ak.
We describe below the candidate Gram matrices found by our proced ure or, in a few
cases which we note explicitly, matrices which were found by other me ans. In higher
orders, where the the number of matrices tends to be large, we so metimes omit the
explicit listing of matrices. Complete lists of matrices are available from the author upon
request.
4.1. n = 3 . The largest determinant is 1 × 22. Our program ﬁnds the unique candidate
Gram matrix, B(13), corresponding to this value, and no other candidates of equal o r
larger determinant.
4.2. n = 7. The maximal determinant, found by Williamson [Wi], is 9 × 26. It corresponds
to the matrix B(23, 1), which is found by our program. No other candidates of equal or
larger determinant are found.
4.3. n = 9 . The maximal determinant, found by Ehlich and Zeller [EZ], is 56 × 28. It
corresponds to the candidate Gram matrix S(5, 17). No other candidates with equal or
larger determinant are found.



## Page 13

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 13
4.4. n = 11 . This case was treated by Ehlich, who found that the maximal determ inant
is 320 × 210, but his analysis was never published. His results were reported in th e paper
of Galil and Kiefer [GK]. There are seven candidate Gram matrices. Fo ur of these have
determinant (324 × 210)2, above the value corresponding to the maximal determinant.
They are B(3, 2, 16), B(4, 17), B(5, 16) and







11 3 3
3 11 − 1 − J3,8
3 − 1 11
− J8,3 B(4, 14)







.
The failure of these four matrices to produce a maximal determinan t is discussed in the
next section.
The other three candidates all correspond to the maximal determ inant. They are
B(5, 23),











11 3 3 − −
3 11 − 3 −
3 − 11 − 3 − J5,6
− 3 − 11 −
− − 3 − 11
− J6,5 B(23)











, and











11 3 3 3 −
3 11 3 − −
3 3 11 − − − J5,6
3 − − 11 3
− − − 3 11
− J6,5 B(23)











,
where “ − ” stands for − 1. All candidates have unique characteristic equations.
4.5. n = 15 . All four candidate Gram matrices are Ehlich block matrices. The matr ices
B(43, 3) and B(6, 3, 23) have determinant (105 ·35 ·214)2, corresponding to the conjectured
maximal value, while B(34, 2, 1) and B(35) have determinant (108 · 35 · 214)2. All of
the matrices have diﬀerent characteristic equations. Our algorith m, implemented as a
Mathematica program, was able to generate the four candidates in about seven hours on
a personal computer. This is a far larger running time than for any o ther order for which
md(n) had been established, all of which require anywhere from a few millise conds to a
few minutes to produce the complete list of candidates.
4.6. n = 17. The maximal determinant for n = 17 was conjectured by Schmidt [Sc] to be
5 × 48 × 216. The conjecture was independently formulated and proved by Moy ssiadis and
Kounias [MK] The candidate Gram matrices are S(− 3, − 3, 114) with determinant (22 ×
47× 216)2, S(5, − 32, 113) with determinant (21 × 47× 216)2, D(− 3; − 33, 112; 13, − 3, 111) with
determinant (83 × 46 × 216)2, D(1; 5, − 3, 113; 1, − 33, 111) with determinant (81 × 46 × 216)2,



## Page 14

14 W. P. ORRICK
the matrix











A J 2 J2 J2 J2
J2 B J 2 J2 J2
J2 J2 B J 2 J2
J2 J2 J2 B J 2 J10,7
J2 J2 J2 J2 B
J7,10 16I7 + J7











where A =
(
17 5
5 17
)
, B =
(
17 − 3
− 3 17
)
with determinant (5175 × 43 × 216)2, and the six matrices
M (17)
1 = D(1; 1, − 36, 18; − 3, 114),
M (17)
2 = S(− 38, 18),
M (17)
3 = S(− 316),
M (17)
4 = D(− 3; − 32, 113; − 32, 113),
M (17)
5 = S(52, − 32, 112),
M (17)
6 =













17 − 3 − 3 − 3 1 1
− 3 17 − 3 1 1 1
− 3 − 3 17 1 1 1
− 3 1 1 17 − 3 − 3 J6,11
1 1 1 − 3 17 1
1 1 1 − 3 1 17
J11,6 16I11 + J11













each with determinant (5 × 48 × 216)2.
The maximal determinant corresponds to the matrix M (17)
3 For some reason, the two
matrices M (17)
1 and M (17)
5 were omitted from the list in [MK]. The characteristic equations
of the above matrices are distinct, except for those of M (17)
2 and M (17)
5 .
4.7. n = 19. Our program fails to run to completion in a reasonable amount of time, or to
turn up any candidate matrices, for any threshold below Ehlich’s bou nd (1.4). Two Gram
matrices, corresponding to the best known determinant value, 83 3 × 46 × 218, are found
by direct computation from the conjectured maximal {− 1, 1} matrices of Smith [Sm] and



## Page 15

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 15
Cohn [Co2]. They are















19 3 3 3 − − −
3 19 3 3 − − −
3 3 19 3 − − −
3 3 3 19 3 3 3 − J7,12
− − − 3 19 3 3
− − − 3 3 19 3
− − − 3 3 3 19
− J12,7 B(34)















and 




















19 − − 3 − − 3 − − 3
− 19 3 3 − − − − − −
− 3 19 3 − − − − − −
3 3 3 19 − − − − − −
− − − − 19 3 3 − − − − J10,9
− − − − 3 19 3 − − −
3 − − − 3 3 19 − − −
− − − − − − − 19 3 3
− − − − − − − 3 19 3
3 − − − − − − 3 3 19
− J9,10 B(33)





















.
Extensive searching by various random methods has failed to improv e upon this deter-
minant value. A simple exhaustive search for Ehlich block matrices with larger perfect
square determinant than that of the above matrices yields the res ult that no such matrices
exist.
4.8. n = 21 . The largest determinant for n = 21 is 29 × 59 × 220 which was found by
Chadjipantelis, Kounias, and Moyssiadis [CKM] and proved by them to be maximal. The
candidate Gram matrices are S(− 35, 115) with determinant (6 × 510 × 220)2, the matrix











A J 2 J2 J2 J2
J2 B J 2 J2 J2
J2 J2 B J 2 J2
J2 J2 J2 B J 2 J10,11
J2 J2 J2 J2 B
J11,10 16I11 + J11











where A =
(
21 5
5 21
)
, B =
(
21 − 3
− 3 21
)



## Page 16

16 W. P. ORRICK
with determinant (18432 × 55 × 220)2, and the three matrices M (21)
1 = S(5, − 35, 114),
M (21)
2 = S(54, 116), and M (21)
3 = S(− 7, − 32, 117) all with determinant (29 × 59 × 220)2.
M (21)
1 and M (21)
3 have the same characteristic equation; all others are distinct. Th e matrix
corresponding to the maximal determinant is M (21)
2 . For some reason the matrices M (21)
1
and M (21)
3 were omitted from the list in [CKM].
4.9. n = 29, 33, and 37. In orders 29 and 33 the largest known determinants were found
by Bruce Solomon using the gradient ascent algorithm described in [O SDS]. In order 37
the largest known determinant was constructed in [OS].
Unfortunately, in all three cases these lower bounds are too low to use as thresholds in
the search for candidate Gram matrices. Both time and space requ irements appear to be
growing exponentially as the threshold is lowered. The best we have b een able to do is
narrow the range within which md( n) must lie, by using somewhat higher thresholds. The
thresholds used, and the number of candidates found for each de terminant value equal to
or exceeding the given threshold, are shown in Table 1.
5. Decomposability of candidate Gram matrices
5.1. General considerations. Given a candidate Gram matrix, M, we would like to
determine whether it admits a decomposition M = RRT where R is a {− 1, 1}-matrix.
This task appears to be rather diﬃcult when only the matrix M is given. In the present
context however, more information is available, namely the complete list of candidate
Gram matrices with determinant equal to a speciﬁed perfect squar e value. In many cases
one can demonstrate the nonexistence of decompositions using th is knowledge.
Let Mr be a candidate Gram matrix from our list, and suppose that Mr = RRT for
some {− 1, 1}-matrix R. Then, by Lemma 2.2 there is a matrix, Mc = RTR, which has
the same determinant and characteristic polynomial as Mr Hence by permuting columns
of R we can convert Mc to an equivalent matrix which also appears on our list. A ﬁrst
step in our procedure is therefore to enumerate the pairs ( Mr, Mc) of candidate Gram
matrices taken from our last which have the same characteristic po lynomial. (Naturally,
for every M on our list, ( M, M ) will be such a pair, but in general there may be other
pairs too.)
The pair of formulas
Mr = RRT, M c = RTR (5.1)
implies a number of constraints on the possible rows and columns of R,
M 2
r = RMcRT (5.2)
M 2
c = RTMrR (5.3)
MrR = RMc, (5.4)
which are veriﬁed by substituting for Mr and Mc using (5.1). Let xT
j denote the jth row
of R, expressed as a row matrix, and let yj denote the jth column of R, expressed as a



## Page 17

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 17
n = 29 n = 33 n = 37
det. num. det. num. det. num.
51 × 713 2 495 × 814 1 680 × 916 1
355 × 712 1 252315 × 811 1 75 × 917 1,1
352 × 712 1 3929 × 813 1 672 × 916 1
50 × 713 1,2 490 × 814 1,1 485070 × 913 1
2448 × 711 1 3919 × 813 1 665 × 916 1
119808 × 79 1 489 × 814 1 53760 × 914 1
349 × 712 1 3911 × 813 1 4352000 × 912 1
348 × 712 1 250047 × 811 1 663 × 916 1,1
2432 × 711 1 1023942465 × 87 1 483000 × 913 1
2430 × 711 1 3906 × 813 3 4345600 × 912 1
347 × 712 2 61 × 815 13 5952 × 915 1
118656 × 79 1 31203 × 812 1 661 × 916 2
2416 × 711 1 3898 × 813 2 5946 × 915 1
345 × 712 1,3,4 3897 × 813 1,1 53504 × 914 1
2413 × 711 1 3895 × 813 1 5942 × 915 2
118128 × 79 1 31131 × 812 1 660 × 916 13
344 × 712 13 3889 × 813 1,2 659 × 916 1
2403 × 711 1 31108 × 812 1
49 × 713 14,2 486 × 814 15,3
2400 × 711 16,2 31098 × 812 1
117504 × 79 13 3887 × 813 1
2397 × 711 3 248724 × 811 1
5750784 × 77 1 3885 × 813 1,2
342 × 712 13,2,3,7 31050 × 812 4
3881 × 813 1,1
Table 1. Exhaustive enumeration of candidate Gram matrices of orders
29, 33, and 37 with thresholds 342 × 712, 485 × 814, and 659 × 916. Square
roots of the determinants of the candidates, with the factor 2 n− 1 omitted,
are given. In number of matrices column, multiple entries refer to mu ltiple
characteristic equation classes.
column matrix. The rows of Mr are denoted by mT
j , while those of Mc are denoted by
m′T
j . Using the notation xji for the ith element of the column matrix xj, we have xji = yij.
The diagonal elements of (5.2) give a constraint on the rows of R,
mT
j mj = xT
j Mcxj (5.5)
while those of (5.3) give a constraint on the columns,
m′T
j m′
j = yT
j Mryj. (5.6)



## Page 18

18 W. P. ORRICK
Finding solutions to these equations is facilitated by the large degree of symmetry that
most candidate Gram matrices with large determinant have. A permu tation of rows,
represented by a permutation matrix P , is an automorphism of M if P M PT = M.
(Multiplying on the right by P T applies the same permutation to columns, preserving
the symmetry of M.) The set of automorphisms forms a group under composition, the
automorphism group of M.
A special type of permutation, the swap, interchanges a pair of rows. The subset of the
automorphism group generated by automorphisms which are swaps forms a subgroup of
the full automorphism group. The permutation that interchanges rows i and j is written
(ij). If ( ij) and ( ik) are automorphisms of M, then ( jk) is as well. Hence we may order
the rows of M so that the rows j such that ( ij) is an automorphism, plus row i, form a
contiguous block. The lexicographic ordering we imposed earlier alrea dy implies such a
structure. It is then easy to see that the automorphism subgrou p consisting of swaps is a
direct sum of symmetric groups acting on these blocks.
When such structure is present, the right-hand side of (5.5) will de pend only on certain
sums of elements of xj, rather than on the elements individually. This greatly reduces the
amount of work that needs to be done, as should become clear in the examples that follow.
Note that we only generate solutions which are compatible with parity normalization (see
Section 2), that is, we require n + ∑
i xji ≡ 0 mod 4. Similar considerations apply to the
equation for columns (5.6).
Once the row and column solutions have been found, we use the oﬀ-d iagonal elements
of (5.2) to determine which combinations of row (or column) solutions are consistent. The
typical oﬀ-diagonal constraint takes the form
mT
j mk = xT
j Mcxk, (5.7)
and involves the sums of elements of xj mentioned above, as above, as well as the inner
products of the sub-vectors of rows j and k corresponding to these sums. The analysis is
most straightforward when the weights of these inner products a re all equal. Then only
the inner product of the full row, xT
j xk = mjk, enters rather than the individual inner
products. We will ﬁnd that this occurs in all the examples studied belo w.
There is also a compatibility condition between row and column solutions , derived
from (5.4), which is sometimes useful, namely
mT
j yk = xT
j m′
k. (5.8)
In general the constraint will depend on the element ykj = xjk and on the sums of elements
referred to previously. In cases where the oﬀ-diagonal elements of the diagonal block of Mr
containing mjj and of the diagonal block of Mc containing m′
kk are equal, the dependence
on ykj = xjk is eliminated. In the examples explicitly worked out below, this constra int
was not needed.
The above constraints, sometimes combined with other elementary consequences of
equation (5.1), can often be used to prove the non-decomposabilit y of a given pair of



## Page 19

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 19
candidate Gram matrices. We will illustrate the method on the candida te Gram matrices
for order 15, and also on a certain pair of candidate Gram matrices o f order 17.
5.2. Order 15. The four candidate Gram matrices listed in Section 4 correspond to
diﬀerent characteristic polynomials. Thus we must investigate four pairs
(B(43, 3), B(43, 3)), (B(6, 3, 23), B(6, 3, 23)),
(B(35), B(35)), and ( B(34, 2, 1), B(34, 2, 1)).
In each case we will write M = Mr = Mc. Because the row and column solution sets are
identical, some simpliﬁcations occur.
5.2.1. ( B(43, 3), B(43, 3)). This Gram matrix corresponds to the conjectured maximal
determinant. We will see that the decomposability analysis completely determines the
form of the determinant.
We may write M = 12I + B where B is the rank-4 matrix
B :=




3J4 − J4 − J4 − J4,3
− J4 3J4 − J4 − J4,3
− J4 − J4 3J4 − J4,3
− J3,4 − J3,4 − J3,4 3J3



 .
If x is a {− 1, 1} row or column vector, deﬁne
a :=
4∑
j=1
xj b :=
8∑
j=5
xj c :=
12∑
j=9
xj d :=
15∑
j=13
xj.
It follows that a, b, and c are even and that d is odd, and that − 4 ≤ a, b, c ≤ 4 and
− 3 ≤ d ≤ 3. Equations (5.5) and (5.6) both reduce to
83 = 4( a2 + b2 + c2 + d2) − (a + b + c + d)2
for rows and columns 1 through 12. It is a simple matter to ﬁnd the pa rity normalized
solutions to this equation, subject to the above constraints, usin g an exhaustive search.
The results are
(a, b, c, d) = ([ − 4, − 4, 0], 1), ([− 4, − 2, 2], − 3), ([− 2, − 2, 2], 3), or ([ − 2, 0, 4], − 1)
where the notation [ a, b, c] indicates that any permutation of a, b, and c is allowed. For
rows and columns 13 through 15, the equation is
75 = 4( a2 + b2 + c2 + d2) − (a + b + c + d)2,
and the solutions are
(a, b, c, d) = ( − 4, − 4, − 4, 1), ([− 4, 0, 2], − 1), (− 2, − 2, − 2, 3), or ([ − 2, 2, 4], 1).



## Page 20

20 W. P. ORRICK
Not all of these solutions for, say, rows are compatible with each ot her. Imposing the
equation (5.7) for all inequivalent choices of j and k reduces the solution sets to
{(− 4, − 2, 2, − 3), (− 2, 0, 4, − 1)} for rows 1–4,
{(2, − 4, − 2, − 3), (4, − 2, 0, − 1)} for rows 5–8,
{(− 2, 2, − 4, − 3), (0, 4, − 2, − 1)} for rows 9–12,
{(− 4, − 4, − 4, 1), (− 2, − 2, − 2, 3)} for rows 13–15 .
Note that the ﬁrst three of these sets may be permuted. Also the ﬁrst three components
of all solution vectors may be simultaneously permuted. Since such p ermutations give
equivalent solutions, we disregard them. The column solutions must b e also be compatible
with each other, and also with the row solutions, according to equat ion (5.8). The latter
ﬁxes a unique permutation of the column solutions, namely
{(− 4, 2, − 2, − 3), (− 2, 4, 0, − 1)} for columns 1–4,
{(− 2, − 4, 2, − 3), (0, − 2, 4, − 1)} for columns 5–8,
{(2, − 2, − 4, − 3), (4, 0, − 2, − 1)} for columns 9–12,
{(− 4, − 4, − 4, 1), (− 2, − 2, − 2, 3)} for columns 13–15 .
For each block of rows (or columns) two diﬀerent row (or column) ty pes can occur. By
using (5.1) we can determine precisely how many times each type occu rs in the block.
Consider rows 13 through 15. If any row has type ( − 4, − 4, − 4, 1), that row will have
inner product 11 or 15 with any other row of the same type. Hence a second row of type
(− 4, − 4, − 4, 1) is not allowed as the inner product must be 3. On the other hand, a type
(− 4, − 4, − 4, 1) row will have inner product 7 with any row of type ( − 2, − 2, − 2, 3), which
is also disallowed. Therefore all three of the rows 13–15 must be of t ype ( − 2, − 2, − 2, 3).
Now the matrix formed by the last three rows can be regarded as co mposed of three 3 × 4
blocks followed by a 3 × 3 block consisting entirely of 1s. The 3 × 4 blocks must have row
sums − 2 and column sums either − 3 or − 1. The row-sum condition implies that there is
a single 1 in each row, while the column-sum condition implies that there c an be no more
than a single 1 in each column. Thus there is one column with column sum − 3 and three
with column sum − 1 in each block. We may choose to place the − 3 type column ﬁrst in
each block, and likewise for rows. Then the structure of the matrix is given by
(− 4, − 2, 2, − 3) row 1
(− 2, 0, 4, − 1) rows 2, 3, and 4
(2, − 4, − 2, − 3) row 5
(4, − 2, 0, − 1) rows 6, 7, and 8 (5.9)
(− 2, 2, − 4, − 3) row 9
(0, 4, − 2, − 1) rows 10, 11, and 12
(− 2, − 2, − 2, 3) rows 13, 14, and 15 ,



## Page 21

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 21
and
(− 4, 2, − 2, − 3) column 1
(− 2, 4, 0, − 1) columns 2, 3, and 4
(− 2, − 4, 2, − 3) column 5
(0, − 2, 4, − 1) columns 6, 7, and 8 (5.10)
(2, − 2, − 4, − 3) column 9
(4, 0, − 2, − 1) columns 10, 11, and 12
(− 2, − 2, − 2, 3) columns 13, 14, and 15 .
5.2.2. Uniqueness of the decomposition. The matrix found by Smith and Cohn exhibits
the structure derived in the previous section. Here we will show tha t the matrix emerges
quite simply from the structure and that there is essentially only one such matrix.
The matrix must have the structure
R =




A1 B1 C D 1
C A 2 B2 D2
B3 C A 3 D3
E1 E2 E3 J3



 , (5.11)
where Aj, Bj, and C are 4 × 4 sub-matrices; Dj are 4 × 3 sub-matrices; and Ej are 3 × 4
sub-matrices. The matrices Aj have row and column sums ( − 4, − 2, − 2, − 2); Bj have
row and column sums ( − 2, 0, 0, 0); and C has row and column sums (2 , 4, 4, 4) (which
determines C completely and is why we need not distinguish diﬀerent Cj). The matrices
Dj have row sums ( − 3, − 1, − 1, − 1) and column sums ( − 2, − 2, − 2), while for the Ej the
row sums are ( − 2, − 2, − 2) and the column sums are ( − 3, − 1, − 1, − 1).
The row and column sums imply that
Aj ∼ A :=




− − − −
− 1 − −
− − 1 −
− − − 1



 , B j ∼ B :=




1 − − −
− − 1 1
− 1 − 1
− 1 1 −



 , C =




− 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1



 ,
Dj ∼ D :=




− − −
1 − −
− 1 −
− − 1



 , and Ej ∼ E :=


− 1 − −
− − 1 −
− − − 1

 ,
where “ ∼ ” means equivalent up to permutation of the last three rows or colum ns. The
structure (5.9), (5.10), (5.11) is preserved under permutation o f rows 2–4, of rows 6–8,
of rows 10–12, of rows 13–15, or of the corresponding columns. W e use the freedom to
permute columns to ﬁx A1 = A, B1 = B, and D1 = D in (5.11). Then use the freedom to
permute rows to ﬁx A2 = A, B3 = B, and E1 = E. Finally, another column permutation
ﬁxes B2 = B. Thus rows 1–4 and columns 1–4 are completely constructed and ha ve



## Page 22

22 W. P. ORRICK
the correct pairwise inner products. In order for these to have t he right inner products
with rows 5–8 and columns 5–8, we must have D2 = D and E2 = E. For rows 13–15 to
have the desired inner products with rows 6–8 necessitates E3 = E. Similarly columns
13–15 have the correct inner products with columns 2–4 only if E3 = E. It then follows
that A3 = A, and the matrix R such RRT = RTR = M is completely determined up
to permutations consistent with the structure of M, and negation of the entire matrix.
Consequently there is essentially only one D-optimal design of order 15 (subject to the
proof of non-decomposability of the other three candidate Gram m atrices, which follows).
5.2.3. ( B(6, 3, 23), B(6, 3, 23)). The candidate matrix may be written M = 12I + B where
B is a rank-5 matrix. Row and column vectors are subdivided in to 5 sub- vectors whose
element sums are denoted a, b, c, d, and e. The sum b is odd whereas the other four are
even. The inequalities − 6 ≤ a ≤ 6, − 3 ≤ b ≤ 3, and − 2 ≤ c, d, e ≤ 2 must hold.
For rows or columns 1 through 6, equations (5.5) and (5.6) reduce t o
99 = 4( a2 + b2 + c2 + d2 + e2) − (a + b + c + d + e)2.
Exhaustive search yields the solution set
(a, b, c, d, e) ∈ { (− 6, − 1, 0, 0, 0), (− 4, 1, [0, 2, 2]), (− 4, 3, − 2, − 2, − 2),
(− 2, − 3, 2, 2, 2), (2, − 3, [− 2, 2, 2]), (4, − 3, 0, 0, 0),
(4, 1, [− 2, − 2, 0]), (6, − 1, [0, 2, 2]), (6, 3, 0, 0, 0)}.
For rows or columns 7 through 9, equations (5.5) and (5.6) reduce t o
75 = 4( a2 + b2 + c2 + d2 + e2) − (a + b + c + d + e)2
which has the solution set
(a, b, c, d, e) ∈ { (− 6, − 3, [− 2, 0, 0]), (− 6, 1, − 2, − 2, − 2), (− 4, − 1, [0, 0, 2]),
(− 2, 3, [− 2, − 2, 0]), (0, 3, − 2, − 2, − 2), (2, − 3, 2, 2, 2),
(4, 1, [− 2, 0, 2])}.
For rows or columns 10 through 15, equations (5.5) and (5.6) reduc e to
67 = 4( a2 + b2 + c2 + d2 + e2) − (a + b + c + d + e)2
which has the solution set
(a, b, c, d, e) ∈ { (− 4, − 1, [− 2, − 2, 2]), (− 2, 1, [− 2, 2, 2]), (0, − 3, [0, 2, 2]),
(2, − 3, [0, 0, 2]), (2, 1, [− 2, − 2, 2]), (4, 3, [− 2, 2, 2]).
If for a given row 1–6 solution the compatibility condition (5.7) fails to h old for all row
7–9 solutions, we drop that solution. Likewise if a given row 7–9 solutio n is incompatible
with all row 1–6 solutions, we do not consider that solution any furth er. The compatibility
condition in this case reduces to
− 33 = xT
7 (4I5 − J5)x1



## Page 23

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 23
where xj is a solution for row j taken from the appropriate list above. Failure to ﬁnd any
x7 such that this equation holds when x1 is one of ( − 4, 1, [0, 2, 2]), ( − 4, 3, − 2, − 2, − 2),
(− 2, − 3, 2, 2, 2), or (4 , 1, [− 2, − 2, 0]) eliminates those solutions. Similarly the solutions
x7 = (− 2, 3, [− 2, − 2, 0]) and (4 , 1, [− 2, 0, 2]) are eliminated.
Imposing compatibility of the remaining row 1–6 solutions with the row 1 0–15 solutions
allows us to eliminate the solutions x10 = (0 , − 3, [0, 2, 2]) and (2 , 1, [− 2, − 2, 2]), and at
the same time, the solutions x1 = (4, − 3, 0, 0, 0) and (6 , 3, 0, 0, 0). As a consequence, x7 =
(2, − 3, 2, 2, 2) is also eliminated, since the only x1 solution with which it was compatible
was (6 , 3, 0, 0, 0).
Compatibility of the row 7–9 solutions with the row 10–15 solutions the n eliminates
x10 = (− 2, 1, [− 2, 2, 2]).
Finally, one may check that the compatibility condition between, say, row 10 and row
12, eliminates all the remaining row 10–15 solutions as possibilities. The refore, there is
no decomposition of ( B(6, 3, 2, 2, 2), B(6, 3, 2, 2, 2)).
5.2.4. ( B(3, 3, 3, 3, 3), B(3, 3, 3, 3, 3)). The equations (5.5) and (5.6) for the sums of row
and column sub-vectors have the same form for all 15 rows and all 1 5 columns, namely
75 = 4( a2 + b2 + c2 + d2 + e2) − (a + b + c + d + e)2,
where a, b, c, d, and e are odd integers in the range [ − 3, 3]. The parity normal-
ized solutions to this equation are ( a, b, c, d, e) = ([ − 3, − 3, 1, 1, 1]) and ( a, b, c, d, e) =
([− 3, − 1, − 1, − 1, 3]). Since all solutions have at least one variable set to − 3, we may use
our freedom to permute columns to ﬁx a = − 3 in the row 1 solution. Likewise, we ﬁx
b = ± 3 in row 1. Now if ( a, b, c, d, e) = ( − 3, − 3, 1, 1, 1) in row 1, then the consistency
equation (5.7) for rows requires that the same solution hold for row s 2 and 3 and that
each of rows 4–15 be one two types: ( a, b, c, d, e) = ( − 3, 3, − 1, − 1, − 1) or ( a, b, c, d, e) =
(3, − 3, − 1, − 1, − 1). On the other hand, if ( a, b, c, d, e) = ( − 3, 3, − 1, − 1, − 1) in row 1,
then the same solution must hold for rows 2 and 3, and the solution ( a, b, c, d, e) =
(− 3, − 3, 1, 1, 1) must obtain in rows 4–15.
The combination of these two facts and permutation symmetry impo ses the requirement
on the ﬁve sets of rows, {1, 2, 3}, {4, 5, 6}, . . ., {13, 14, 15}, that within each set all three
rows must be of the same type, but that outside the set, all rows m ust be of the other
type. As no more than two row sets may be constructed under the se constraints, whereas
we require ﬁve, no decomposition exists.
5.2.5. ( B(3, 3, 3, 3, 2, 1), B(3, 3, 3, 3, 2, 1)). The impossibility of decomposition follows by
an argument that is similar to but more involved than that of the prev ious case. We need
only look at the solution set for rows 1–12. Equation (5.5) becomes
75 = 4( a2 + b2 + c2 + d2 + e2 + f 2) − (a + b + c + d + e + f )2



## Page 24

24 W. P. ORRICK
where a, b, c, and d are odd integers in the range [ − 3, 3], e is an even integer in the range
[− 2, 2], and f ∈ {− 1, 1}. The parity normalized solutions are in the set
{([− 1, − 1, 3, 3], 2, − 1), ([− 3, 1, 1, 3], 2, 1), ([1, 1, 3, 3], − 2, − 1),
([− 1, 1, 3, 3], − 2, 1), ([− 3, − 3, 1, 1], 0, 1), ([− 3, − 1, − 1, 3], 0, − 1)}.
We now use the compatibility conditions among rows (5.7) to prove the impossibility
of a decomposition. We leave the arithmetical checking of the consis tency of various pairs
of solutions to the reader. A requirement of decomposability is that we be able to assign
consistent solutions to the four sets of rows {1, 2, 3}, . . ., {10, 11, 12}. If the set {1, 2, 3}
has a row of type ( − 1, − 1, 3, 3, 2, − 1) then rows 4–12 must be of type (1 , 1, [− 3, 3], 2, 1).
But two rows, in diﬀerent row sets, which both are of the latter typ e are not compatible
with each other, so it is not possible to construct four sets when on e of them contains a
row of type ([ − 1, − 1, 3, 3], 2, − 1).
Similarly, if the set {1, 2, 3} contains a row of type ( − 3, 1, 1, 3, 2, 1), then rows 4–12
must all be of type (1 , 3, 3, 1, − 2, − 1). Again, two rows of this type in diﬀerent row sets
are not compatible, so ( − 3, 1, 1, 3, 2, 1) has been eliminated.
If either of the two types ( − 1, 1, 3, 3, − 2, 1) and (1 , 1, 3, 3, − 2, − 1) appears in the set of
rows {1, 2, 3}, then rows 4–12 are of a suitable form of type ([ − 3, − 3, 1, 1], 0, 1) or type
([− 3, − 1, − 1, 3], 0, − 1). This means that at least two of the three sets {4, 5, 6}, {7, 8, 9},
{10, 11, 12} must both contain a row of the ﬁrst type, or both contain a row of t he
second type. However neither of the latter two types can appear in two diﬀerent row sets.
Hence the solutions ([ − 1, 1, 3, 3], − 2, 1) and ([1 , 1, 3, 3], − 2, − 1) are ruled out. But since,
as we just argued, neither of the two remaining solution types, ([ − 3, − 3, 1, 1], 0, 1) and
([− 3, − 1, − 1, 3], 0, − 1) can appear in two diﬀerent row sets, constructing four row set s is
impossible. Therefore there is no decomposition.
5.3. Other orders. In orders 3, 7, and 9, decompositions of the the unique largest can -
didate Gram matrices have been known for some time.
5.3.1. n = 11 . Ehlich proved the non-decomposability of the four candidates of lar gest
determinant, and showed that the three candidates of the next la rgest determinant do
decompose. We have applied our method to these seven matrices, a nd conﬁrmed his
results. As the method does not diﬀer in any substantial way from t hat applied to the
case n = 15, we omit the details.
5.3.2. n = 17 . In [MK] eight of the nine reported candidate Gram matrices were sho wn
to be non-decomposable, thus establishing the maximality of the det erminant associated
with the ninth. Since our list contains two additional candidates, we m ust, in order
to verify that result, prove them non-decomposable as well. Furth ermore, one of the
additional candidates has the same characteristic equation as one of the original nine, so
this pair must also be checked.



## Page 25

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 25
The three decompositions to be tested are then
(S(52, − 32, 112), S(52, − 32, 112)),
(D(1; 1, − 36, 18; 3, 114), D(1; 1, − 36, 18; 3, 114)),
(S(52, − 32, 112), S(− 38, 18)).
For the former two, follow the model of proof in [MK]. (We have check ed these, as well as
the original nine candidates.) As the last pair gives us a chance to illust rate the method
when Mr ̸= Mc, we present the proof here.
We let Mr = S(52, − 32, 112) and Mc = S(− 38, 18). We compute the sets of solutions to
the quadratic equation (5.5) for row 1 and for rows 2–3, and then s how that the sets are
incompatible. The equation for row 1 is
97 = a2 + b2 + c2 − 6ab + 2ac + 2bc
where a ∈ {− 1, 1} and b and c are even integers in the range [ − 8, 8]. The parity normalized
solutions are (a, b, c) = (1 , − 2, − 8) and (a, b, c) = ( − 1, 6, 2). For rows 2 and 3, the equation
is
57 = a2 + b2 + c2 − 6ab + 2ac + 2bc
and the parity normalized solutions are ( − 1, 4, − 8), ( − 1, 6, − 2), (1 , − 6, 8), (1 , − 4, − 2),
and (1 , 8, 2). The compatibility constraint (5.7)
m1 ·m2 − 16m1,2 = xT
1 (Mc − 16I)x2
which reduces to
101 = a1a2 + b1b2 + c1c2 − 3(a1b2 + b1a2) + a1c2 + c1a2 + b1c2 + c1b2
where xT
1 is represented by ( a1, b1, c1) and xT
2 by ( a2, b2, c2). Taking all pairs of solutions
from the sets enumerated above, we ﬁnd that none satisfy the co nstraint. Therefore no
decomposition exists.
5.3.3. n = 19. There are presently no known candidate Gram matrices.
5.3.4. n = 21. As in the case n = 17, in order to verify the result of [CKM] we have three
additional pairs of Gram matrices to prove non-decomposable,
(S(5, − 35, 114), S(5, − 35, 114),
(S(− 7, − 32, 117), S(− 7, − 32, 117)), and
(S(5, − 35, 114), S(− 7, − 32, 117)).
The proof parallels that of the n = 17 case, so we omit it here.



## Page 26

26 W. P. ORRICK
5.3.5. n = 29 , 33, and 37. All of the candidate Gram matrices enumerated in Table 1
have been shown not to decompose. As there are a great many mat rices to check, an
automated procedure was used for this purpose which combines so me, but not all, aspects
of the method illustrated in the case of n = 15 with a backtracking search. (In fact, the
result for n = 15 was originally obtained by the use of this algorithm. As its perform ance
is far from optimal, we will not describe it in detail here. We hope to pre sent an improved
version in a forthcoming publication.)
Combining the above with the results of [OSDS] and [OS] we are able t o place new
bounds on md(n) for these three orders. For n = 29 we conclude that 320 × 712 ≤ md(29) <
342 × 712 or in terms of Barba’s bound (1.2), 0 .865001 . . . ≤ md(29)/B(29) < 0.92447.
For n = 33 we have 441 × 814 ≤ md(33) < 485 × 814 or 0 .854667 . . . ≤ md(33)/B(33) <
0.939951. Finally, for n = 37 we ﬁnd 72 × 917 ≤ md(37) < 659 × 916 or 0 .936329 . . . ≤
md(37)/B(37) < 0.952224.
6. The range of the determinant function for n = 9 and n = 11
Another application of these methods is the determination of the co mplete range of
the determinant function for {− 1, 1}-matrices. By negation of appropriate rows and
columns, we can make the ﬁrst row of a matrix consist entirely of 1s a nd the ﬁrst column,
except for the (1 , 1) entry consist entirely of − 1s. Such matrices are called normalized.
Adding the ﬁrst row of a normalized matrix to every other row does n ot change the
determinant, and produces a matrix whose ﬁrst column has a single 1 in the (1 , 1) position
and 0s elsewhere. All entries in rows 2 through n, where n is the size of the matrix,
are either 0 or 2. Expansion of the determinant by minors on the ﬁrs t column then
shows that the determinant is equal to that of a {0, 2}-matrix of size n − 1. Thus an
n × n {− 1, 1}-determinant is always divisible by 2 n− 1. Furthermore, we have shown the
problem of maximizing the determinant of n × n {− 1, 1}-matrices to be equivalent to that
of maximizing ( n − 1) × (n − 1) {0, 1}-matrices.
The problem of the range of the determinant function was studied b y Craigen [Cr]
who asked for the complete list of integers, d, such that d is the determinant of some
(n − 1) × (n − 1) {0, 1}-matrix, or equivalently, 2 n− 1d is the determinant of some n × n
{− 1, 1}-matrix. We are focusing here on {− 1, 1}-matrices, but it is convenient to omit
the factor 2 n− 1 in the discussion, so we will be careful always to refer to normalized
determinants (see Section 1).
We ignore the sign of the determinant. For n ≤ 7 the range of the normalized deter-
minant function is [0 , md(n)], where the notation [ a, b] means all integer values between
a and b. Craigen proved that in n = 8, a gap appears for the ﬁrst time. In particular he
showed that there are no normalized determinants in the range [28 , 31] whereas the order
8 Hadamard matrix has normalized determinant 32.
Craigen also provided a table of normalized determinant values known to him at the
time. For n = 8 and n = 9 we reproduce his lists in Table 2. (For n = 8 Craigen also lists



## Page 27

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 27
n = 8 n = 9 n = 10 n = 11
[0, 18] [0, 40] [0, 102] [0, 268]
20 42 [104, 105] [270, 276]
24 [44, 45] 108 [278, 280]
32 48 110 [282, 286]
56 112 288
[116, 117] 291
120 [294, 297]
125 304
128 312
144 315
320
Table 2. The range of the normalized determinant function for orders 8,
9, 10, and 11.
19, which is almost surely a misprint.) For orders 10 and 11, Craigen ga ve partial lists.
In the table, we give what we believe to be complete lists of normalized d eterminants.
We have been able to exhibit a determinant for each of the values in th e table. The
method by which this was done is beyond the scope of this paper, and we intend to
describe it elsewhere. What is of relevance to us here is that for the two odd orders,
n = 9 and n = 11, we are able to prove that the lists are complete, that is, there are no
normalized determinant values other than those given in the table.
The method is as follows: we set the threshold in our candidate Gram m atrix ﬁnding
routine to the lowest gap in the range. For n = 9 this is 41 × 28 and for n = 11 it
is 269 × 210. The program then produces a complete list of candidate Gram matr ices
corresponding to determinants equaling or exceeding the thresho ld. If none of these
determinants correspond to any of the gaps, then we have prove d the claim. On the other
hand, if any of the candidate Gram matrices do correspond to gaps , we must then show
that these matrices do not decompose.
In the case n = 9 we ﬁnd candidate Gram matrices corresponding to the following
normalized determinants: 56 (1 matrix), 48 (4 matrices), 45 (1 mat rix), 44 (2 matrices),
and 42 (1 matrix). Since none of these correspond to gaps, comple teness is proved.
For n = 11 we ﬁnd matrices corresponding to the determinants listed in Tab le 3. There
are 196 matrices in total. All of the determinant values correspond to gaps except for
three of them, namely 300, 306, and 324. The non-decomposability of the four matrices
with determinant (324 × 210)2 was discussed previously. To establish the desired result,
one need only show that the three matrices with determinant (300 × 210)2 and the matrix



## Page 28

28 W. P. ORRICK
det. 270 271 272 273 274 275 276 278 279 280
mult. 47 1 37 8 2 8 5 1 7 10
det. 282 283 284 285 286 288 291 294 295 296
mult. 2 1 2 2 1 41 1 2 1 1
det. 297 300 304 306 312 315 320 324
mult. 1 3 2 1 1 1 3 4
Table 3. Multiplicities of the candidate Gram matrices corresponding to
the listed normalized determinants of order 11. The threshold used is 269.
with determinant (306 × 210)2 do not decompose. These matrices are











11 3 3 − −
3 11 − 3 −
3 − 11 − 3 − J5,6
− 3 − 11 3
− − 3 3 11
− J6,5 B(32)











,









11 3 3 −
3 11 − 3
3 − 11 3 − J4,7
− 3 3 11
− J7,4 B(32, 1)









,











11 3 3 − −
3 11 − 3 −
3 − 11 − 3 − J5,6
− 3 − 11 3
− − 3 3 11
− J6,5 B(4, 12)











, and











11 3 3 3 −
3 11 − − 3
3 − 11 − − − J5,6
3 − − 11 −
− 3 − − 11
− J6,5 B(3, 13)











.
There are no unusual features in the proofs of non-decomposab ility, so we omit them.
7. Conclusion and outlook
We have proved that the maximal determinant of a 15 × 15 {− 1, 1}-matrix is 25515 × 214
and conﬁrmed the known maximal values for the other odd orders w hich do not attain the
Barba bound, up to order 21, except for 19. We have also establish ed new upper bounds
on the maximal determinant in orders 29, 33, and 37.
Convincing conjectures exist for the maximal determinants for or ders n = 19 [Sm], 22,
23 [OSDS], and 37 [OS]. We hope that the methods of this paper can be e xtended to
handle at least some of these cases.
Order 19 may be tractable using the current method with eﬃciency im provements in
the computer code, and perhaps parallelization. For higher orders , n ≡ 3 mod 4, there are
excellent lower bounds on the maximal determinant, but these can p ossibly be improved.
It is unlikely that our method can be applied to these cases without a n ew algorithm.



## Page 29

THE MAXIMAL {−1, 1}-DETERMINANT OF ORDER 15 29
The smallest even order for which the maximal determinant is unknow n is 22, which
may well be tractable, although it is too early to tell until experiment s are done.
The biggest hope is for orders n ≡ 1 mod 4, the lowest open case of which is n = 29.
The major hurdle to be overcome here is the ineﬃciency of the progr am that searches for
candidate Gram matrices. Eﬀorts are underway to try to improve t his. In general, the
n ≡ 1 mod 4 cases are the most amenable to our method, and the major d eterminant of
success is how close the actual maximum lies to the Barba bound. Thu s we are especially
optimistic about the case n = 37.
Acknowledgments
I carried out much of this work as a Research Associate in the Depar tment of Math-
ematics and Statistics at the University of Melbourne, and gratefu lly acknowledge the
support of Tony Guttmann and of the Australian Research Council. A stimulating col-
laboration with Judy-anne Osborn extending this work has produce d some new insight
into the original result. In particular I thank her for a discussion in w hich a key property
of the lexicographic ordering used in the Gram matrix ﬁnding algorithm was understood.
I used Mathematica extensively during this project and also thank Indiana University fo r
the use of its Sun E10000 and IBM RS/6000 SP computing platforms.
References
[Ba] G. Barba, Intorno al teorema di Hadamard sui determinanti a valore massimo, Giorn. Mat.
Battaglini 71 (1933) 70–86.
[Br] A. E. Brouwer, An inﬁnite series of symmetric designs, Math. Centrum Amsterdam Report ZW
202/83 (1983).
[CKM] T. Chadjipantelis, S. Kounias and C. Moyssiadis, The maximum de terminant of 21 × 21 (+1, − 1)-
matrices and D-optimal designs, J. Statist. Plann. Inference 16 (1987) 167–178.
[Co1] J. H. E. Cohn, On determinants with elements ± 1,II, Bull. London Math. Soc. 21 (1989) 36–42.
[Co2] J. H. E. Cohn, Almost D-optimal designs, Utilitas Math. 57 (2000) 121–128.
[Cr] R. Craigen, The range of the determinant function on the set o f n × n (0, 1)-matrices, J. Combin.
Math. Combin. Comput. 8 (1990) 161–171.
[Eh1] H. Ehlich, Determinantenabsch¨ atzungen f¨ ur bin¨ are Matrizen, Math. Z. 83 (1964) 123–132.
[Eh2] H. Ehlich, Determinantenabsch¨ atzungen f¨ ur bin¨ are Matrizen mit N ≡ 3 mod 4, Math. Z. 84 (1964)
438–447.
[EZ] H. Ehlich and K. Zeller, Bin¨ are Matrizen, Z. Angew. Math. Mech. 42 (1962) T20–T21.
[FKS] R. J. Fletcher C. Koukouvinos and J. Seberry, (submitted, 2 003).
[GK] Z. Galil and J. Kiefer, D-optimum weighing designs, Ann. Statist. 8 (1980) 1293–1306.
[Ha] J. Hadamard, R´ esolution d’une question relative aux d´ eterminants, Bull. Sci. Math. 2 (1893) 240–
246.
[KKS] C. Koukouvinos, S. Kounias and J. Seberry, Supplementary d iﬀerence sets and optimal designs,
Discrete Math. 88 (1991) 49–58.
[McK] B. D. McKay, Isomorph-free exhaustive generation, J. Algorithms 26 (1998) 306–324.
[MK] C. Moyssiadis and S. Kounias, The exact D-optimal ﬁrst order s aturated design with 17 observa-
tions, J. Statist. Plann. Inference 7 (1982) 13–27.
[OS] W. P. Orrick and B. Solomon, Large-determinant sign matrices o f order 4 k + 1, arXiv preprint
math.CO/0311292.



## Page 30

30 W. P. ORRICK
[OSDS] W. P. Orrick, B. Solomon, R. Dowdeswell & W. D. Smith, New Low er Bounds for the maximal
determinant problem, arXiv preprint math.CO/0304410.
[Pa] R. E. A. C. Paley, On orthogonal matrices, J. Math. Phys. 12 (1933) 311–320.
[Sc] K. W. Schmidt, Problem 72–19, A bound for a 4k-order maximal ( 0, 1) determinant, SIAM Rev. 15
(1973) 673–674.
[Sm] Warren D. Smith, Studies in Computational Geometry Motivated by Mesh Genera tion, Ph. D.
dissertation, Princeton University (1988).
[Sp] E. Spence, Skew-Hadamard matrices of the Goethals-Seidel t ype, Canad. J. Math. 27 (1975) 555–
560.
[Wo] W. Wojtas, On Hadamard’s inequality for the determinants of or der non-divisible by 4, Colloq.
Math. 12 (1964) 73-83.
[Wi] J. Williamson, Determinants whose elements are 0 and 1, Amer. Math. Monthly 53 (1946) 427–434.
Department of Mathematics, Indiana University, Bloomingt on IN 47405, USA
