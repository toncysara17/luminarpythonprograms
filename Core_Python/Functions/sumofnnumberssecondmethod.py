#sum of n numbers
#function with argument and no return type
def sum(n):
    num=n  #10
    i=1
    sum=0
    while(i<=num): #1<=10
        sum=sum+i
        i=i+1
    print(sum)

num=int(input("Enter a number"))
sum(num)