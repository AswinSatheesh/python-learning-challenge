#finding the largest element in the list

#method 1

list = [10, 20, 30, 40, 64, 2]

list.sort()

print("largest element in this list is :",list[-1])

#method 2

list1 = [5, 8, 100, 77, 2, 54]
result = max(list1)

print("Largest element in the list is :",result)


#Method 3 : Find max list element on inputs provided by user

num = int(input("Ener the number of elements in the list :"))

list2 = []

for i in range(1,num + 1):
    value = int(input("Enter the element :"))
    list2.append(value)
    
print(list2)
print("Largest element in the list is :",max(list2))


#method 4 ,Without using built in functions in python


def myMax(list1):
    max = list1[0]

    for x in list1:
        if x > max:
            max = x

    return max

list1 = [10, 20, 4, 100,  45, 99, 77]
print("Largest element is:", myMax(list1))


