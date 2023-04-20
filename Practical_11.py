#  Perform vectorized implementation of simple matrix operation like finding the transpose of a
# matrix, adding, subtracting or multiplying two matrices.

import numpy as np

A = np.array([[1, 2], [3, 4]]) 
B = np.array([[5, 6], [7, 8]]) 

print("A:")
print(A)
print("B:")
print(B)

A_T = A.T 
B_T = B.T 

print("A_T:")
print(A_T)
print("B_T:")
print(B_T)

C = A + B 
print("C:")
print(C)

D = A - B 
print("D:")
print(D)

E = A @ B
print("E:")
print(E)
