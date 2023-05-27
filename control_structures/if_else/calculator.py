#This program is used to sum,su,multiply and divide

num1=input("Enter first number ")
num2=input("ENter second number ")
operation=input("Tpe operation that you want, like: sum,sub,multiply or divide ")


if(operation=='sum'):
    print(int(num1)+int(num2))
elif(operation=='sub'):
    print(int(num1)-int(num2))
elif(operation=='multiply'):
    print(int(num1)*int(num2))
elif(operation=='divide'):
    print(int(num1)/int(num2))
else:
     print("Invalid Choice")

