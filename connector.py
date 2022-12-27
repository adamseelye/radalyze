import mysql.connector

class db_connect:
    @staticmethod
    def db_connection():
        """call mysql.connector to connect to database"""
        try:
            mydb = mysql.connector.connect(host="192.168.1.59",
                                           user="remote",
                                           password="MN3ttXP9LE",
                                           database="radalyze")
            mycursor = mydb.cursor(buffered=True)
            return [mydb, mycursor]


        except mysql.connector.Error as error:
                print(error)
