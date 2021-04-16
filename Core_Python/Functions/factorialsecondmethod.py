#factorial of a number
#function with argument and no return type
def fact(num):
    num=int(input("Enter a number"))
    fact=1
    for i in range(1,(num+1)):
        fact*=i
    print(fact)
fact(5)