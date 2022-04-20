

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd


#import csv data and initialize dataframes 
sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=389223940"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

pd.set_option('display.width', None)


val = pd.read_csv(url_1,)
#df = pd.DataFrame(np.zeros([460, 13]))
#IGNORE COLUMNS 1,2,3
print(val)



finalisc = pd.DataFrame(np.zeros([92, 13]))
#GO FROM WAVELENGTH RANGE 200nm to 650nm
finalisc.columns = ['a', 'b', 'c',
                    'd', 
                    'e', 'f','g','h','i','j','k','l','m']

finalisc.iloc[:,0] = val.iloc[0:91,0]
finalisc.iloc[:,1] = val.iloc[0:91,1]
finalisc.iloc[:,2] = val.iloc[0:91,2]
finalisc.iloc[:,3] = val.iloc[0:91,3]
finalisc.iloc[:,4] = val.iloc[0:91,4]
finalisc.iloc[:,5] = val.iloc[0:91,5]
finalisc.iloc[:,6] = val.iloc[0:91,6]
finalisc.iloc[:,7] = val.iloc[0:91,7]
finalisc.iloc[:,8] = val.iloc[0:91,8]
finalisc.iloc[:,9] = val.iloc[0:91,9]
finalisc.iloc[:,10] = val.iloc[0:91,10]
finalisc.iloc[:,11] = val.iloc[0:91,11]
finalisc.iloc[:,12] = val.iloc[0:91,12]


#portion in which we sum the overall J, and determine the final Jsc
#has an additional 1/100 factor as the transmission data is in 90% instead of 0.9 
SUM1 = 5 * finalisc['e'].sum() 
print(SUM1)
SUM2 =  5 * finalisc['f'].sum()
print(SUM2)
SUM3 =  5 * finalisc['g'].sum()
print(SUM3)
SUM4 =  5 * finalisc['h'].sum()
print(SUM4)
SUM5 =  5 * finalisc['i'].sum()
print(SUM5)
SUM6 =  5 * finalisc['j'].sum()
print(SUM6)
SUM7 =  5 * finalisc['k'].sum()
print(SUM7)
SUM8 =  5 * finalisc['l'].sum()
print(SUM8)
SUM9 =  5 * finalisc['m'].sum()
print(SUM9)



#figure being scatter plotted and labeled 
fig = go.Figure()
fig = make_subplots(rows=1, cols=2, subplot_titles=("Full Wavelengths",
                                                    "Degraded Wavelengths, most and least samples,))
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 4],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 5],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 6],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 7],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 8],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 9],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 10],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)
fig.add_trace(go.Scatter(x=val.iloc[:, 0], y=val.iloc[:, 11],
                         mode='markers',
                         name='ALL post-suv'), row=1, col=1)


#MOST DEGRADED
fig.add_trace(go.Scatter(x=finalisc.iloc[:, 0], y=finalisc.iloc[:, 8],
                         mode='markers',
                         name='1-4 UV region'), row=1, col=2)
#LEAST DEGRADED
fig.add_trace(go.Scatter(x=finalisc.iloc[:, 0], y=finalisc.iloc[:, 4],
                         mode='markers',
                         name='1-1 UV region'), row=1, col=2)
#MINUS BETWEEN MOST AND LEAST
fig.add_trace(go.Scatter(x=finalisc.iloc[:, 0], y=finalisc.iloc[:, 4]-finalisc.iloc[:,8],
                         mode='markers',
                         name='Difference Between'), row=1, col=2)
fig.show()
