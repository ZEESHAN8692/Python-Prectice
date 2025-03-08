# Python Dictionaries

# thisdict = {
#   "name": "manoj",
#   "class": "pyhon",
#   "year": 2024
# }
# print(thisdict)

# thisdict = {
#     "name": "manoj",
#     "class": "pyhon",
#     "year": 2024
  
# }
# print(thisdict["name"])
# print(thisdict["class"])
# print(thisdict["year"])

# Duplicates Not Allowed

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# #print(thisdict)

# print(len(thisdict))

# Dictionary Items - Data Types

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict)

# type()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# print(type(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]

# print(x)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.keys()

# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.values()

# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.items()

# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2024

# print(thisdict)


# Update Dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# print(thisdict)

# Python - Add Dictionary Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# Python - Remove Dictionary Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


