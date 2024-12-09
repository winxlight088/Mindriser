#concepts of oop: Inheritance, Pomorphism, Encapsulation,Abstraction


#Inheritance

class Car: #parent class
    #attributes:
    brand = None
    color = None
    
    #methods/function:
    def set_car_data(self, brand, color):
        # self in paramater is used to refer to the current instance-
        # of the class and is used to access variables and methods-
        # from the class.
        
        self.brand = brand 
        self.color = color
        
class ElectricCar(Car): #child class has inheritated the attributes and function of parent class
    #attributes of child class:
    def speed(self, speed):
        self.speed = speed

Ecar1= ElectricCar()    
Ecar1.set_car_data('Tesla', 'Red')
Ecar1.speed("200 HP")
print(Ecar1.brand)
print(Ecar1.color)
print(Ecar1.speed)


    
# car1 = Car() #class Car is  called also argument is applied and an object - car1 is created

