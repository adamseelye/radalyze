from radgraphs import graph
from db_queries import Queries
import connector
import re

try:
    connected_list = connector.db_connect.db_connection()
    conn = Queries(connected_list[0], connected_list[1])

except:
    print("Connection Error")


class progFunctions:
    def __init__(self):
        self.view_graphs = view_graphs(self)

    def prog_continue():
        try:

            menu_cont = True                # continue displaying menu after a function

            try:
                while menu_cont == True:
                    print("What would you like to do?")
                    prog_choice = input("(V)iew radiation graphs, (Q)uery database, or (E)xit: ")

                    if prog_choice == 'q' or prog_choice == 'Q':
                        print("Alter Database Files")
                        try:
                            choice = input("Please choose whether to (q)uery db, (v)iew log, or (e)xit: ")
                            if choice == 'v' or choice == 'V':
                                clean = re.split("'", str(conn.get_uid()))
                                uid = clean[1]
                                log = conn.read_log(uid)
                                print("Current graph query log:")
                                print("\n")
                                print(log)
                            else:
                                Queries.radFiles(conn, choice)

                        except:
                            print("Database error")
                            exit(1)

                    elif prog_choice == 'v' or prog_choice == 'V':
                        print("Viewing radiation graph")
                        try:
                            graph.radiation_graphs()
                        except:
                            print("Viewing Error")

                    elif prog_choice == 'e' or prog_choice == 'E':
                        from ui import main_func
                        main_func()
                        menu_cont = False

                    else:
                        print("Input error")
                        return

                else:
                    menu_cont = False;
                    exit(0)
                    return

            except:
                print("Menu error, exiting")
                exit(1)
                
        except:
            print("Error, program must exit")
            exit(1)

