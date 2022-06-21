from db_queries import Queries
from functions import progFunctions
from hashpassword import hashedPassword
from ui import mainUI
import connector

try:
    connectedList = connector.db_connect.db_connection()
    obj = Queries(connectedList[0], connectedList[1])

except:
    print("Database connection failure")

try:
    mainUI()

    user_in = input("Please (L)ogin, (C)reate a new user, (D)elete a user, or (E)xit: ")

    if user_in == 'c' or user_in == 'C':
        obj.create_user()

    elif user_in == 'd' or user_in == 'D':
        obj.delete_user()

    elif user_in == 'l' or user_in == 'L':
        obj.login()
        prg = progFunctions.prog_continue()

    elif user_in == 'e' or user_in == 'E':
        print("Exiting")
        exit()

    else:
        exit()

except:
    ("Program execution failure")
