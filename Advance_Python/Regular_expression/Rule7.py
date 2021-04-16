import re
x="[^a-zA-Z0-9]"                       # special symbols
matcher=re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())