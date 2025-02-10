#!/usr/bin/python

# Lists
list1 = [1, 2, 3, 4]
list2 = ["John", "Amaka", 8]
list3 = [[1, 2, "Jane"], {}, 5, 0]

# Accessing Values
print("list1[0]", list1[0])
print("list2[1]", list2[1])
print("list3[0][2]", list3[0][2])

# Updating Lists
list1[0] = 0
list2[1] = "codewitgabi"
list1.append("Coder")

print(list1)
print(list2)

# Deleting List Elements
del list1[0]
list2.remove(8)

print(list1)
print(list2)