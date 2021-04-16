
import  mysql.connector
db=mysql.connector.connect(
    user="root",
    host="localhost",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="febpython"
)
cursor=db.cursor()
f=open("employee","r")
for lines in f:
    #102,ram,developer,26500
    data=lines.rstrip("\n").split(",")
    #[102,ram,developer,26500]
    sql="insert into emp1(eid,ename,design,salary)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()
