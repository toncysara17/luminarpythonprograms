#sum even and odd numbers
f=open("numbers","r")
lst=[]
oddlst=[]
evenlst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
    if(int(num)%2==0):
         evenlst.append(int(num.rstrip("\n")))
    else:
        oddlst.append(int(num.rstrip("\n")))
print(lst)
print(oddlst)
print(evenlst)
print(sum(evenlst))
print(sum(oddlst))