#factorial of a number
#function with argument and  return type
def fact(num):
    num=int(input("Enter a number"))
    fact=1
    for i in range(1,(num+1)):
        fact*=i
    return fact
data=fact(5)
print(data)
