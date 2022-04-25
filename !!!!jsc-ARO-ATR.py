import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=1380123471"
url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
pd.set_option('display.width', None)



def atr_measure(letternumber):
    atrdf = pd.DataFrame(np.zeros([461,3]))
    ONE = pd.DataFrame(np.zeros([461,1]))+ 100
    atrdf.iloc[:,0] = df[letternumber + ' REF']
    atrdf.iloc[:,1] = df[letternumber + ' TRANS']
    #for i in range(len(atrdf.index)):
    atrdf.iloc[:,2] = ONE.iloc[:,0] - (atrdf.iloc[:,0] + atrdf.iloc[:,1]) #absorbance
    return atrdf



prsuvO = atr_measure('O7')
print(prsuvO.iloc[:,2])
print(df)
psuvO = atr_measure('O2')


prsuvL = atr_measure('N7')
psuvL = atr_measure('N3')


fig = go.Figure()
fig = make_subplots(rows=1, cols=2, subplot_titles=("O groups",
                                                    "L groups"))
fig.update_yaxes(range=[0, 100], row=1, col=1)
fig.update_yaxes(range=[0, 100], row=1, col=2)

fig.update_xaxes(range=[200, 500], row=1, col=1)
fig.update_xaxes(range=[200, 500], row=1, col=2)


fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvO.iloc[:,0],
                    mode='lines',
                    name='ref'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvO.iloc[:,1],
                    mode='lines',
                    name='trans'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvO.iloc[:,2],
                    mode='lines',
                    name='abs'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvO.iloc[:,0],
                    mode='lines',
                    name='ref'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvO.iloc[:,1],
                    mode='lines',
                    name='trans'),row=1, col=1)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvO.iloc[:,2],
                    mode='lines',
                    name='abs'),row=1, col=1)


fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvL.iloc[:,0],
                    mode='lines',
                    name='ref'),row=1, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvL.iloc[:,1],
                    mode='lines',
                    name='trans'),row=1, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=prsuvL.iloc[:,2],
                    mode='lines',
                    name='abs'),row=1, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvL.iloc[:,0],
                    mode='lines',
                    name='ref'),row=1, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvL.iloc[:,1],
                    mode='lines',
                    name='trans'),row=1, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=psuvL.iloc[:,2],
                    mode='lines',
                    name='abs'),row=1, col=2)
fig.show()
