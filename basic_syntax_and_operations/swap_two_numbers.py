"""
Description: Swap Two numbers
Author: R.agg
Date: 15-06-24
"""
num1=5
num2=6

print("before swap num1="+ str(num1)+" and num2=" +str(num2))
#solution traditional way
temp=num1
num1=num2
num2=temp
print("after swap with traditional method num1="+ str(num1)+" and num2=" +str(num2))

#solution without traditional way
num1,num2 = num2,num1
print("Swapped swap values without traditional method num1="+ str(num1)+" and num2=" +str(num2))
