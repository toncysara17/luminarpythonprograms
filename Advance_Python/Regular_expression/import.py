import re
count=0
matcher=re.finditer('ab', 'abaabbab')
for match in matcher:
    print("match available:",match.start())
    count+=1
print("count:",count)