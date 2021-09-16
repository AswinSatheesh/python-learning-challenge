#Python Program for cube sum of first n natural numbers

#function1
def cubesum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i*i)
    return sum

# #function 2
# def cubesum(n):
#     x = (n * (n + 1)  / 2)
#     return (int)(x * x)

num = int(input("Enter the number : "))

print("Sum of cube of the ",num,"is : ",cubesum(num))