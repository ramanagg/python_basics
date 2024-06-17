"""
Description: Reverse a string
Author: R.agg
Date: 17-06-24
"""

string_given= input("enter string to reverse\n")
reverse_string =''
for char in string_given:
    reverse_string = char + reverse_string
print(f"with for loop = {reverse_string}")
    
print(f"without loop = {string_given[::-1]}") #without loop