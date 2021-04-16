#min length 8 and maximum 15
#except numbers
import re
n=input("enter")
x="[a-zA-Z]{8,15}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
