# Extracted text: Craigen 1990 range paper

Source PDF: ../pdfs/craigen_1990_range_determinant_function_01_matrices.pdf

Pages: 10

## Page 1

The Range of the Determinant Function on the Set of n× n
(0, 1)-Matrices
R. Craigen
Department of Mathematics
University of Manitoba
Winnipeg, Manitoba
CANADA R3T 2N2
craigenr@cc.umanitoba.ca
Appeared in JCMCC, 1990. Pre-pub version
Abstract
As stated in [2], there is a conjecture that the determinant function maps the set of n×n
(0, 1)-matrices onto a set of consecutive integers for any given n. While this is true for n≤ 6, it
is shown to be false for n = 7. In particular there is no 7 × 7 determinant in the range 28 − 31
but there is one equal to 32. Then the more general question of the range of the determinant
function for alln is discussed. A lower bound is given on the largest string of consecutive integers
centered at 0, each of which is a determinant of an n×n (0, 1)-matrix.
1 Introduction
Let us begin with a few conventions:
• Write Υn for the set of n×n (0, 1)-matrices.
• βn = maxMϵΥn|M|.
• Dk(n) is the assertion that there is a matrix in Υ n whose determinant is k. Abusing the
notation somewhat, any such matrix shall be denoted a Dk(n).
Knowing the range of the determinant function on Υ n may be useful, since the existence of a
combinatorial design is equivalent to the existence of the corresponding (0, 1)-incidence matrix, and
hence implies that the corresponding (usually predictable, as in the case of SBIBD’s) determinant
exists when that matrix is square.
Brenner and Cummings ([2], 1972) relate the following conjecture: that for a given n, the
determinant function maps Υ n onto a set of consecutive integers. In my notation, this translates
to “|k|≤ βn implies Dk(n)” for n >1 (since we have Dk(n) if and only if D−k(n) —see lemma
3—and consequently this set is symmetric with respect to 0). Subsequently we refer to this as the
Consecutive Integer Determinant Conjecture.
Brenner says that he had raised the question with Marshall Hall in correspondence before 1972.
He also relates that some time ago he heard someone had a counterexample. In any case I have
not been able to ﬁnd any that appear in print to date.
1

## Page 2

In section 2 we show that the above conjecture is in fact false. In section 3 we discuss some
results on how large a set of consecutive integers k may be obtained satisfying Dk(n). In the last
section we outline some of the relevant unsolved questions, indicating some partial results obtained.
A ﬁnal resolution to some of these questions may lead to a solution of the Hadamard maximum
determinant problem, which is the question as to what is the maximum determinant among ( ±1)-
matrices of a given order ([2], [8]) 1. This is because Dk(n) is equivalent to the existence of a
(±1)-matrix of order n + 1 with determinant 2nk, modulo the following transformation:
2n|D| = |2D|
=
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1 1 ··· 1
0
... 2D
0
⏐⏐⏐⏐⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1 1 ··· 1
−1
... 2D−J
−1
⏐⏐⏐⏐⏐⏐⏐⏐⏐
,
(1)
where D is a Dk(n) [11].2
Let us take note of a nice (well-known) property of rank-one matrices which will prove useful
at several points. If U is rank-one, it is similar to an upper-triangular matrix. The only possible
form for an upper-triangular rank-one matrix with trace equal to that of U is


trU ∗
0
... 0
0

. (2)
Noting that trace is similarity-invariant, immediately we have:
Lemma 1 (the “Rank-one Lemma”) If U is rank-one, then |I +U| = 1 +tr(U).
2 The consecutive integer determinant conjecture is false
We shall see in the next section that the consecutive integer determinant conjecture holds for
n = 1,..., 6. However, that is as far as it goes, as the following result shows:
Theorem 2 There is no Dk(7) for 27<k< 32.
Proof: First note that β6 = 9 (see section 3). This tells us that any matrix whose minors along
a row are in Υ6, and whose entries in this row are from{0,±1}, has determinant less than or equal
1the Hadamard bound, n
n
2 , holds in all orders. A (±1)-matrix achieving this bound is called a Hadamard matrix.
Equivalently, a Hadamard matrix H is one which satisﬁes HH t = nI.
2and using the fact that we can negate rows and columns of a matrix without changing the absolute value of its
determinant.
2

