#find the second largest number#100 40 60
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if(num1>num2)&(num1<num3):
    print("num1 is second largest")
elif(num1<num2)&(num1>num3):
    print("num1 is second largest")
elif(num2>num3)&(num2<num1):
    print("num2 is second large")
elif(num2<num3)&(num2>num1):
    print("num2 is second large")
else:
    print("num3 is second large")