#!/usr/bin/python

# 2D-Array

arr2D = [
	[1, 2],
	[5, 6, "a"],
	[12]
]

# Accessing Values
print("Accessing Values")
print("arr2D[0] =>", arr2D[0]) # [1, 2]
print("arr2D[1][2] =>", arr2D[1][2]) # 'a'

for i in arr2D:
	for j in i:
		print(j, end=" ")
	print()


# Inserting Elements
print("Inserting Elements")
arr2D.insert(1, [0, 9, 7, 4, 0])


# Updating Elements
print("Updating Elements")
arr2D[0] = [6, 7, 8, 9]

print("arr2D[0] =>", arr2D[0]) # [6, 7, 8, 9]

# Deleting Elements
print("Deleting Elements")

del arr2D[0]

arr2D.remove([12])

print("arr2D[0] =>", arr2D[0]) # [0, 9, 7, 4, 0]

for i in arr2D:
	for j in i:
		print(j, end=" ")
	print()

