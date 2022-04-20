import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math
q = 1.602*10**-19


#import csv data and initialize dataframes
sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=1059015030"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
pd.set_option('display.width', None)
#LENGTH OF TRANSMISSION DATA IS 429 #len(df.index) = 429
df = pd.DataFrame(np.zeros([463, 7]))
newdf = pd.DataFrame(np.zeros([463*5, 9]))


#repeats 5 times, as the transmission data is spaced to every 5 um wavelengths
#while the QE data is every 1 um wavelength
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 1]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 3] = val.iloc[i, 1]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 3, for pet ctrl
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 2]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 4] = val.iloc[i, 2]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 4, for etfe hast
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 3]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 5] = val.iloc[i, 3]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end


#portion where we convert val (raw google sheets csv) to a compact df, newdf with columns
newdf.iloc[:, 0] = val.iloc[:, 0]
newdf.iloc[:, 1] = val.iloc[:, 1]
newdf.iloc[:, 2] = val.iloc[:, 2]
newdf.columns = ['wavelength', 'EQE - cougar', 'Flux - AM1.5',
                 'STCH CTRL', 'PPE CTRL',
                 'STCH SUV24', 'PPE SUV24',
                 'STCH SUV100', 'PPE SUV100']

print(newdf)

#np . zeros = [A,B] , A is 463*5 , B is 6
#portion to calculate the current J per wavelength
finalisc = pd.DataFrame(np.zeros([2315*5, 6]))
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 0] = q*newdf.iloc[i, 3] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
    #finalisc.iloc[i, 0] = val.iloc[i, 4] * \
    #       val.iloc[i, 2]*val.iloc[i, 1]*(1/10000)
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 1] = q*newdf.iloc[i, 4] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 2] = q*newdf.iloc[i, 5] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
#print(finalisc)


#figure being scatter plotted and labeled
fig = go.Figure()
fig = make_subplots(rows=1, cols=3, subplot_titles=("EVA wavelength vs Transmittance (Full Spectrum)",
                                                    "Silicone wavelength vs Transmittance (Full Spectrum)",
                                                    "POE wavelength vs Transmittance (Full Spectrum)"))
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 3],
                         mode='markers',
                         name='EVA - A'), row=1, col=1)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 4],
                         mode='markers',
                         name='Silicone - A'), row=1, col=2)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 5],
                         mode='markers',
                         name='POE - A'), row=1, col=3)
#fig.update_xaxes(range=[150, 500])
fig.update_yaxes(range=[0, 100])
fig.update_layout(
    xaxis1_title="Wavelength",
    xaxis2_title="Wavelength",
    xaxis3_title="Wavelength",
    yaxis_title="Transmittance"
    )

fig.show()