## Page 3

to 9 times the number of non-zero entries in this row. We shall use this observation repeatedly in
the proof.
Now suppose A is a Dk(7) with k> 27. Write r1,..., r7 for the rows of A, ri for∥ri∥, and λi,j
for < ri, rj >, i̸=j. Then proceed as follows: 3
1. For each i, ri≥ 4. This follows from the above observation.
2. Suppose r1 = 7. Then:
A =
r1
r2


1 1 1 1 1 1 1
1 1 1 1 ∗ ∗ ∗
...

∼
(
0 0 0 0 ∗ ∗ ∗
...
)
. (3)
Here∼ denotes equivalence via the action of adding a multiple of one row to another4. Plainly
we have forced|A|≤ 27, which is a contradiction.
We argue similarly for each row, concluding that for each i, ri< 7.
3. Suppose that r2 = r3 = ... = r7 = 4. Then for i,j > 1 we cannot have λi,j = 3 or 4 —else
|A|≤ 18 as in 3. Thus λi,j = 1 or 2.
Now suppose λ2,3 = 1. Then:
r2
r3
( 1 1 1 1 0 0 0
1 0 0 0 1 1 1
)
(4)
and we cannot have λ2,j = 1 for j >3, else then λ3,j = 3 or 4, which, as we have just seen,
cannot happen. Similarly, λ3,j̸= 1, and so we have:
r2
r3
rj


1 1 1 1 0 0 0
1 0 0 0 1 1 1
0 1 1 0 1 1 0

. (5)
Clearly, the ﬁrst column of A must then have at most three nonzero entries. Expanding by
minors along this column, we see that |A|≤ 27, which is a contradiction.
We conclude that if all ri = 4 with at most one exception, then λi,j = 2 when ri =rj = 4.
4. Suppose that r1 = 6. If in addition r2 has a 0 in the same column as the 0 in r1, then:
A =
r1
r2


0 1 1 1 1 1 1
0 1 1 1 1 ∗ ∗
...

∼
(
0 0 0 0 0 ∗ ∗
...
)
(6)
This gives a contradiction as before. Thus, rj must have a 1 in this column for j >1.
It follows in the same manner that rj = 4 for j > 1. Now by step 3, λi,j = 2 for i,j > 1.
LettingB be the submatrix obtained by excluding the ﬁrst row and column ofA, then, this all
3With no loss of generality, we assume at each step that the columns of A are arranged conveniently for display
purposes.
4a determinant-preserving operation.
3

## Page 4

translates to BJ =BtJ = 3J andBBt = 2I +J. Thus BBtJ = 9J = 2IJ +J2 = 8J, which
is a contradiction (thus showing the well-known fact that an SBIBD(6,3,1) cannot exist).
We conclude that for each i, ri< 6.
5. If ri =rj = 5, then λi,j = 3 —for if λi,j = 5 or 4 then |A| = 0 or≤ 18 respectively, as in (3)
and (6). Similarly, if ri = 5 and rj = 4 we cannot then have λi,j = 3 or 4 —else as above,
|A|≤ 27 or 9 respectively. In any case, if ri = 5 then every other row must have 1’s in the
columns corresponding to the 0’s in ri. But then |A| = 0 —a contradiction.
We conclude that ri = 4, all i.
6. Together, steps 3 and 5 tell us that AAt = 2I + 2J.
We now can derive the following using the Rank-one Lemma:
|A| = |AAt|1/2
= |2I + 2J|1/2 (7)
= 2 7/281/2 = 32
We have shown that if AϵΥ7 then either|A|≤ 27 or|A| = 32. The result follows. 2
The existence of a D32(7) may be inferred from the existence of a Hadamard matrix of order 8.
This provides the claimed counterexample.
3 Proliferation of (0, 1)-determinants
Here are some of the best bounds on βn:
n≡ 0 mod4: βn≤ (2n + 1)1/2(n/4)n/2 (Barba, [1].)
n≡ 1 mod4: βn≤n((n− 1)/4)
n−1
2 (Ehlich [6], and Wojtas, [12] ).
Equality holds for n≤ 100 except n = 21, 33, 57, 69, 73, 77, 89, 93, 97 ([13] [3] ).
n≡ 2 mod4: βn≤ (2n + 1)1/2(n/4)n/2 (Barba, [1]).
n≡ 3 mod4: βn≤ 2−n(n + 1)
n+1
2 (this follows from the Hadamard bound and (1)).
This bound is achieved precisely when there exists a Hadamard matrix of order n + 1 (this is
established for many orders≡ 0 mod 4 including all less than 428 [9]).
• There is also the lower bound βn > 2−n(3(n + 1)/4)
n+1
2 for all n (Clements and Lindstrom,
[4]; Schmidt [10] gives a sharper, but less straightforward, lower bound).
• We haveβn = 1, 1, 2, 3, 5, 9, 32, 56, 144, 320, 1458, 3645, 9531 for n = 1, 2,..., 13 ([2], [11], [7]).
n = 14 is apparently the ﬁrst case for which βn is not known.
The following main result for this section is given as one “monster lemma” since the diﬀerent
parts are designed to be used together recursively.
4

