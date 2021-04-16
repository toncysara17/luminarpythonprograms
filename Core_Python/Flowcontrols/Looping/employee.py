#assign employees to work areas
age=int(input("Enter employee's age"))
gender=input("Employee's gender(M/F)")
maritialstatus=input("Enter employee's maritual status(Y/N)")
if (age<20) | (age>60) :
    print("Error")
else:
    if (gender=="f"):
        print("urban areas")
    elif (gender=="m") & (age>=20) & (age<=40):
        print("Any where")
    elif (gender=="m") & (age >40) & (age <=60):
        print("Urban areas")