#binary search
#algorithm
#1.sorting
lst=[3,4,2,11,10,13,12,14,15]
lst.sort()
print(lst)
low=0
upp=len(lst)-1     #8
element=int(input("enter element to search"))      #11
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")





