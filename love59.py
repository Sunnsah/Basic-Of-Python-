# Recurison using make factorials

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * i + 1
        return product
fact = factorial_iter(4)
print(fact)
# print(factorial_iter(5))