## Page 5

Lemma 3 (Monster Determinant Lemma, or MDL)
1. Dk(n) iﬀ D−k(n) for all n> 1
2. For any positive integers a,k and n, Dk(n) implies Dak(n +a)
3. If Dk(n) and Dl(m) then
(a) Dkl(m +n)
(b) Dkmln(mn)
(c) D2mnln+1km+1(mn +m +n)
(d) if the former is r-row-regular5 and the latter has no row sum greater than r (for example,
if it iss-row-regular withs≤r or ifm≤r+1), then there is anr-row-regularDkl(m+n).
4. If there is an r-row-regularDk(n) and an s-row-regularDl(m) then
(a) there is an rs-row-regularDkmln(mn)
(b) there is a (rm +sn− 2rs)-row-regularD2(m−1)(n−1)kmln( n
r−2)m−1( m
s−2)n−1( n
r + m
s−2)(mn)
(c) for 0≤d≤n, 0≤c≤m there is aD kl
rs (rs−cd)(m+n) and aD kl
rs (n(c−s)+m(d−r)+2rs−2cd)(m+
n− 1)
(d) for − min(r,s )≤t≤ min(n−r,m−s), there is an (r+s+t)-row-regularD kl
rst(r+s+t)(m+
n).
5. If there is an ri-row-regularDki(ni) for each i = 1,...,s then
(a) Dk1···ks( a1
r1
+···+ as
rs−1)(n1 +··· +ns) for ai satisfying 0≤ai≤ni
(b) Dk1···ks( n1
r1
+···+ ns
rs−2)(n1 +··· +ns− 1).
6. There is a 1-regularD1(1).
7. If there is an r-row-regular Dk(n) then there is an ( n−r)-row-regularDk( n
r−1)(n)
8. If there is a Hadamard matrix of order n + 1 (for example, any n≡ 3 mod 4 and≤ 407) then
there is an (n + 1)/2-regularD
2( n+1
4 )
n+1
2
(n)
9. If there is a Hadamard matrix of order n and excess6 x then D(n/4)
n
2 (1+x/n)(n).
Proof:
5a matrix R is r-row(respectively column)-regular if RJ = rJ (respectively J R = rJ). A matrix is r-regular if
it is both r-row and r-column-regular. In the lemma we shall disallow 0-row-regularity whenever this would imply
division by 0.
6The excess of a matrix is the sum of its entries. Many such cases may be inferred from results in [5] —for example,
all x≡ 0 mod 4 satisfying |x|≤ max(n, 3n− 8), and all x = 2a√n for|a|≤ n/2 when n is the order of a regular
Hadamard matrix, as is the case for each n where √n is the order of a Hadamard matrix.
5

## Page 6

