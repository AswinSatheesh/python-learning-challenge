# print all prime numbers in an interval

#1

start = 2
end = 20

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            print(i)

#2    

num = int(input("Enter the number to check whether it is prime number or not :"))

for i in range(2,num):
    if num % 2 == 0:
        print("It is not a prime number")
        break
    else:
        print("it is a prime number")


#3
start = int(input("Enter the start number :"))
end   = int(input("Enter the last number  :"))

for value in range(start,end+1):
    if value > 0:
        for check in range(2,value):
            if value % check  == 0:
                break
        else:
            print(value)