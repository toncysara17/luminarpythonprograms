#word count program
line="hai hello hai hello hai"
print(line)
#split
word=line.split(" ")
print(word)
dic={}
for i in word:
    if(i not in dic):       #hai hello hai hello
        dic[i]=1               #dic[hello]=1
    else:
        dic[i]+=1
print(dic)

