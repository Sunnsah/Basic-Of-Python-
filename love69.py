# we use here how to use input and ouput of file function 

# file = open('awesome.txt', 'w')
# file.write("This is awesome file , here you can thing and write about your jounery of life")
# # print(file)           : we can direct make a file.txt using .write command        
# file.close()


# with file handling use for automatically close the program 

with open('awesome.txt', 'r') as file:
    apple = file.read()

with open('awesome.txt', 'w') as file:
    apple = file.write("David")
    # print(apple)
    print(apple)




