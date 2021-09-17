#Python program to swap first and last elements in a list

# Swap function
def swap_list(list):
    size = len(list)
    # print(size)
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp
    return list

list = [12,35,9,56,24]
print(swap_list(list))

# list1 = [2,5,7,9]
# print(swap_list(list1))