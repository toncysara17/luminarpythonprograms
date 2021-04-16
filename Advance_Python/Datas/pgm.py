#combination of upper case and lower case letters ending with a number
import re
n="tocyARa1"
x="[a-zA-Z]+\d{1}$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")