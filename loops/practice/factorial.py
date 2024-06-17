"""
Description: Generate factorial of given number
Author: R.agg
Date: 17-06-24 
"""
number = int(input("Enter number for factorial\n"))

number_range=range(1,number+1)

response=1



print("Output")
for num in number_range:
    response *= num
print(response)