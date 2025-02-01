# def Hello():
#     print ('This is a function')
# Hello()


# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Zeeshan", "Khan")




# If the number of arguments is unknown, add a * before the parameter name:


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# If the number of keyword arguments is unknown, add a double ** before the parameter name:


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")