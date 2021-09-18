# Reversing a list using reversed()

def reverse(lst):
    return [values for values in reversed(lst)]

list = [5, 10, 15, 20]
print(reverse(list))



# Reversing a list using reverse()
# This method directly modifies the original list.

def Reverse(lst):
    lst.reverse()
    return lst

list = [5, 10, 15, 20]
print(Reverse(list))

# Reversing a list using slicing technique
#reference link : https://www.geeksforgeeks.org/python-list-slicing/

def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst
	
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
