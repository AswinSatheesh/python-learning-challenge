#finding length of list

#function to calculate the count
def length_count(list):

    count = 0
    for i in list:
        count = count + 1  # incrementing counter
    return count

#list
list = [1, 2, 3, 4, 5, 6]
list2 = [5,3,2,26,8,9,7,8,9,0,2]

#function call and printing result.
print(length_count(list))
print(length_count(list2))
