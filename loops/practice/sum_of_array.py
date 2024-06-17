"""
Description: Return sum of given array
Author: R.agg
Date:17-06-24
"""
number_array=[1,2,3,5,9,15,20,0]
sum_of_array=0
for i in number_array:
    sum_of_array += i
print(f"loop output =  {sum_of_array}")

print(f"without loop output = {sum(number_array)}") # without loop