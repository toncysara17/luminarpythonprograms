import re
x="[A-Z]"                       # A to Z
matcher=re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())