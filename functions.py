from radgraphs import graph
from db_queries import Queries
#from ui import main_func
import connector

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
                    prog_choice = input("(V)iew radiation graphs, (A)lter files, or (E)xit: ")

                    if prog_choice == 'a' or prog_choice == 'A':
                        print("Alter Database Files")
                        try:
                            choice = input("Please choose whether to (a)dd, (u)pdate, (d)elete, (q)uery db, or (e)xit: ")
                            Queries.radFiles(conn, choice)

                        except:
                            print("Database error")

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
                    exit()
                    return

            except:
                exit()
                
        except:
            exit()
