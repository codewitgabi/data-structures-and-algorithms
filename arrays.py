#!/usr/bin/python

# Arrays

from array import *

arr = array("i", [1, 2, 3, 4, 5])

for i in arr:
	print(i)
	
# Accessing array elements
print("Accessing Elements")
print("arr[0]", arr[0])
print("arr[2]", arr[2])
print("arr[-1]", arr[-1]) # negative indexing

# Insertion Operation
print("Insertion Operation")
arr.insert(1, 6)

for i in arr:
	print(i)

# Deletion Operation
print("Deletion Operation")
arr.remove(5)
arr.remove(1)

for i in arr:
	print(i)

# Search Operation
print("Search Operation")
print(0 in arr)
print(arr.index(4))

# Update Operation
print("Update Operation")
arr[0] = 10
arr[1] = 20

for i in arr:
	print(i)


# Array Methods
print("Array Methods")
print(".count(elem)", arr.count(5)) # returns the amount of occurence of an element in an array
arr.extend([6, 7, 8]) # unpacks an object to the array.
print(arr)
print(".itemsize", arr.itemsize) # returns the amount of byte(s) an element hold in an array
print(".typecode", arr.typecode) # returns the typecode of an array
arr.reverse() # reverses an array
print(arr)