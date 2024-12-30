#ask user for login or register
#if regester ask for their name,password or usertype
# (buyer.seller),(format for data store may change) and store it in file
# if login ask for username and password and check if it exist in
# file, if it exit printsome message
#if user is buyer show them the option to view products, buy products and view bill
#if the choice is view product then show them the details of the products
#if the user is seller then show then the option to add products,view products,
#if the choice is add products then they have to enter the name, description, price of the product 

import json
def add_product(seller): #this parameter  
    name = input("Enter the name of the product: ")
    description = input("Enter the description of product: ")
    price = input("Enter the price: ")
    product = {"name":name, "description":description, "price":price,"seller":seller}
    
    f = open("C:/python file/ecommerce/product.txt", "a")
    json_product= json.dumps(product) #converting dictionery to json module
    f.write(json_product+"-")
    f.close()


def view_product(): # buyer
    f=open("C:/python file/ecommerce/product.txt", "r")
    a= f.read().split("-")
    f.close()
    for i in a: # to dispy the details
        print(i)


def view_seller_product(seller):
    f=open("C:/python file/ecommerce/product.txt", "r")
    a= f.read().split("-") #converted to list 
    f.close()
    
    for i in a: # to dispy the details
        if i!="":
            json_product =json.loads(i)
            if json_product.get("seller")== seller:
                print(json_product)
                
            
        
def register():
    username=input("Enter the name: ")
    password = input("Enter the password: ")
    usertype = input("Enter the usertype (buyer/seller): ").lower()
    

    data = {
        "userkey":username,
        "passkey":password,
        "typekey":usertype
        
        } #sending dta as dictionaery
    print(data)
    
    file = open("C:/python file/ecommerce/e_user_data.txtt", "a") #append
    json_data = json.dumps(data) # dumps is function of json, in this line of code "data" is being converted into json format
    file.write(json_data+"-") 
    file.close()
    
def buy_product():
    f= open("C:/python file/ecommerce/product.txt", "r")
    user_data = f.read().split('-')
   
    print(user_data)
    purchase = input("Enter the item you want to buy from above list:")
    for i in user_data:
        if i != "":
            json_product = json.loads(i)
            if purchase == json_product.get("name"):
                print("Bill:" + json_product.get("price"))
    f.close()
    
    

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_login = False 
    
    file = open("C:/python file/ecommerce/e_user_data.txt", "r")
    user_data = file.read().strip('-')
    
    list_user_data = user_data.split("-") #splitting the data in list
    # print(list_user_data)
    file.close()
    # print(list_user_data)
    for i in list_user_data:
        if i != "":
            json_user_data = json.loads(i)
            if json_user_data.get("userkey")==username and json_user_data.get("passkey")== password:
               is_login = True 
               usertype = json_user_data.get("typekey")
    if is_login == True:
        print("Login Successfull")
        
        
        if usertype == "seller":
            choice = input('''Enter
                  1. Add product
                  2. View product
                  ''')
            
            if choice == "1":
                add_product(username)
                
            elif choice =="2":
                view_seller_product(username)
                
                
        elif usertype =="buyer":
            choice = input('''Enter
                  1. view product
                  2. Buy product
                  ''')
            if choice == "1":
                view_product()
                
            elif choice == "2":
                buy_product()
                
                
                
    elif is_login == False:
        print("Login Failed")
    

choose = input("login or register:").lower()
if choose =="register":
    register()
elif choose=="login":
    login()
    

