# login TASK
#make a dictionaery with key as username and password as value
info = {'username':'anisha','password': '123', 'username':'nisha','password': '231'}
#ask user for his username and password
entered_name = input("Enter username: ")
entered_password = input("Enter password: ")

#check if the username and password in the disctionaert is correct or not
if entered_name == info['username'] and entered_password == info['password']:
    print(f'Welcome {entered_name}')
else :
    print("Invalid username or password")
# if username and password is correct print welcome message else print invalid username or password