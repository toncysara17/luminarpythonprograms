import re
n="aecghijkb"
x="^a[a-z]b&"
match=re.finditer(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")