1. This follows from the fact that interchanging two rows or columns negate a determinant
(henceforth, this fact will be used without reference).
2. Suppose A is a Dk(n). Expanding the following array by minors will verify that it is a
D±ak(n +a): 

0 1 ··· 1 1 0 ··· 0
1
... Ia−1 0
1
v 0 A


(8)
Here v is the ﬁrst column of A.
3. Let A be a Dk(n) and B be a Dl(m). Then
(a) |A ⨁B| =
⏐⏐⏐⏐
A 0
0 B
⏐⏐⏐⏐ =|A||B|.
(b) |A ⨂B| =|A|m|B|n.
(c) using (1), Construct (±1)-matricesA′ of order n + 1 andB′ of order m + 1. Then verify
thatA′ ⨂B′ is a (±1)-matrix of ordermn+m+n+1 with determinant (2nk)m+1(2ml)n+1.
Then (1) implies the existence of the required matrix in Υ mn+m+n.
(d) If the row sums of B are all less than or equal to r, then we can choose C in Υn such
that B +C is r-row-regular, so then
( A 0
C B
)
an r-row-regularDkl(m +n).
4. Now further suppose that A is r-row-regular and B is s-row-regular. then
(a) consider A ⨂B.
(b) apply the Rank-one lemma three times to Jmn−(2A−Jn) N(2B−Jm)
2 .
(c) choose C to be c-row-regular and D to be rank one and d-row-regular. Let X =( A C
D B
)
. Using the Rank-one lemma (with X = Y +
( 0 0
D 0
)
), we get |X| =
kl
rs(rs−cd), which is the ﬁrst determinant. The reader may verify that X−1 = Y−1 +
rs
cd−rsY−1
( 0 0
D 0
)
Y−1. Thus, tr(X−1Jm+n) = n(c−b)+m(d−a)
cd−rs . From this we may use
the Rank-one lemma again to show that 2 X−Jm+n is a (±1)-matrix with determi-
nant 2m+nkl
rs(n(c−s)+m(d−r)
2 +rs−cd), which together with (1) establishes the second
determinant.
(d) Now if − min(r,s )≤t≤ min(n−r,m−s), we can ﬁnd c and d as above with r +c =
s +d =r +s +t. Then X isr +s +t-row-regular and has determinant−kl
rst(r +s +t).
5. Now let X1,...,X s be, respectively,ri-row-regularDki(ni)’s fori = 1,...,s . For compactness,
write Ja
m,n for the m×n matrix whose entries in the ﬁrst a columns are all 1 and the rest of
whose entries are 0. Then take
6

## Page 7

M =


X1 0
...
0 Xs

 and U =


Ja1
n1×n1 ··· Jas
n1×ns
... ...
Ja1
ns×n1 ··· Jas
ns×ns

. (9)
(a) It is easy to verify that
M−1U =


1
r1
Ja1
n1×n1 ··· 1
r1
Jas
n1×ns
... ...
1
rsJa1
ns×n1 ··· 1
rsJas
ns×ns

. (10)
Thustr(M−1U) = a1
r1
+··· + as
rs , and so|M−U| =|M||I−M−1U| =k1...k s(1− (a1
r1
+
··· + as
rs )), by an application of the Rank-one lemma. Negating the appropriate columns
gives a matrix in Υn whose determinant has the same norm.
(b) When ai =ni, all i, then U =J, so tr(M−1J) = n1
r1
+··· + ns
rs . Apply (1) to 2 M−J.
6. This is clear.
7. Now let A be an r-row-regularDk(n). Then J−A is (n−r)-row-regular and the Rank-one
lemma gives|J−A| =±|A||I−A−1J| =±k(1−tr( 1
rJ)) =±k(n
r− 1).
8. this follows directly from the construction in (1), and the fact that the given Hadamard matrix
has determinant (n + 1)
n+1
2 .
9. Apply the Rank-one lemma to J+H
2 , where H is the given Hadamard matrix.
2
The following two theorems are just a simple demonstration of the power of this lemma:
Theorem 4 For each n and 0≤k<n , there is a k-row-regularDk(n).
Proof: Ik+1 is a 1-regular D1(k + 1) ak-regularDk(k + 1) follows by part 7 of MDL. The result
follows by using this matrix together with In−k−1 in part 3d). 2
Theorem 5 If there is an r-row-regularDk(n) then r|k.
Proof: Using this matrix and I1 in part 3d), we get an r-row-regulardk(n + 1). Thus there is a
Dk( n
r−1)(n) and a Dk( n+1
r −1)(n + 1), by part 7. So r|kn and r|k(n + 1) and so r|k. 2
Table 1 compiles the results given by MDL for n≤ 10, comparing them to determinants found
using other methods (“−” indicates an entire range of determinants which are established, the left
endpoint defaulting to 0).
7

