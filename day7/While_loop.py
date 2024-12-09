#while loop - Muti lined statement
#check the condition and execute block if the condition is true
#if the condition is true and dosent change then it will run infinetly
#

a = 5
b = 0

while a > b:
    print("A is greater than B")
    b += 1 # b = b+1
    break

print("End of while loop")
#break -terminate the loop and execute the nxt line of code
#continue - goes back to while Loop 