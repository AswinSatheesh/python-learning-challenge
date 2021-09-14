# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# names = ["abc","def","ghi"]

# result = [x.upper() for x in names]
# print(result)


# ------------------------------------

items = ["Car","Bike","Flight","Boat"]

#start index from 1
# for index, item in enumerate(items, start=1):

for index, item in enumerate(items):
    print(index, item)