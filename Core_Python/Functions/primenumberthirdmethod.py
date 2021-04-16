#check a prime number
#function with argument and  return type
def prime(num):
    num=int(input("Enter a number")) #9
    flag=0
    for i in range(2,num):#
        if(num%i==0):#11%2==0 11%3==0 11%4==0 9%2==0 9%3==0
            flag=1
            break
    else:
        flag=0
    if(flag>0):
        result="not prime"
    else:
        result="prime"
    return result
data=prime(2)
print(data)