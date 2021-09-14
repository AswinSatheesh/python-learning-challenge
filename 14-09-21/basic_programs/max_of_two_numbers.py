# maximum of two numbers

def maxnum(a,b):
    if a > b:
        return a
    else:
        return b


a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))

print("maximum of two numbers is : ",maxnum(a,b))


# -----------------------------
# By using max function ,find the maximum of the values passed as its arguments.

value1 = float(input("Enter the first number :"))
value2 = float(input("Enter the second number :"))

maximum = max(value1,value2)
print(maximum)

#By using ternary operator

print(value1 if value1 > value2 else value2)