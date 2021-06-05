import numpy as np
import time

start = time.time()
ITERATION_LIMIT = 1500

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])
# prints the system
#print("System:")
#for i in range(A.shape[0]):
 #   row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
  #  print(" + ".join(row), "=", b[i])
#print()
iter = 0
x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        iter += 1
        #print("Iteration {0}: {1}".format(it_count, x))
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x = x_new
print("Iterations:", iter)
#print("A =", A)
#print("B =", b)
print("Solution with method Jacobi:")
print(x)
end = time.time()
print("Run time program: ", end - start)
