#!/usr/bin/python

# Matrix

from numpy import *

arr = array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 9, 9],
	[0, 5, 7]
])

matrix = reshape(arr, (4, 3))

# Accessing Values
print("Accessing Values")

print("matrix[1] =>", matrix[1]) # [4, 5, 6]
print("matrix[1][2] =>", matrix[1]) # 6

# Adding rows
print("Adding rows")

matrix = append(matrix, [
	[0, 1, 1]
], 0)

print("matrix =>", matrix)

# Adding Columns
print("Adding Columns")
matrix = insert(matrix, [3], [ [0], [0], [0], [0], [0] ], 1)

print("matrix =>", matrix)

# Deleting rows
print("Deleting rows")

matrix = delete(matrix, [2], 0)

print("matrix =>", matrix)

# Deleting columns
print("Deleting columns")

matrix = delete(matrix, [2], 1)

print("matrix =>", matrix)

# Update row
print("Update row")

matrix[0] = [1, 1, 1]

print(matrix)

