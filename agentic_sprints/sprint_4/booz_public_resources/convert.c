/* Converts .txt file containing n by n integer matrix into compressed format.
   This version removes redundant characters at the end
   of each line and uses the characters 'A', 'B', etc to matrix entries
   (see comments in procedure compress).
   
   First edit the file to remove all characters that are not decimal digits
   or "-", " ", crlf. This can be done using the program extract,
   e.g.  cat data-file | ./extract | ./convert n > output-file
   or the program extract.c.
   
   If a second command-line argument is present, 
   e.g. cat data-file | ./extract | ./convert n 1 > output-file
   then the output is put in lexmax format (or close to it anyway - it does
   not always work because not always possible using just transpositions that
   increase the objective function - see Will's email of 20090906).
   
   The determinant is computed using type long double (64-bit fraction),
   hence may be inaccurate for n > 36 (approx).
   
   RPB, 20090719..20101019
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#ifndef NMAX
#define NMAX 100
#endif

long double fastdetl (int *g, int n, int nmax, long double delta)

/* g[nmax][nmax] + delta.I contains principal submatrix G of size n by n, 
   n <= nmax.  G assumed to have small integer entries and to be symmetric
   positive definite.  Only the diagonal and lower triangle of G is used,
   since assumed that G = G^t.
   
   fastdet returns det(G) using Cholesky factorization without square roots,
   i.e. via the factorization G = L.D.L^t where L is lower triangular with
   unit diagonal, and D is diagonal with positive diagonal elements.  For
   efficiency we also store V = L.D and DR = D^{-1}.
   
   Assumes 0 < n <= nmax, n <= NMAX.
   
   RPB, 20090717..20090724
*/
   
  {
  int i, j, k;
  long double zero = (long double)0.0;
  long double one  = (long double)1.0;
  long double det, s;
  long double dr[NMAX];
  long double l[NMAX][NMAX], v[NMAX][NMAX];
  
  det = one;
  for (j = 0; j < n; j++)
    {
    for (s = zero, k = 0; k < j; k++)
      s += l[j][k]*v[j][k];
    s = ((long double)g[nmax*j+j]+delta) - s; /* g[j][j] + delta - s */
    if (s == zero)
      return s;				 /* Should never occur */  
    dr[j] = one/s;			 /* Store reciprocal (positive) */
    det *= s;  				 /* Update determinant */
    for (i = j+1; i < n; i++)
      {
      for (s = zero, k = 0; k < j; k++)
        s += l[i][k]*v[j][k];
      s = (long double)g[nmax*i+j] - s;	/* g[i][j] - s */
      v[i][j] = s;
      l[i][j] = s*dr[j];  
      }
    }
  return det;				 /* Normal return */
  }

long double scaledsqrtdetl (int *g, int n, int nmax)

/* Returns sqrt(|det(g)|)/2^{n-1}. If rounded to the nearest integer, this seems to give
   the exact result for n <= 29, but would not always do so for larger n. In that case we
   would have to use modular arithmetic or information about known divisors of the result. */

  {
  return sqrt(fabs(fastdetl ((int *)g, n, nmax, (long double)0.0)))/
    (long double)ldexp(1.0,n-1);
  }

char compress (int n, int x)
 
 /* Maps integer x to a character in {A, B, ... } with rule depending on n:
 
    If n = 1 mod 4, (+1, -3, +5, -7, ... ) -> (A, B, C, D, ...);
    if n = 3 mod 4, (-1, +3, -5, +7, ... ) -> (A, B, C, D, ...);
    if n = 0 mod 2, ( 0, -2, +2, -4, ... ) -> (A, B, C, D, ...). */ 

  {
  if (n&1)
    return (char)(abs(x)/2 + (int)'A');		/* n odd */
  else
    return (char)(abs(x) - (x<0) + (int)'A');  	/* n even */
  }
  
int expand (int n, char c)

/* Reverses the effect of compress, so expand(n, compress(n, x)) = x. */

  {
  int s;
  s = (int)(c - 'A');				/* translate to s in {0, 1, 2, ... } */
  if (n&1)
    return (1 - (2&((s<<1)^n)))*(2*s+1);	/* n odd, return +-(2*s+1) */
  else  
    return (1-2*(s&1))*s - (s&1);  		/* n even, return s or -(s+1) */
  }  
  
int lexcomp (int n, int *a, int *b)

// returns -1 if a < b, 0 if a == b, +1 if a > b in the lex ordering
// of rows in the lower triangle.  Assumes that a and b are symmetric
// n by n matrices with equal diagonals.
// Only uses lower triangles of a and b.

  {
  int i, j, u, v;
  for (j = 0; j < n; j++)
    for (i = j+1; i < n; i++)
      {
      u = abs(a[NMAX*i+j]);
      v = abs(b[NMAX*i+j]);
      if (u < v)
        return -1;
      if (u > v)
        return 1;
      }     
  return 0;
  }
  
void swap (int n, int p, int q, int *b)

// Swaps rows p and q of b, assuming b is symmetric with constant diagonal
// Only uses lower triangle of b.

  {
  int j, t;
  if ((p == q) || (p < 0) || (q < 0) || (p >= n) || (q >= n))
    return;
  if (p > q)
    {
    t = p;
    p = q;
    q = t;
    }  
  for (j = 0; j < p; j++)		// Now 0 <= p < q < n
     {
     t = b[NMAX*p+j];
     b[NMAX*p+j] = b[NMAX*q+j];
     b[NMAX*q+j] = t;
     }
  for (j++; j < q; j++)
     {
     t = b[NMAX*j+p];
     b[NMAX*j+p] = b[NMAX*q+j];
     b[NMAX*q+j] = t;        
     }  
  for (j++; j < n; j++)
     {
     t = b[NMAX*j+p];
     b[NMAX*j+p] = b[NMAX*j+q];
     b[NMAX*j+q] = t;        
     }  
   }      
  
