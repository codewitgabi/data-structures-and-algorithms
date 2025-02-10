#!/usr/bin/python

# Sets

# Creating Sets

set1 = set([1, 2, 3, 4])
set2 = {1, 2, 3, 4}

print("set1 =>", set1)
print("set2 =>", set2)

# Accessing Values

print("Accessing Values")
for val in set1:
	print(val)

# Adding values

print("Adding values")
set2.add(8)
set2.add(0)

print("set2 =>", set2)


# Removing items

print("Removing items")
set1.remove(1) # throws an error if item does not exist
set1.discard(0) # better for removing items

print("set1 =>", set1)

# Union of sets

print("Union of sets")
set3 = set1.union(set2)
set4 = set1 | set2

print("set3 =>", set3)
print("set4 =>", set4)

# Intersection of sets

print("Intersection of sets")

set5 = set1.intersection(set2)
set6 = set1 & set2

print("set5 =>", set5)
print("set6 =>", set6)

# Difference of sets
print("Difference of sets")

set7 = set1.difference(set2)
set8 = set1 - set2

print("set7 =>", set7)
print("set8 =>", set8)

# Set comparison
print("Set comparison")

set9 = set1.issuperset(set2)
set0 = set1.issubset(set2)

print("set9 =>", set9)
print("set0 =>", set0)

set9 = set1 >= set2
set0 = set1 <= set2

print("set9 =>", set9)
print("set0 =>", set0)

