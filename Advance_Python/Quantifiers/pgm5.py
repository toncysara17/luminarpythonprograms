import re
n="kl08au2467"
x="[a-zA-Z0-9]{10}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")