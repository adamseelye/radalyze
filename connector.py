import mysql.connector

class db_connect:
    @staticmethod
    def db_connection():
        """call mysql.connector to connect to database"""
        try:
            mydb = mysql.connector.connect(host="192.168.1.206",
                                           user=" ",
                                           password=" ",
                                           database="proj_0")
            mycursor = mydb.cursor(buffered=True)
            return [mydb, mycursor]


        except mysql.connector.Error as error:
                print(error)
