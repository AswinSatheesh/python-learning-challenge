#different way to clear list

#initializing list
list = [1, 2, 3]

#clearing list by using clear() method
list.clear()
print(list)

#deleting list using *= 0
list *= 0

print(list)

# Using del : del can be used to clear the list elements in a range,
# if we don’t give a range, all the elements are deleted.
del list[:]
print(list)