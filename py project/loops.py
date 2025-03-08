# loop 
# While loop while is use smoll

# x = 2

# while x <= 10:
#     print(x)
#     x +=1

# table = 2

# while table <=20:
#     print(table)
#     table += 2

# 2. Nasted While Loop

"""while condition :
	code//
	while condition :
		code//
		(operator) Assignment
	(operator) Assignment"""

# table = 2
# while table <=5:
#     print("table of : " ,table)
#     mul = 1
#     while mul <=10:
#         print(table,"x",mul , "=", table*mul)
#         mul +=1
#     table +=1    

#Q1 WAP create calculater  with help of input funtions .

fv = int(input("Enter Your first value "))
sv = int(input("Enter Your second value "))
sign = input("Enter Your sign ")

if sign == "+":
    print(fv+sv)
elif sign == "-":
    print(fv-sv)
elif sign == "*":
    print(fv*sv)
elif sign == "/":
    print(fv/sv)
else:
    print("Invalid sign")