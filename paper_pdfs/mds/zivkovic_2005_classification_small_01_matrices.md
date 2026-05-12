# Extracted text: zivkovic_2005_classification_small_01_matrices.pdf

Source PDF: zivkovic_2005_classification_small_01_matrices.pdf

Pages: 45



## Page 1

arXiv:math/0511636v1  [math.CO]  25 Nov 2005
Classiﬁcation of small (0, 1) matrices
Miodrag ˇZivkovi´ c
11000 Beograd
Marka ˇCelebonovi´ ca 61/15
Serbia and Montenegro
Abstract
Denote by An the set of square (0 , 1) matrices of order n. The set An, n≤ 8, is
partitioned into row/column permutation equivalence clas ses enabling derivation of
various facts by simple counting. For example, the number of regular (0, 1) matrices
of order 8 is 10160459763342013440. Let Dn,Sn denote the set of absolute determi-
nant values and Smith normal forms of matrices from An. Denote by an the smallest
integer not in Dn. The sets D9 andS9 are obtained; especially, a9 = 103. The lower
bounds for an, 10≤ n≤ 19, (exceeding the known lower bound an≥ 2fn− 1, where
fn is nth Fibonacci number) are obtained. Row/permutation equiva lence classes of
An correspond to bipartite graphs with n black and n white vertices, and so the
other applications of the classiﬁcation are possible.
Key words: (0, 1) matrices, Smith normal form, permutation equivalence,
determinant range, classiﬁcation
1991 MSC: 15A21, 15A36, 11Y55
1 Introduction
LetAn denote the set of square (0 , 1) matrices of order n. Hadamard maximum
determinant problem is: ﬁnd the maximum determinant among the mat rices
inAn. In this paper we consider a slightly more general problem: determin e
the setDn ={|detA|| A∈A n}.
It is known [1] that determinants of (0 , 1) matrices of order n are related to
determinants of± 1 matrices of order n + 1. If A is a (0 , 1)-matrix of order n,
let B = Ψ( A) be a ± 1-matrix of order n + 1 obtained from A by replacing
Email address: ezivkovm@matf.bg.ac.yu (Miodrag ˇZivkovi´ c).
1 Supported by Ministry of Science and Technology of Serbia, G rant 1861
Preprint submitted to Linear Algebra and its Applications 3 0 October 2018


## Page 2

its 0 by − 1, bordering with a row − 1’s on the top, and a column of 1’s on
the right. Clearly, Ψ is a one-to-one correspondence. By adding ro w 1 of B to
each of the other rows of B, we see that det B = 2 n det A.
By the Hadamard inequality |det B|≤
√
(n + 1)n+1, and therefore for all A∈
An|det A|≤ 2− n
√
(n + 1)n+1. The equality is attained if B is an Hadamard
matrix, i.e. if BB T = (n+ 1)In+1, where T denotes transposition, and In is the
unit matrix of order n; for n > 2 this implies n = 4 k− 1. For upper bounds
for determinants of A∈A n see for example [2].
Let dn denote the largest element in Dn, and let an be the smallest integer not
inDn. Craigen [3] shows that the set Dn is the interval{1, 2, . . . , d n} for n≤ 6,
but not for n = 7, because a8 = 41 < d 8 = 56; he suggests that a9 = 103.
Some interesting sequences, related to (0 , 1) matrices are found in [4]: A003432
(the sequence dn), A013588 (the sequence an), A051752 ( cn, the number of
matrices in An with the determinant dn) and A055165 ( mn, the number of
regular matrices in An). A few ﬁrst members of these sequences are given in
the following table. The values of a9, c8, c9 and m8 seem to be new.
A003432 A013588 A051752 A055165
n dn an cn mn
1 1 2 1 1
2 1 2 3 6
3 2 3 3 174
4 3 4 60 22560
5 5 6 3600 12514320
6 9 10 529200 28836612000
7 32 19 75600 270345669985440
8 56 41 ∗195955200 ∗10160459763342013440
9 144 ∗103 ∗13716864000
10 320
11 1458
12 3645
13 9477
In this paper, which is a continuation of [5], the matrices in An, n≤ 8, are
2


## Page 3

partitioned into row/column permutation equivalence classes, enab ling the
classiﬁcation by ADV, and more precisely — by SNF (see section 2). Le tSn
denote the set of SNF’s of matrices in An. In section 3 the sets D9 andS9 are
determined. In section 4 the lower bounds for an, 10≤ n≤ 19 are obtained;
cn, n≤ 9, are obtained in section 5.
We introduce now some notation. If A = [ aij] and B = [ bij] are matrices of
the same dimension m× n, we say that A < B if A is lexicographically less
than B, i.e. if for some pair of indices ( i, j ) the ﬁrst i− 1 rows of A and B
are equal, the ﬁrst j− 1 elements in the ith row of A and B are equal, and
aij < b ij. For example,



1 0
1 0


 <



1 0
1 1


 .
The smallest matrix in a set A is the representative of A.
Denote by Pi,j the permutation matrix obtained from In by exchanging the
ith and jth row.
The matrices A, B ∈ An are equivalent [7], A ∼ B, if B is be obtained
from A by a sequence of elementary row/column operations of the follow-
ing types: exchange of two rows/columns, multiplication of a row/co lumn by
− 1, and addition/subtraction of a row/column to/from another row /column.
Let SNF( A) denote the SNF of A. It is known that A∼ B is equivalent to
SNF(A) = SNF( B) (in [7] this statement is proved for polynomial matrices).
The SNF diag( d1, d 2, . . . , d n) is written simply as a vector ( d1, d 2, . . . , d n). If
diagonal elements of SNF are repeated, we use the shortened exp onential
notation. For example, (1 3, 2, 0) is short (1 , 1, 1, 2, 0). If s∈S n, then we also
say that the SNF-class s is the set {A∈A| SNF(A) = s}.
Let Jn denote the square matrix of order n with all elements equal to one.
2 Classiﬁcation of (0, 1) matrices of order 8 or less
The set Dn could be obtained by computing determinants of all A∈A n. A
better approach is to group matrices with the same determinant, a nd then
to compute the determinant of only one matrix in each group. It is us eful
to classify An into subsets with constant absolute determinant value(ADV),
or into even smaller subsets with constant SNF. We now review some s uch
partitions ofAn.
3


## Page 4

Let Π r denote the group of row permutations of matrices from An. Permuta-
tions from Π r preserve ADV.
The representative of the matrix A orbit is obtained from A by sorting its rows
into a nondecreasing sequence. Rows of A correspond to binary numbers less
than N = 2 n. Therefore, the number of orbits of Π r inAn is equal to
(N +n− 1
n− 1
)
,
i.e. the number of nondecreasing sequences of length n from{0, 1, . . . , N − 1}.
Let Π denote the group of row and column permutations; Π also pres erves
ADV. The group Π induces an equivalence relation π overAn. We say that
matrices A and B are permutationally equivalent, A∼ π B, if they are in the
same orbit of Π. Let Aπ denote the representative of the matrix A equivalence
class ( π-class; we say shorter that Aπ is a π-representative of A).
Example 1 The π-representative of







1 0 1
1 1 0
1 0 0







is the matrix 






0 0 1
0 1 1
1 0 1







,
the smallest of all 36 permutationally equivalent matrices.
LetAπ
n denote the set of π-representatives inAn. In [8] it is shown that the
number of π-classes inAn is given by:
|Aπ
n|=
∑
i1+2i2+...+nin=n
∑
j1+2j2+...+njn=n
C(i)C(j) exp2
n∑
r,s=1
irjs2(r,s), (1)
where the summation is over all vectors i = (i1, i 2, . . . , i n), j = (j1, j 2, . . . , j n),
and
C(i) = n!/ (1i1i1! . . . n inin!)
is the number n-permutations with ir cycles of length r, r = 1, 2, . . . , n ; ( r, s )
denotes GCD of integers r, s. The values |Aπ
n| are listed in Table 1; they are
easily computed for quite a large n using, for example, UBASIC [9]. It is seen
that pn is close to 2 n2
/ (n!)2 for n≤ 15. An eﬀective algorithm to generate the
representative Aπ of a given matrix A (section 2.3) simpliﬁes the classiﬁcation
of matrices, because it enables to deal with the small subset Aπ
n ofAn.
4


## Page 5

Table 1
The number of permutationally nonequivalent matrices in An, n≤ 15.
n (2n2
/n !2)/|Aπ
n|
|Aπ
n|
1 1.00000 2
2 0.57143 7
3 0.39506 36
4 0.35892 317
5 0.41433 5624
6 0.52685 251610
7 0.65875 33642660
8 0.77266 14685630688
9 0.85533 21467043671008
10 0.91045 105735224248507784
11 0.94565 1764356230257807614296
12 0.96754 100455994644460412263071692
13 0.98088 19674097197480928600253198363072
14 0.98886 13363679231028322645152300040033513414
15 0.99358 31735555932041230032311939400670284689732948
2.1 Matrix extension
In order to classify matrices in An by ADV values, one has to select carefully
the order by which determinants are computed. It is natural to st art from
matrices of order n− 1, and then to extend them by one row and one column
of ones and zeros in each possible way. For an arbitrary B∈A n− 1, let bord( B)
denote the subset of An, containing matrices with the upper left minor equal
to B. We say that the matrices in bord( B) are obtained by extending B; if
A∈ bord(B), then A is an extension of B.
The calculation of determinants of all matrices in bord( B) is an easy task. If
A∈ bord(B), then A is of the form
A =



B y
x b


 , (2)
5


## Page 6

where x = [x1 x2 . . . x n− 1] and y = [y1 y2 . . . y n− 1]T . Then [1]
det A = b det B−
n− 1∑
i=1
n− 1∑
j=1
xiyj det Bij, (3)
where Bij is the cofactor of B, corresponding to aij.
Obviously,
An ={A|(B, x, y, b )∈A n− 1×{ 0, 1}n− 1×{ 0, 1}n− 1×{ 0, 1}}.
If we precompute cofactors Bij, then determinant of each matrix from bord( B)
is computed by only one addition: for the ﬁxed x, the column y might traverse
the set of possible values via a Gray code (so that in the sequence of y’s each
two subsequent vectors diﬀer in exactly one position).
Williamson [1] noted that it is enough to let B cross the set of π-representa-
tives inAn− 1. Let bord π(B) denote the set of π-representatives of matrices in
bord(B).
Lemma 2 If B∼ π B′ then bordπ(B) = bord π(B′).
PROOF. Let A∈ bordπ(B). If the row/column permutations, transforming
B into B′, are applied to the ﬁrst n− 1 rows/columns of A, then the ma-
trix with the upper left minor equal to B′ is obtained. Therefore, the matrix
permutationally equivalent to A is obtained by extending B′, meaning that A
is permutationally equivalent to a matrix from bord( B′), i.e. A∈ bordπ(B′).
Analogously, bord π(B′)⊆ bordπ(B), and so bord π(B′) = bord π(B). ✷
Not only determinants, but also SNF’s of matrices in bord( B) can be ef-
ﬁciently computed. The preprocessing step is to compute D = SNF( B) =
diag(d1, d 2, . . . , d n), and the matrices P , Q, such that P BQ = D,|det P| =
|det Q| = 1. In order to determine SNF( A) for an arbitrary A∈ bord(B) of
the form (2), we use the identity



P 0
0 1






B y
x b






Q 0
0 1


 =



D P y
xQ b


 . (4)
Denote xQ = [ a1 a2 . . . a n], P y = [ c1 c2 . . . c n]T . Suppose d1 = d2 =
··· = dk = 1, for some k, 1 ≤ k ≤ n. Transforming the matrix from the
righthand side of (4) by subtracting the row i multiplied by ci from the row
n, 1 ≤ i≤ k, and then subtracting the column i multiplied by ci from the
6


## Page 7

column n, 1≤ i≤ k, we derive that A is equivalent to
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

1 . . . 0
0 . . . 0 0
.
.
. . . . .
.
.
.
.
. .
.
.
.
.
.
0 . . . 1
0 . . . 0 0
0 . . . 0 dk+1 . . . 0 ck+1
.
.
. .
.
.
.
.
. . . . .
.
.
.
.
.
0 . . . 0
0 . . . d n cn
0 . . . 0 ak+1 . . . a n b−
∑k
i=1 aici
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

. (5)
Hence, SNF(A) determination is reduced to determination of SNF of a matrix
of order n− k. The special cases when k≥ n− 1 are extremely simple, and
they are not rare at all, because the corresponding SNF-classes a re among the
largest ones (at least for n≤ 9). More generally, one can reduce ai, ci modulo
di, 1≤ i≤ rank B.
2.2 Φ-extension
Following Williamson [1], the approach based on extending π-representatives
only, can be further improved.
For an arbitrary A∈A n let A′ = XiA denote the matrix with the ith row
equal to the ith row of A, and with the row j̸= i equal to the coordinatewise
modulo two sum of jth and ith row of A. Equivalently, A′ = RAS, where
R is the matrix obtained from In by subtracting ith row from the others,
and then by multiplying ith row by − 1; S is the matrix obtained from In by
changing sign of columns corresponding to ones in the ith row of A. A third
equivalent deﬁnition of Xi [1] can be stated as follows: in the ± 1 matrix
B = Ψ(A) of order n + 1, the rows 1 and ( i + 1) are exchanged, then the ﬁrst
row is ”normalized” to all ones by changing signs of appropriate colum ns. By
applying Ψ − 1, the matrix A′ is obtained. Therefore, application of Xi to A
corresponds to a special row permutation in Ψ( A) (followed by scaling). It is
natural to denote the identity transformation by X0, X0A = A.
The transformation Xi also preserves ADV. The composition of arbitrary two
transformations Xi, Xj is equivalent to only one:
Xi(XjA) =





Pi,j(XiA), if 1≤ i, j ≤ n if i̸= j
A, if 1≤ i = j≤ n
.
7


## Page 8

Let Φr denote the set of ( n + 1)! transforms of the form P Xi, 0≤ i≤ n, where
P is an arbitrary permutation matrix.
Theorem 3 The set Φr is a transformation group of An.
PROOF. We have
XiP A = P XpiA,
where pi is the index of the row of A, which is moved to the position i after the
left multiplication by P . Let P1 and P2 be the two permutation matrices and
let pj be the position to which P1 moves the row j after the left multiplication.
Then
P2XjP1Xi = P2P1Xpj Xi =





P2P1, p j = i
P2P1Ppj,iXpj , p j̸= i
.
If P1 = P is an arbitrary permutation matrix, 1 ≤ i≤ n, P2 = P − 1, and
pj = i, then
(P Xi)− 1 = P − 1Xj. ✷
Clearly, each orbit of Φ r contains at most n + 1 orbits of Π r.
The corresponding transformation AXj over the columns of A (coordinatewise
addition modulo two of the column i to all other columns) is deﬁned by AXj =
(XjAT )T . Let Φ c denote the group generated by column permutations and
column transformations (·)Xi.
Let Φ be the group generated by the elements of groups Φ r and Φ c; it also
preserves ADV and its size is ( n + 1)! 2. Matrices A and A′ are said to be
φ-equivalent, A∼ φ A′, if they belong to the same orbit of Φ. Equivalently,
A∼ φ A′ if and only if there exist row and column permutations P , Q, and
row and column transformations Xi, Xj, such that A = P XiA′XjQ. For an
arbitrary A∈A n let Aφ denote the φ-representative of A; φ-class of A is the
orbit of Φ containing A.
Let bord φ(B) denote the set of φ-representatives of matrices in bord( B).
Williams [1] noted that Φ and Π have similar properties: in order to obtain the
setAφ
n of all φ-representatives inAn, it is enough to extend φ-representatives
inAn− 1.
Lemma 4 If B∼ φ B′, then bordφ(B) = bord φ(B′).
PROOF. If B and B′ are φ-equivalent, then there exist g∈ Φ, transforming
B into B′. Suppose A∈ bordφ(B). Then there exists a matrix A′∈ bord(B),
A′∼ φ A. By applying g to upper left minor of A, the matrix A′′∼ φ A′, A′′∈
8


## Page 9

