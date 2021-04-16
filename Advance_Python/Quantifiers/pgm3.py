import re
n=input("Enter number to validate")
x="\d{10}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")