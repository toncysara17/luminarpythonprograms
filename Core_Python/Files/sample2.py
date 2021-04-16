f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
print(lst)
print(sum(lst))

#\n
# rstrip                end of character removed using rstrip
# lstrip               first character remove using lstrip