bord(B′) is obtained. Therefore, A∼ φ A′′, and A∈ bord(B′). Because A is a
φ-representative, we obtain A∈ bordφ(B′), implying bord φ(B)⊆ bordφ(B′).
Analogously, bord φ(B′)⊆ bordφ(B), and hence bord φ(B) = bord φ(B′). ✷
2.3 Eﬀective determination of π-representatives
The classiﬁcation of matrices in An by extending matrices from Aφ
n− 1 must
be accompanied by an eﬀective procedure to determine Aπ and Aφ for an
arbitrary A∈A n.
The matrix Aπ is the smallest among the family of at most n! matrices obtained
by sorting rows of all the column permutations of A. Search is performed more
eﬃciently by a branch-and-bound algorithm. If we know the ﬁrst i rows of Aπ
(i.e. the row and column permutations P , Q such that the ﬁrst i rows of P AQ
are minimal), then the next row of Aπ is a smallest column permutation (only
permutations preserving the ﬁrst i rows of P AQ are considered) of some of
the remaining rows of P AQ.
Algorithm 1 Branch-and-bound algorithm to determine Aπ given A∈A n.
Input : A∈A n
Output : Aπ; the permutation matrices P , Q, such that P AQ = Aπ;
count – the number of pairs (P, Q ), such that P AQ = Aπ;
P (0)← In; Q(0)← In; Aπ← Jn;
i← 0;
count← 0;
Optimize(i);
{Continuation of the search for Aπ starting from the row i of P (i− 1)AQ(i− 1),}
{i.e. when the ﬁrst i− 1 rows are already chosen and permuted}
Optimize(i)
Generate the minimal set of boundaries Σ(i) = (s(i)
0 = 0, s (i)
1 , . . . , s (i)
ki = n)
between adjacent columns of P (i− 1)AQ(i− 1), such that the (i− 1)-preﬁxes
of columns from s(i)
j− 1 + 1 to s(i)
j are mutually equal, 1≤ j≤ ki;
for j = i to n do
vjl←
∑sl
r=sl− 1+1
(
P (i− 1)AQ(i− 1)
)
j,r
, 1≤ l≤ ki ;{the number of 1’s}
{in positions from s(i)
j− 1 + 1 to s(i)
j in the jth row of P (i− 1)AQ(i− 1)}
L(i)← the list of indices of largest vectors vj = (vj1, v j2, . . . , v jki), i≤ j≤ n;
for all j∈ L(i) do{ the candidates for the ith row of Aπ}
P (i)← Pi,jP (i− 1);{ exchange the rows i and j}
9


## Page 10

compute Q(i) from Q(i− 1), so that all 1’s in the part of the row i from
s(i)
l− 1 + 1 to s(l)
i are moved to the right end of the part, 1≤ l≤ ki;
{hence preserving the ﬁrst i− 1 rows of P (i)AQ(i)}
compare the ith row of P (i)AQ(i) to the ith row of Aπ:
if the ith row of P (i)AQ(i) is less then
copy the ﬁrst i rows from P (i)AQ(i) into Aπ;
ﬁll with ones the rest of Aπ;
if i = n then P← P (i); Q← Q(i); count← 1; else Optimize(i + 1);
else if the ith row of P (i)AQ(i) greater then
continue;{bound step: try the next row index from L(i)}
else
if i = n then count← count + 1; else Optimize(i + 1);
Example 5 Algorithm 1, applied to the matrix from Example 1, gives the
same π-representative as obtained by trivial algorithm, see Figu re 1.
The Algorithm 1 is not eﬃcient for extremely symmetric matrices, suc h as In:
in that case bound step does not ever occur, because all the rema ining rows
are always equally good. Hence, Algorithm 1 must be improved, in orde r to
detect some symmetries, and to avoid some unnecessary repetitio ns. Suppose
that there remain l rows not included in Aπ, and that the column classes
deﬁned by Σ (n− l− 1) are such, that all column classes in the remaining rows
are uniform (they contain either all ones or all zeros), except for at most one
column class, which in that case has l columns, with the row and column sums
both equal to l− 1 or 1. Then, because of the symmetry, it is enough to put
in L(n− l− 1) only one of the l remaining rows. After the incorporation of this
simple heuristic, the algorithm much more eﬃciently deals with the matr ices
such as In, the complement of In, and the other highly symmetric matrices.
Using Algorithm 1, it is possible to determine Aφ for an arbitrary A∈A n: it is
enough to ﬁnd π-representatives of all ( n + 1)2 matrices XiAXj, 0≤ i, j ≤ n,
and then to choose the smallest among them.
One of the outputs from Algorithm 1 is the number of the pairs of row /column
permutations, transforming A into Aπ. That number is used to determine the
size of the π-class of AT , as it will be demonstrated below.
Consider the problem of counting the matrices in the π-class of an arbitrary
A∈A n. For an arbitrary B∈A n let B0 denote the matrix obtained from B
by sorting its rows. If A has ik groups of k equal rows, 1 ≤ k≤ n, then the
number of matrices that could be obtained from A by row permutations is
a = n!/
n∏
k=1
ik!
10


## Page 11

i = 0, Aπ =
[ 1 1 1
1 1 1
1 1 1
]
, P (0)AQ(0) =
1 2 3
1 1 0 1
2 1 1 0
3 1 0 0
i = 1, Σ (1) ={0, 3}, L(1) = (3)
1 2 3
3 1 0 0
2 1 1 0
1 1 0 1
→
3 2 1
3 0 0 1
2 0 1 1
1 1 0 1
→ P (1)AQ(1), Aπ←
[ 0 0 1
1 1 1
1 1 1
]
i = 2, Σ (2) ={0, 2, 3}, L(2) = (2, 3)
3 2 1
3 0 0 1
2 0 1 1
1 1 0 1
→ P (2)AQ(2), Aπ←
[ 0 0 1
0 1 1
1 1 1
]
i = 3, Σ (3) ={0, 1, 2, 3}, L(3) = (3)
3 2 1
3 0 0 1
2 0 1 1
1 1 0 1
→ P (3)AQ(3), Aπ←
[ 0 0 1
0 1 1
1 0 1
]
P← P (3) =
[ 0 0 1
0 1 0
1 0 0
]
, Q← Q(3) =
[ 0 0 1
0 1 0
1 0 0
]
3 2 1
3 0 0 1
1 1 0 1
2 0 1 1
→
2 3 1
3 0 0 1
1 0 1 1
2 1 0 1
→ P (2)AQ(2)
i = 3, Σ (3) ={0, 1, 2, 3}, L(3) = (3)
2 3 1
3 0 0 1
1 0 1 1
2 1 0 1
→ P (3)AQ(3),
❄
❄
j = 3
❄
j = 2 j = 3
 
 
 
 
   ✠
❅
❅
❅
❅
❅❅ ❘
❄ ❄
❄ ❄
j = 3 j = 3
Fig. 1. An example of π -representative determination by Algorithm 1.
The representative of these a matrices is A0. An arbitrary matrix A′, obtained
from A by a column permutation, generates in the same manner a new set of
a matrices if and only if A′
0̸= A0. If the number of diﬀerent matrices A′
0 is
b, then the size of the π-class of A is ab. It is simpler to obtain b by counting
the number p of column permutations A′ of A satisfying A′
0 = A0, because
b = n!/p . Note that p is preserved by row and column permutations of A.
Applying Algorithm 1 to (AT )π, p is obtained even more easily. Indeed, suppose
that A is already a π-representative, i.e. A = Aπ. Then Algorithm 1 counts the
row permutations A′′of A, such that there exists a column permutation A′′′of
A′′, equal to Aπ. Now we ﬁnd A′ = (( AT )π)T and apply Algorithm 1 (again)
11


## Page 12

to ( A′)T . The matrix ( A′)T is a π-representative, because (( A′)T )π = ( A′)T .
Algorithm 1 gives the number of row permutations ( A′′)T of ( A′)T , such that
there exists a column permutation ( A′′′)T of ( A′′)T , equal to ( A′)T . In other
words, we obtain the number of column permutations A′′of A′, such that there
exists a row permutation A′′′of A′′, equal to A′ — which is exactly p (count
in Algorithm 1).
Example 6 Looking again at Example 5, we see that there are two pairs
(P, Q ) that minimize P AQ. Therefore, there are 3!2/ 2 = 18 matrices in the
π-class of AT .
The problem of counting the matrices in the SNF-class of an arbitrar y A∈A n
is much harder. It is even harder is to enumerate the sets An,k ={A∈A|
rank A = k}, 0≤ k≤ n: (especially mn =An,n) We now explicitly enumerate
the setsAn,1,An,2, using the following characterization of matrices in An,2.
Lemma 7 If the matrix A∈A n,2 contains three diﬀerent nonzero columns
a, b, c, then one of them is equal to the sum of the other two, for examp le
c = a + b. Furthermore, the set of nonzero rows of the matrix [a b ] equals to
{[0 1] , [1 0]}. There can not be four diﬀerent nonzero columns in A.
PROOF. Suppose A∈A n,2. If two nonzero columns of A are linearly de-
pendent, then they are obviously equal. Suppose a, b, c are the three diﬀerent
nonzero linearly dependent columns, i.e. αa + βb + γc = 0 for some integers
α , β , γ. The coeﬃcients α , β , γ must be nonzero; otherwise, if for example
α = 0, then βb + γc = 0 implies b = c. Denote by U the set of nonzero rows
of the n× 3 matrix [ a b c ]. Then
• |U|> 1; otherwise it would be a = b = c.
• U∩{ [1 0 0] , [0 1 0] , [0 0 1]} =∅; if, for example [1 0 0] ∈ U, then α = 0.
• therefore, U⊆{ [1 1 1] , [0 1 1] , [1 0 1] , [1 1 0]} and U̸={[1 1 1]}.
• [1 1 1] /∈ U; if [1 1 1]∈ U, and for example [0 1 1]∈ U, then from α +β +γ = 0
and β + γ = 0, it follows α = 0.
• U̸={[0 1 1] , [1 0 1] , [1 1 0]}; otherwise β + γ = 0, α + γ = 0, α + β = 0
implies α = β = γ = 0.
Hence, there are three possibilities for U left:{[0 1 1], [1 0 1]}, or{[0 1 1], [1 1 0]},
or{[1 0 1] , [1 1 0]}. If U ={[0 1 1] , [1 0 1]}, then β + γ = 0, α + γ = 0 implies
(α, β, γ ) = γ(− 1,− 1, 1), i.e. c = a + b; the set of nonzero rows of [ a b ] is
{[0 1] , [1 0]}. The two other cases are symmetrical.
Suppose that A contains four diﬀerent columns a, b, c, d. Then we must have
for example c = a + b and the set of nonzero rows of [ a b ] is {[0 1] , [1 0]}.
Applying the ﬁrst part of Lemma to a, b, d, we conclude that d = a + b or
a = b + d or b = a + d. But d = a− b and d = b + a are impossible, and
12


## Page 13

d = a + b implies d = c. The lemma is proved. ✷
Theorem 8 a) For an arbitrary A∈A n the following three statements are
equivalent:
(1) rank A = 1;
(2) SNF(A) = (1 , 0n− 1);
(3) A contains a column a̸= 0, such that all nonzero columns of A are equal
to a.
The number of matrices in An,1 equals
|An,1|= (2 n− 1)2.
b) For an arbitrary A∈A n the following three statements are equivalent:
(1) rank A = 2;
(2) SNF(A) = (1 , 1, 0n− 2);
(3)• A contains the two nonzero columns a̸= b, such that all columns of A
are in{0, a, b}, or
• A contains the two nonzero columns a̸= b, such that the set of nonzero
rows of [a b ] equals{[0 1] , [1 0]}, and that the set of nonzero columns
of A is{a, b, a + b}.
The number of matrices in An,2 equals
|An,2|= (3 n− 2·2n + 1)(2·4n− 3·3n + 1)/ 2.
PROOF. a) If rank A = 1 then A contains nonzero column a, such that all
nonzero columns of A are equal to a. By subtracting one of nonzero columns
from the others, we obtain an equivalent matrix with exactly one non zero
column a. By the column permutation column a is moved to the ﬁrst position,
and by the row permutation some 1 is moved to the upper left corner . By
subtracting the ﬁrst row from the other nonzero rows, we obtain that SNF of
A is (1 , 0n− 1). How many matrices of rank 1 there are? The number of choices
for nonzero column a is 2 n− 1, and the number of matrices corresponding to
the ﬁxed a is 2 n− 1: each its column is 0 or a, but at least one of them has to
be equal to a. Hence,|An,1|= (2 n− 1)2.
b) If rank A = 2 then A contains two linearly independent columns, such
that the other columns are their linear combinations. The number of diﬀerent
nonzero columns in A is either two or it is greater than two.
Case 1. Suppose there are exactly two diﬀerent nonzero columns a, b in A.
13


## Page 14

The number of such matrices A is
(
2n− 1
2
)
(3n− 2·2n + 1).
Indeed, the number of choices for a, b equals to the above binomial coeﬃ-
cient. Without loss of generality we suppose that a < b . For ﬁxed a, b, by
the inclusion-exclusion principle the number of matrices A is 3 n− 2·2n + 1,
because
• 3n is the number of matrices with the columns from the set {0, a, b},
• 2n is the number of matrices without a, and also the number of matrices
without b,
• 1 is the number of matrices without a and b.
Case 2. If there are more than two diﬀerent nonzero columns in A, then by
Lemma 7 there are two diﬀerent nonzero columns a, b (a < b ) in A, such
that the set of nonzero columns in A is{a, b, c = a + b}, and such that the
row set of the matrix [ a b] is{[0 1], [1 0]}. There are (3 n− 2·2n +1)/ 2 choices
for columns a, b satisfying these conditions. Indeed, consider all matrices
[a b ], [ b a ]:
• 3n is the number of matrices with the row set {[0 0] , [0 1] , [1 0]},
• 2n is the number of matrices without the row [0 1], and also the number
of matrices without the row [1 0],
• 1 is the number of matrices without the rows [0 1], [1 0]).
The number of matrices [ a b ] is therefore (3 n− 2·2n + 1)/ 2. The number
4n− 3·3n + 3·2n− 1 of matrices with the set of nonzero columns {a, b, c}
(where c = a + b) is also obtained by the inclusion-exclusion principle:
• 4n is the number of matrices with all the columns 0, a, b, c;
• 3n is the number of matrices without the column a (and analogously with-
out b, c);
• 2n is the number of matrices without columns a, b (and analogously with-
out a, c; and without b, c);
• 1 is the number of matrices without columns a, b, c.
Therefore, the number of matrices of the rank 2, with more than t wo diﬀer-
ent nonzero columns equals
(3n− 2·2n + 1)(4n− 3·3n + 3·2n− 1)/ 2.
The total number of matrices in An,2 equals
(
2
(
2n− 1
2
)
+ (4n− 3·3n + 3·2n− 1)
)
(3n− 2·2n + 1)/ 2 =
= (3n− 2·2n + 1)(2·4n− 3·3n + 1)/ 2.
In either case, in order to obtain SNF( A), the other nonzero columns are ﬁrst
transformed to 0 by subtracting a, b or a + b from them. Next, in [ a b] there is
a row [0 1], because a < b ; using that 1, the other elements of b are changed to
14


## Page 15

0. Finally, choosing some 1 in a, and subtracting if necessary that row from the
others, after permuting rows/columns, we obtain the SNF. Hence , rank A = 2
implies SNF( A) = (1 , 1, 0n− 2). ✷
2.4 Iterative classiﬁcation of (0, 1) matrices
According to Lemma 2 we have
Aπ
n+1 =∪ A∈A π
n bordπ(A).
By changing the order of calculations, it is possible to simplify repeate d de-
termination of π-representatives of matrices from bord( A) by Algorithm 1.
Matrices B in bord( A) are of the form (2). For each y the π-representatives
of B’s corresponding to various inserted rows [ x b] are found spending smaller
number of steps. The point is that the rows of the π-representative preceding
the row [ x b ] are already determined for some previous variants for that row.
Somewhat more detailed description follows. Determine ﬁrst the π-represen-
tative of the matrix, corresponding to x = 0, b = 0; the inserted zero row [ x b]
is certainly the ﬁrst row in the π-representative. The corresponding row and
column permutations P , Q are recorded. The remaining pairs ( x, b ) are then
considered in turn, lexicographically ordered. The question arises, to which
position l might [ x b ] be moved during the π-representative determination,
skipping the determination of ﬁrst l− 1 rows of the representative. The obvi-
ous lower bound for l is the smallest among all positions where the previous
rows w, obtained from [ x b] by changing exactly one 1 into 0, have been moved
(except if there was an alternative to w during that step, i.e. if L(i) had more
than one member at the moment when w arrived to its destination).
Instead of extending all A∈A π
n, it is enough to extend the matrices from the
setAφ
n of all φ-representatives in An. By extending all A∈A φ
n a subset of
Aπ
n+1 is obtained; the set of φ-representatives of matrices from that subset is
exactlyAφ
n+1.
It is convenient to use a balanced tree to collect π-representatives in an or-
dered fashion. We chose A VL tree [6] — the binary search tree satis fying the
condition that, for every node, the diﬀerence between the height s of its left
and right subtrees is at most 1. For n = 8, in order to save memory, a com-
bination of A VL tree and the sorted array of matrices is used: from time to
time the content of the tree is merged into the array. After collect ing all π-
representatives, the π-representatives set is reduced to the corresponding φ-
representatives set. To determine the set of φ-representatives, corresponding
to a given set of π-representatives, the following simple algorithm is used.
15


