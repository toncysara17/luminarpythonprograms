#predefined functions
#map()
    #2 arguments
    #functions
    #iterables

lst=[10,20,30,21,22,23,24]
# squ=[]
# for num in lst:
#     res=num**2
#     squ.append(res)
# print(squ)

squ=list(map(lambda num1:num1**2,lst))
print(squ)

cube=list(map(lambda num1:num1**3,lst))
print(cube)



# squares=list(map(lambda num1:num1**2,lst))
# print(squares)
#
# cube=list(map(lambda num1:num1**3,lst))
# print(cube)



#filter()
#reduce()

