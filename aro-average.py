from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

pd.set_option('display.width', None)
df = pd.read_csv("C:/Users/Andrew Hu/Dropbox/PC/Downloads/AVA-O.txt")

MindexNames = df[(df.iloc[:, 7] >= 4)].index
df.drop(MindexNames, inplace=True)
print(df)


df.iloc[:, 7] = df["Label"].str.slice(1, 2)
#df = df.sort_values(by='Material', ascending=True)
df = df.sort_values(['Duration [hrs] 3', 'Material',
                    'Wavelength [nm]'], ascending=[False, True, False])


newdf = pd.DataFrame(np.zeros([len(df.index), 8]))
newdf.iloc[:, 5] = newdf.iloc[:, 5].round(decimals=5)

#df = df.iloc[0:10, :]
count = 1
for i in range(1, len(df.index)):
    if df.iloc[i, 6] == df.iloc[i-1, 6] and (df.iloc[i, 0] == df.iloc[i-1, 0]):
        count = count+1
    else:
        if count > 1:
            newdf.iloc[i, :] = df.iloc[i, :]
            newdf.iloc[i, 2] = (df.iloc[i, 2]+df.iloc[i-1, 2]) / count
        count = 1
    #print(count)
print(newdf.iloc[0:12, :])

newdf.to_csv(
    r'C:/Users/Andrew Hu/Dropbox/PC/Downloads/04-20-22-AROaverage.csv')