## Page 16

Algorithm 2 Reduction of a given set Lπ of π-representatives to the set Lφ
of corresponding φ-representatives.
{ T — auxiliary A VL tree used to collect π-representatives.}
while Lπ̸=∅
while there is a space in T for at least (n + 1)2 matrices
remove the ﬁrst matrix A from Lπ;
generate the set TA of π-representatives contained in the φ-class of A;
insert TA into T ;
insert Aφ into Lφ;
remove from Lπ all the matrices contained in T ;
T←∅ ;
The classiﬁcation of A8 lasted about a month in parallel on ﬁve PC’s. A huge
number of collected π-representatives of order n = 8 caused serious diﬃculties.
The space requirement is reduced by dividing π-representatives into subsets,
according to their SNF. For each extended matrix, its SNF is determ ined, and
the π-representatives are classiﬁed into subsets with the same SNF. Th ese sub-
sets are then independently processed. The hardest was the SNF -class (1 7, 0),
with 5204144555 π-representatives contained in a number of non disjoint sub-
sets. These subsets were independently processed by Algorithm 2 , producing
the non disjoint sets of φ-representatives; their union consists of 71348129 φ-
representatives, approximately 1 / 3 of matrices in Aφ
8.
In order to save the space, Lπ and Lφ are stored in a sorted, compressed form:
one byte for each matrix row; the group of consecutive matrices w ith the same
ﬁrst n− 2 rows is stored so that the common n− 2 rows are stored only once.
As a result, the average space for a matrix of order 8 was little more than two
bytes.
If somebody tries to extend φ-representatives of order 8, he could expect to
process about 300 times more φ-representatives, each giving approximately 4
times more π-representatives. Therefore, the classiﬁcation of matrices of o rder
9 is expected to last 1000 times longer, requiring huge memory.
2.5 Results of classiﬁcation
We start with the simplest nontrivial case.
Example 9 The 16 matrices of order 2 are divided into 3 φ-classes, which
are further subdivided into 7 π-classes:
16


## Page 17

{{[
0 0
0 0
]}}
,
{{[
0 0
0 1
]
,
[
0 0
1 0
]
,
[
0 1
0 0
]
,
[
1 0
0 0
]}
,
{[
0 0
1 1
]
,
[
1 1
0 0
]}
,
{[
0 1
0 1
]
,
[
1 0
1 0
]}
,
{[
1 1
1 1
]}}
,
{{[
0 1
1 0
]
,
[
1 0
0 1
]}
,
{[
0 1
1 1
]
,
[
1 0
1 1
] [
1 1
0 1
]
,
[
1 1
1 0
]}}
.
In Table A.1 all the 36 π-representatives of order 3 are shown. The 5 SNF-
classes are in separate blocks, divided into compartments with φ-classes. The
ﬁrst matrix in each φ-class is the smallest π-representative, i.e. the φ-rep-
resentative. For each π-and SNF-class, their size is given. The matrices are
represented by hexadecimal vectors, each component represe nting a row of a
matrix. For example, the last vector (3 , 5, 6) in Table A.1 represents the matrix





0 1 1
1 0 1
1 1 0




 .
The matrix (1 , 2, 5) is a π-representative of the matrix from Example 5.
In Table A.2 all the 39 φ-representatives of order 4 are shown, together with
the sizes of their φ-classes.
In Table 2 ρn,|Aφ
n|, sn, an,|Dn|, and the set Dn are given for 1 ≤ n≤ 8,
where sn =|Sn| and ρn = (2 n2
/ (n + 1)!2)/|Aφ
n|. In the last row of Table 2 s9,
|D9|, a9,D9 are given; the explanation how they are obtained will be given in
section 3.
Denote by F (n) the following statement:
A∈A n, satisfying SNF( A) = d = (d1, d 2, . . . , d n) exists if and only if(6)
there exists A′∈A n+1, satisfying SNF( A′) = d′ = (d1, d 2, . . . , d n, 0).
Obviously, the ﬁrst condition implies the second one. The implication in t he
opposite direction is not obvious at all; it would follow from the following
stronger statement:
H(n) : Let A′∈A n+1, rank A′ = n, and SNF( A′) = d′ = (d1, d 2, . . . , d n, 0).
Then A′ has at least one minor A∈A n with SNF( A) = d = (d1, d 2, . . . , d n).
17


## Page 18

Table 2
The numbers of equivalence classes in An.
n ρn |Aφ
n|
sn an|Dn| Dn
1 0. 250 2 2 2 2{0, 1}
2 0. 148 3 3 2 2{0, 1}
3 0. 074 12 5 3 3{0− 2}
4 0. 117 39 8 4 4{0− 3}
5 0. 167 388 14 6 6{0− 5}
6 0. 334 8102 26 10 10{0− 9}
7 0. 528 656103 56 19 22{0− 18, 20, 24, 32}
8 0. 701 199727714 129 41 46{0− 40, 42, 44, 45, 48, 56}
9 333 103 114{0− 102, 104, 105, 108, 110,
112, 116, 117, 120, 125, 128, 144}
But the following matrix F∈A 10 is a counterexample to H(10):
F =



A B
C D


 =
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

0 0 1 1
1 0 1 0 0 1
0 1 1 0 0 1 0 1 0 1
1 1 0 0 0 1 1 0 1 0
1 0 0 1 1 0 0 1 1 0
0 0 1 1 0 0 0 1 1 1
1 1 0 0 0 0 1 1 1 0
1 0 1 0 0 1 1 1 0 0
0 1 0 1 1 1 1 0 0 0
0 1 1 0 1 1 0 0 0 1
1 0 0 1 1 0 0 0 1 1
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

.
The matrix F consists of blocks A, B, C, D , having 2 , 3, 2, 3 ones in each row
respectively, and also having 2 , 2, 3, 3 ones in each column, respectively; F is
singular, because the sums of rows of [ A B ] and [ C D ] are equal. It can be
veriﬁed that rank F = 9, SNF( F ) = (1 9, 0), but all minors of F have SNF
diﬀerent from (1 9).
In Table A.3 the SNF-representatives of matrices in An, n≤ 8, are listed, ac-
companied with the size measures of corresponding SNF-classes (t he number of
18


## Page 19

Table 3
The number of matrices of the rank k inAn, n≤ 8.
n 1 2 3 4 5 6 7 8
k
0 1 1 1 1 1 1 1 1
1 1 9 49 225 961 3969 16129 65025
2 6 288 6750 118800 1807806 25316928 336954750
3 174 36000 3159750 190071000 9271660734 397046059200
4 22560 17760600 5295204600 1001080231200 144998212423680
5 12514320 34395777360 32307576315840 17952208799918400
6 28836612000 259286329895040 720988662376725120
7 270345669985440 7547198043595392000
8 10160459763342013440
matrices, the number of π-representatives and the number of φ-representatives
in each SNF-class). The sizes of π-classes are determined using Algorithm 1.
The classes are ordered lexicographically by the SNF (with zeros mov ed to
the end of SNF).
One can verify this classiﬁcation starting from the sorted list of all φ-repre-
sentatives. For each of them one has to check if it is indeed a φ-representative.
The next step is to sum the numbers of π-representatives in all φ-classes, and
to compare the sum with the corresponding entry in Table 1. One cou ld also
check that the sum of sizes of SNF-classes in An equals 2 n2
for each n≤ 8, see
Table A.3. The sorted lists of φ-representatives for n≤ 8 can be downloaded
from http://www.matf.bg.ac.yu/∼ ezivkovm/01matrices.htm.
We now review some interesting facts, which are seen from Table A.3.
Let T (n, k ) = |An,k|. In Table 3 the numbers T (n, k ), 0 ≤ k ≤ n ≤ 8,
are shown (of course, they are easily obtained from Table A.3). The part of
Table 3 corresponding to n≤ 7 is the same as in [10]; it is also an entry
in [4, Sequence A064230]. Another interesting entry in [4, Sequence A055165]
is the sequence mn, where mn is the number of regular (0 , 1) matrices of order
n — the diagonal of Table 3. The seemingly new member of that sequenc e
is m8 = 10160459763342013440. If we suppose that all matrices in An are
equiprobable, then the rank probability distribution is shown in Table 4 for
n≤ 8. Looking at Table 4, one could erroneously conclude that large fra ction
of matrices in An is singular. In fact, the fraction of singular matrices in An
tends to 0 for n large [11].
19


## Page 20

Table 4
The probability that a random matrix in An has the rank k, 0≤ k≤ n≤ 8.
n 1 2 3 4 5 6 7 8
k
0 0.5 0.0625 0.00195 0.00002 0.00000 0.00000 0.00000 0.00000
1 0.5 0.5625 0.09570 0.00343 0.00003 0.00000 0.00000 0.00000
2 0.3750 0.56250 0.10300 0.00354 0.00003 0.00000 0.00000
3 0.33984 0.54932 0.09417 0.00277 0.00002 0.00000
4 0.34424 0.52931 0.07706 0.00178 0.00001
5 0.37296 0.50052 0.05739 0.00097
6 0.41963 0.46059 0.03908
7 0.48023 0.40913
8 0.55080
Table 5
The possible numbers of π -orbits inside φ-orbits ofAn.
n The set of φ-orbit sizes
1 {1}
2 {1, 2, 4}
3 {1, 2, 4, 5, 9}
4 {1− 5, 7, 9− 11, 13, 16, 17}
5 {1− 18, 20, 21, 25, 26, 30, 36}
6 {1, 2, 4− 27, 29− 32, 35− 37, 42, 49}
7 {1− 38, 40, 42− 44, 48− 50, 56, 64}
8 {1− 46, 48− 51, 53, 54, 56− 58, 63− 65, 72, 81}
It turns out that F (n) (6) is true for n≤ 7, i.e. the set of SNF’s of rank k
is the same for all n, k≤ n≤ 8. For example, the SNF-representative of the
SNF-class (1 , 1, 2, 0n− 3) is the matrix (0 n− 3, 3, 5, 6) for 3 ≤ n≤ 8.
The smallest n for which there are two matrices in An with the same deter-
minant, but with diﬀerent SNF’s is 5: SNF(3,C,15,16,19) = (1 , 1, 1, 4) and
SNF(3,5,9,11,1E) = (1 , 1, 2, 2).
In Table 5 the possible numbers of π-orbits inside φ-orbits are shown for
1≤ n≤ 8. These numbers are between 1 and ( n + 1)2; as it is seen, the value
(n + 1)2 is attained only if n≥ 5.
20


## Page 21

Table 6
The maximal ADV’s of matrices from An+1, obtained by extending matrices equiv-
alent to In.
n|det A| A
3 3 3 5 9 E
4 5 3 5 E 16 19
5 9 3 D 15 1 A 26 39
6 18 7 19 2 A 34 4 C 53 65
7 40 7 19 2 A 56 65 9 C B 3 CB
8 105 7 39 5 A AC D 5 E3 136 14 D 19B
If A∈A n, A∼ In and B∈ bord(A), then SNF( B) contains at least n ones,
see (5). The question arises, what are the possible values of the las t element
of SNF( B), i.e. which values can take |det B|? The largest possible values of
|det B| under these assumptions, along with the examples of matrices B for
which these values are attained, are given in Table 6. In fact, the ma trices
from Table 6 maximize |det B/ det A| for all regular A∈A , n≤ 8.
More generally, it is interesting to describe the relationship of SNF( A) to
SNF(A′) if A′∈ bord(A). During iterative classiﬁcation, the sets
{SNF(B)|B∈ bord(A), A ∈A n, SNF(A) = s}
are recorded for all SNF-classes s∈S n. The results are represented by the
incidence matrix Mn of dimensions|Sn|×|S n+1|, with entries
ms,s′ =





1, if there exist A∈A n and B∈ bord(A), with SNF’s s and s′
0, otherwise
.
(7)
Let G(n), denote the following statement:
G(n) : There exist matrices A∈A n, A′∈ bord(A), such that (8)
SNF(A) = ( d1, d 2, . . . , d n), SNF( A′) = ( d′
1, d ′
2, . . . , d ′
n, d ′
n+1) if and only if
there exist matrices B∈A n+1, B′∈ bord(B), such that
SNF(B) = ( d1, d 2, . . . , d n, 0), SNF( B′) = ( d′
1, d ′
2, . . . , d ′
n, d ′
n+1, 0).
By exhaustive search it is veriﬁed that G(n) is true for n≤ 6, enabling to put
all the transposed incidence matrices Mn, n≤ 7 together into single Table A.4.
The 1’s are represented by • ; the 0’s are represented by ⋆ if they are the
21


## Page 22

consequence of the following Lemma (describing constraints for SN F(A′) if
A′∈ bord(A)); otherwise, they are represented by ◦ .
Lemma 10 For an arbitrary A∈A n, let A′∈ bord(A), and let SNF(A) =
(d1, d 2, . . . , d n), SNF(A′) = ( d′
1, d ′
2, . . . , d ′
n, d ′
n+1). Then
(1) rank A≤ rank A′≤ rank A + 2;
(2) d′
1d′
2 . . . d ′
i divides d1d2 . . . d i for all i, 1≤ i≤ rank A;
(3)
∏n− 1
i=1 di divides det A′.
PROOF.
(1) The ﬁrst inequality follows from the fact that the rank of a subm atrix
is a lower bound on the rank of a matrix. The second inequality follows
from the observation that A′ is an at most rank 2 perturbation of A.
(2) This is a direct consequence of the fact that d′
1d′
2 . . . d ′
i is the largest
common divisor of all minors of A′ of order i, see for example [7].
(3) Let P , Q be the matrices such that SNF( A) = P AQ = D = (d1, d 2, . . . , d n),
|det P|=|det Q|= 1. Let
A′ =



A y
x b


 .
The case det A′ = 0 is trivial; suppose det A′̸= 0. If xQ = [a1 a2 . . . a n],
P y = [c1 c2 . . . c n]T , then from the identity



P 0
0 1






A y
x b






Q 0
0 1


 =



D P y
xQ b



it follows (another way to express determinants of matrices obtain ed by
extension, see (3))
det A′ = b
n∏
i=1
di−
n∑
i=1
aici
∏
1≤ j≤ n,
j̸=i
dj. (9)
Since rank A′ = n + 1, then we have rank A≥ n− 1. If rank A = n− 1,
then dn = 0, implying
det A′ =− ancn
n− 1∏
i=1
di;
otherwise
det A′ =
(
bdn−
n∑
i=1
aicidn/d i
) n− 1∏
i=1
di.
22


## Page 23

