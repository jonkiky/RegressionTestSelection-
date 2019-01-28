import mysql.connector
import os
username="root"
password="123456"
address="/home/yc518178/itmdatabas/"
conn = mysql.connector.connect (user='root', password='123456',
                               host='localhost',buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
for (databases) in cursor:
     print databases[0]
     baseCommand="mysqldump -u "+username+"  -p"+password+" "+databases[0]+">"+address+databases[0]+".sql"
     os.system(baseCommand)