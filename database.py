import mysql.connector


class Database:

  @staticmethod
  def dbconnect():
    return  mysql.connector.connect(
      host="localhost",
      user="adolf",
      password="passwort",
      database="ssp_projekt"
    )

  def db_insert(wahl_eigene, wahl_gegner):
    mydb = Database.dbconnect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO spiele (wahl_eigene, wahl_gegner) VALUES ( %s, %s)"
    val = (wahl_eigene, wahl_gegner)
    mycursor.execute(sql, val)
    mydb.commit()