In both cases ∏n− 1
i=1 di divides det A. ✷
Suppose A∈A n, A′∈ bord(A). From Table A.4, we see the following inter-
esting facts:
• The ﬁrst◦ in some Mn corresponds to s = (1, 0), s′ = (1, 1, 2). It is equiva-
lent to following statement: if A∈A 2,1 then|det A′|< 2.
• if A∈A 3,2, then|det A′|< 3.
• if A∈A 4, SNF( A) = (1 , 1, 1, 0), then|det A′|< 5.
• if A∈A 4, SNF( A) = (1 , 1, 2, 0), then|det A′|< 4.
• if A∈A 5, SNF( A) = (1 , 1, 1, 1, 0), then|det A′|̸= 7.
• if A∈A 5, SNF( A) = (1 , 1, 1, 2, 0), then|det A′|̸= 6.
• if A∈A 5, SNF( A) = (1 , 1, 1, 3, 0), then|det A′| /∈{ 6, 9}.
• if A∈A 5, SNF( A) = (1 , 1, 1, 2, 2), then SNF( A′)̸= (1, 1, 1, 1, 4, 0).
• if SNF( A) = (1 n− 1, d n) and SNF( A′) = (1 n− 1, d ′
n, 0) then d′
n divides dn for
all n≤ 7.
• if SNF( A) = s = (1 n− 1, d n)∈S n and SNF( A′) = s′ = (1 n, d ′
n+1)∈S n+1
then
· if n≤ 6, then ms,s′ = 1.
· if n = 7, then ms,s′ = 1 if and only if
(dn, d ′
n+1) /∈{ (17, 34), (7, 39), (13, 39), (1, 42),
(4, 42), (6, 42), (7, 42), (13, 42), (14, 42)} .
· if n = 8, then there are more exceptions to ms,s′ = 1, but there is one
exotic group of them: if dn = 19 then d′
n+1 must be divisible by 19; 19 is
the only integer satisfying such a condition.
3 Determinant and SNF sets of (0, 1) matrices of order 9
Determination of{|det(A′)|| A′∈ bord(A)} is a simple operation, see the ex-
planation following (3). It was eﬀectively performed for all 1997277 14 matrices
inAφ
8 ; merging these sets D9 is obtained, see Table 2.
The similar idea — determine ADV’s, and only if necessary, determine SN F’s
of the results of extension — is used to obtain S9. Suppose we know in advance
the number fd of diﬀerent SNF’s in D9 corresponding to a given ADV d > 0.
During the extension of matrices from An, the SNF’s of extended matrices
with the ADV d are determined only if the number of SNF’s with ADV d
is still less than fd. If we know only upper bound on fd, then the heuristic
does not work — we have to determine SNF’s of all matrices with the AD V
d. Therefore, it is useful to determine fd for at least some d > 0.
23


## Page 24

Table 7
The number of partitions of r into at most n positive integers.
r 0 1 2 3 4 5 6 7
n
0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1
2 1 1 2 2 3 3 4 4
3 1 1 2 3 4 5 7 8
4 1 1 2 3 5 6 9 11
5 1 1 2 3 5 7 10 13
6 1 1 2 3 5 7 11 14
7 1 1 2 3 5 7 11 15
Denote by pn(r) the number of partitions of r into at most n positive integers.
In order to determine the upper bound for fd, suppose ﬁrst that d is a prime
power, d = pr. If A∈A n and|det A|= d, then SNF( A) is of the form
(px1, p x2, . . . , p xn), 0≤ x1≤ x2≤···≤ xn,
n∑
i=1
xi = r.
The number of diﬀerent exponent vectors ( x1, x 2, . . . , x n) is equal to pn(r).
The values pn(m) are computed using the recurrence (see for example [12])
pn(0) = 1 , n ≥ 0, p0(r) = 0 for r≥ 1, and pn(r) = pn− 1(r) + pn(r− n), see
Table 7.
Example 11 If d = 8 = 2 3 and n = 6 we have p6(3) = 3 ; SNF(A) is one of
(15, 8), (14, 2, 4) and (13, 2, 2, 2). We see from Table A.3 that all these SNF do
exist, i.e. for each of them there exists some (0, 1) matrix. Another example
d = 3 2, n = 6 , shows that p6(2) = 2 is only an upper bound: the SNF-class
(14, 3, 3) is empty.
More generally, if d =
∏m
i=1 pαi
i , where pi are diﬀerent primes, then the upper
bound on the number of diﬀerent SNF’s with the ADV d is ∏m
i=1 pn(α i).
Example 12 If n = 8 and d = 36, then there are p8(2)p8(2) = 4 such SNF’s:
(16, 2, 18), (17, 36), (16, 3, 12), (16, 6, 6); all these SNF’s are found in Table A.3.
In order to obtain a tighter upper bound for the number of diﬀeren t SNF’s,
we have to include somewhat more information. If we further suppo se that
A′∈ bord(A) and SNF( A) = s = (d1, d 2, . . . , d n), then by Lemma 10 for some
s′ = (d′
1, d ′
2, . . . , d ′
n+1) the equality SNF( A′) = s is impossible. For example, if
24


## Page 25

s contains k ones, then s′ contains at least k ones and if rank A≥ k + 1 then
d′
k+1 divides dk+1.
Using these facts, the regular part of S9 was determined, see Table A.5. The
φ-representatives from the chosen SNF-class of A8 were extended computing
determinants, and, if necessary, determining SNF’s. The upper bo unds for the
number of diﬀerent SNF’s, obtained by Lemma 10, are rough for larg er ADV
values, but the consequences are not dangerous, because of th e small number
of extended matrices with the large ADV: it is not hard to compute th e SNF’s
of all of them.
To complete S9, it is necessary to determine the singular part of S9. If we
would know that F (8) is true, then the set of singular SNF’s of order 8 would
be equal to S8 (with each SNF extended by one zero, of course). Not knowing
a simple proof of F (8), we proceed with a shortened exhaustive proof.
The idea is to narrow the set of SNF-classes in S8, the extension of which
can lead to a new singular SNF of order 9. If SNF( A) = ( d1, d 2, . . . , d 8, 0)
for some A ∈ A9, then (because we know the set of SNF’s of lower or-
ders) by Lemma 10 we can narrow the set SNF-classes, containing A. We
obtain that the only new possible SNF’s are the following SNF’s of the ra nk 8:
(17, m, 0), m = 44 , 45, 48, 56 and (1 6, 2, 28, 0); and the following SNF’s of the
rank 7: (1 6, 20, 0, 0), (16, 24, 0, 0), (16, 32, 0, 0), (15, 2, 12, 0, 0), (15, 2, 16, 0, 0),
(15, 4, 8, 0, 0), (14, 2, 2, 8, 0, 0), (14, 2, 4, 4, 0, 0).
The extension of which matrices gives the matrices with such SNF’s? F or ex-
ample, we know that the SNF (1 7, 44, 0) can be obtained only by the extension
of a matrix in which 44 divides all minors of order 8; therefore 44 also d ivides
a nonsingular minor of order 8; hence the SNF of that minor could be o nly
(16, 2, 22). Considering analogously the rest of listed SNF’s of order 8, we o b-
tain that matrices from A9,8, with the SNF equal to some from the list above,
can be obtained only by the extension of matrices from A8 with the SNF
(16, 2, 22), (16, 2, 24), (16, 3, 15), (15, 2, 2, 12), or (1 5, 2, 2, 14).
Analogously, we obtain that matrices from A9,7 with one of the listed SNF’s,
can be obtained only by double extension of matrices from A7 with the SNF
(15, 2, 10), (14, 2, 2, 6), or (1 3, 2, 2, 2, 4). After the complete search through all
matrices that can be obtained by the extensions listed, it is found th at there
are no new singular SNF’s of order 9 i.e. that F (8) is also true. That completes
the determination of S9.
In Table A.6 the part of the incidence matrix M8 is shown, corresponding to
regular matrices inS9. The table was obtained by extending φ-representatives
fromA8,7 andA8,8; the singular extended matrices were ignored.
25


## Page 26

4 The lower bounds for the ﬁrst missing determinant, an
Denote by fn the nth Fibonacci number ( f1 = f2 = 1 and fn = fn− 1 + fn− 2
for n≥ 3). Paseman [13] shows that an≥ 2fn− 1. We give the sketch of his
proof, and then we give the sharper lower bounds for an, n≤ 19.
Consider the so called Fibonacci matrices Fn ∈A n with the ( i, j ) element
equal to 1 if and only if j− i =− 1, 0, 2, 4, . . . ; det Fn = fn. The cofactors
corresponding to the ﬁrst row of Fn are fn− 1, fn− 2,− fn− 3,− fn− 4 . . . , − f1.
Consider the matrix U∈ bord(Fn),
U =



Fn y
x b


 ,
where x = [x1 x2 . . . x n− 1], y = [y1 y2 . . . y n− 1]T . Let y1 = 1, y2 = y3 =···=
yn = 0 and x1 = x2 = 0. Then from (3) we have
det U =
n− 2∑
i=1
xn+1− ifi + bfn.
Therefore, each integer from [0 , 2fn− 1] is determinant of some U∈ bord(Fn),
and an≥ 2fn− 1.
In order to prove that an≥ m, one can give a list of matrices from An− 1, such
that determinants of their extensions cover [1 , m− 1]. The proof veriﬁcation
then includes the procedure of ﬁnding determinants of all extensio ns of a given
matrix. Still, such a list is essentially more compact than the list of matr ices
fromAn, with determinants covering [1 , m− 1].
Denote by aA the minimal integer not in ∪{| det B| |B ∈ bord(A)}, the
”extension spectrum” of A∈A n. In this context, the matrices A with high
aA are of special interest. If aA > 1 and SNF( A) = ( d1, d 2, . . . , d n), then
d1 = d2 =···= dn− 1 = 1, because determinants of all extensions of A are
divisible by dn− 1, see (9).
In order to ﬁnd lower bounds for some an, one can start from a well chosen
setBn− 1⊂A n− 1, and then to ﬁnd ADV’s of all extended matrices. If m is the
smallest number not equal to some of these ADV’s, then an≥ m. Afterwards,
some subset of extended matrices with diﬀerent SNF’s is taken to be the set
Bn, and the next iteration can be started.
The starting setB9 was constructed in the following way. From each SNF-class
inA8 a number of matrices is taken, with diﬀerent numbers of π represen-
tatives in their φ-classes. Extending these matrices, a set of matrices with
26


## Page 27

diﬀerent SNF’s is obtained, but without any matrix with the SNF (1 8, 97).
By adding one such matrix, the set B9 is completed. The sets B10,B11 and
B12 are generated iteratively, as explained above. At the end, the ADV ’s of
all matrices obtained by extending the matrices in B12 are determined. The
resulting lower bounds are a10≥ 259, a11≥ 739, a12≥ 2107, a13≥ 6157.
For n > 13 we used an alternative heuristic, described by Algorithm 3.
Algorithm 3 Heuristic to ﬁnd lower bound for an+1.
Input :Ln⊂A n, list of matrices to be extended.
Output : lower bound for an+1, and list Ln+1⊂A n+1
of ”promising” matrices for the following iteration.
{ Initialization:}
f irst0← 1;{ the ﬁrst integer not ”covered” by ADV’s }
dmax← 1;{ the largest ADV found until now }
Ln+1←∅ ;{ output list }
for all A∈L n do
{ Consider the extensions A′ =



A y
x b


}
Compute det A and B = [Bij] = adj A;{ transposed cofactor matrix of A}
for all y∈{ 0, 1}n do
{ the next linear combination of rows of B}
determine the coeﬃcients of the linear combination
− b det A + ∑n
i=1 xi
(∑n
j=1 yjBij
)
and the sums s+, s− of its positive and negative members;
if max{− s− , s +}≥ f irst0 then{”poor” linear combinations are skipped}
for all (x, b )∈{ 0, 1}n+1 do
compute det A′;{ by one addition only, using Gray code }
if|det A′|= f irst0 then
update f irst0;
if|det A′|> dmax then
dmax←| det A′|;
if|det A′|> 0. 9 dmax then
append A′ toLn+1;
Elimination of ”poor” linear combinations is a powerful heuristics if the ma-
trices with the high extension spectra are placed in the beginning of Ln. The
major part of linear combinations is skipped after only a few ﬁrst mat rices in
Ln, reducing the extension complexity roughly to O(n2n) (instead of O(4n)).
In Table A.7 for 10 ≤ n≤ 19 we give
• lower bound for an,
27


## Page 28

• |Ln− 1|, the number of extended matrices,
• a matrix An− 1 with the highest extension spectrum found in |An− 1|,
• extension spectrum and determinant of An− 1.
Complete lists of matrices, whose extension determinants prove th ese lower
bounds, can be fount at http://www.matf.bg.ac.yu/∼ ezivkovm/01matrices.htm.
5 Counting (0, 1) matrices with the maximum determinant
Using the classiﬁcation of An, it is not hard to compute the number cn [4,
Sequences A051752] of matrices in An with the maximal determinant dn (i.e.
1/ 2 of the number of matrices with the ADV dn) for n≤ 9.
The ﬁrst 8 members of the sequence cn are found in Table A.3; the number
c8 = 195955200 is new.
In order to determine c9, from Table A.4 we see that the matrix from A9 with
the ADV 144 could be obtained only by extending matrices from A8 with the
SNF (1 5, 2, 2, 6) or (1 5, 2, 2, 12). After the extension of these two SNF-classes,
it turned out that there is a unique φ-class with the ADV 144 — the class with
the representative (F,33,C3,FC,155,15A,166,196,1A9). Half of the nu mber of
matrices in that φ-class is c9 = 13716864000. It is interesting that for all n≤ 9
there is a unique φ-class with the maximal ADV.
6 Acknowledgement
I am greatly indebted to the anonymous referee whose comments h elped to
improve the exposition.
References
[1] J. Williamson, Determinants whose elements are 0 and 1, Amer. Math. Monthly
53:427–434 (1946).
[2] M. G. Neubauer, A. J. Radcliﬀe, The maximum determinant ± 1 matrices,
Linear Algebra Appl. 257:289–306 (1997).
[3] R. Craigen, The range of the determinant function on the s et of n× n (0, 1)-
matrices, J. Combin. Math. Combin. Comput. 8:161–171 (1990).
28


## Page 29

[4] N. J. A. Sloane, An On-Line Version of the Encyclopedia of Integer Sequences ,
http://www.research.att.com/∼ njas/sequences/eisonline.html
[5] M. ˇZivkovi´ c, Massive Computation as a Problem Solving Tool, Proceedings of
the 10th Congress of Yugoslav Matematicians 113–128 (Belgrade, 2001).
[6] G. M. Adel’son-Vel’skii, Y. M. Landis, An algorithm for t he organization of
information, Soviet Math. Dokl. 3:1259–1262 (1962).
[7] F. R. Gantmacher: Teoriya matric, Nauka (Moskva, 1988).
[8] F. Harary, E. M. Palmer: Graphical Enumeration, Academic Press (New York,
1973).
[9] Y. Kida, UBASIC, version 8.74 (1994).
[10] G. M. Ziegler: Lectures on 0/ 1 polytopes, Graduate Texts in Mathematics 152,
Springer (Berlin 1995, Revised ed. 1998).
[11] J. Koml´ os, On the determinant of (0, 1) matrices, Studia Sci. Math. Hungarica
2:7–21 (1967).
[12] V. K. Balakrishnan: Combinatorics, McGraw–Hill (New York, 1995).
[13] G. R. Paseman, A Diﬀerent Approach To Hadamard’s Maximum Determinant
Problem, ICM 1998 Berlin , http://grpmath.prado.com/detspec.html
A Large tables
29


## Page 30

Table A.1
π -representatives of (0 , 1) matrices of order 3.
SNF size
0 0 0 1
0 0 0 1
SNF size
1 0 0 49
0 0 1 9
0 0 7 3
1 1 1 3
7 7 7 1
0 0 3 9
3 3 3 3
0 1 1 9
0 7 7 3
0 3 3 9
SNF size
1 1 0 288
0 1 2 18
0 1 7 18
1 1 3 18
1 1 6 9
3 7 7 9
0 1 3 36
0 1 6 18
0 3 7 18
1 1 2 18
1 3 3 18
1 1 7 9
3 3 7 9
1 6 6 9
1 7 7 9
0 3 5 18
3 3 5 18
1 2 3 18
1 6 7 18
SNF size
1 1 1 168
1 2 4 6
1 2 7 18
1 3 5 18
1 3 6 36
3 5 7 18
1 2 5 36
1 3 7 36
SNF size
1 1 2 6
3 5 6 6
30


## Page 31

Table A.2
φ-representatives of (0 , 1) matrices of order 4.
SNF size
0 0 0 0 1
0 0 0 0 1
SNF size
1 0 0 0 225
0 0 0 1 25
0 0 0 3 50
0 0 1 1 50
0 0 3 3 100
SNF size
1 1 0 0 6750
0 0 1 2 200
0 0 1 3 400
0 0 1 6 600
0 0 3 5 600
0 0 3 7 300
0 1 1 2 600
0 1 1 6 450
0 1 2 3 600
0 1 3 3 300
0 1 6 6 900
0 1 6 7 900
0 3 3 5 900
SNF size
1 1 1 0 35400
0 1 2 4 600
0 1 2 5 3600
0 1 2 7 1800
0 1 3 5 1800
0 1 3 6 3600
0 1 3 7 3600
0 1 6 A 3600
0 3 5 7 1800
0 3 5 9 1200
0 3 5 A 3600
1 2 3 4 3600
1 2 4 7 1200
1 2 5 6 3600
1 6 7 A 1800
SNF size
1 1 2 0 600
3 5 6 0 600
SNF size
1 1 1 1 20040
1 2 4 8 600
1 2 4 9 7200
1 2 5 A 1440
1 2 5 B 7200
1 2 7 B 3600
SNF size
1 1 1 2 2400
1 6 A C 2400
SNF size
1 1 1 3 120
3 5 9 E 120
31


