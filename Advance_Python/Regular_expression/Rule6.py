import re
x="[0-9]"                       # check digits
matcher=re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())





















