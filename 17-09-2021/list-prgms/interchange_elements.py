#Python program to swap first and last elements in a list
# method1


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

list1 = [2,5,7,9]
print(swap_list(list1))


#method2

def swap_list(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist

newlist = [1,2,4,5]
print(swap_list(newlist))
