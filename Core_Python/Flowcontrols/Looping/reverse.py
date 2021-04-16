#Reverse a number
num=int(input("Enter a number")) #153
res=0 #0
while(num!=0): #153!=0 15!=0 1!=0
    digit=num%10
    res=(res*10)+digit
    num=num//10
print(res)