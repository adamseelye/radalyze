from db_queries import Queries
#from functions import progFunctions
#from hashpassword import hashedPassword
from ui import mainUI, main_func
import connector

try:
    connectedList = connector.db_connect.db_connection()
    obj = Queries(connectedList[0], connectedList[1])

except:
    print("Database connection failure")

try:

    mainUI()
    main_func()

except:
    ("Program execution failure")
