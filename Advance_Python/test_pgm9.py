import re
n="ABCDabcd"
x="[A-Za-z]{8}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")