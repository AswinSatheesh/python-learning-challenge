# Python program to find sum of all elements in list using recursion

def sum_of_list(list, size):
    if size == 0:
        return 0
    else:
        total = list[size - 1] + sum_of_list(list, size-1)
        return total


list = [1, 2, 3, 4, 5]
print("sum of elements in the list is : ",sum_of_list(list, len(list)))
