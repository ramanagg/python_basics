# program to check numer is even or odd
evenOrOddNumber= input("enter numer to check even or odd? ")
#cast integer evenOrOddNumber as input gives string that cause TypeError
if((int(evenOrOddNumber)%2) == 0):
    print('even')
else:
    print('odd')
