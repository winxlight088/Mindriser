#encapsuation-wrapping attributes & method in single unit, it hides data

class Student: #class is created
    __email = None # 
    __password = None
    
    def get_email_password(self,email,password): #method is created
        self.__email=email
        self.__password=password
    
    def get_email(self): # but when i want to acces the email even when encapsulated then i created the method 
        return f"your email is {self.__email}"

std1 = Student()
std1.get_email_password("student@gmail.com","password")
print(std1.get_email()) #this is how we access the encapsulated data using method
print(std1.__password)