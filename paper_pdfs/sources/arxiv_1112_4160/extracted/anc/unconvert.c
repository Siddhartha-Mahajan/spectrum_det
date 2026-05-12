/* unconvert Richard's compact matrix format to classical notation (PZ);
   modified RPB to allow comments (preceded by a blank) at end of line
   and to align columns of output (assuming width at most 2). 
   Was giving wrong sign of entries in case n=1 mod 4, fixed 20100627, RPB. 
   Assumes n odd. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main()
{
  char line[1024], *nptr, *endptr[1];
  long n;
  int **M, i, j, len, k = 0;
  int code[8] = {1, -3, 5, -7, 9, -11, 13, -15};

  while (fgets (line, 1024, stdin) != NULL)
    {
      n = strtol (nptr = line, endptr, 10);
      M = (int**) malloc (n * sizeof (int*));
      for (i = 0; i < n; i++)
        M[i] = (int*) malloc (n * sizeof (int));
      for (i = 0; i < n; i++)
        M[i][i] = n;
      nptr = *endptr;
      /* skip blank */
      nptr ++;
      /* skip determinant */
      while (*nptr != ' ')
        nptr ++;
      /* skip blank */
      nptr ++;
      len = strlen (line);
      *endptr = line + len - 1;
      i = 1;
      j = 0;
      while (i < n)
        {
          if ((*nptr != ' ') && (nptr < *endptr))
            k = *nptr++ - 'A';
          if (k > 8)
            {
              fprintf (stderr, "Error, too few precomputed elements\n");
              exit (1);
            }
          M[i][j] = ((n & 3) == 1) ? code[k] : -code[k];
          M[j][i] = M[i][j];
          if (++j == i)
            {
              i++;
              j = 0;
            }
        }
      /* print matrix */
      for (i = 0; i < n; i++)
        {
          printf ("[");
          for (j = 0; j < n; j++)
            {
              printf ("%2d", M[i][j]);
              if (j < n - 1)
                printf (",");
            }
          if (i < n - 1)
            printf ("],\n");
          else
            printf ("]\n");
        }
      printf ("\n");
      for (i = 0; i < n; i++)
        free (M[i]);
      free (M);
    }
  return 0;
}
