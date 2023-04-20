# Use command to compute the size of a matrix, size/length of a particular row/column, load 
# data from a text file, store matrix data to a text file, finding out variables and their features in the
# current scope

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)

size = matrix.size
print("Size of matrix: ", size)

row_size = matrix.shape[0]
print("Size of first row: ", row_size)

col_size = matrix.shape[1]
print("Size of second column: ", col_size)

# data = np.loadtxt("data.txt")
# np.savetxt("matrix.txt", matrix)

vars = dir()
print("All variables and functions in the scope: ")
for var in vars:
    print("\t",var, type(eval(var)))
