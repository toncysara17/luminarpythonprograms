import re
n="56kg"
x= "a-z0-9{4}"   #"d{2}[a-z]{2}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")