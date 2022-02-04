# write a program to greet that person of list - start with S only

list = ["Mohan", "Sohan", "Sunny", "Sony", "Shivani"]
# list = input("Enter your name : ")

for name in list:
    if name.startswith("S"):
        print("Hello Sir/Madam  " + name)
# else:
#             print("name is not found in our system " + list)
