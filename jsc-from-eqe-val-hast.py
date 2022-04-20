from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

q = 1.602*10**-19

sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=149062991"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
pd.set_option('display.width', None)
#LENGTH OF TRANSMISSION DATA IS 429
#len(df.index) = 429
df = pd.DataFrame(np.zeros([429, 7]))
#column 2, for etfe ctrl
newdf = pd.DataFrame(np.zeros([429*5, 9]))


set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 4]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 3] = val.iloc[i, 4]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end


#column 3, for pet ctrl
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 5]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 4] = val.iloc[i, 5]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 4, for etfe hast
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 6]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 5] = val.iloc[i, 6]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 5, for pet hast
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 7]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 6] = val.iloc[i, 7]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 8]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 7] = val.iloc[i, 8]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 7, for pet suv
set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 9]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 8] = val.iloc[i, 9]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end

newdf.iloc[:, 0] = val.iloc[:, 0]
newdf.iloc[:, 1] = val.iloc[:, 1]
newdf.iloc[:, 2] = val.iloc[:, 2]
newdf.columns = ['wavelength', 'EQE - cougar', 'Flux - AM1.5',
                 'STCH CTRL', 'PPE CTRL',
                 'STCH SUV24', 'PPE SUV24',
                 'STCH SUV100', 'PPE SUV100']

finalisc = pd.DataFrame(np.zeros([2145, 6]))

# stch ctrl
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 0] = q*newdf.iloc[i, 3] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
    #finalisc.iloc[i, 0] = val.iloc[i, 4] * \
    #       val.iloc[i, 2]*val.iloc[i, 1]*(1/10000)
# ppe ctrl
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 1] = q*newdf.iloc[i, 4] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
# stch 24
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 2] = q*newdf.iloc[i, 5] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
# ppe 24
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 3] = q*newdf.iloc[i, 6] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
# stch 100
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 4] = q*newdf.iloc[i, 7] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
# ppe 100
for i in range(0, len(newdf.index)):
    finalisc.iloc[i, 5] = q*newdf.iloc[i, 8] * \
            newdf.iloc[i, 2]*newdf.iloc[i, 1]*(1/10000)
print(finalisc)

finalisc.columns = ['a', 'b', 'c',
                    'd', 'e', 'f']
SUMA = finalisc['a'].sum()*(1/100)
print(SUMA)
SUMB = finalisc['b'].sum()*(1/100)
print(SUMB)
SUMC = finalisc['c'].sum()*(1/100)
print(SUMC)
SUMD = finalisc['d'].sum()*(1/100)
print(SUMD)
SUME = finalisc['e'].sum()*(1/100)
print(SUME)
SUMF = finalisc['f'].sum()*(1/100)
print(SUMF)


fig = go.Figure()
fig = make_subplots(rows=1, cols=2, subplot_titles=("wavelength vs Jsc (125 ETFE 50 POE)",
                                                    "wavelength vs Jsc (125 PET 50 POE)",))
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 3],
                         mode='markers',
                         name='etfe CTRL'), row=1, col=1)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 4],
                         mode='markers',
                         name='etfe HAST24'), row=1, col=1)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 5],
                         mode='markers',
                         name='etfe HAST100'), row=1, col=1)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 6],
                         mode='markers',
                         name='pet CTRL'), row=1, col=2)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 7],
                         mode='markers',
                         name='pet HAST24'), row=1, col=2)
fig.add_trace(go.Scatter(x=newdf.iloc[:, 0], y=newdf.iloc[:, 8],
                         mode='markers',
                         name='pet HAST100'), row=1, col=2)
fig.show()
