import mysql.connector
import hidden           # Store username/password/database info in hidden.py

class db_connect:
    @staticmethod
    def db_connection():
        """call mysql.connector to connect to database"""
        try:
            mydb = mysql.connector.connect(host = hidden.host,
                                           user = hidden.user,
                                           password = hidden.password,
                                           database = hidden.database)
            mycursor = mydb.cursor(buffered=True)
            return [mydb, mycursor]


        except mysql.connector.Error as error:
                print(error)