## Page 32

Table A.3
The representatives and the sizes of SNF-classes in An, n≤ 8.
A1 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 1 1 1 0
1 1 1 1 1 1 1
Total: 2 2 2
A2 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 1 1 1 0 0
1 0 0 1 9 4 1 0 1
2 1 1 1 6 2 1 1 2
Total: 16 7 3
A3 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 1 1 1 0 0 0
1 0 0 0 1 49 9 4 0 0 1
2 0 0 1 1 288 18 4 0 1 2
3 1 1 1 1 168 7 2 1 2 4
4 2 1 1 2 6 1 1 3 5 6
Total: 512 36 12
A4 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 0 1 1 1 0 0 0 0
1 0 0 0 0 1 225 16 4 0 0 0 1
2 0 0 0 1 1 6750 84 12 0 0 1 2
3 0 0 1 1 1 35400 150 14 0 1 2 4
4 0 0 1 1 2 600 5 1 0 3 5 6
5 1 1 1 1 1 20040 49 5 1 2 4 8
6 2 1 1 1 2 2400 10 1 1 6 A C
7 3 1 1 1 3 120 2 1 3 5 9 E
Total: 65536 317 39
32


## Page 33

Table A.3
Continued
A5 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 0 0 1 1 1 0 0 0 0 0
1 0 0 0 0 0 1 961 25 9 0 0 0 0 1
2 0 0 0 0 1 1 118800 260 37 0 0 0 1 2
3 0 0 0 1 1 1 3134400 1346 113 0 0 1 2 4
4 0 0 0 1 1 2 25350 25 5 0 0 3 5 6
5 0 0 1 1 1 1 16853400 2589 141 0 1 2 4 8
6 0 0 1 1 1 2 880200 210 17 0 1 6 A C
7 0 0 1 1 1 3 27000 15 2 0 3 5 9 E
8 1 1 1 1 1 1 9702720 831 39 1 2 4 8 10
9 2 1 1 1 1 2 2427840 254 15 1 2 C 14 18
10 3 1 1 1 1 3 289440 51 5 1 6 A 12 1C
11 4 1 1 1 1 4 65520 12 2 3 5 9 11 1E
12 5 1 1 1 1 5 7200 3 1 3 5 E 16 19
13 4 1 1 1 2 2 21600 2 1 3 C 15 16 19
Total: 33554432 5624 388
A6 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0
1 0 0 0 0 0 0 1 3969 36 9 0 0 0 0 0 1
2 0 0 0 0 0 1 1 1807806 660 76 0 0 0 0 1 2
3 0 0 0 0 1 1 1 189336000 7586 472 0 0 0 1 2 4
4 0 0 0 0 1 1 2 735000 86 10 0 0 0 3 5 6
5 0 0 0 1 1 1 1 5168108400 47605 1913 0 0 1 2 4 8
6 0 0 0 1 1 1 2 124744200 2120 115 0 0 1 6 A C
7 0 0 0 1 1 1 3 2352000 91 9 0 0 3 5 9 E
8 0 0 1 1 1 1 1 30991962960 112080 3262 0 1 2 4 8 10
9 0 0 1 1 1 1 2 3122915040 14986 511 0 1 2 C 14 18
10 0 0 1 1 1 1 3 226603440 1618 75 0 1 6 A 12 1C
11 0 0 1 1 1 1 4 38419920 307 16 0 3 5 9 11 1E
12 0 0 1 1 1 1 5 3175200 46 3 0 3 5 E 16 19
13 0 0 1 1 1 2 2 12700800 78 4 0 3 C 15 16 19
14 1 1 1 1 1 1 1 18480102480 39637 952 1 2 4 8 10 20
15 2 1 1 1 1 1 2 7737327360 17642 442 1 2 4 18 28 30
16 3 1 1 1 1 1 3 1537446960 4079 128 1 2 C 14 24 38
17 4 1 1 1 1 1 4 628548480 1685 52 1 6 A 12 22 3C
18 5 1 1 1 1 1 5 127224720 429 18 1 6 A 1C 2C 32
19 6 1 1 1 1 1 6 93139200 263 9 3 5 9 16 2E 31
20 7 1 1 1 1 1 7 12877200 54 3 3 5 9 1E 2E 31
21 8 1 1 1 1 1 8 6703200 27 2 3 5 E 19 29 36
22 9 1 1 1 1 1 9 1058400 7 1 3 D 15 1A 26 39
23 4 1 1 1 1 2 2 208857600 473 17 1 6 18 2A 2C 32
24 8 1 1 1 1 2 4 3175200 12 1 3 C 15 1A 26 29
25 8 1 1 1 2 2 2 151200 2 1 7 19 1E 2A 2D 33
Total: 68719476736 251610 8102
33


## Page 34

Table A.3
Continued
A7 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 16129 49 16 0 0 0 0 0 0 1
2 0 0 0 0 0 0 1 1 25316928 1428 170 0 0 0 0 0 1 2
3 0 0 0 0 0 1 1 1 9254300328 31994 1908 0 0 0 0 1 2 4
4 0 0 0 0 0 1 1 2 17360406 246 34 0 0 0 0 3 5 6
5 0 0 0 0 1 1 1 1 989588124000 501563 17596 0 0 0 1 2 4 8
6 0 0 0 0 1 1 1 2 11359807200 13645 694 0 0 0 1 6 A C
7 0 0 0 0 1 1 1 3 132300000 400 30 0 0 0 3 5 9 E
8 0 0 0 1 1 1 1 1 30826279895040 4358421 105808 0 0 1 2 4 8 10
9 0 0 0 1 1 1 1 2 1405763634240 316904 9295 0 0 1 2 C 14 18
10 0 0 0 1 1 1 1 3 64153434240 22902 853 0 0 1 6 A 12 1C
11 0 0 0 1 1 1 1 4 8175222720 3714 168 0 0 3 5 9 11 1E
12 0 0 0 1 1 1 1 5 509443200 413 23 0 0 3 5 E 16 19
13 0 0 0 1 1 1 2 2 2694686400 1032 58 0 0 3 C 15 16 19
14 0 0 1 1 1 1 1 1 219225571810560 13834240 261882 0 1 2 4 8 10 20
15 0 0 1 1 1 1 1 2 34159997168640 2624469 53874 0 1 2 4 18 28 30
16 0 0 1 1 1 1 1 3 4018162256640 376699 8633 0 1 2 C 14 24 38
17 0 0 1 1 1 1 1 4 1176364465920 123510 3024 0 1 6 A 12 22 3C
18 0 0 1 1 1 1 1 5 182858215680 23489 633 0 1 6 A 1C 2C 32
19 0 0 1 1 1 1 1 6 110954188800 13823 361 0 3 5 9 16 2E 31
20 0 0 1 1 1 1 1 7 12940704000 2133 64 0 3 5 9 1E 2E 31
21 0 0 1 1 1 1 1 8 5966553600 1006 33 0 3 5 E 19 29 36
22 0 0 1 1 1 1 1 9 829785600 189 7 0 3 D 15 1A 26 39
23 0 0 1 1 1 1 2 2 389700057600 37489 927 0 1 6 18 2A 2C 32
24 0 0 1 1 1 1 2 4 2857680000 415 19 0 3 C 15 1A 26 29
25 0 0 1 1 1 2 2 2 127008000 29 4 0 7 19 1E 2A 2D 33
34


## Page 35

Table A.3
Continued
A7 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
26 1 1 1 1 1 1 1 1 135491563468800 5593528 91764 1 2 4 8 10 20 40
27 2 1 1 1 1 1 1 2 83220427382400 3493129 58179 1 2 4 8 30 50 60
28 3 1 1 1 1 1 1 3 23436399974400 1020752 17707 1 2 4 18 28 48 70
29 4 1 1 1 1 1 1 4 13285672243200 581948 10189 1 2 C 14 24 44 78
30 5 1 1 1 1 1 1 5 3754520017920 172714 3169 1 2 C 14 38 58 64
31 6 1 1 1 1 1 1 6 4201407745920 185688 3320 1 6 A 12 2C 5C 62
32 7 1 1 1 1 1 1 7 813250851840 39068 749 1 6 A 12 3C 5C 62
33 8 1 1 1 1 1 1 8 693389168640 32490 645 1 6 A 1C 32 52 6C
34 9 1 1 1 1 1 1 9 257766405120 12609 253 1 6 1A 2A 34 4C 72
35 10 1 1 1 1 1 1 10 215881142400 10094 199 3 5 9 1E 2E 4E 71
36 11 1 1 1 1 1 1 11 49798425600 2598 55 3 5 9 1E 31 51 6E
37 12 1 1 1 1 1 1 12 67511808000 3263 71 3 5 E 16 39 59 66
38 13 1 1 1 1 1 1 13 12283084800 686 17 3 5 E 19 36 56 69
39 14 1 1 1 1 1 1 14 12260505600 615 12 3 5 19 29 36 4E 71
40 15 1 1 1 1 1 1 15 4064256000 215 6 3 D 15 26 38 5E 61
41 16 1 1 1 1 1 1 16 2235340800 143 6 3 C 15 36 39 5A 65
42 17 1 1 1 1 1 1 17 406425600 27 2 3 D 16 2E 39 5A 65
43 18 1 1 1 1 1 1 18 541900800 24 1 7 19 2A 34 4C 53 65
44 4 1 1 1 1 1 2 2 4413330432000 184475 3220 1 2 C 30 54 58 64
45 8 1 1 1 1 1 2 4 343226419200 15119 317 1 6 18 2A 34 4C 52
46 12 1 1 1 1 1 2 6 21946982400 997 28 3 5 19 29 36 4E 51
47 16 1 1 1 1 1 2 8 1219276800 102 6 3 C 31 55 5A 66 69
48 20 1 1 1 1 1 2 10 135475200 10 1 7 19 2A 34 4C 52 63
49 9 1 1 1 1 1 3 3 29940019200 1358 37 3 5 18 28 49 4E 71
50 18 1 1 1 1 1 3 6 139708800 10 2 3 1D 2D 36 3A 4E 71
51 16 1 1 1 1 1 4 4 254016000 19 3 3 C 35 3A 55 66 69
52 8 1 1 1 1 2 2 2 15969139200 750 29 1 E 32 3C 54 5A 66
53 16 1 1 1 1 2 2 4 118540800 20 4 3 C 30 55 5A 66 69
54 24 1 1 1 1 2 2 6 9676800 5 1 7 19 2A 34 4C 52 61
55 32 1 1 1 2 2 2 4 151200 1 1 F 33 3C 55 5A 66 69
Total: 562949953421312 33642660 656103
35


## Page 36

Table A.3
Continued
A8 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1 65025 64 16 0 0 0 0 0 0 0 1
2 0 0 0 0 0 0 0 1 1 336954750 2800 295 0 0 0 0 0 0 1 2
3 0 0 0 0 0 0 1 1 1 396683821800 110064 5758 0 0 0 0 0 1 2 4
4 0 0 0 0 0 0 1 1 2 362237400 596 52 0 0 0 0 0 3 5 6
5 0 0 0 0 0 1 1 1 1 144191294561160 3696215 114651 0 0 0 0 1 2 4 8
6 0 0 0 0 0 1 1 1 2 801119894400 65292 2744 0 0 0 0 1 6 A C
7 0 0 0 0 0 1 1 1 3 5797968120 1422 95 0 0 0 0 3 5 9 E
8 0 0 0 0 1 1 1 1 1 17559952974446400 88462953 1874266 0 0 0 1 2 4 8 10
9 0 0 0 0 1 1 1 1 2 379659804531840 3806686 96326 0 0 0 1 2 C 14 18
10 0 0 0 0 1 1 1 1 3 11124304309440 199374 6235 0 0 0 1 6 A 12 1C
11 0 0 0 0 1 1 1 1 4 1070841280320 27679 957 0 0 0 3 5 9 11 1E
12 0 0 0 0 1 1 1 1 5 50409475200 2430 108 0 0 0 3 5 E 16 19
13 0 0 0 0 1 1 1 2 2 350465875200 8104 265 0 0 0 3 C 15 16 19
14 0 0 0 1 1 1 1 1 1 669716034190338240 1150627540 18733404 0 0 1 2 4 8 10 20
15 0 0 0 1 1 1 1 1 2 46673270510307840 114940091 2053226 0 0 1 2 4 18 28 30
16 0 0 0 1 1 1 1 1 3 3467174719659840 11464276 226089 0 0 1 2 C 14 24 38
17 0 0 0 1 1 1 1 1 4 744008322193920 3048569 63679 0 0 1 6 A 12 22 3C
18 0 0 0 1 1 1 1 1 5 90294382946880 474025 10919 0 0 1 6 A 1C 2C 32
19 0 0 0 1 1 1 1 1 6 45671213145600 258700 5870 0 0 3 5 9 16 2E 31
20 0 0 0 1 1 1 1 1 7 4508891956800 33971 883 0 0 3 5 9 1E 2E 31
21 0 0 0 1 1 1 1 1 8 1853237232000 15033 409 0 0 3 5 E 19 29 36
22 0 0 0 1 1 1 1 1 9 225909129600 2474 74 0 0 3 D 15 1A 26 39
23 0 0 0 1 1 1 1 2 2 244678270233600 953097 19406 0 0 1 6 18 2A 2C 32
24 0 0 0 1 1 1 1 2 4 905427331200 6401 185 0 0 3 C 15 1A 26 29
25 0 0 0 1 1 1 2 2 2 37302249600 348 18 0 0 7 19 1E 2A 2D 33
26 0 0 1 1 1 1 1 1 1 5946448529329701120 5204144555 71348129 0 1 2 4 8 10 20 40
27 0 0 1 1 1 1 1 1 2 1255541169460515840 1268895126 18075782 0 1 2 4 8 30 50 60
28 0 0 1 1 1 1 1 1 3 201557577515938560 230051193 3411083 0 1 2 4 18 28 48 70
29 0 0 1 1 1 1 1 1 4 78772224791393280 98524334 1498752 0 1 2 C 14 24 44 78
30 0 0 1 1 1 1 1 1 5 16904181842714880 23305541 367457 0 1 2 C 14 38 58 64
31 0 0 1 1 1 1 1 1 6 15287255687531520 21926711 345484 0 1 6 A 12 2C 5C 62
32 0 0 1 1 1 1 1 1 7 2483072124099840 3947501 65221 0 1 6 A 12 3C 5C 62
33 0 0 1 1 1 1 1 1 8 1831786505418240 3014954 50240 0 1 6 A 1C 32 52 6C
34 0 0 1 1 1 1 1 1 9 601674419243520 1055591 17966 0 1 6 1A 2A 34 4C 72
35 0 0 1 1 1 1 1 1 10 451640549606400 806664 13584 0 3 5 9 1E 2E 4E 71
36 0 0 1 1 1 1 1 1 11 94403115878400 185595 3296 0 3 5 9 1E 31 51 6E
37 0 0 1 1 1 1 1 1 12 118893204864000 230334 4033 0 3 5 E 16 39 59 66
38 0 0 1 1 1 1 1 1 13 19770573312000 42957 793 0 3 5 E 19 36 56 69
39 0 0 1 1 1 1 1 1 14 18696085632000 39443 695 0 3 5 19 29 36 4E 71
40 0 0 1 1 1 1 1 1 15 5859844300800 12842 235 0 3 D 15 26 38 5E 61
41 0 0 1 1 1 1 1 1 16 3094524518400 7404 157 0 3 C 15 36 39 5A 65
42 0 0 1 1 1 1 1 1 17 526727577600 1380 27 0 3 D 16 2E 39 5A 65
43 0 0 1 1 1 1 1 1 18 702303436800 1376 24 0 7 19 2A 34 4C 53 65
36


## Page 37

