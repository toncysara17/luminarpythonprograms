#Quantifiers
import re
x = "a{3}"                #no of a position
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())