# problem no.6 to ask user to enter number to display factorials number

num = int(input("Enter a number : "))

factorial = 1

for i in range(1, 1+num):
    factorial = factorial * i


    print( f"the {num} of facotiral is {factorial}")