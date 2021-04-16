#checking the highest in 2 numbers and checking its equal
num1=int(input("Enter a first number"))#10 30 50 100
num2=int(input("Enter a second number"))
if(num1>num2):
    print("highest number",num1)
elif(num1<num2):
    print("highest number",num2)
else:
    print("both are equal")