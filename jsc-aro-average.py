from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd


pd.set_option('display.width', None)
df = pd.read_csv(r"C:\Users\andre\Downloads\AVA-O.txt")
MindexNames = df[(df.iloc[:, 7] >= 4)].index
df.drop(MindexNames, inplace=True)

df.iloc[:, 7] = df["Label"].str.slice(1, 2)
df = df.sort_values(['Wavelength [nm]', 'Material'
                    ], ascending=[True, True])




projectboolean = df[~df['Part ID'].str.contains('N3')]
df.drop(projectboolean.index, inplace=True)
print(df)







projectboolean = df[~df['Duration [hrs]'].str.contains('0_')]
df.drop(projectboolean.index, inplace=True)
print(df)


fig = go.Figure()
fig = make_subplots(rows=1, cols=2, subplot_titles=("O groups",
                                                    "L groups"))

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,2],
                    mode='lines',
                    name='ref'),row=1, col=2)
#fig.show()
exit()

df.to_csv(
    r"\Users\andre\Downloads\N3-temp.csv")

