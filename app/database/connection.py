import mysql.connector
from app.database.settings import Settings

class DatabaseConnection:

    def connection(self):


        try:
            mydb = mysql.connector.connect(
                **Settings.DB_CONFIG
            )

            if mydb.is_connected():
                print("✅ Connection successful!")

                cursor = mydb.cursor()
                cursor.execute("SELECT DATABASE();")
                print("Connected to database:", cursor.fetchone())

                # cursor.close()
                # mydb.close()
                return mydb

        except mysql.connector.Error as err:
            print("❌ Connection failed:", err)
