# Recursion using make factorails

n = (int(input("Enter a number : ")))
product = 1

for i in range(n):
    product = product * (i+1)
    print(product)