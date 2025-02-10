#!/usr/bin/python

# Maps
from collections import ChainMap

dict1 = {"day1": "Mon", "day2": "Sun"}
dict2 = {"day3": "Sat"}

data = ChainMap(dict1, dict2)

map = data.maps

print(list(data.keys())) # get all keys
print(list(data.values())) # get all values
print(list(data.items())) # get all items

# Update maps

data["day4"] = "Tue"

print(data.maps)

