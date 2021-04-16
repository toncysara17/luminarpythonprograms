#Quantifiers
import re
x = "a$"                #check ending with a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())