## Page 8

Table 1: Determinants found up to order 10 with and without MDL
n MDL implies Dk(n) for k = other determinants found without MDL
1 −1
2 −1
3 −2
4 −3
5 −5
6 −8 9
7 −13, 16, 18, 20, 24, 32 14, 15, 17, 19
8 −18, 20, 24, 28, 32, 40, 48, 56 19, 21− 23, 25− 27, 29− 31, 33− 39, 42, 44, 45
9 −24, 26, 28, 32, 40, 48, 56, 64, 72, 80, 25, 27, 29− 31, 33− 39, 41− 47, 49− 55, 57− 63, 65− 71, 73− 79,
88, 144 89− 102, 104, 105, 108, 110, 112, 116, 120, 125, 128
10 −34, 36, 38− 40, 44, 48, 56, 64, 72, 80, 35, 37, 41− 43, 45− 47, 49− 55, 57− 63, 65− 71, 73− 79, 81− 87,
88, 96, 104, 112, 120, 128, 136, 144 89− 95, 97− 103, 105− 111, 113− 119, 121− 127, 129− 135,
137− 143, 145− 232, 234− 256, 258, 260, 261, 263− 267, 270,
272− 276, 279, 280, 283− 285, 288, 291, 294− 297, 304, 312, 315, 320
4 What next?
With the demise of the consecutive integer determinant conjecture, several related questions are
left wide open:
• What is the range of the determinant function on Υ n in general, and the value of βn in
particular?
• It appears from constructions so far that very strong structure is dictated for matrices of
large determinant in Υn. For example, if a Hadamard matrix of order n + 1 exists, a Dβn(n)
must be an SBIBD(n, n+1
2 , n+1
4 ) (or rather, the (0, 1)-incidence matrix corresponding to it—
however, we shall not distinguish between them here). Now consider a matrix from Υ n of the
form
( 1 ··· 1 0 ··· 0
A B
)
. We can show that it has, up to sign, the same determinant
as
( 1 ··· 1 0 ··· 0
J−A B
)
. If we combine transformations of this type with row and
column permutation and the transpose operation, these together deﬁne an equivalence relation
in Υn with respect to which the absolute value of the determinant is invariant. With this
notion of equivalence it is possible to show that s D1(2) is equivalent to I2, a D2(3) is
equivalent toJ3−I3 (that is, an SBIBD(3, 2, 1)), a D3(4) is equivalent to an SBIBD(4, 3, 2),
or alternately,


0 1 1 1
1 1 0 0
1 0 1 0
1 0 0 1

. Similarly, a D5(5) is equivalent to


1 0 1 1 1
0 1 1 1 1
1 1 1 0 0
1 1 0 1 0
1 1 0 0 1


.
Are there principles which dictate, up to equivalence, the structure of a Dβn(n), or in general
any “large enough” determinant in any given order?
• With what frequency does each determinant occur in each order? Figure 1 compiles results
obtained from a fairly large sample in order 7.
8

## Page 9

