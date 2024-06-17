"""
Description: Fibonacci series
Author: R.agg
Date: 17-06-24
"""

number =int(input("Enter number to generate Fibonacci series\n"))

#default 2 numbers
a , b = 0 , 1
print(a,end=" ")#end is for blank space
for _ in range(a,number): # underscore for temp or non used vars
    print(b,end=" ")
    a,b=b,a+b
print("\n") #next line after execute program