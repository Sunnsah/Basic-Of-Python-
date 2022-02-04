#WAp to find greatest number, enter by users

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third  number: "))
num4 = int(input("Enter a fourth number: "))


if(num1>num2):
    print( str(num1) + " first  number is greater than second number ")
elif(num2>num3):
    print(str(num2) + " second number is greater than third number ")
elif(num3>num4):
    print(str(num3) + " third number is greater number than fourth number")
else:
    print( str(num4) + " fourth number is greater than all three number")

