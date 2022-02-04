# Question no.4 of chapter 6 : ask user to enter name which name contains less than 10 characters

name = input("Enter a Username : ")
print(name)
container = len(name)
print(container)

if(container<=10):
    print("the username you enter have less than 10 character")
else:
    print("more than 10 character ")        