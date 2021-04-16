#sum even number and odd number
low=int(input("Enter a lower limit")) #5
upp=int(input("Enter a upper limit")) #10
evensum=0
oddsum=0
for i in range(low,(upp+1)): #(5,11)
    if(i%2==0): #5%2==0
        evensum+=i
    else:
        oddsum+=i #0+5=5 5+7=12

print("sum of even is",evensum)
print("sum of odd is",oddsum)