#word count
f=open("C:/Users/MAC/PycharmProjects/FebPython/Core_Python/Files/data","r")
dic={}
for lines in f:
   words=lines.rstrip("\n").split(" ")
print(words)
# for i in words:
#     if(i not in dic):
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)