import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
import time

start = time.time()
#  Define a system of linear equations. A  is the coefficient matrix and b is the vector of knowns
#  We are using the same matrix as above
A = np.array( [[2, -1, 0],[-1, 2, -1.], [0, -1, 2.]])
b = np.array([20, 14, 3, 9]); b.shape = (4, 1)

#  Do the matrix factorization.  In our case, the permutation matrix P is the identity
P, L, U = lu(A)

print('The L matrix is:')
print(L)
print()
print('The U matrix is:')
print(U)

end = time.time()
print("Run time program: ", end - start)