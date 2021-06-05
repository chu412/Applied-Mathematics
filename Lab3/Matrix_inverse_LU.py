import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
from time import time

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

def plu_inverse(A):
    n = A.shape[0]
    b = np.eye(n)
    Ainv = np.zeros((n, n))
    P, L, U = lu(A)
    for i in range(n):
        y = forward_substitution(L, np.dot(P, b[i, :]))
        Ainv[i, :] = back_substitution(U, y)
    return Ainv
A = np.array([[2, -1, 0],[-1, 2, -1.], [0, -1, 2.]])
print("Matrix inverse is:")
print(plu_inverse(A))
#[[0.75, 0.5 , 0.25],
# [0.5 , 1.  , 0.5 ],
# [0.25, 0.5 , 0.75]]