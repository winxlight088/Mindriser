#Task:
# Requirements:
# ask user for 2 numbers
# ask user for the operation(+,-,*,/)
# if user enter + then add two number
# if user enter - then subtract two number
# if user enter * then multiply two number
# if user enter / then divide two number
# else print invalid operation
# optional : you can use f string to print the output
# ask user if they want to rerun the calculator if yes continue the loop and if no exit the loop
#exception handling and print them out

while True:
     try:
         a = int(input("enter first number:"))
         b = int(input("enter second number:"))
         operation = input("enter +,-,*,/ for calulation: ")
         if  operation == '+':
            sum = a + b
                # result = int(sum)
            print(f"sum of {a} and {b} is:")
            print(sum)
                    
         elif operation == '-':
            difference = a - b
            print(f"difference of {a} and {b} is:")
            print(difference)
            
         elif operation == '*':
            product = a * b
            print(f"product of {a} and {b} is:")
            print(product)
         elif operation == '/':
            divide = a / b
            print(f"division of {a} and {b} is:")
            print(divide)
         else:
            print("Invalid choice")
                    
         choice = input("do you want to continue: (Yes/No?) ").capitalize()
         if choice == 'Yes':
             continue
         else:
             break
     except ValueError:
        print("Please enter proper number ") 
     except TypeError:
        print("TYPE ERROR.............")
            
        
        
    
