#lower upper limit between even numbers
low=int(input("Enter a lower limit")) #4
upper=int(input("Enter a upper limit")) #6
for i in range(low,upper+1):
    if(i%2==0):
        print(i)