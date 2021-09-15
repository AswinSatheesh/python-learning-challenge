
# factorial of  number using function method
#Recursive

def factorial(n):
    return 1 if(n == 0 or n == 1) else n * factorial(n-1)

num = int(input("Enter a Non-Negative number :"))
print("Factiorial of ",num,"is : ",factorial(num))


# -----------------------------
#Iterative method:


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact *= n
            n -= 1
        return fact

num = int(input("Enter a Non- Negative number :"))

print("Factorial of" ,num, "is :",factorial(num))


# --------------------------------------
# By using In-built function:

import math

def factorial(n):
    return (math.factorial(n))

num = int(input("Enter a Non-Negative number :"))
print("Factiorial of ",num,"is :",factorial(num))