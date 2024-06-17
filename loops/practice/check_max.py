"""
Decription: Find max and min in given array
Author: R.agg
Date: 17-06-24
"""
given_array=[10,2,3,14,25,29,65,2,3,9]

max_val,min_val =given_array[0],given_array[0]
print(f"Max number without loop = {max(given_array)}")
print(f"Min number without loop = {min(given_array)}")


for num in given_array:
    if num > max_val:
        max_val=num
    elif num < min_val:
        min_val=num

        
print(f"Max number with loop = {max_val}")
print(f"Min number with loop = {min_val}")
