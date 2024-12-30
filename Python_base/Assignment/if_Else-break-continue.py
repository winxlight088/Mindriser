# Task:
   # ask user for their age
age = int(input("Enter your age:"))
   # if user is 18 or older than 18,
if age >= 18: 
   # show that they can get the drivers license
   print("You can get a driver's license")
   # ask user if they have their their own vechile .
   car = input("do you own a car? (yes/no): ")
   if car =='yes':
       print("Drive safe")
   # if yes print drive safe, if not print get a vechile.
   elif car == 'no':
       print("you should buy a car")
   else :
       print("please enter only yes or no: ")
elif age < 18 :
    print("you must be above 18 to get driver's license")

   
   #if user is not 16, show that they can't get the license yet.