Determinant
Frequency
0
529
1
239
2
144
3
46
4
28
5
4
6
4
7
3
8
1
9
1
10
1
Figure 1: Occurrences of determinants of order 7 among a sample of 1000
• With regard to the relationship between row-regularity and determinants, there are a number
of questions. Chief among these is the following: for what triples ( r,n,k ) do there exist an
r-row-regularDk(n)? Some elementary partial results:
– (r,n,k ) must satisfy 0 ≤ r≤ n, k≤ βn, r|k. If r = 0 or n, k = 0; if r = 1, k= 0 or
1;ifr=n-1,k=0orn− 1.
– if r|k and Dp(r + 1) for every factor p in some factorization of k then there is an n for
which (r,n,k ) is such a triple ( this is almost certainly true when the second condition
is replaced with r> 1). In particular, when r≥
√
k we may take n≤ 2k.
– if (r,n,k ) is such a triple and n′>n then (r,n′,k ) is one as well.
• For each n, let β′
n be the largest number such that k≤ β′
n implies Dk(n). In other words,
[−β′
n,β′
n] is the largest possible interval of consecutive integer (0 , 1)-determinants in order n
centered at 0. We have shown that β′
7̸=β7. Can we have β′
n =βn forn> 7? What are some
non-trivial bounds on β′
n? The only upper bound I know so far is βn. A trivial lower bound
from theorem 4 is β′
n≥n− 1. Here is a somewhat better one:
Theorem 6 For all n, β′
n≥⌊ n
2⌋2− 1.
Proof: Writeu =⌊n
2⌋. If m≤u then theorem 4 provides a Dm(n). If u<m ≤u2− 1, we can
writem =s(u− 1) +t, where 1≤s≤u and 1≤t≤u. Now take an s-row-regularDs(u) and In−u
and apply part 5a) of MDL, with a1 =t and a2 =u. This gives us a D1·s( t
s + u
1−1)(u + (n−u)) =
Dm(n). 2
This theorem actually shows that part 2 of MDL is not neccesary for a> 4, since then β′
a>a ,
and so the ﬁrst point of part 3 gives the same result (we note that part 2 is not used to establish
this result).
Acknowledgement
I am indebted to my supervisor, Dr. L. Cummings, for much practical advice in the preparation
of this paper, and to the referees, who updated my references and observed that there is a more
elementary proof of Theorem 5 using the fact that r must be an eigenvalue of the matrix.
9

## Page 10

References
[1] G. Barba. Intorno al teorema di Hadamard sui determinanti a valore massimo. Giorn. Mat.
Battaglini, 71:70–86, 1933.
[2] J. Brenner and L. Cummings. Hadamard’s maximum determinant problem. Amer. Math.
Monthly, 79(6):626–630, 1972.
[3] Theo Chadjipantelis and Stratis Kounias. Supplementary diﬀerence sets andD-optimal designs
for n≡ 2 mod 4. Discrete Math., 57:211–216, 1985.
[4] G. F. Clements and B. Lindstrom. A sequence of ( ±1)-determinants with large values. Proc.
Amer. Math. Soc., 16:548–550, 1965.
[5] R. Craigen. Excess and moderation of Hadamard matrices. to be submitted.
[6] H. Ehlich. Determinantenabsch¨ atzungen f¨ ur bin¨ are matrizen.Math. Zeitschr. , 83:123–132,
1964. (english manuscript available from R. Craigen).
[7] Z. Galil and J. Kiefer. D-optimum weighing designs. Ann. Stat., 8:1293–1306, 1980.
[8] J. Hadamard. Resolution d’une question relative aux determinants. Bull. des Sciences Math. ,
17:240–246, 1893.
[9] Kazue Sawade. A Hadamard matrix of order 268. Graphs and Combinatorics, 1:185–187, 1985.
[10] K. W. Schmidt. Lower bounds for maximal (0 , 1)-determinants. SIAM J. Appl. Math. ,
19(2):440–442, 1970.
[11] J. Williamson. Determinants whose elements are 0 and 1. Amer. Math. Monthly , 53:427–434,
1946.
[12] M. Wojtas. On Hadamard’s inequality for the determinants of order non-divisible by 4. Colloq.
Math., 12:73–83, 1964.
[13] C. H. Yang. On designs of maximal (+1 ,−1)-matrices of order n≡ 2 mod 4. Math. Comp. ,
22:174–180, 1968.
10
