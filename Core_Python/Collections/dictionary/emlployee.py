#employee
#id,name,design,salary,keyvalues
#check a company key
#add a company,luminar
#update a salary 15000
#print all key value pairs

employee={"id":10001,"name":"arjun","design":"bigdata","salary":10000}
print(employee)
print(employee["name"])
print("company"in employee)
employee["company"]="luminar"
employee["salary"]+=15000
for i in employee:
    print(i,",",employee[i])