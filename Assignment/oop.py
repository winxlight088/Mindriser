#task:
#create class name accoubt
#it should have 2 attributes(accout_number,balance), 
# --account number shoud be private 
#it should have methods(bedit,credit and total balance:)
#the output returned from the methods should have the accoubt_number incuded in them

class Account():
    __account_no = "1234"
    balance = 5000.00
    
    
   
    
    def get_account(self):
        return self.__account_no

    def debit(self):
        
        useramt= int(input("enter the amount to debit: "))
        if useramt>self.balance:
            print("insufficient balance")
        elif useramt<= self.balance:
            total = self.balance - useramt
            print(f'''Amount: {useramt} debited from Account no: {self.__account_no},
               New Balance: {total}''')
        
    
    def credit(self):
        
        print(f"Initial aomount in balance: {self.balance}")
        useramt= int(input("enter the amount to credit: "))
        total = self.balance + useramt
        print(f'''Amount: {useramt} credited to Account no: {self.__account_no},
               New Balance: {total}''')
    
    def display_opt(self):
        while True:
            choice = input("Enter 1 dor debit, 2 dor credit, 3 for exit: ")
            if choice == "1":
                self.debit()
            elif choice == "2":
                self.credit()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please choose again.")
        
    

obj1 = Account()
obj1.display_opt()


