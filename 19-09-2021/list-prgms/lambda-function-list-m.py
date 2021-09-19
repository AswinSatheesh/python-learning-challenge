# program to multiply all values in the list using lambda function and reduce()

from functools import reduce

list = [1, 2, 3, 4, 5]

result = reduce((lambda x, y: x * y ),list)
print(result)