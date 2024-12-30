#Read
# f = open("text_file.txt", "r")
# store = f.read()
# print(store)
# f.close()

#Write
# f = open("text_file.txt", "w")
# store = f.write("This text is overwritten")
# # print(store)
# f.close()

#Append add text to the end of the file
f = open("text_file.txt", "a")
store = f.write("This text is added using append")
# print(store)
f.close()