#polymorphism is the ability of an object to take on many forms
class Dog: 
    def move(self): #method 1 move is defined 
        return "Dog is walking"

class Bird:
    def move(self): #method 2 same "move" is defined but with different implementation
        return "Bird is flying"

class Fish:
    def move(self):  #method 3 same function called "move" is defined but with different implementation
        return "fish is swimming"

dog1=Dog() #class is called
bird1=Bird()
fish1=Fish()

print(dog1.move())
print(bird1.move())
print(fish1.move())
    
    