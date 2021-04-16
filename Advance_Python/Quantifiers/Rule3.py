#Quantifiers
import re
x = "a?"                #count a as each including zero no of a
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())