"""
Description: check given number is even or odd, take input from user
Author: R.agg
Date: 15-06-24
"""
number=int(input("Enter your desired number to check \n"))

#solution traditional way
if number <= 0:
    print ("Number should be greater than zero")
    
elif number % 2 == 0:
    print (number, "is even number")

else:
    print (number, "is odd number")
    
#solution without tradition way

response= ("Number should be greater than zero" if number <=0 else f"{number} is even number" if number % 2 == 0 else f"{number} is odd number")

print("Response using tennary operator \n" ,response)
    