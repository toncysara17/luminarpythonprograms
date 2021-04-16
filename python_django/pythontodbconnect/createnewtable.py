import mysql.connector
db=mysql.connector.connect(
    user="root",
    host="localhost",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="febpython"

)
cursor=db.cursor();
#sql="create table emp1(eid int,ename varchar(50),design varchar(50),salary int)";
#cursor.execute(sql)
#db.close()
sql="insert into emp1(eid,ename,design,salary)values(100,'akhila','developer',10000)";
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()