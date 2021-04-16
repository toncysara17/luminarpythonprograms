#read lower limit, upper limt and check prime number in lower limit to uppper limit
low=int(input("Enter a lower limit")) #2
upp=int(input("Enter a upper limit")) #10
for i in range(low, (upp+1)): #assign the values from lower limit to upper limit to the variable i
    flag=0
    for x in range(2,i):
        if(i%x==0):
            flag=1
            break
        else:
            flag = 0
    if (flag == 0):
        print(i)












