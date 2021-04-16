employees={
    1000:{"name":"sajay","desig":"pythontrainer","exp":3},
    1001: {"name": "jay", "desig": "bigdatarainer", "exp": 2},
    1002: {"name": "ajay", "desig": "java", "exp": 3}
}
# eid=int(input("enter  employee eid"))
# if( eid in employees):
#     print(employees[eid]["name"])
# else:
#     print("eid not exist")



def emp_details(**datas):
    id=datas["eid"]
    prop=datas["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("eid not exist")
emp_details(eid=1000,prop="desig")