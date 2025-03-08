# Python Tuples 

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
# print(type(mytuple))


# Allow Duplicates

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Tuple Length

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Create Tuple With One Item

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple

# thistuple = ("apple")
# print(type(thistuple))

# Tuple Items - Data Types

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# tuple1 = ("abc", 34, True, 40, "male")

#type()

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))


# The tuple() Constructor

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Python - Access Tuple Items

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# Change Tuple Values


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# Add Items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# set in python

# myset = {"apple", "banana", "cherry"}
# print(myset)
# print(type(myset))

# Duplicates Not Allowed

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)

#add

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# update

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

#Python - Remove Set Items

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)




# Step 1: Write to the file

# with open("example.txt", "w") as file:
#     file.write("This is a line of text.\n")
#     file.write("This is another line of text.")


    # Step 2: Read the file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File content after writing:")
#     print(content)


    # Step 3: Append to the file
# with open("example.txt", "a") as file:
#     file.write("\nThis is an appended line of text.")

def zeshan ():
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nFile content after appending:")
        print(content)

zeshan()