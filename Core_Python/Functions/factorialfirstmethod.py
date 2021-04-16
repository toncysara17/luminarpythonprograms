#factorial of a number
#function without argument and no return type
def factnum():
    num=int(input("Enter a value")) #5
    fact=1
    for i in range(1,(num+1)): #(1,6)
        fact*=i #1*1=1
    print(fact)
factnum()


