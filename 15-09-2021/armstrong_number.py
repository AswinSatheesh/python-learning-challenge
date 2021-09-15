# Armstrong number
'''
source = https://www.programiz.com/python-programming/examples/armstrong-number
'''

num = int(input("Enter the number to check the if it's armstrong or not :"))

# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

'''
-------------------------------------------------------------

'''
#finding armstrong number using same method!

num = int(input("Enter Non-Negative numbers to check if it is a armstrong or not :"))
length = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if sum == num:
    print("Given number ", num, "is armstrong ")
else:
    print("Given number", num, " is not armstrong!")
