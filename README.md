# Project Description
**30 days of DSA-python** covers some very important concepts in Data Structures and Algorithms. Begin your journey of *DSA* today to understand how to get things done with it.

## Arrays
Array is a container which can hold a fixed number of items and these items should be of the same type.

** Important Terms **
* Element: Each item stored in an Array
* Index: Each location of an element in an array has a numerical value used to identify the element.

Array is created in python by importing array module and declared as shown below

```
from array import *
arr = array(typecode, [initializers])
```

Some of the available typecodes are as follows;
* b: Represents signed integer of size 1 byte
* B: Represents unsigned integer of size 1 byte
* c: Represents character of size 1 byte
* i: Represents signed integer of size 2 bytes
* I: Represents unsigned of size 2 bytes
* f: Represents floating point of size 4 bytes
* d: Represents floating point of size 8 bytes

### Accessing Array Elements
We can access each element of an array using the index of that element

### Insertion Operation
Insertion operation is to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end or any given index of array.

```
from array import array

arr = array("i", [5, 10, 15, 20])
arr.insert(12, 0)

print(arr) # 12, 5, 10, 15, 20
```

### Deletion Operation
Deletion refers to removing an existing element from an array and reorganizing all elements from an array.

```
from array import array

arr = array("i", [5, 10, 15, 20])
arr.remove(10)
del arr[2]

for elem in arr:
    print(elem)

# output -> 5, 15
```

### Search Operation
You can perform a search for an array element based on its value or index.

```
from array import array

arr = array("i", [5, 10, 15, 20])

print(10 in arr) # True
print(arr.index(15)) # 2
```

### Update Operation
Elements in an array can be modified after creation.

```
from array import array

arr = array("i", [2, 4, 6, 8, 10])

arr[3] = 0

for elem in arr:
    print(elem)
  
# output -> 2, 4, 6, 0, 10
```

## Lists
The list is most versatile data type available in Python, which can be written as a list of comma-separated values between square brackets. The most important thing about a list is that elements need not be of the same datatype.

```
# example
list1 = ["Physics", "Chemistry", "Maths"]
list2 = [1, 2, 3, "a", "b"]
```

Similar to string indices, list indices start from 0 and can be sliced, concatenated and so on.

### Accessing Values
To access elements in a list, use the square bracket for slicing and the index or indices to obtain value available at that index.

```
list1 = [1, 2, 3, 4, 5]

print(list1[3]) # 4
print(list1[-1]) # 5
print(list1[:3]) # [1, 2, 3]
```

### Updating List Elements
You can update single or multiple elements of list by giving the slice on the left hand side of the assignment operator and you can add to the list using the .append() method.

```
list1 = [1, 2, "a", { "a": 3 }, 4]

list1[1] = 10
list1[-1] = 3
list1.append(6)

print(list1) # [1, 10, "a", { "a": 3 }, 3, 6]
```

### Deleting List Elements
To remove an element from a list, you can use the `del` keyword or .remove() method.

```
list1 = [1, 2, "a", { "a": 3 }, 4]

del list1[-2]
list1.remove(2)

print(list1) # [1, "a", 4]
```

### Basic List Operations
```
print(len("a", "b", 3)) # 3
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print(["a"] * 5) # ["a", "a", "a", "a", "a"]
print(5 in [3, 5, 8]) # True
for i in [1, 2, 3]: print(i) # 1, 2, 3
```

## Tuples
A tuple is a sequence of immutable Python objects, just like lists. The differences between tuples and list are that elements of a list can be modified while that of a tuple cannot; Lists use [] while tuples use () or comma-separated values without ().

```
tup1 = (1, 2, 3)
tup2 = "a", "b", 6
tup3 = 5,

# both tup1, tup2 and tup3 all valid tuples.
```

### Accesing Values
Just like lists and arrays, elements in a tuple can be accessed by using the index.

```
tup = (1, 2, 3, 4, 5)

print("tup[2]", tup[2]) # 3
```

### Updating Values
Recall; elements in a tuple cannot be modified, which is why it is called `immutable`.

```
tup = (1, 2, 3)

tup[0] = 10 # error
```

### Deleting Elements
Tuples do not support item modification and deleting elements is an example of item modification.

### Basic Operations
Tuples work like lists so therefore they perform similar operations

```
print(len((1, 2, 3))) # 3
print((1, 2, 3) + (4, 5, 6)) # (1, 2, 3, 4, 5, 6)
print(("Hi",) * 4) # ("Hi", "Hi", "Hi", "Hi")
print(3 in (1, 2, 3)) # True
for i in (1, 2, 3): print(i) # 1, 2, 3
```

## Dictionaries
A dictionary is a data structure that holds data in key-value pair,just like the standard English dictionary. It does not allow duplicate keys and values can be nested or straight.

### Accessing Values
To access values in a dictionary, the dictionary object is called and references the key like an array index.
```
d = {"a": 1, "b": 2, "c": 3}

print(d["a"]) # 1
print(d["c"]) # 3
```

### Updating Dictionary
A dictionary canbe updated using various methods.

```
d = {"a": 1, "b": 2, "c": 3}

d["b"] = 5
d["d"] = 6

print(d) # {"a": 1, "b": 5, "c": 3, "d": 6}

d.update({"e": 0})
```

### Deleting Elements
Keys can be deleted by using the del statement or the .clear() method of a dictionary.

```
d = {"a": 1, "b": 2, "c": 3}

del d["a"]

print(d) # {"b": 2, "c": 3}

d.clear()

print(d) # {}
```

## 2D-Array
A two dimensional(2D) array is simply an array in an array. It must be in this format => [[]]. __[[], 2]__ is not a valid 2D-Array.

### Accessing Elements
Elements in a 2D-Array can be accessed by using the index of the elements just like regular arrays. 

```
arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

print(arr[0]) # [1, 2]
# Since arr[0] returns an array, we can also get an element bu indexing it.

print(arr[0][1]) # 2
```

### Inserting Elements
Elements can be inserted using the .insert() method.

```
arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

arr.insert(2, [0] * 3)
print(arr[2]) # [0, 0, 0]
```

### Updating 2D-Array
Updating a 2D-Array is done same way a regular array is done.

```
arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

arr[0] = [1, 6, 8, 0]

print(arr[0]) # [1, 6, 8, 0]
```

### Deleting Elements
Similarly, elements can be deleted same way it is done in a regular array; by using the del statement or .remove() method.

```
arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

del arr[2]
arr.remove([1, 2])

print(arr) # [[ 3, 4, 5 ]]
```
