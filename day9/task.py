# #task
# create a list/tuple containing the name of people
# ask the user to enter a Name
# if the entered name is in the list  then show "lOgin succesfully" 

names = ['anish','bina','sita']
user = input("Enter the name you want to search:")

for search_name in names:
    if search_name == user:
        print(f"login Successfully. Welcome {user}")
        break
else:
    print("Noo name found")

    