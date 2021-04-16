import re
n=input("enter")            #asuryak123b"
x="(^a[a-zA-Z]*\d*b$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")