# pip install mysql.connector

# import libraries
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
try:
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="20171987"
    )

  db = conn.cursor()
  myDataBase = "mydatabas"
  db.execute("SHOW DATABASES")
  lst = db.fetchall()
  if (myDataBase,) not in lst:
    db.execute("CREATE DATABASE {}".format(myDataBase))
  print(lst)
  db.execute("SELECT * FROM SAKILA.ACTOR")
  lst1 = db.fetchall()
  df = pd.DataFrame(lst1)
  print(df)
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))