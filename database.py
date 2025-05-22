import mysql.connector


class Database:

  @staticmethod
  def dbconnect():
    return  mysql.connector.connect(
      host="PKG-MDO",
      user="marcel",
      password="passwort",
      database="game"
    )

  def db_insert(wahl_eigene, wahl_gegner, ergebnis):
    mydb = Database.dbconnect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO spiele (wahl_eigene, wahl_gegner, ergebnis) VALUES ( %s, %s, %s)"
    val = (wahl_eigene, wahl_gegner, ergebnis)
    mycursor.execute(sql, val)
    mydb.commit()