int lexmax (int n, int *a)

// Returns 1 if a might be lex-max, 0 if definitely not
// Looks at all possible ways to swap two rows (and corresponding cols).

  {
  int i, j, p, q;
  int b[NMAX*NMAX];
  if (n > NMAX)
    {
    printf ("Increase NMAX to %d in lexmax\n", n);
    exit (33);
    }
  for (i = 0; i < n; i++)
    for (j = 0; j < i; j++)
      b[NMAX*i+j] = a[NMAX*i+j];		// Copy b := a
  for (q = 0; q < n; q++)
    {
    for (p = 0; p < q; p++)
      {
      swap (n, p, q, b);			// Swap rows & cols p, q
      if (lexcomp (n, a, b) < 0)
        return 0;
      swap (n, p, q, b);  			// Restore rows & cols p, q
      }
    }      
  return 1;    
  }    

int lexmaxify (int n, int *a)

// Does row/col swaps to try to put a in lexmax form.
// Returns 1 if a not changed, 0 if changed.
// Assumes a declared int[NMAX][NMAX].
// Does not always succeed (see Will's 5x5 counterexample) but OK
// most of the time.
// RPB, 20090906

  {
  int i, j, p, q, res, retry;
  int b[NMAX*NMAX];
  if (n > NMAX)
    {
    printf ("Increase NMAX to %d in lexmaxify\n", n);
    exit (34);
    }
  res = 1;  
  for (i = 0; i < n; i++)
    for (j = 0; j < i; j++)
      b[NMAX*i+j] = a[NMAX*i+j];		// Copy b := a

  for (retry = 1; retry;)			// Loop until no change
    {
    retry = 0;
    for (q = 0; q < n; q++)
      {
      for (p = 0; p < q; p++)
        {
        swap (n, p, q, b);			// Swap rows & cols p, q of b
        if (lexcomp (n, a, b) < 0)
          {
          res = 0;
          retry = 1;
          swap (n, p, q, a);			// So now a == b
          swap (n, p, q, b);  			// Restore b
          }
        swap (n, p, q, b);  			// Restore b (maybe again)
        }
      }      
    }
  return res;    
  }    

int main (int argc, char *argv[])

  {
  long double dd;
  int done, i, j, k, kk, kt, last, n, x=0;
  int g[NMAX][NMAX];			/* A symmetric positive definite input matrix */

  argc--;
  if (argc < 1)
    {
    fprintf (stderr, "Usage: ./convert n [lexmaxify] < input.txt > output.txt \n");
    return 1;
    }

  n = atoi(argv[1]);

  if (n > NMAX)
    {
    printf ("Increase NMAX to %d\n", n);
    return 1;
    }

  done = 0;
  for (k = 1; !done; k++)
    {
    for (i = 0; i < n; i++)
      for (j = 0; j < n; j++)
        g[i][j] = 0;
    for (i = 0; i < n; i++)
      g[i][i] = n;
          
    for (i = 0; !done && (i < n); i++)
      {
      for (j = 0; !done && (j < n); j++)
        {
        done = (scanf ("%d", &x) == EOF);
        if (done && ((i > 0) || (j > 0)))
          {
          fprintf (stderr, "Input matrix %d is incomplete\n", k);
          exit (1);
          }
        if (!done)
          g[i][j] = x;
        }
      }

    for (i = 0; i < n; i++)
      {
      if (g[i][i] != n)
        {
        fprintf (stderr, "Data error for matrix %d, g[%d][%d] = %d != %d\n", 
          k, i, i, g[i][i], n);
        exit (2);
        }
      for (j = 0; j < i; j++)
        {
        if (g[i][j] != g[j][i])
          {
          fprintf (stderr, "Data error for matrix %d, g[%d][%d] = %d != g[%d][%d] = %d\n", 
                   k, i, j, g[i][j], j, i, g[j][i]);
          exit (3);
          }
        if ((g[i][j] >= n) || (g[i][j] <= -n))
          {
          fprintf (stderr,  "Data error for matrix %d, g[%d][%d] = %d should be in [%d, %d] \n", 
                   k, i, j, g[i][j], 1-n, n-1);
          exit (4);
          }
        }    
      }

    if (!done)      
      {
      if (argc > 1)
        lexmaxify (n, (int *)g);
      
      dd = scaledsqrtdetl ((int *)g, n, NMAX);
      
  /* Note that the det value printed may be inaccurate for n > 29, due to rounding
     errors.  */
          
      printf ("%d %1.0Lf ", n, dd);
      kk = kt = 0;
      last = 0;
      for (i = 0; i < n; i++)
        for (j = 0; j < i; j++)
          {
          kk++;
          if (g[i][j] != last)
            {
            last = g[i][j];
            kt = kk;
            }
          } 
      if (kt == 0) kt = 1;     
      kk = 0;
      for (i = 0; i < n; i++)
        for (j = 0; j < i; j++)
          {
          kk++;
          if (kk <= kt)
            printf ("%c", compress(n, g[i][j]));
          }
      printf ("\n");    
      }
    }

  return 0;  
  }
