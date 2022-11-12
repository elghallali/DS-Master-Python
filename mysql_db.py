import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20171987"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")