# Create/Define single dimension / multi-dimension arrays,
# and arrays with specific values like array of all ones, all zeros, array with random values within a range, or a diagonal matrix.

import numpy as np

singleArray = np.array([])

multiArray = np.array([], [])

allOneArray = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

allZeroArray = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

randArray = np.array([])

for x in range(0, 1000):
    temp = np.random.randint(100000)
    print(temp)
    randArray = np.append(randArray, temp)

value = [1, 1, 1, 1, 1, 1, 1, 1, 1]
diagMatrix = np.diag(value)