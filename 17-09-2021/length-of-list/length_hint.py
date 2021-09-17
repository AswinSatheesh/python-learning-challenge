#Using length_hint() method

from operator import length_hint

def length_cal(list):
    length = length_hint(list)
    return length

letters = ['A','B','C','D','E','F','G','H','I']
print(length_cal(letters))