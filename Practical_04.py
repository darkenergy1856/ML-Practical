# Create/Define single dimension / multi-dimension arrays,
# and arrays with specific values like array of all ones, all zeros, array with random values within a range, or a diagonal matrix.

import numpy as np

singleArray = np.array([1,3,5])
print("Single Array:\n", singleArray)

multiArray = np.array([ [4,8,1], [1,5,2] ])
print("multiArray:\n", multiArray)

allOneArray = np.array([1, 1, 1, 1, 1, 1])
print("Array of all 1s:\n", allOneArray)

randArray = np.random.rand(3,4)
print("Array of Randoms:\n", randArray)

value = [1,5,3,6,9]
diagMatrix = np.diag(value)
print("Diagoanl Matrix:\n", diagMatrix)
