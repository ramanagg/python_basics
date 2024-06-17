"""
Description: Generate table for a given number
Author: R.agg
Date: 17-06-24
"""

number=int(input("Enter number to generate table\n"))

multiply_range=range(1,11)

print("output\n")
for num in multiply_range:
    response=number * num
    print(f"{number} * {num} = {response}")