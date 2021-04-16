#check the highest 3 numbers
num1=int(input("Enter the first number"))#40 50
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if(num1>num2)&(num1>num3):
    print("number1 is the highest",num1)
elif(num2>num3):
    print("number2 is the highest",num2)
else:
    print("number3 is the highest",num3)