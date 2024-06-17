"""
Description: print simple number series from 1 to n, 
where n is given by user
Author: R.agg
Date: 15-06-24
"""
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number%2 == 0:
        return False
    else:
        max_divisor=int(number**0.5) + 1
        for digit in range(3,max_divisor,2): #iterate second number like 3 5 7 9
            if number % digit ==0:
                return False
            
        return True
    




n_number=int(input("Enter number to get simple series till that number\n"))
number_range=range(1,n_number)

#output of simple number series like 1 2 3 4
print("output of simple number series")
for number in number_range:
    print(number)

#output of even number series like 2 4 6 8
print("output of even number series")
for number in number_range:
    if number%2 ==0:
        print(number)
        
#output of odd number series like 1 3 5 7
print("output of odd number series")
for number in number_range:
    if number%2 !=0:
        print(number)
        
#output of prime number series like 1 3 5 7
print("output of prime number series")
for number in number_range:
    if is_prime(number):        
        print(number)
        
