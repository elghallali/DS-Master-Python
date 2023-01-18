# pip install mysql-connector-python

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
  print(conn)
  db = conn.cursor()
  myDataBase = "test_master"
  db.execute("SHOW DATABASES")
  lst = db.fetchall()
  if (myDataBase,) not in lst:
    db.execute(f"CREATE DATABASE {myDataBase}")
    db.execute("CREATE TABLE etudiant (name VARCHAR(255), address VARCHAR(255))")
  print(lst)

  db.execute("SELECT * FROM test_master.personne")
  lst1 = db.fetchall()
  df = pd.DataFrame(lst1)
  print(df)
except mysql.connector.Error as err:
  print("Something went wrong: {err}")