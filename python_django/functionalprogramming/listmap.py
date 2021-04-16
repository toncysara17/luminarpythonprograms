lst=[4,2,1,6,7,8]
lst1=[]
# for i in lst:
#     if(i<5):
#         i-=1
#         lst1.append(i)
#     else:
#         i+=1
#         lst1.append(i)
# print(lst1)



#another method


result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)


#output   3,1,0,7,8,9