Table A.3
Continued
A8 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
44 0 0 1 1 1 1 1 2 2 25998918420787200 31764328 476566 0 1 2 C 30 54 58 64
45 0 0 1 1 1 1 1 2 4 904945412044800 1434616 23722 0 1 6 18 2A 34 4C 52
46 0 0 1 1 1 1 1 2 6 38868105830400 70882 1251 0 3 5 19 29 36 4E 51
47 0 0 1 1 1 1 1 2 8 1777705574400 4348 114 0 3 C 31 55 5A 66 69
48 0 0 1 1 1 1 1 2 10 175575859200 408 10 0 7 19 2A 34 4C 52 63
49 0 0 1 1 1 1 1 3 3 70619902617600 117219 1972 0 3 5 18 28 49 4E 71
50 0 0 1 1 1 1 1 3 6 181062604800 385 10 0 3 1D 2D 36 3A 4E 71
51 0 0 1 1 1 1 1 4 4 362125209600 902 23 0 3 C 35 3A 55 66 69
52 0 0 1 1 1 1 2 2 2 40931905996800 65455 1203 0 1 E 32 3C 54 5A 66
53 0 0 1 1 1 1 2 2 4 192036096000 606 26 0 3 C 30 55 5A 66 69
54 0 0 1 1 1 1 2 2 6 12541132800 66 5 0 7 19 2A 34 4C 52 61
55 0 0 1 1 1 2 2 2 4 195955200 5 1 0 F 33 3C 55 5A 66 69
56 1 1 1 1 1 1 1 1 1 3766962568171582080 2363927011 29610494 1 2 4 8 10 20 40 80
57 2 1 1 1 1 1 1 1 2 3107221856321587200 1958051993 24598561 1 2 4 8 10 60 A0 C0
58 3 1 1 1 1 1 1 1 3 1128344550375409920 717105693 9069162 1 2 4 8 30 50 90 E0
59 4 1 1 1 1 1 1 1 4 798113338051276800 508274669 6438161 1 2 4 18 28 48 88 F0
60 5 1 1 1 1 1 1 1 5 280558398045864960 180518667 2303868 1 2 4 18 28 70 B0 C8
61 6 1 1 1 1 1 1 1 6 391839981330309120 249971410 3172566 1 2 C 14 24 58 B8 C4
62 7 1 1 1 1 1 1 1 7 92717618729258880 60152437 772896 1 2 C 14 24 78 B8 C4
63 8 1 1 1 1 1 1 1 8 98081405804067840 63280071 811462 1 2 C 14 38 64 A4 D8
64 9 1 1 1 1 1 1 1 9 46392962843324160 30131275 388116 1 2 C 34 54 68 98 E4
65 10 1 1 1 1 1 1 1 10 49370839378882560 31886563 408631 1 6 A 12 3C 5C 9C E2
66 11 1 1 1 1 1 1 1 11 14214384381012480 9334363 121275 1 6 A 12 3C 62 A2 DC
67 12 1 1 1 1 1 1 1 12 25287474431600640 16375045 211035 1 6 A 1C 2C 72 B2 CC
68 13 1 1 1 1 1 1 1 13 6076097931697920 4012940 52419 1 6 A 1C 32 6C AC D2
69 14 1 1 1 1 1 1 1 14 8661618203857920 5648182 72918 1 6 A 32 52 6C 9C E2
70 15 1 1 1 1 1 1 1 15 4660876422921600 3060154 39958 1 6 1A 2A 4C 70 BC C2
71 16 1 1 1 1 1 1 1 16 3363977985177600 2214742 29108 1 6 18 2A 6C 72 B4 CA
72 17 1 1 1 1 1 1 1 17 1206477746611200 804732 10608 1 6 1A 2C 5C 72 B4 CA
73 18 1 1 1 1 1 1 1 18 2308713728025600 1503637 19409 1 E 32 54 68 98 A6 CA
74 19 1 1 1 1 1 1 1 19 548565282316800 367458 4865 3 5 9 31 51 6E 9E E1
75 20 1 1 1 1 1 1 1 20 883792178841600 583710 7689 3 5 E 19 36 68 A9 D6
76 21 1 1 1 1 1 1 1 21 420654153830400 280261 3719 3 5 E 19 36 69 A9 D6
77 22 1 1 1 1 1 1 1 22 358862424883200 237040 3085 3 5 E 32 56 69 99 E6
78 23 1 1 1 1 1 1 1 23 113325986995200 76671 1023 3 5 E 36 56 69 99 E6
79 24 1 1 1 1 1 1 1 24 228366581990400 152796 2117 3 5 18 68 A9 B6 CE D1
80 25 1 1 1 1 1 1 1 25 59747916211200 40146 532 3 5 18 2E 69 76 B1 CE
81 26 1 1 1 1 1 1 1 26 73204159795200 48393 630 3 5 19 2E 69 76 B1 CE
82 27 1 1 1 1 1 1 1 27 33155489203200 22046 293 3 5 39 59 6E 76 9E E1
83 28 1 1 1 1 1 1 1 28 34709152665600 23559 324 3 C 15 36 5A 65 B9 C6
84 29 1 1 1 1 1 1 1 29 9118971187200 6180 82 3 C 31 55 7A 96 D9 E5
85 30 1 1 1 1 1 1 1 30 28015323033600 18147 238 3 C 31 54 6A 9A A6 C9
86 31 1 1 1 1 1 1 1 31 3621252096000 2436 32 3 D 16 2E 5A 75 B9 C6
37


## Page 38

Table A.3
Continued
A8 The number of The SNF-class
det SNF matrices π -classes φ-classes representative
87 32 1 1 1 1 1 1 1 32 5423648025600 3953 68 3 C 31 56 6A 9A A6 C5
88 33 1 1 1 1 1 1 1 33 2806470374400 1866 27 3 D 1E 35 66 79 AA D5
89 34 1 1 1 1 1 1 1 34 2831160729600 1815 23 3 D 31 54 6A 9A A6 C9
90 35 1 1 1 1 1 1 1 35 757170892800 491 7 3 1D 2E 56 69 9A B1 CD
91 36 1 1 1 1 1 1 1 36 1327792435200 873 13 3 D 35 56 69 99 AE C5
92 37 1 1 1 1 1 1 1 37 131681894400 81 1 7 19 2A 4C 71 A5 CB D6
93 38 1 1 1 1 1 1 1 38 592568524800 389 5 3 1D 2E 56 69 9A B5 CD
94 39 1 1 1 1 1 1 1 39 65840947200 45 1 7 19 2A 56 6D 9C B3 CB
95 40 1 1 1 1 1 1 1 40 263363788800 200 4 7 19 2A 4C 71 96 AD CB
96 42 1 1 1 1 1 1 1 42 65840947200 45 1 7 19 3E 63 AA B5 CC D2
97 4 1 1 1 1 1 1 2 2 264489939127895040 166494351 2095861 1 2 4 18 60 A8 B0 C8
98 8 1 1 1 1 1 1 2 4 48628694487582720 30927272 394107 1 2 C 30 54 68 98 A4
99 12 1 1 1 1 1 1 2 6 8317470133324800 5286249 67857 1 6 A 32 52 6C 9C A2
100 16 1 1 1 1 1 1 2 8 1671575454259200 1087782 14500 1 6 18 62 AA B4 CC D2
101 20 1 1 1 1 1 1 2 10 300128743756800 194974 2641 1 E 32 54 68 98 A4 C6
102 24 1 1 1 1 1 1 2 12 119718045619200 80651 1172 3 5 18 60 A9 B6 CE D1
103 28 1 1 1 1 1 1 2 14 14388990336000 9935 157 3 C 15 3A 65 A5 D6 D9
104 32 1 1 1 1 1 1 2 16 4180900147200 3259 65 3 C 31 56 6A 9A A6 C1
105 36 1 1 1 1 1 1 2 18 1360712908800 1103 23 3 D 31 54 6A 9A A6 C1
106 40 1 1 1 1 1 1 2 20 271593907200 232 5 3 D 35 59 6E 9E A9 C5
107 44 1 1 1 1 1 1 2 22 76814438400 74 2 3 1D 2E 56 79 9A B5 CD
108 48 1 1 1 1 1 1 2 24 16460236800 28 1 7 19 3E 61 AB B5 CC D2
109 9 1 1 1 1 1 1 3 3 5728974559056000 3662516 47056 1 6 A 30 50 92 9C E2
110 18 1 1 1 1 1 1 3 6 292630089830400 187420 2455 1 6 3A 5A 6C 74 9C E2
111 27 1 1 1 1 1 1 3 9 6466129689600 4234 71 3 C 31 54 7A 9A A6 C9
112 36 1 1 1 1 1 1 3 12 285310771200 219 7 3 1C 65 6A A6 B1 C9 D2
113 45 1 1 1 1 1 1 3 15 2743372800 6 1 7 39 5A 6C 9C AB B6 D1
114 16 1 1 1 1 1 1 4 4 282699080294400 186028 2556 1 6 18 6A 74 AA CC D2
115 32 1 1 1 1 1 1 4 8 724250419200 713 21 3 C 35 3A 56 69 99 A6
116 25 1 1 1 1 1 1 5 5 2339411155200 1497 22 3 D 15 26 5E 61 B8 C5
117 36 1 1 1 1 1 1 6 6 142655385600 136 4 7 19 2A 4B 74 8C D2 E1
118 8 1 1 1 1 1 2 2 2 2260349894476800 1421783 18397 1 2 1C 64 78 A8 B4 CC
119 16 1 1 1 1 1 2 2 4 136245037824000 90153 1346 1 6 18 60 AA B4 CC D2
120 24 1 1 1 1 1 2 2 6 6530011084800 5175 114 1 E 32 54 68 98 A4 C2
121 32 1 1 1 1 1 2 2 8 625488998400 578 15 3 D 31 55 6A 9A A6 C1
122 40 1 1 1 1 1 2 2 10 54867456000 96 5 3 D 31 56 6A 9A A6 C1
123 48 1 1 1 1 1 2 2 12 16460236800 49 3 3 1C 65 7A A9 B6 CE D1
124 56 1 1 1 1 1 2 2 14 391910400 6 1 3 1D 65 7A A9 B6 CE D1
125 32 1 1 1 1 1 2 4 4 98761420800 134 4 3 1C 64 78 A9 B2 CA D1
126 27 1 1 1 1 1 3 3 3 101504793600 96 6 7 19 2A 4B 74 8D B1 D6
127 16 1 1 1 1 2 2 2 2 1082717798400 754 17 3 1C 64 78 A9 AA B5 CD
128 32 1 1 1 1 2 2 2 4 28217548800 74 4 1 1E 66 78 AA B4 CC D2
Total: 18446744073709551616 14685630688 199727714
38


## Page 39

Table A.4
Transposed incidence matrix M7 containing all Mn, 1≤ n≤ 7. Symbol at position
(s′, s ) carries information about ms,s′ (7):•, ⋆,◦ denotes respectively 1, 0 explained
by Lemma 10, and 0 not explained by Lemma 10.
0 0 0 00 000 00000 0 000000000 000 111111111111111111 11111 11111110 0 0 00 000 00000 0 111111111 111 111111111111111111 11111 1111111s 0 0 0 00 000 11111 1 111111111 111 111111111111111111 11111 11111110 0 0 00 111 11111 1 111111111 111 111111111111111111 11111 11111120 0 0 11 111 11111 1 111111111 112 111111111111111111 11111 11122220 0 1 11 111 11111 2 111111111 222 111111111111111111 22222 3342222
s′ 0 0 0 00 000 00000 0 000000000 000 000000000111111111 00001 00000000 1 1 12 123 12345 2 123456789 242 123456789012345678 24680 3642464
0000000 0 •· · ·· ··· ······ ············ ······························
0000000 1 •• · ·· ··· ······ ············ ······························
0000001 1 •• • ·· ··· ······ ············ ······························
0000011 1 ·• • •• ··· ······ ············ ······························0000011 2 ·◦ • ⋆• ··· ······ ············ ······························
0000111 1 ··• •• ••• ······ ············ ······························0000111 2 ··• •• ⋆•⋆ ······ ············ ······························0000111 3 ··◦ •• ⋆⋆• ······ ············ ······························
0001111 1 ·· ·•⋆ ••• •••••• ············ ······························0001111 2 ·· ·•• ••• ⋆•⋆•⋆• ············ ······························0001111 3 ·· ·•⋆ ••• ⋆⋆•⋆⋆ ⋆ ············ ······························0001111 4 ·· ·•◦ ••• ⋆⋆⋆•⋆◦ ············ ······························0001111 5 ·· ·◦⋆ ••• ⋆⋆⋆⋆• ⋆ ············ ······························0001112 2 ·· ·•◦ ⋆•⋆ ⋆⋆⋆⋆⋆• ············ ······························
0011111 1 ·· · ··•⋆⋆ ••••• ⋆ •••••••••••◦ ······························0011111 2 ·· · ··••⋆ •••••• ⋆•⋆•⋆•⋆•⋆••• ······························0011111 3 ·· · ··•⋆• ••••• ⋆ ⋆⋆•⋆⋆•⋆⋆• ⋆⋆⋆ ······························0011111 4 ·· · ··••⋆ •••••• ⋆⋆⋆•⋆⋆⋆•⋆◦•◦ ······························0011111 5 ·· · ··•⋆⋆ ••••• ⋆ ⋆⋆⋆⋆•⋆⋆⋆⋆ ⋆⋆⋆ ······························0011111 6 ·· · ··•◦◦ •••••• ⋆⋆⋆⋆⋆•⋆⋆⋆ ⋆⋆⋆ ······························0011111 7 ·· · ··◦⋆⋆ ••••• ⋆ ⋆⋆⋆⋆⋆⋆•⋆⋆ ⋆⋆⋆ ······························0011111 8 ·· · ··••⋆ •••••• ⋆⋆⋆⋆⋆⋆⋆•⋆ ⋆◦◦ ······························0011111 9 ·· · ··•⋆◦ ••••• ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆• ⋆⋆⋆ ······························0011112 2 ·· · ··••⋆ ⋆•⋆•⋆• ⋆⋆⋆⋆⋆⋆⋆⋆⋆••• ······························0011112 4 ·· · ··••⋆ ⋆•⋆•⋆• ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆•◦ ······························0011122 2 ·· · ·· ⋆•⋆ ⋆⋆⋆⋆⋆• ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆• ······························
0111111 1 ·· · ·· ···•⋆⋆⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ••••••••••••••••••••••••••◦◦◦◦0111111 2 ·· · ·· ···••⋆⋆⋆ ⋆ •••••••••••⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆•••••◦0111111 3 ·· · ·· ···•⋆•⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆• ⋆⋆•⋆⋆••⋆⋆⋆◦⋆0111111 4 ·· · ·· ···••⋆•⋆◦ •••••••••••◦ ⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆◦•◦•◦ ⋆⋆•◦•◦◦0111111 5 ·· · ·· ···•⋆⋆⋆• ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆•⋆⋆⋆⋆•⋆⋆⋆⋆•⋆⋆⋆ ⋆⋆⋆⋆• ⋆⋆⋆⋆⋆⋆⋆0111111 6 ·· · ·· ···•••⋆⋆ ⋆ •••••••••••⋆ ⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆• ⋆⋆•⋆⋆ ⋆•⋆⋆⋆•⋆0111111 7 ·· · ·· ···•⋆⋆⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 8 ·· · ·· ···••⋆•⋆◦ •••••••••••◦ ⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆⋆•⋆⋆ ⋆◦⋆•⋆ ⋆⋆◦◦◦◦◦0111111 9 ·· · ·· ···•⋆•⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆⋆⋆• ⋆⋆⋆⋆⋆◦◦⋆⋆⋆⋆⋆0111111 10 ·· · ·· ···•◦⋆⋆◦ ⋆ •••••••••••⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆• ⋆⋆⋆⋆⋆⋆⋆0111111 11 ·· · ·· ···◦⋆⋆⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 12 ·· · ·· ···•••◦⋆◦ •••••••••••◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆⋆ ⋆⋆◦⋆⋆ ⋆⋆⋆⋆⋆◦⋆0111111 13 ·· · ·· ···◦⋆⋆⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 14 ·· · ·· ···•◦⋆⋆⋆ ⋆ •••••••••••⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 15 ·· · ·· ···•⋆◦⋆◦ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 16 ·· · ·· ···••⋆◦⋆◦ •••••••••••◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆⋆ ⋆⋆⋆◦⋆ ⋆⋆◦⋆◦⋆◦0111111 17 ·· · ·· ···◦⋆⋆⋆⋆ ⋆ ••••••••• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆•⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆0111111 18 ·· · ·· ···••◦⋆⋆ ⋆ •••••••••••⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆• ⋆⋆⋆⋆⋆ ⋆◦⋆⋆⋆⋆⋆0111112 2 ·· · ·· ···••⋆◦⋆• ⋆•⋆•⋆•⋆•⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆•••••0111112 4 ·· · ·· ···••⋆•⋆• ⋆•⋆•⋆•⋆•⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆•⋆•⋆ ⋆⋆•◦•◦•0111112 6 ·· · ·· ···•••◦⋆◦ ⋆•⋆•⋆•⋆•⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆•⋆⋆ ⋆⋆⋆⋆⋆•⋆0111112 8 ·· · ·· ···••⋆◦⋆◦ ⋆•⋆•⋆•⋆•⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆•⋆ ⋆⋆◦⋆◦⋆◦0111112 10 ·· · ·· ···◦◦⋆◦◦◦ ⋆•⋆•⋆•⋆•⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆• ⋆⋆⋆⋆⋆⋆⋆0111113 3 ·· · ·· ···•⋆◦⋆⋆ ⋆ ⋆⋆•⋆⋆•⋆⋆• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆0111113 6 ·· · ·· ···••◦⋆⋆ ⋆ ⋆⋆•⋆⋆•⋆⋆• ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆•⋆⋆⋆⋆⋆0111114 4 ·· · ·· ···••⋆◦⋆◦ ⋆⋆⋆•⋆⋆⋆•⋆◦•◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆•⋆◦⋆◦0111122 2 ·· · ·· ··· ⋆•⋆◦⋆• ⋆⋆⋆⋆⋆⋆⋆⋆⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆••••0111122 4 ·· · ·· ··· ⋆•⋆◦⋆◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆•⋆•0111122 6 ·· · ·· ··· ⋆◦⋆◦⋆◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆•⋆0111222 4 ·· · ·· ··· ⋆⋆⋆⋆⋆◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆•
39


