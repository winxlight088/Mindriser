#Abstraction - Hiding the unnecessary details from the users

class Bike:
    def __init__(self):
        self.brand = False
        self.brake= False
        self.acc= False
        self.clutch= False
        
        
    def start(self):
        self.clutch = True
        self.acc = True
        return "BIKE started"
    
    
bike1=Bike()
print(bike1.start())        

#task:
#create class name accoubt
#it should have 2 attributes(accout,balance)
#it should have methods(bedit,credit and total balance:)

