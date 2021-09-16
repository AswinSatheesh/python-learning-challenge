# Program to print ASCII Value of a character

# reference link = https://www.geeksforgeeks.org/program-print-ascii-value-character/

character = str(input("Enter the character :"))
result = ord(character)
print("The ASCII value of", character, "is :", result)



# print the ASCII value of the characters in a string using python:


text = input("Enter a String: ")
textlength = len(text)

for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)
