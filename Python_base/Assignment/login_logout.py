
#Requirment
# ask user if they want to login or register
# if register, ask for username and password and save it in a file
# if login, ask for username and password then check it in the file if the data of the user is in the file then print certain output if not print certain output
# if user is valid user then ask his/her for three optioins:check balance, add balance
# check -print amount of user
# add  - ask amount they want to add, add the given amt with the entered-
# amount and print the amountimport json #json is used to store data
# extra: if user balance xaina vaee, say them to add balance first
# Register() extra: check the file if the username is unique or not, 
# if it is unique register the username if not then display that the username is already taken and to user another username



import json
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if not unq_username(username):
        print("Username is already taken. Please choose another username.")
        return
    
    data = {username:password} #sending dta as dictionaery
    
    file = open("user_data.txt", "a") #append
    json_data = json.dumps(data) # dumps is function of json, in this line of code "data" is being converted into json format
    file.write(json_data+"-") 
    print("sucessful registered")
    file.close()
def unq_username(username):
    file = open("user_data.txt", "r")
    user_data = file.read()
    list_user_data=user_data.split("-")
    for i in list_user_data:
        if i!="":
            json_user_data = json.loads(i)
            if username in json_user_data:
                return False
    return True
    
        
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_login = False 
    
    file = open("user_data.txt", "r")
    user_data = file.read()
    list_user_data = user_data.split("-") #splitting the data in list
    file.close()
    # print(list_user_data)
    for i in list_user_data:
        if i != "":
            json_user_data = json.loads(i)
            if username in json_user_data and json_user_data.get(username)== password:
               is_login = True 
               
    if is_login == True:
        print("Login Successfull")
        choice = input("Enter 1 for check balance, 2 for add balance, 3 for withdraw: ")
        
        if choice =="1":
            check_balance(username)
        elif choice == "2":
            add_balance(username)
        elif choice =="3":
            withdraw_balance(username)
    elif is_login == False:
        print("Login Failed")
       
        
def withdraw_balance(username):
   
        useramount = int(input("Ente the amount you want to withdraw: "))
        file = open("C:/python file/Assignment/accounting.txt","r")
        amt_data = file.read()
        list_user_amt = amt_data.split("-")
        file.close()
        withdrawal_sucessfull = False
        for i in list_user_amt:
            if i !="":
                dict_list= json.loads(i)
                if username in dict_list: # Check if username exists in the dictionary
                    amount = int(dict_list[username]) # Convert amount to int
                    if useramount> amount:
                        print("Insufficient balance")
                        
                    else:
                        amount -= useramount
                        print(f"you now have balance: {amount}")
                        
                        dict_list[username] = amount # Set the new balance
                        withdrawal_sucessfull= True # Mark withdrawal as successful
                        break
        if withdrawal_sucessfull:
            file = open("C:/python file/Assignment/accounting.txt","a")
            json_dict_amount = json.dumps(dict_list)
            file.write(json_dict_amount+"-")
            file.close()
        else: 
            print("Not successful withdrawal")
                
            
   
    
    
def add_balance(username):
    amount= input("Enter the amount:")
    dict_amount = {username:amount}
    f=open("C:/python file/Assignment/accounting.txt","a")
    json_dict_amount = json.dumps(dict_amount) 
    #he json.dumps() function can convert various Python data structures, 
    #including lists, dictionaries, strings, numbers, and more, into a JSON-formatted string.
    f.write(json_dict_amount+"-")
    f.close()
    print(f"Added {amount} to your account")

def check_balance(username):
    f = open("C:/python file/Assignment/accounting.txt","r")
    total = 0
    
    user_data  =f.read()
    list_user_data = user_data.split("-")
    for i in list_user_data:
        if i != "":
            dict_list_user_data = json.loads(i)
            if username in dict_list_user_data:
                amount = dict_list_user_data.get(username)
                int_amount = int(amount)
                total +=int_amount
    print(total)
    f.read()
    f.close()

choose = input("login or register:").lower()
if choose =="register":
    register()
    print("Registered sucessfully")
elif choose=="login":
    login()
    
