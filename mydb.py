import mysql.connector

mydb = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = 'mysqlPasswordPLP',
)

cursorObject= mydb.cursor()

cursorObject.execute("CREATE DATABASE codeCamp")

print("All Done!")