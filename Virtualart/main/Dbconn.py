import mysql.connector as sql
conn=sql.connect(host='localhost',database='vrt',user='root',password='sanika')#connecting with database
if conn.is_connected:#checking for successful database connection
    print("Database Is Connected:")