# Perform other matrix operations like converting matrix data to absolute values, taking the
# negative of matrix values, additing/removing rows/columns from a matrix, finding the maximum 
# or minimum values in a matrix or in a row/column, and finding the sum of some/all
# elements in a matrix

import numpy as np

A = np.array([[-1, -2], [3, -4]])

B = np.abs(A)
print("Absolute value of A:\n",B)

C = -A
print("Negative of A:\n",C)

D = np.append(A, [[5, 6]], axis=0)
print("Adding row to A:\n",D)

E = np.delete(A, 1, axis=1)
print("Deliting second column from A:\n",E)

F = np.max(A)
print("maximum value in A: ",F)

G = np.min(A, axis=1)
print("minimum value in each row",G)

H = np.sum(A)
print("sum of all elements in A: ", H)

I = np.sum(A[0])
print("sum of elements in the first row of A: ",I)