## Page 40

Table A.4
Continued.
0 0 0 00 000 00000 0 000000000 000 111111111111111111 11111 11111110 0 0 00 000 00000 0 111111111 111 111111111111111111 11111 1111111s 0 0 0 00 000 11111 1 111111111 111 111111111111111111 11111 11111110 0 0 00 111 11111 1 111111111 111 111111111111111111 11111 11111120 0 0 11 111 11111 1 111111111 112 111111111111111111 11111 11122220 0 1 11 111 11111 2 111111111 222 111111111111111111 22222 3342222
s′ 0 0 0 00 000 00000 0 000000000 000 000000000111111111 00001 00000000 1 1 12 123 12345 2 123456789 242 123456789012345678 24680 3642464
1111111 1 ·· · ·· ··· ······•⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 2 ·· · ·· ··· ······••⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 3 ·· · ·· ··· ······•⋆•⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 4 ·· · ·· ··· ······••⋆•⋆⋆⋆⋆⋆◦⋆⋆ ••••••••••••••••••••••• ⋆⋆•◦◦◦⋆1111111 5 ·· · ·· ··· ······•⋆⋆⋆•⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 6 ·· · ·· ··· ······•••⋆⋆•⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••••••••••⋆⋆⋆⋆⋆1111111 7 ·· · ·· ··· ······•⋆⋆⋆⋆⋆•⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 8 ·· · ·· ··· ······••⋆•⋆⋆⋆•⋆◦◦◦ ••••••••••••••••••••••• ⋆⋆•◦◦◦◦1111111 9 ·· · ·· ··· ······•⋆•⋆⋆⋆⋆⋆• ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 10 ·· · ·· ··· ······••⋆⋆•⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 11 ·· · ·· ··· ······•⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 12 ·· · ·· ··· ······••••⋆•⋆⋆⋆◦⋆⋆ ••••••••••••••••••••••••••◦◦◦⋆1111111 13 ·· · ·· ··· ······•⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 14 ·· · ·· ··· ······••⋆⋆⋆⋆•⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 15 ·· · ·· ··· ······•⋆•⋆•⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 16 ·· · ·· ··· ······••⋆•⋆⋆⋆•⋆◦◦◦ ••••••••••••••••••••••• ⋆⋆•◦◦◦◦1111111 17 ·· · ·· ··· ······•⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 18 ·· · ·· ··· ······•••⋆⋆•⋆⋆◦ ⋆⋆⋆ •••••••••••••••••••••••••⋆⋆⋆⋆⋆1111111 19 ·· · ·· ··· ······◦⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 20 ·· · ·· ··· ······••⋆◦•⋆⋆⋆⋆◦⋆⋆ ••••••••••••••••••••••• ⋆⋆•◦◦◦⋆1111111 21 ·· · ·· ··· ······•⋆◦⋆⋆⋆◦⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 22 ·· · ·· ··· ······•◦⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 23 ·· · ·· ··· ······◦⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 24 ·· · ·· ··· ······••••⋆•⋆◦⋆◦◦◦ ••••••••••••••••••••••••••◦◦◦◦1111111 25 ·· · ·· ··· ······•⋆⋆⋆◦⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 26 ·· · ·· ··· ······•◦⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 27 ·· · ·· ··· ······•⋆•⋆⋆⋆⋆⋆◦ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 28 ·· · ·· ··· ······••⋆◦⋆⋆◦⋆⋆◦⋆⋆ ••••••••••••••••••••••• ⋆⋆•◦◦◦⋆1111111 29 ·· · ·· ··· ······◦⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 30 ·· · ·· ··· ······•••⋆•◦⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••••••••••⋆⋆⋆⋆⋆1111111 31 ·· · ·· ··· ······◦⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 32 ·· · ·· ··· ······••⋆•⋆⋆⋆◦⋆◦◦◦ ••••••••••••••••••••••• ⋆⋆•◦◦◦◦1111111 33 ·· · ·· ··· ······•⋆◦⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111111 34 ·· · ·· ··· ······◦◦⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••◦•••••• ⋆⋆⋆⋆⋆⋆⋆1111111 35 ·· · ·· ··· ······•⋆⋆⋆◦⋆◦⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 36 ·· · ·· ··· ······••••⋆◦⋆⋆◦◦⋆⋆ ••••••••••••••••••••••••••◦◦◦⋆1111111 37 ·· · ·· ··· ······◦⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ •••••••••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111111 38 ·· · ·· ··· ······◦◦⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆1111111 39 ·· · ·· ··· ······◦⋆◦⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ ••••••◦•••••◦••••• ⋆⋆⋆⋆⋆•◦⋆⋆⋆⋆⋆1111111 40 ·· · ·· ··· ······••⋆◦◦⋆⋆◦⋆◦◦◦ ••••••••••••••••••••••• ⋆⋆•◦◦◦◦1111111 42 ·· · ·· ··· ······◦◦◦⋆⋆◦◦⋆⋆ ⋆⋆⋆ ◦•••◦•◦◦••••◦◦••••••••••◦⋆⋆⋆⋆⋆1111112 2 ·· · ·· ··· ······••⋆◦⋆⋆⋆⋆⋆•⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆◦•••⋆1111112 4 ·· · ·· ··· ······••⋆•⋆⋆⋆◦⋆••◦ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆••••◦1111112 6 ·· · ·· ··· ······•••◦⋆•⋆⋆⋆•⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆•◦•••⋆1111112 8 ·· · ·· ··· ······••⋆•⋆⋆⋆•⋆••◦ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆••••◦1111112 10 ·· · ·· ··· ······••⋆◦•⋆⋆⋆⋆•⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆◦•••⋆1111112 12 ·· · ·· ··· ······••••⋆•⋆◦⋆•◦◦ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆•••••◦1111112 14 ·· · ·· ··· ······••⋆◦⋆⋆◦⋆⋆◦⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆◦•••⋆1111112 16 ·· · ·· ··· ······••⋆•⋆⋆⋆◦⋆◦•◦ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆••••◦1111112 18 ·· · ·· ··· ······••◦◦⋆◦⋆⋆◦•⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆•◦•••⋆1111112 20 ·· · ·· ··· ······••⋆◦◦⋆⋆◦⋆◦◦◦ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆••••◦1111112 22 ·· · ·· ··· ······◦◦⋆◦⋆⋆⋆⋆⋆◦⋆⋆ ⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•⋆•••••• ⋆⋆◦•••⋆1111112 24 ·· · ·· ··· ······◦•◦◦⋆◦⋆◦⋆◦◦◦ ⋆◦⋆◦⋆◦⋆•⋆•⋆◦⋆•⋆•⋆◦••••◦ ⋆◦◦◦••◦1111113 3 ·· · ·· ··· ······•⋆•⋆⋆⋆⋆⋆◦ ⋆⋆⋆ ⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111113 6 ·· · ·· ··· ······•••⋆⋆•⋆⋆◦ ⋆⋆⋆ ⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆• ⋆⋆•⋆⋆••⋆⋆⋆⋆⋆1111113 9 ·· · ·· ··· ······•⋆•⋆⋆⋆⋆⋆◦ ⋆⋆⋆ ⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111113 12 ·· · ·· ··· ······••••⋆◦⋆⋆◦◦⋆⋆ ⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆•⋆⋆• ⋆⋆•⋆⋆••⋆⋆⋆◦⋆1111113 15 ·· · ·· ··· ······◦⋆◦⋆◦⋆⋆⋆◦ ⋆⋆⋆ ⋆⋆•⋆⋆◦⋆⋆◦⋆⋆•⋆⋆◦⋆⋆• ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111114 4 ·· · ·· ··· ······••⋆•⋆⋆⋆◦⋆••◦ ⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆◦•◦•◦ ⋆⋆•◦•◦◦1111114 8 ·· · ·· ··· ······••⋆•⋆⋆⋆◦⋆◦•◦ ⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆⋆•⋆⋆◦•◦•◦ ⋆⋆•◦•◦◦1111115 5 ·· · ·· ··· ······•⋆⋆⋆◦⋆⋆⋆⋆ ⋆⋆⋆ ⋆⋆⋆⋆•⋆⋆⋆⋆•⋆⋆⋆⋆•⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆1111116 6 ·· · ·· ··· ······••◦◦⋆◦⋆⋆◦•⋆⋆ ⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆•⋆⋆⋆⋆⋆• ⋆⋆•⋆⋆ ⋆◦⋆⋆⋆•⋆1111122 2 ·· · ·· ··· ······ ⋆•⋆◦⋆⋆⋆◦⋆•◦• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆◦••••1111122 4 ·· · ·· ··· ······ ⋆•⋆•⋆⋆⋆◦⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆•••••1111122 6 ·· · ·· ··· ······ ⋆•⋆◦⋆•⋆◦⋆•◦• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆◦••••1111122 8 ·· · ·· ··· ······ ⋆•⋆•⋆⋆⋆◦⋆••◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆•••••1111122 10 ·· · ·· ··· ······ ⋆◦⋆◦⋆⋆⋆◦⋆◦◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••◦ ⋆⋆◦••••1111122 12 ·· · ·· ··· ······ ⋆•⋆◦⋆◦⋆◦⋆•◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆••••• ⋆⋆◦••••1111122 14 ·· · ·· ··· ······ ⋆◦⋆◦⋆⋆⋆◦⋆◦◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆◦◦••◦ ⋆⋆◦•◦••1111124 4 ·· · ·· ··· ······ ⋆•⋆•⋆⋆⋆◦⋆••◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆•⋆•⋆ ⋆⋆•◦•◦•1111133 3 ·· · ·· ··· ······ ⋆⋆•⋆⋆⋆⋆⋆◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆••⋆⋆⋆⋆⋆1111222 2 ·· · ·· ··· ······ ⋆⋆⋆⋆⋆⋆⋆⋆⋆•◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆•••◦1111222 4 ·· · ·· ··· ······ ⋆⋆⋆⋆⋆⋆⋆⋆⋆••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆••••
40


## Page 41

Table A.5
The part of S9 corresponding to nonsingular part of A9.
det SNF
1-106 m 1 1 1 1 1 1 1 1 m m∈{ 1− 98, 100, 101, 102,}
∪{ 104, 105, 108, 110, 120}
107-135 4m 1 1 1 1 1 1 1 2 2 m m∈{ 1− 29}
136-148 9m 1 1 1 1 1 1 1 3 3 m m∈{ 1− 13}
149-155 16m 1 1 1 1 1 1 1 4 4 m m∈{ 1− 7}
156-159 25 1 1 1 1 1 1 1 5 5 m m∈{ 1− 3, 5}
160 36 1 1 1 1 1 1 1 6 6
161 72 1 1 1 1 1 1 1 6 12
162 108 1 1 1 1 1 1 1 6 18
163 49 1 1 1 1 1 1 1 7 7
164 98 1 1 1 1 1 1 1 7 14
165 64 1 1 1 1 1 1 1 8 8
166 128 1 1 1 1 1 1 1 8 16
167 81 1 1 1 1 1 1 1 9 9
168 100 1 1 1 1 1 1 1 10 10
169-182 8m 1 1 1 1 1 1 2 2 2 m m∈{ 1− 13, 15}
183 32 1 1 1 1 1 1 2 4 4
184 64 1 1 1 1 1 1 2 4 8
185 96 1 1 1 1 1 1 2 4 12
186 72 1 1 1 1 1 1 2 6 6
187 128 1 1 1 1 1 1 2 8 8
188 27 1 1 1 1 1 1 3 3 3
189 54 1 1 1 1 1 1 3 3 6
190 81 1 1 1 1 1 1 3 3 9
191 108 1 1 1 1 1 1 3 3 12
192 64 1 1 1 1 1 1 4 4 4
193 128 1 1 1 1 1 1 4 4 8
194 16 1 1 1 1 1 2 2 2 2
195 32 1 1 1 1 1 2 2 2 4
196 48 1 1 1 1 1 2 2 2 6
197 64 1 1 1 1 1 2 2 2 8
198 80 1 1 1 1 1 2 2 2 10
199 96 1 1 1 1 1 2 2 2 12
200 64 1 1 1 1 1 2 2 4 4
201 144 1 1 1 1 1 2 2 6 6
202 81 1 1 1 1 1 3 3 3 3
203 32 1 1 1 1 2 2 2 2 2
204 64 1 1 1 1 2 2 2 2 4
41


## Page 42

Table A.6
The part of the transposed incidence matrix M8, corresponding to the regular part
ofS9. Symbol at position ( s′, s ) carries information about ms,s′ (7):•, ⋆,◦ denotes
respectively 1, 0 explained by Lemma 10, and 0 not explained b y Lemma 10.
000000000000000000 0000 00000000 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111s 111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111112 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1122111111111111111111 1111 11112222 11111111111111111111111111111111111111111 111111111111 11111 1111 2222222 2322111111111111111111 2222 23342222 11111111111111111111111111111111111111111 222222222222 33333 4456 2222222 4322
s′ 000000000111111111 0000 10000000 00000000011111111112222222222333333333344 000011111222 00011 0000 0000111 0000123456789012345678 2468 03642464 12345678901234567890123456789012345678902 246802468024 36925 4856 2468024 4324
1111111 1 1 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 2 •• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 3 • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 4 •• ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 5 • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 6 ••• ⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 7 • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 8 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 9 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 10 •• ⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 11 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 12 •••• ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 13 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 14 •• ⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 15 • ⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 16 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 17 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 18 ••• ⋆⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 19 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 20 •• ⋆ •• ⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ••• ⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 21 • ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 22 •• ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 23 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 24 •••• ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ ◦◦◦ ⋆ ⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 25 • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 26 •• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 27 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 28 •• ⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 29 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 30 ••• ⋆ •• ⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆ •• ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 31 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 32 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 33 • ⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 34 •• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 35 • ⋆⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 36 •••• ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ⋆ ◦ ⋆⋆1111111 1 37 • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 38 •• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••••••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 39 • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 40 •• ⋆ •• ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ••• ⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 41 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 42 ••• ⋆⋆ •• ⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 43 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 44 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 45 • ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 46 •◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 47 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 48 •••• ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆ ◦◦◦◦ ⋆⋆⋆ ◦◦◦◦ ⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 49 • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 50 •• ⋆⋆ • ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 51 • ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 52 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 53 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 54 ••• ⋆⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 55 • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 56 •• ⋆ • ⋆⋆ •◦ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 57 • ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••••••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 58 •◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 59 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 60 •••••• ⋆⋆⋆ • ⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• •••• ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 61 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 62 •◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 63 • ⋆ • ⋆⋆⋆ • ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 64 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 65 • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 66 ••• ⋆⋆ ◦ ⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 67 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 68 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆
42


## Page 43

