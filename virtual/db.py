import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
password ="JeYsUrIyA12345",
port = '3306'
)

mycursor = dataBase.cursor()

mycursor.execute("SHOW DATABASES")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(100), address VARCHAR(100))")

for i in mycursor:
  print(i)

