#task:
# ask user for their name
# ask the number of times they want to display the name
# print the name of user for that number of times

name = str(input("what is your name?: "))
times = int(input("how many times do you want to print your name: "))
num = 0
while num < times :
    print(name)
    num += 1