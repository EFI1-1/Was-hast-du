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


