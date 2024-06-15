"""
Description: Find max number among three numbers
Author: R.agg
Date:15-06-24 
"""

num1=6
num2=8
num3=9

#solution for without using python inbuilt functions
if num1 > num2 and num1 > num3:
     print(str(num1) + " is greatest number")
elif num2 > num1 and num2 > num3:
     print(str(num2) + " is greatest number")    
elif num3 > num1 and num3 > num2:
    print(str(num3) + " is the greatest number")
else:
    print("Seems all are equal")
    
#solution with python max function
print(str(max(num1,num2,num3)) + " is the greatest number")  
    