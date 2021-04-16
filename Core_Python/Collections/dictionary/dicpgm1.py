#collect key values

students3={"roll":1001,"name":"amal","age":25,"cpp":30}
for i in students3:
    print(i)                        #collect keys
    print(students3[i])             #collect values
    print(i,",",students3[i])       #collect key values

#update name,cpp
student={"roll":1001,"name":"amal","age":25,"cpp":30}
student["name"]="arjun"
student["cpp"]=40   #or   student["cpp"]+=10
print(student)

#delete
#del
del student["cpp"]
print(student)


#total
print("total" in student)              # false


print("cpp" in student)                    #true

#add key values
student["total"]=150
print(student)