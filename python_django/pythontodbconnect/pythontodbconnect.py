
# #step1 import my sql module
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123" ,
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
#execute sql queries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
