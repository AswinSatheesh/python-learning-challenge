#program to find the smallest number in a list

#method 1:

list = [10, 4 ,15 , 3 , 22, 1]

list.sort()

# print(list)

# print("smallest number in the list is :",list[0])
print("smallest number in the list is :",*list[:1])

# method 2;