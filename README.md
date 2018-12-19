# Learn dot or inner product math
This is a quick program to practice the math behind dot and inner products with
a simple user interface. 

## Screenshot 

[Opening Screen](sc.png)
## How To Run
      python learn_inner.py

## Inner Product
If you take the inner product, C, of two matrices A and B, then cols_A = cols_B
so that each vector in this dot product will be the same size:


    C[i, j] = sum(A[i, :] * B[j, :])


## Dot Product
Likewise, if you take the dot product, C, of two matrices A and B, then 
cols_A = rows_B so that each vector in this dot product will be the same size:

    C[i, j] = sum(A[i, :] * B[:, j])


This post was inspired by a comment over on stackoverflow:
- [StackoverFlow](https://stackoverflow.com/questions/11033573/difference-between-numpy-dot-and-inner)


Feel free to reproduce this as you like.

