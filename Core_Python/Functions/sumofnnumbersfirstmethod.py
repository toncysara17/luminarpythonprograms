#sum of n numbers
#function without argument and no return type
def sum():
    num=int(input("Enter a number"))  #10
    i=1
    sum=0
    while(i<=num): #1<=10
        sum=sum+i
        i=i+1
    print(sum)
sum()
