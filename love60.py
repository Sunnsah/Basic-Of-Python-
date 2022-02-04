# Recurive

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)  

fact = factorial_recursive(0)
# print(factorial_recursive(7))
print(fact)

