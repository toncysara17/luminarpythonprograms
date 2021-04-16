#Quantifiers
import re
x = "a{1,3}"                #minimum 2 and maximum 3 a     #{2,3}
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())