Table A.6
Continued.
000000000000000000 0000 00000000 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111s 111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111112 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1122111111111111111111 1111 11112222 11111111111111111111111111111111111111111 111111111111 11111 1111 2222222 2322111111111111111111 2222 23342222 11111111111111111111111111111111111111111 222222222222 33333 4456 2222222 4322
s′ 000000000111111111 0000 10000000 00000000011111111112222222222333333333344 000011111222 00011 0000 0000111 0000123456789012345678 2468 03642464 12345678901234567890123456789012345678902 246802468024 36925 4856 2468024 4324
1111111 1 69 • ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 70 •• ⋆⋆ ◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •◦•••••••••• ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 71 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 72 •••• ⋆ • ⋆ •◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦◦◦ ⋆ ⋆ ◦◦ ⋆ ◦ ⋆ ◦ ⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ◦◦◦◦1111111 1 73 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 74 ◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••◦•••• •••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 75 • ⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 76 •◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••••••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 77 • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 78 ••◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 79 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 80 •• ⋆ •• ⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ◦ ⋆⋆ ◦◦◦ ⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ ••• ⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 81 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 82 ◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 83 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 84 •••• ⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ••••• •• ⋆ • ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 85 • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 86 ◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 87 ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••◦•••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 88 •• ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 89 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 90 ••• ⋆ ◦• ⋆⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ••••• ⋆⋆ •• ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 1 91 • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 92 •◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 93 ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••◦•••••••••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 94 ◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••◦•◦•• •••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 95 ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••••••••••••••••••••••••••••◦◦•◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 96 ••◦• ⋆ ◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ ◦◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ••••••••••••••••••◦•••••••••••••••••••••• •••••••••••• ••••◦ •• ⋆ • ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 97 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ •◦◦••◦•◦••◦•••◦••◦◦◦•••◦••••◦•◦•◦•◦•◦◦◦•◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 98 •• ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••••••••••◦•••••••••••••••••◦•••• •••••••••••• ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 100 •◦ ⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦•◦•••••◦•••◦•••••◦•••••◦•••••••••••◦•◦•◦ •••••••••••• ⋆⋆⋆⋆⋆ ••◦ ⋆ ◦◦◦◦◦◦◦ ⋆⋆⋆⋆1111111 1 101 ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ •◦••◦◦◦•••••••◦◦••◦◦••••◦◦••••◦••◦◦◦◦•••◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 102 •◦◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ••••◦•◦•••••••••••◦•••••••••••••••••••••• •••••••••••• ••••◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 104 ◦◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ••◦•◦◦••◦◦••◦•••◦•◦•••◦•◦◦••◦•••••◦••◦◦•◦ ◦•••••••◦•◦◦ ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 1 105 • ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ •◦•••••◦•◦••••••••◦•••••◦•••◦•••••••◦•••• ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••◦◦ ⋆⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 108 ◦••◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ◦•◦•◦◦◦•◦•◦•◦•◦•◦•◦•◦•••••◦◦•◦••◦◦••◦◦◦•◦ ◦•◦◦•••◦•••• ◦◦◦◦◦ ◦◦ ⋆ ◦ ◦◦◦◦◦◦◦ ⋆ ◦ ⋆⋆1111111 1 110 ◦◦ ⋆⋆ ◦ ⋆⋆⋆⋆ ◦• ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ◦•◦◦••◦•◦•◦•••••◦•◦•◦◦••◦•••◦•••◦•••••◦•◦ ◦•◦◦••••••◦• ⋆⋆⋆⋆⋆ ⋆⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 1 120 ◦◦◦◦◦◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆ ◦ ⋆ ◦◦•◦•◦◦•◦◦◦•◦◦•◦◦◦◦•◦◦◦•◦◦◦◦◦•◦◦◦◦••◦◦◦•• ◦◦•◦◦•◦•◦◦◦◦ ◦••◦◦ ◦•◦◦ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦
1111111 2 2 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 4 •• ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •• ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 6 •••◦ ⋆ • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆ • ⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ ◦◦ ⋆ • ••••••• ⋆⋆⋆⋆1111111 2 8 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ • ⋆⋆⋆ ◦◦◦ ⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 10 •• ⋆ ◦• ⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 12 •••• ⋆ • ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ ••• ⋆ ⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ •• ⋆ • ••••••• • ⋆ ◦◦1111111 2 14 •• ⋆ ◦ ⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 16 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆ •• ⋆ • ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 18 •••◦ ⋆ • ⋆⋆ • ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ • ⋆ • ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ ◦◦ ⋆ • ••••••• ⋆⋆⋆⋆1111111 2 20 •• ⋆ •• ⋆⋆ ◦ ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ •• ⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 22 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 24 •••• ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆ •••◦ ⋆⋆⋆ ◦◦◦◦ ⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ •• ⋆ • ••••••• • ⋆ ◦◦1111111 2 26 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 28 •• ⋆ • ⋆⋆ •◦ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ •◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 30 •••◦•• ⋆⋆⋆ • ⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆ • ⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ ◦◦ ⋆ • ••••••• ⋆⋆⋆⋆1111111 2 32 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 34 •• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 36 •••• ⋆ • ⋆ ◦◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ••◦ ⋆ ⋆ ◦◦ ⋆ ◦ ⋆ ◦ ⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ •• ⋆ • ••••••• • ⋆ ◦◦1111111 2 38 ◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 40 •• ⋆ •• ⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ◦ ⋆⋆ ◦◦◦ ⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 42 ••◦◦ ⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆ • ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ ◦◦ ⋆ • ••••••• ⋆⋆⋆⋆1111111 2 44 •• ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 46 ◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •◦ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 48 ••◦• ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ •◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆ • ⋆ • ⋆ •• ⋆ • ••••••• • ⋆ ◦◦1111111 2 50 •• ⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •◦ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ⋆⋆⋆⋆1111111 2 52 ◦• ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ •• •••••••••••• ⋆⋆⋆⋆⋆ •◦ ⋆⋆ ••••••• • ⋆ ◦◦1111111 2 54 •••◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆ ◦ ⋆ ◦ ⋆ • ⋆ ◦ ⋆ • ⋆ • ⋆ ◦ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ ◦◦ •••••••••◦•• ⋆ ◦ ⋆ ◦ ⋆ ◦◦ ⋆ • ••••••• ⋆⋆⋆⋆1111111 2 56 ◦◦ ⋆ ◦ ⋆⋆ ◦◦ ⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆⋆ ⋆ • ⋆ ◦ ⋆ ◦ ⋆ • ⋆ • ⋆ ◦ ⋆ ◦ ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆ • ⋆ • ⋆ ◦ ⋆ • ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆ •◦ ◦•••••◦••••• ⋆⋆⋆⋆⋆ ◦• ⋆⋆ ••◦◦••◦ • ⋆ ◦◦1111111 2 58 ◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆ ◦ ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆ ◦◦ •••◦•◦•◦•◦◦◦ ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ◦◦••◦•• ⋆⋆⋆⋆
43


## Page 44

Table A.6
Continued.
000000000000000000 0000 00000000 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111s 111111111111111111 1111 11111111 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1111111111111111111111 1111 11111112 11111111111111111111111111111111111111111 111111111111 11111 1111 1111111 1122111111111111111111 1111 11112222 11111111111111111111111111111111111111111 111111111111 11111 1111 2222222 2322111111111111111111 2222 23342222 11111111111111111111111111111111111111111 222222222222 33333 4456 2222222 4322
s′ 000000000111111111 0000 10000000 00000000011111111112222222222333333333344 000011111222 00011 0000 0000111 0000123456789012345678 2468 03642464 12345678901234567890123456789012345678902 246802468024 36925 4856 2468024 4324
1111111 3 3 • ⋆ • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 6 ••• ⋆⋆ • ⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ •• ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 9 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 12 •••• ⋆ • ⋆⋆ ◦ ⋆⋆ • ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ •◦ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••••• ⋆⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆ ⋆ • ⋆⋆1111111 3 15 • ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 18 ••• ⋆⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ •◦ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 21 • ⋆ • ⋆⋆⋆ • ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 24 •••• ⋆ • ⋆ •◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦◦◦ ⋆ ⋆ ◦◦ ⋆ ◦ ⋆ ◦ ⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••••• ⋆⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆ ⋆ • ⋆⋆1111111 3 27 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 30 ••• ⋆ ◦• ⋆⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 33 ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ ◦ ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111111 3 36 •••◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ ◦ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ••◦•◦ ⋆⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆ ⋆ • ⋆⋆1111111 3 39 ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ • ⋆⋆ ◦ ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••◦• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆
1111111 4 4 •• ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ •◦◦ ⋆⋆ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 8 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ • ⋆⋆⋆ •◦◦ ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 12 •••• ⋆ • ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆ •••◦ ⋆⋆⋆ ◦◦◦◦ ⋆ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆ • ⋆ •• ⋆ ◦ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 16 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 20 •• ⋆ •• ⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ◦ ⋆⋆ ◦◦◦ ⋆⋆ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 24 ••◦• ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ •◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆ ◦•◦•◦•◦•◦•◦• ⋆⋆⋆ • ⋆ •• ⋆ ◦ ◦•◦•◦•◦ • ⋆ ◦◦1111111 4 28 ◦◦ ⋆ ◦ ⋆⋆ ◦◦ ⋆⋆⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆⋆ ⋆⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆ ◦◦◦◦◦•◦•◦◦◦◦ ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦◦◦◦◦ ◦ ⋆ ◦◦
1111111 5 5 • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 5 10 •• ⋆⋆ • ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 5 15 • ⋆ • ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 5 25 ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆
1111111 6 6 •••◦ ⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ • ⋆ • ⋆ ⋆ •◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆ • ⋆ ⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆1111111 6 12 •••• ⋆ • ⋆ ◦◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ••◦ ⋆ ⋆ ◦◦ ⋆ ◦ ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ • ⋆ • ⋆ ⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆1111111 6 18 ◦••◦ ⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ◦ ⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ ◦ ⋆ • ⋆ ◦ ⋆ ⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆
1111111 7 7 • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 7 14 •• ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆1111111 8 8 •• ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ • ⋆ ⋆ ◦ ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆ • ⋆⋆⋆⋆⋆ ◦• ⋆⋆ ◦◦◦•◦◦◦ ◦ ⋆ ◦◦1111111 8 16 ◦◦ ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ • ⋆ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦• ⋆⋆ ◦◦◦◦◦◦◦ ◦ ⋆ ◦◦1111111 9 9 • ⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦•◦◦ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆1111111 10 10 •• ⋆ ◦◦ ⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ • ⋆ ⋆⋆⋆⋆ • ⋆⋆⋆⋆ • ⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆ • ⋆⋆ ⋆⋆⋆⋆
1111112 2 2 ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦ ⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ◦ ⋆ ••1111112 2 4 ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•• ⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ••1111112 2 6 ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆ •◦• ⋆ ⋆⋆⋆⋆ • ⋆ • ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆ • ••••••• ◦ ⋆ ••1111112 2 8 ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ • ⋆⋆⋆ ◦•• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ••1111112 2 10 ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆ •◦ ⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ◦ ⋆ ••1111112 2 12 ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆ •••◦ ⋆⋆⋆ ◦••◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆ • ••••••• • ⋆ ••1111112 2 14 ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆ •◦ ⋆⋆ ⋆⋆⋆⋆ • ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ◦ ⋆ ••1111112 2 16 ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ••1111112 2 18 ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ •◦◦ ⋆ ⋆⋆ ◦ ⋆ • ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ ◦◦ ⋆ • ••••••• ◦ ⋆ ••1111112 2 20 ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ◦ ⋆⋆ ◦•◦ ⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆⋆ ••••••• • ⋆ ••1111112 2 22 ⋆ ◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••••••••◦• ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ◦ ⋆ ••1111112 2 24 ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ •◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••••• ⋆⋆⋆⋆⋆ •• ⋆ • ••••••• • ⋆ ••1111112 2 26 ⋆ ◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ⋆⋆⋆⋆ ◦ ⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••••••••◦•◦ ⋆⋆⋆⋆⋆ ◦◦ ⋆⋆ ••••••• ◦ ⋆ ••1111112 2 30 ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆ ◦ ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦••◦••◦•◦•◦ ⋆⋆⋆⋆⋆ ◦◦ ⋆ • ◦•••◦•◦ ◦ ⋆ •◦
1111112 4 4 ⋆ • ⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ••• ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦•1111112 4 8 ⋆ • ⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ • ⋆ ◦•1111112 4 12 ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆ •◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ • ⋆ ◦ ⋆⋆⋆⋆⋆ •• ⋆⋆ ◦•◦•◦•◦ ◦ ⋆ ◦•
1111112 6 6 ⋆ • ⋆ ◦ ⋆ • ⋆ ◦ ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ •◦◦ ⋆ ⋆⋆ ◦ ⋆ • ⋆ ◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆⋆⋆⋆⋆ ⋆⋆⋆ • ⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆1111112 8 8 ⋆ ◦ ⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆ • ⋆⋆⋆⋆⋆ ◦• ⋆⋆ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦◦
1111113 3 3 ⋆⋆ • ⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111113 3 6 ⋆⋆ • ⋆⋆ • ⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆⋆⋆ ⋆ •◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111113 3 9 ⋆⋆ • ⋆⋆⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ••••• ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111113 3 12 ⋆⋆ • ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆ ◦ ⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦ ⋆ ⋆ ◦◦ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •••◦• ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ⋆ ◦ ⋆⋆
1111114 4 4 ⋆⋆⋆ • ⋆⋆⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦• ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ •• ⋆⋆ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ • ⋆ ◦◦1111114 4 8 ⋆⋆⋆ ◦ ⋆⋆⋆ • ⋆⋆⋆⋆⋆⋆⋆ ◦ ⋆⋆ ◦◦ ⋆ ◦ ⋆⋆⋆ ◦◦◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ •• ⋆⋆ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦ ⋆ ◦◦
1111122 2 2 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦ ⋆ ◦ ⋆⋆⋆ ◦•◦ ⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ••••••• ◦ ⋆ ••1111122 2 4 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•• ⋆ • ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ••••••• • ⋆ ••1111122 2 6 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦•◦ ⋆⋆⋆ ◦•◦◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ••••••• ◦ ⋆ ••1111122 2 8 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ••••••• • ⋆ ••1111122 2 10 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦ ⋆ ◦ ◦ ⋆⋆ ◦•◦ ⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ••••••• ◦ ⋆ ••1111122 2 12 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •◦◦◦ ⋆⋆⋆ ◦◦◦◦◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ◦•••◦•◦ ◦ ⋆ ••
1111122 4 4 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ •• ⋆ ◦ ⋆⋆⋆ ◦•◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆ • ⋆ • ⋆ • ⋆ ◦•1111122 6 6 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ◦◦◦◦ ⋆⋆⋆ ◦◦◦◦ ⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆ • ⋆⋆ • ⋆ ⋆⋆⋆⋆1111133 3 3 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆ • ⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆ • ⋆⋆1111222 2 2 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆ •◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆ ••1111222 2 4 ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆ •◦ ⋆ ◦ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ ⋆⋆⋆⋆⋆ ⋆⋆⋆⋆ ⋆⋆⋆⋆⋆⋆⋆ ⋆⋆ ••
44


## Page 45

Table A.7
Lower bounds for an and matrices with high extension spectra, 10 ≤ n≤ 19.
n an≥ |Ln− 1| det An− 1 aAn− 1 An− 1
10 259 2 110 257 [7, 39, 5A, 9C, E 1, 149, 174, 193, 1AA]
11 739 6 291 679 [F, 71, B 6, 13A, 1C3, 1DC, 256, 299, 2EC, 325]
12 2107 19 779 1894 [F, 73, 195, 1EA, 2A6, 35C, 4D6, 53E, 565,
6B9, 703]
13 6157 18 2201 5618 [1F, E 3, 17C, 3A5, 649, 6D6, 732, A 6E, AB 8,
B53, C 35, D 8E]
14 19073 40 6731 16821 [3F, 1C7, 2D9, 76A, C 4D, CF 2, F 94, 1575,
168E, 195A, 19A9, 1A64, 1E13]
15 58741 46 23288 53117 [7D, 38F, 5B2, ED 5, 189B, 19E4, 1F 29, 2AEA,
2D1C, 32B4, 3353, 34C9, 3C27, 164E]
16 185693 190 67832 161599 [F D, 71F, BE 3, 1D29, 324F, 36B2, 3995, 5370,
55C6, 5A9A, 61AB, 6C53, 6E24, 27C8, 297E]
17 610187 480 213175 517794 [1F B, E 3E, 17C6, 3A53, 649F, 6D64, 732B,
A6E2, AB 8D, B 535, C 356, D 8A7, DC 49, 4F 91,
72F C, F 99A]
18 2039033 697 709503 1719277 [3F 9, 1C7E, 2D95, 76AC, C 4D2, CF 27, F 949,
15755, 168E5, 195A3, 19A9C, 1A64B, 1E13E,
14D8A, 17A33, 33C6, 1AF 70]
19 6478579 54 2331887 4663774 [7E9, 38F 7, 5F 13, E 95D, 19277, 1B599, 1CCAF,
29B8E, 2AE31, 2D4C5, 30D56, 3629F, 37125,
13E4C, 1EBC 2, 358F 8, 2F 46A, E 7B4]
45
