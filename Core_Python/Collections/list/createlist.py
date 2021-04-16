#create a list,read a value,then found or not
#pgm is linear search
ls=[1,4,2,6,7]
ls.sort()
print(ls)
element=int(input("enter element to search"))
flag=0
for i in ls:
    if(i==element):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("element found")
else:
    print("element not found")

