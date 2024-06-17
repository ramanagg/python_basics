"""
Description: Make a number series till n number given by user
Author: R.agg
Date: 15-06-24
"""

n_number= int(input("Enter any number to generate series\n"))

print("Output of simple series")
start_from=1
sum_numbers=0

while start_from <= n_number:
    print(f"{start_from}")
    start_from += 1

print("Output of sum of series")   
start_from=1
sum_of_numbers=0   

while start_from <= n_number:
    sum_of_numbers = sum_of_numbers + start_from
    start_from += 1
print(f"{sum_of_numbers}")

#without looping sum of n series
""" 
I know it's quite awkward but, if you know maths and recall the formulas , try to
replace loops. As they are simple.For example sum of n series can be done by simple formula
n((n+1)/2)
"""
print("Output of sum of series without any loop")

print(n_number * (n_number+1)/2) 
