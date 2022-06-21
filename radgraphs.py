import plotext as plt
import pandas as pd

class graph:
    def radiation_graphs():
        try:

            df = pd.read_csv("testdata/AL_BIRMINGHAM_2020.csv")

            df = df.groupby(['SAMPLE COLLECTION TIME', 'GAMMA COUNT RATE R02 (CPM)', 'GAMMA COUNT RATE R05 (CPM)', 'GAMMA COUNT RATE R09 (CPM)'])[['DOSE EQUIVALENT RATE (nSv/h)']].mean()

            df.reset_index(inplace=True)

        except:
            print("Data Error")

        try:

            plt.title('Radiation Events over Time')
#            plt.clc()
            plt.plotsize(120, 35)
            plt.xlabel=("XLABEL")
            plt.ylabel=("YLABEL")

            y1 = df['GAMMA COUNT RATE R02 (CPM)']
            y2 = df['GAMMA COUNT RATE R05 (CPM)']
            y3 = df['GAMMA COUNT RATE R09 (CPM)']

            plt.plot(y1, label="Gamma Detector Channel 02")
            plt.plot(y2, label="Gamma Detector Channel 05")
            plt.plot(y3, label="Gamma Detector Channel 09")

        except:

            print("Graph Error")

        try:

            plt.show()
            

        except:
            print("Output Error")
