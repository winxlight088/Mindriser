#function - same as variable but stores the block af statements(if etc) in them
# to define function we use- def(keyword)
# paranthesis with function must be cumpolsory


# def person(name, age): # tths is function, #note: name and age in side paranthesis is parameter 
#     print(f"Name :{name}")
#     print(f"Age: {age}")

# argumeents - values passed when function is called    
# person("ram", '23') # function is called, data must be assigned

#global statement
# a=10
# b=9
# def sum():
#     global a
#     print(a+b)

# sum()


# *-args is used to read multiple data, store the tuple
# def sum(*a):
#     b=0
#     for i in a:
#         b+=i
#         print(i)
#     print(b)

# sum(2,3,4,5,1)


#twargs(keyword arguments)- we use ** to define twargs
# def person(**t):
#     for i in t.keys():#helps to acces key of dictionary
#         print(i)
#     # print(t)
#     for i,j in t.items(): #helps to acces key and values of dictionary
#         print(i,j)
#     print(t)
    
# person(name="sdsd",age="11", address="ktm")
