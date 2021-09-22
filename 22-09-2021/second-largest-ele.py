#python program to find the second largest number in list.

list = [3, 10 , 6 , 55, 88, 4]

list.sort()

# print("Second largest element in the list is: ",list[-2])

#same program using function method:

def second_large_ele(list):
    list.sort()
    return list[-2]


list = [3, 10 , 6 , 55, 88, 4, 77]
# print("Second largest element is :",second_large_ele(list))



#program to find second largest number in a list

list1 = [10, 20, 4, 45, 99, 88]

new_list = set(list1)

new_list.remove(max(new_list))

print("Second largest element in the given list is :",max(new_list))