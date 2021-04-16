from functools import reduce
lst=[10,20,30,50,80]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
max=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(max)
min=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(min)
