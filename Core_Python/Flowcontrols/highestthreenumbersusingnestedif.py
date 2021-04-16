#check highest 3 numbers using nested if
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if(num1>num2):
    print("Number 1 is highest",num1)
    if(num1>num3):
        print("Number 1 is highest",num1)
        if(num2>num3):
            print("Number 2 is highest",num2)
else:
    print("Number 3 is highest",num3)

