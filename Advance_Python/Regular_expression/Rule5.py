import re
x="[a-zA-Z]"                       # both lower and upper case are checked
matcher=re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())