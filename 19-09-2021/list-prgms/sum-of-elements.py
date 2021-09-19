# Python program to find sum of elements in list

def sum_ele(list):
    total = 0
    length = len(list)
    for ele in range(0, length):
        total = total + list[ele]
    return total


list = [2, 4, 6, 8, 10,12]
print("Sum of elements in the list is :", sum_ele(list))
