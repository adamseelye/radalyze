import plotext as plt
import pandas as pd
import connector
import re
from db_queries import Queries

try:

    connected_list = connector.db_connect.db_connection()
    obj = Queries(connected_list[0], connected_list[1])

except:
    print("Database connection error: graphs")

class graph:
    def radiation_graphs():
        try:
            state = input("Please choose radiation data from Ari(Z)ona, (L)ouisiana, Ma(S)sachussetts, or (M)ontana: ")

            if state == 'z' or state == 'Z':
                year = input("Please choose the year to analyze and enter the last two digits, from between 08 and 21: ")
                
                try:

                    clean = re.split("'", str(obj.get_uid()))
                    uid = clean[1]
                    print(state)
                    print(year)
                    print(uid)
                    obj.choice_log(state, year, uid)
                except:
                    print("log error")
                    exit()

                print("\n")
                print(f"~~~Displaying radiation data from the Gamma detector in Tucson, Arizona for the year 20{year}~~~")
                print("")
                print("The X axis displays the Gamma detection count in Counts Per Minute (CPM)")
                print("The Y axis displays the data point count collected over the entire year, with January at the origin")
                print("\n")

                df = pd.read_csv(f"raddata/az_tucson/AZ_TUCSON_20{year}.csv")
                df = df.groupby(['SAMPLE COLLECTION TIME', 'GAMMA COUNT RATE R02 (CPM)', 'GAMMA COUNT RATE R05 (CPM)', 'GAMMA COUNT RATE R09 (CPM)'])[['DOSE EQUIVALENT RATE (nSv/h)']].mean()

                df.reset_index(inplace=True)

            elif state == 'l' or state == 'L':
                year = input("Please choose the year to analyze and enter the last two digits, from between 08 and 21: ")
                print("\n")
                print(f"~~~Displaying radiation data from the Gamma detector in Baton Rouge, Louisiana for the year 20{year}~~~")
                print("")
                print("The X axis displays the Gamma detection count in Counts Per Minute (CPM)")
                print("The Y axis displays the data point count collected over the entire year, with January at the origin")
                print("\n")

                df = pd.read_csv(f"raddata/la_baton_rouge/LA_BATON_ROUGE_20{year}.csv")
                df = df.groupby(['SAMPLE COLLECTION TIME', 'GAMMA COUNT RATE R02 (CPM)', 'GAMMA COUNT RATE R05 (CPM)', 'GAMMA COUNT RATE R09 (CPM)'])[['DOSE EQUIVALENT RATE (nSv/h)']].mean()

                df.reset_index(inplace=True)

            elif state == 's' or state == 'S':
                year = input("Please choose the year to analyze and enter the last two digits, from between 06 and 21: ")
                print("\n")
                print(f"~~~Displaying radiation data from the Gamma detector in Boston, Massachussetts for the year 20{year}~~~")
                print("")
                print("The X axis displays the Gamma detection count in Counts Per Minute (CPM)")
                print("The Y axis displays the data point count collected over the entire year, with January at the origin")
                print("\n")

                df = pd.read_csv(f"raddata/ma_boston/MA_BOSTON_20{year}.csv")
                df = df.groupby(['SAMPLE COLLECTION TIME', 'GAMMA COUNT RATE R02 (CPM)', 'GAMMA COUNT RATE R05 (CPM)', 'GAMMA COUNT RATE R09 (CPM)'])[['DOSE EQUIVALENT RATE (nSv/h)']].mean()

                df.reset_index(inplace=True)

            elif state == 'm' or state == 'M':
                year = input("Please choose the year to analyze and enter the last two digits, from between 17 and 21: ")
                print("\n")
                print(f"~~~Displaying radiation data from the Gamma detector in Kalispell, Montana for the year 20{year}~~~")
                print("")
                print("The X axis displays the Gamma detection count in Counts Per Minute (CPM)")
                print("The Y axis displays the data point count collected over the entire year, with January at the origin")
                print("\n")

                df = pd.read_csv(f"raddata/mt_kalispell/MT_KALISPELL_20{year}.csv")
                df = df.groupby(['SAMPLE COLLECTION TIME', 'GAMMA COUNT RATE R02 (CPM)', 'GAMMA COUNT RATE R05 (CPM)', 'GAMMA COUNT RATE R09 (CPM)'])[['DOSE EQUIVALENT RATE (nSv/h)']].mean()

                df.reset_index(inplace=True)
            
            else:
                exit()

        except:
            print("Data Error")

        try:
            
            plt.title('Radiation Events over Time')
            plt.plotsize(120, 35)

            y1 = df['GAMMA COUNT RATE R02 (CPM)']
            y2 = df['GAMMA COUNT RATE R05 (CPM)']
            y3 = df['GAMMA COUNT RATE R09 (CPM)']

            plt.plot(y1, label="Gamma Detector Channel 02")
            plt.plot(y2, label="Gamma Detector Channel 05")
            plt.plot(y3, label="Gamma Detector Channel 09")

            plt.show()

        except:
            print("Graph Error")
