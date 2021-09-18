# checking of element existence using loops 

def check_list(list):
    for i in list:
        if i == 2:
            return "Item exists"


# Initializing list
list = [1, 2, 3, 4, 5]

print(check_list(list))



# checking of element existence using in

if 4 in list:
    print("item exists")