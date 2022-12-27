from getpass import getpass
from hashpassword import hashedPassword
import mysql.connector
import datetime



class Queries:
    def __init__(self, mydb, mycursor):
        self.curs = mycursor
        self.conn = mydb


    def create_user(self):

        """Create new user in database"""

        UID = input("Please enter a username: ")
        name = input("Please enter your (real or pseudo) name: ")
        password = input("Please enter a (secure) password: ")
        
        try:
            hashed = hashedPassword.hash_func(password)
        except:
            print("Password hashing error")

        try:
            sql = "INSERT INTO radalyze.users (`name`, UID, `password`) VALUES (%s, %s, %s);"
            self.curs.execute(sql,(name, UID, hashed))
            self.conn.commit()

            print(f"User {name} successfully added to database")

            sql = "INSERT INTO radalyze.crypto (`enc`, `UID`) VALUES (%s, %s);"
            self.curs.execute(sql,(hashed, UID))
            self.conn.commit()

        except mysql.connector.Error as error:
            print(f"Error creating user: {error}")

        except:
            print("Create Statement error")


    def delete_user(self):

        """DELETE a user from the database"""

        user_uid = input("Please enter the username to delete: ")
        password = getpass("Please enter the password: ")

        try:
            sql = f"SELECT `password` FROM radalyze.users WHERE UID = '{user_uid}';"
            self.curs.execute(sql)
            self.conn.commit()

            try:
                pw_result = self.curs.fetchone()
                hashed = pw_result[0]
                byte_hash = bytes(hashed, 'utf-8')

                user_pwd = password
                check_pass = hashedPassword.check_func(user_pwd, byte_hash)

            except:
                print("Password error!")
                exit()

            try:
                if check_pass == True:
                    sql = f"DELETE FROM radalyze.users WHERE (`UID` = '{user_uid}');"
                    self.curs.execute(sql)
                    self.conn.commit()


                    print(f"User {user_uid} successfully deleted from database")

            except:
                print("Failed to remove user")            

        except mysql.connector.Error as error:
            print(f"Error deleting user: {error}")

        except:
            print("Delete Statement Error")


    def update_user(self, uid, user_input):

        sql = f"UPDATE radalyze.users SET `name` = '{user_input}' WHERE UID = '{uid}';"
        self.curs.execute(sql)
        self.conn.commit()

        print(f"Successfully updated name to {user_input}")

        return


    def login(self):
        """login user"""

        UID = input("Please enter your username to login: ")

        try:
            sql = f"SELECT `UID` FROM radalyze.users WHERE `UID` = '{UID}';"
            self.curs.execute(sql)
            self.conn.commit()

            result = self.curs.fetchone()

            if result[0] == UID:
                
                sql = f"SELECT `password` FROM radalyze.users WHERE UID = '{UID}';"
                self.curs.execute(sql)
                self.conn.commit()

                pw_result = self.curs.fetchone()

                try:
                    hashed = pw_result[0]
                    byte_hash = bytes(hashed, 'utf-8')
                except:
                    print("byte conversion error")
                
                try:
                    user_pwd = getpass("Please enter your password: ")              # use getpass to hide input
                    check_pass = hashedPassword.check_func(user_pwd, byte_hash)
                except:
                    print("Password hash error")


                if check_pass == True:
                    sql = f"UPDATE radalyze.users SET logged_in=1 WHERE UID = '{UID}';"
                    self.curs.execute(sql)
                    self.conn.commit()

                    print(f"Thank you {UID}, you are now logged in")
                    print("")

                    return True

                else:
                    print("Password error!")
                    exit()

            else:
                print("UID error")
                exit()

        except:
            print("Login error")
            exit()


    def logout(self, UID):
        try:
            sql = f"UPDATE radalyze.users SET logged_in=0 WHERE UID = '{UID}';"
            self.curs.execute(sql)
            self.conn.commit()
            print(f"You have logged out")
            print("")

        except:
            print("Logout error")



    def radFiles(self, choice):
            
        try:
            if choice == 'q' or choice == 'Q':
                print("\n")
                print("~~Query Database File Table~~")
                print("")
                sql = f"SHOW TABLES;"

                self.curs.execute(sql)
                self.conn.commit()

                result = self.curs.fetchall()
                for i in result:
                    print(i)

            elif choice == 'e' or choice == 'E':
                return

            else:
                print("Statement error")
        except:
            exit()

    def get_uid(self):      # this is required for choice_log to work
        sql = "SELECT `UID` FROM radalyze.users WHERE logged_in = 1;"

        self.curs.execute(sql)
        self.conn.commit()

        result = self.curs.fetchall()
        for i in result:
            print(i)

        return result

    def choice_log(self, state, year, uid):
        now = datetime.datetime.now()
        log_text = f"State code: {state} .. Year: {year} || datetime: {now}"

        sql = f"INSERT INTO radalyze.choice_log (user_graph_choice, `UID`) VALUES ('{log_text}', '{uid}');"

        self.curs.execute(sql)
        self.conn.commit()

        return

    def read_log(self, uid):
        sql = f"SELECT (user_graph_choice) FROM radalyze.choice_log WHERE `UID` = '{uid}';"
        
        self.curs.execute(sql)
        self.conn.commit()

        result = self.curs.fetchall()

        return result
