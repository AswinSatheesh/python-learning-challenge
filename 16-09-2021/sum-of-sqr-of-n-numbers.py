#Python Program for Sum of squares of first n natural numbers

#function 1 
def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i)
    return sum

#function 2 

# def squaresum(n) :
#     return (n * (n + 1) * (2 * n + 1)) // 6

#function 3
# def squaresum(n):
#     return (n * (n + 1) / 2) * (2 * n + 1) / 3


num = int(input("Enter the number : "))

print("Sum of square of the ",num,"is : ",squaresum(num))