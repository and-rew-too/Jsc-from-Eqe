import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/andre/Downloads/All-101521-Modules.csv")
PARAM = "Isc_(A)"


MindexNames = df[(df.iloc[:, 5] <= 6.1) | (
    df.iloc[:, 11] <= 9) ].index
df.drop(MindexNames, inplace=True)

#condition to only choose a specific Batch_ID \ Project ID
Projstr = 'REFERENCE'
projectboolean = df[~df['Batch_ID'].str.contains(Projstr)]
df.drop(projectboolean.index, inplace=True)

IDstr = 'REFERENCE1-1X2'
#IDstr = 'REFERENCE2-1X1'
idboolean = df[~df['Sample_ID'].str.contains(IDstr)]
df.drop(idboolean.index, inplace=True)

#for i in range(1,len(df.index)) :
#    df['Measurement_Date-Time'] = str(df['Measurement_Date-Time'])
#    df['Measurement_Date-Time'] = datetime.strptime(df.iloc[i,4], '%d-%b-%y')
df['Measurement_Date-Time'] = pd.to_datetime(df['Measurement_Date-Time'], format='%d-%b-%y')


pmpmean = df[PARAM].mean()
print(pmpmean)
#Pmp standard deviation
P1 = (df[PARAM].sub(pmpmean)).pow(2)
P2 = P1.sum()
pmpSD = (P2 / len(df.index))**(1/2)

#pmpSD = df["Pmp_(W)"].std()
pmpUCL = pmpmean+pmpSD*3
pmpLCL = pmpmean-pmpSD*3

pmp2sigU = pmpmean+pmpSD*2
pmp2sigL = pmpmean-pmpSD*2
print(pmpLCL)



outside = []
xoutside = []
for i in range(0,len(df.index)) :
    a = df.columns.get_loc(PARAM)
    if (df.iloc[i, a] <= pmpLCL ):
        outside.append(df.iloc[i, a])
        xoutside.append(i+1)
        print('outside expected values, please review')
    else:
        pass
print(outside)
print(df)

#x = np.linspace(1, len(df.index), num=len(df.index))
fig, ax = plt.subplots(figsize = (10, 6))
ax.axhline(pmpUCL, color='red')
ax.axhline(pmpLCL, color='red')
ax.axhline(pmp2sigU, color='yellow')
ax.axhline(pmp2sigL, color='yellow')
# Create a chart title
#plt.scatter(x, df[PARAM], s=40, facecolors='none', edgecolors='b')
#plt.scatter(xoutside, outside,s=40, facecolors='none', edgecolors='r')
#plt.plot(x,df[PARAM], 'b-')
plt.plot(df["Measurement_Date-Time"],df[PARAM], 'b-')
plt.scatter(df["Measurement_Date-Time"], df[PARAM], s=40, facecolors='none', edgecolors='b')

ax.set_title('Reference-1x2 SPC Chart of ' + PARAM)
right = 1000
ax.set_xlim([datetime.date(2020, 11, 10), datetime.date(2021, 11, 3)])
ax.text(right + 0.3, pmpUCL, "UCL = " + str("{:.2f}".format(pmpUCL)), color='red')
ax.text(right + 0.3, pmpmean, r'$\bar{x}$' + " = " + str("{:.2f}".format(pmpmean)), color='green')
ax.text(right + 0.3, pmpLCL, "LCL = " + str("{:.2f}".format(pmpLCL)), color='red')
ax.set(xlabel='Observation', ylabel='Individual Value')


#import pygsheets
#gc = pygsheets.authorize(
#    service_file=r'C:\Users\andre\Downloads\fluent-outlet-329800-d7ce5f1f4cd1.json')
#sh = gc.open('PY to Gsheet Test') #open the google spreadsheet
#wks = sh[3] #select which sheet you want to use
#wks.set_dataframe(df.iloc[:120,:],(1,1)) #inside the sheet, now it gets updated with specific dataframe

plt.grid()
plt.show()
