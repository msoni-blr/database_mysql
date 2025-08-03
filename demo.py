from dotenv import dotenv_values
import mysql.connector

config = dotenv_values("demo.env")

mydb = mysql.connector.connect(
    host=config['MYSQL_HOST'],
    user=config['MYSQL_USER'],
    passwd=config['MYSQL_PASSWD'],
    database=config['MYSQL_DATABASE']
)

mycursor = mydb.cursor()

mycursor.execute("show databases")
# mycursor.execute("select * from table")

# for i in mycursor:
#     print(i)

result = mycursor.fetchall()
# result = mycursor.fetchone()

print(result)
