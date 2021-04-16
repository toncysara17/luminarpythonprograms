
import re
valid = []
x = "[+][9][1]\d{10}"
f = open("validno", "r")
for num in f:
    number = num.rstrip("\n")
    matcher = re.fullmatch(x, number)
    if matcher != None:
        valid.append(number)
    print(valid)