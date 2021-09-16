#check if given number is fibonacci or not!

#method 1

import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


for i in range(1,11):
     if (isFibonacci(i) == True):
         print(i,"is a Fibonacci Number")
     else:
         print(i,"is a not Fibonacci Number ")


#method 2
#accepting the number from user and checking whether given input is fibonacci or not.

import math

def perfectsquare(x):
    s =int(math.sqrt(x))
    return s*s == x


n = int(input("Enter the number :"))
result1 = 5* (n*n)+4
result2 = 5* (n*n)-4

if perfectsquare(result1) or perfectsquare(result2):
    print(n,"is a fibonacci number!")
else:
    print(n,"is not a fibonacci number!")