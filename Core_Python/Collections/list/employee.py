employee=[[1001,"arjun",15000],
          [1002,"arun",20000],
          [1003,"vinu",25000],
          [1004,"binu",10000]]
print(employee)

#adding a list insert a list is known as nested list

for i in employee:
    print(i[1])

#print employee name who salary greater than 17000

for i in employee:
    if(i[2]>17000):
        print(i[1])

#calculate  total salary
sum=0
for i in employee:
    sum=sum+i[2]
print(sum)