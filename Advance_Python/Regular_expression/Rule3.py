import re
x="[a-z]"                       # a to z
matcher=re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())