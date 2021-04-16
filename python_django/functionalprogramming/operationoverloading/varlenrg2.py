#variable length arguments
def add(*args):                 #tuple format
    print(args)

add(10,20,30)




def add(*datas):
    sum=0
    for num in datas:
        sum+=sum
    return sum
res=add(10,20,30,40)
print(res)