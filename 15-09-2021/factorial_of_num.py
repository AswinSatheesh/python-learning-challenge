
# factorial of  number using function method

def factorial(n):
    return 1 if(n == 0 or n == 1) else n * factorial(n-1)

num = int(input("Enter a Non-Negative number :"))
print("Factiorial of ",num,"is : ",factorial(num))

