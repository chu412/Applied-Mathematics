import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
import time

start = time.time()
def forward_substitution(L, b):
    #Get number of rows
    n = L.shape[0]
    #Allocating space for the solution vector
    y = np.zeros_like(b, dtype=np.double);
    #Here we perform the forward-substitution.  
    #Initializing  with the first row.
    y[0] = b[0] / L[0, 0]
    #Looping over rows in reverse (from the bottom  up),
    #starting with the second to last row, because  the 
    #last row solve was completed in the last step.
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]  
    return y

def back_substitution(U, y):
    #Number of rows
    n = U.shape[0]
    #Allocating space for the solution vector
    x = np.zeros_like(y, dtype=np.double);
    #Here we perform the back-substitution.  
    #Initializing with the last row.
    x[-1] = y[-1] / U[-1, -1]
    #Looping over rows in reverse (from the bottom up), 
    #starting with the second to last row, because the 
    #last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

def plu_solve(A, b):
    P, L, U = lu(A)
    y = forward_substitution(L, P@ b)
    return back_substitution(U, y)
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])
print("Result: ")
print(plu_solve(A, b))
end = time.time()
print("Run time program: ", end - start)
#[ 0.19354839,  0.20843672, -0.0471464 ]
