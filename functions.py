from radgraphs import graph
from db_queries import Queries
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

            print("What would you like to do?")
            prog_choice = input("(V)iew radiation graphs, (A)lter files, (P)revious menu, or (E)xit: ")
            
            try:

                if prog_choice == 'a' or prog_choice == 'A':
                    print("Alter Files")
                    try:
                        choice = input("Please choose whether to (a)dd, (u)pdate, (d)elete, (q)uery db, or (e)xit: ")
                        Queries.radFiles(conn, choice)
                        print("altering")

                    except:
                        print("Database error")

                elif prog_choice == 'v' or prog_choice == 'V':
                    print("Viewing radiation graph")
                    try:
                        graph.radiation_graphs()
                    except:
                        print("Viewing Error")

                elif prog_choice == 'e' or prog_choice == 'E':
                    return

                elif prog_choice == 'p' or prog_choice == 'P':
                    print("Be sure to update this")
                    return

                else:
                    print("Error")

            except:
                print("Error, please restart program")
            
        except:
            print("Program start error")
