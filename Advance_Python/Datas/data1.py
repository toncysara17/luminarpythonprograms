import re
lst=[]
f2=open("data2","w")
rule="[L][U][M][0-9]{2}[P][Y]\d{3}"
f=open("data","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")