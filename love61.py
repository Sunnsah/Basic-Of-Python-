# Wap to display the greater numer amonge three number
def maximum(num1 ,num2 ,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
    else:
        return num3
    if(num2>num1):
       if (num2>num3):
        return num2
    else:
        return num3

greater = maximum(40,70,86)
print("the greater number is " + str(greater))




    