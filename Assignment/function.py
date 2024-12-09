# Task
# make dictionary for user data (eg: {"dia":"123","ram":"987"})
user = {'dia':'123','ram':'987'}
# make another dictionary where you have username as key and amount as value(eg:{"ram":10000})
balance = {'ram':10000, 'dia':30000}
# def balance(username, amount):
# ask user to login by asking username and password
try:
    name = input("Enter your username: ")
    passw = input("Enter your password: ")
    # if user is valid user then ask his/her for three optioins:check balance, add balance, withdraw balance
    if name in user and user[name]==passw:
        print("welcome")
        
        inquiry = input(f"if u want to check balance: press 1, Add balance: press 2,  withdraw balance: press 3: ")  
        # check -print amount of user
        if inquiry == "1":
            print(f"your balance: {balance[name]}")
        # add  - ask amount they want to add, add the given amt with the entered amount and print the amount
        elif inquiry == "2":
            add = int(input("How much do you want to add: "))
            balance[name]+=add
            print(f"You now have balance {balance[name]}")
        # redeem - ask the amount to withdraw then subtract the amount
        # with balance and print it but if withdraw amount is greater than balance then print insufficient balance
        elif inquiry =="3":
            while True:
                withdraw = int(input("enter the amount you want to withdraw:"))
                if withdraw > balance[name]:
                    print("Insufficient balance")
                    continue
                else:
                    balance[name]-= withdraw
                    print(f"u have withdrawn amont: {withdraw}")
                    
                    break
        else:
            print("Invalid option")
    else:
        print("Username OR Password is incorrect")
except ValueError:
    print("Type proper name and password")
except TypeError:
    print("Type Error")
                
            
        
        
