
#TO DO : requirements
# Ask user for any 2 number (type casting ao required)
# Ask user for the operation(+,-,)
#if user enter +operation, then add
# two number and print the result
# if user enter -operation, then subtract two number and print the result

a = input("enter first number:")
# or a = int(input("enter first number:"))

b = input("enter second number:")
# or b = int(input("enter second number:"))
num1 = int(a)
num2 = int(b)
operation = input("enter 1 for add and 2 for subtract: ")

if  operation == '1':
    sum = num1 + num2
    # result = int(sum)
    print(f"sum of {num1} and {num2} is:")
    print(sum)
elif operation == '2':
    difference = num1 - num2
    print(f"difference of {num1} and {num2} is:")
    print(difference)
else:
    print("Invalid number")