from getpass import getpass
from hashpassword import hashedPassword
import mysql.connector



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
            sql = "INSERT INTO proj_0.users (`name`, UID, `password`) VALUES (%s, %s, %s);"
            self.curs.execute(sql,(name, UID, hashed))
            self.conn.commit()

            print(f"User {name} successfully added to database")

        except mysql.connector.Error as error:
            print(f"Error creating user: {error}")

        except:
            print("Create Statement error")


    def delete_user(self):

        """DELETE a user from the database"""

        user_uid = input("Please enter the username to delete: ")
        password = getpass("Please enter the password: ")

        try:
            sql = f"SELECT `password` FROM proj_0.users WHERE UID = '{user_uid}';"
            self.curs.execute(sql)
            self.conn.commit()

            try:
                pw_result = self.curs.fetchone()
                hashed = pw_result[0]
                byte_hash = bytes(hashed, 'utf-8')

                user_pwd = password
                check_pass = hashedPassword.check_func(user_pwd, byte_hash)
                print("Check password success")

            except:
                print("Password error!")
                exit()

            try:
                if check_pass == True:
                    sql = f"DELETE FROM proj_0.users WHERE (`UID` = '{user_uid}');"
                    self.curs.execute(sql)
                    self.conn.commit()


                    print(f"User {user_uid} successfully deleted from database")

            except:
                print("Failed to remove user")            

        except mysql.connector.Error as error:
            print(f"Error deleting user: {error}")

        except:
            print("Delete Statement Error")


    def login(self):
        """login user"""

        UID = input("Please enter your username to login: ")

        try:
            sql = f"SELECT `UID` FROM proj_0.users WHERE `UID` = '{UID}';"
            self.curs.execute(sql)
            self.conn.commit()

            result = self.curs.fetchone()

            if result[0] == UID:
                
                sql = f"SELECT `password` FROM proj_0.users WHERE UID = '{UID}';"
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
                    sql = f"UPDATE proj_0.users SET logged_in=1 WHERE UID = '{UID}';"
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
            sql = f"UPDATE proj_0.users SET logged_in=0 WHERE UID = '{UID}';"
            self.curs.execute(sql)
            self.conn.commit()
            print(f"You have logged out")
            print("")

        except:
            print("Logout error")



    def radFiles(self, choice):
            
        try:
            if choice == 'a' or choice == 'A':
                print("\n")
                print("~~Add File Pointer To The Database~~")
                print("")
                file_name_in = input("Please enter the name of the file to add to the database: ")
                add = f"INSERT INTO proj_0.raddata (file_name) VALUES ('raddata/{file_name_in}')"
                sql = add
                print(sql)

                self.curs.execute(sql)
                self.conn.commit()
   
            elif choice == 'u' or choice == 'U':
                print("\n")
                print("~~Update File Database Pointer~~")
                print("")
                file_name_in = input("Please enter the updated file name: ")
                file_id_in = input("Please enter id of file: ")
                update = f"UPDATE proj_0.raddata SET file_name='raddata/{file_name_in}' WHERE id = {file_id_in};"
                sql = update
                print(sql)

                self.curs.execute(sql)
                self.conn.commit()

            elif choice == 'd' or choice == 'D':
                print("\n")
                print("~~Delete File Pointer From Database~~")
                print("")
                file_id_in = input("Please enter id of file to be deleted: ")
                delete = f"DELETE FROM proj_0.raddata WHERE id = {file_id_in}"
                sql = delete

                self.curs.execute(sql)
                self.conn.commit()

            elif choice == 'q' or choice == 'Q':
                print("\n")
                print("~~Query Database File Table~~")
                print("")
                sql = f"SELECT * FROM proj_0.raddata;"

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
