# question number 1. of chapter 7 take number from user and make mutliplicationtable

num = int(input("Enter a number : "))

for i in range(1,11):
    # print( str(num) + " X " + str(i) + " = " + str(num*i))
    print(f"{num}  X  {i} = {num*i}") #second way to print multiplication table using -f-