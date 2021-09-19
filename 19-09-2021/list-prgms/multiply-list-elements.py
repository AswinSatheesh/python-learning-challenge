# Python program to multiply all values in the list using traversal
 
def multiply_list(ls):
    result = 1   #Initialize the value of the result to 1(not 0 as 0 multiplied with anything returns zero).
    for value in ls:
        result = result *value
    return result 

list = [5, 10, 15, 20, 25]
print(multiply_list(list))