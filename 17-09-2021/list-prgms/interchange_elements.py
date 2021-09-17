#Python program to swap first and last elements in a list
#reference link : https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

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


#method3
def swap_list(list):

    # Storing the first and last element
    # as a pair in a tuple variable get
    get = list[0], list[-1]

    # unpacking those elements
    list[-1], list[0] = get
    return list


new_list = [5,10,15,20]
print(swap_list(new_list))


#method 4

def swap_list(list):

    # the usage of * operarnd
    start, *middle, end = list
    list = [end, *middle, start]
    return list

lis = [1,3,6,9,12]
print(swap_list(lis))

#method 5

def swap_list(list):
    first = list.pop(0)
    last  = list.pop(-1)

    list.insert(0,last)
    list.append(first)
    return list

newlist = [2,4,6,8]
print(swap_list(newlist))