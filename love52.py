# problem number 3 to check the input 

from turtle import Turtle


num = int(input("Enter a  number : "))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break

if prime:
    print( "  is Number  prime   "  + str(i))
else:
    print(  "  is not Number  prime "  + str(i) )






