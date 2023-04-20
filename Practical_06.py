# Perform basic operations on matrices (like addition, subtraction, multiplication) and display
# specific rows or columns of the matrix.

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n",A)
print("Matrix B:\n",B)

print("First row of A:\n",A[0]) # The first row of A
print("Second column of B:\n",B[:,1]) # The second column of B

C = A + B # Matrix addition
D = A - B # Matrix subtraction
E = A * B # Matrix multiplication

print("sum of A and B:\n",C)
print("difference of A and B:\n",D)
print("product of A and B:\n",E)
