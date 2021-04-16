#lower limit,upper limit between even numbers
low=int(input("Enter a lower limit")) #5
upper=int(input("Enter a upper limit")) #15
while(low<=upper):
    if(low%2==0):
        print(low)
    low+=1