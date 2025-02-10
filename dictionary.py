#!/usr/bin/python

# Dictionary
my_dict = {
	"name": "codewitgabi",
	"age": 12,
	"stack": [
		"Python",
		"JavaScript",
		"HTML",
		"React",
		"Postgres"
	]
}

print("my_dict['name']", my_dict["name"])
print("my_dict['stack']", my_dict["stack"])

# Update Dictionary
print("Updating Dictionary")

my_dict["name"] = "Michael"
my_dict["experience"] = "1 year+"

my_dict.update({"a": 1, "b": 2})

# Merge Dictionaries

print({"name": "name"} | {"age": "age"})

print(my_dict)

# Delete Dictionary
print("Deleting Dictionary")
del my_dict["experience"]

# my_dict.clear() # delete all keys from the dictionary

print(my_dict)

# Traversing a dictionary
for i in my_dict:
	print(i) # print the keys

for i in my_dict.values():
	print(i) # print the valuee

for key, val in my_dict.items():
	print(key, val) # print the key and corresponding value

