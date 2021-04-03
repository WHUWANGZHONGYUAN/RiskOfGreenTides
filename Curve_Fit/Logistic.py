import pandas as pd
import osr
import ogr
import seaborn  as sns
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
""""""
data2016=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\2016ULVACH.csv")
data2017=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\2017ULVACH2.csv")
data2018=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\2018ULVACH.csv")
data2019=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\2019ULVACH2.csv")
def minmax(data):
    data['m_area'] =100* (data['area']-data['area'].min())/(data['area'].max()-data['area'].min())
    return data

data2016=minmax(data2016)
data2017=minmax(data2017)
data2018=minmax(data2018)
data2019=minmax(data2019)

data=data2016.append(data2019)
data=data.append(data2018)
data=data.append(data2017)

source = osr.SpatialReference()
source.ImportFromEPSG(32651)

target = osr.SpatialReference()
target.ImportFromEPSG(4326)
transform = osr.CoordinateTransformation(source, target)

def getLat(dataframe,x,y):
    source = osr.SpatialReference()
    source.ImportFromEPSG(32651)
    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(source, target)
    point = ogr.CreateGeometryFromWkt("POINT ("+str(dataframe[x])+" "+ str(dataframe[y])+")")
    point.Transform(transform)
    lat=float(str(point.ExportToWkt()).split(" ")[1][1:-1])
    return lat

def getLon(dataframe,x,y):
    source = osr.SpatialReference()
    source.ImportFromEPSG(32651)
    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(source, target)
    point = ogr.CreateGeometryFromWkt("POINT ("+str(dataframe[x])+" "+ str(dataframe[y])+")")
    point.Transform(transform)
    lon=float(str(point.ExportToWkt()).split(" ")[2][0:-1])
    return lon
#print(projection(434799.7778,3719653.793))

data['lat']=data.apply(getLat,axis=1,args=('POINT_X','POINT_Y'))
data['lon']=data.apply(getLon,axis=1,args=('POINT_X','POINT_Y'))

"""
sns.lineplot(data=data,x='lon',y='m_area',hue='year',palette='colorblind')
plt.show()
sns.lineplot(data=data,x='lat',y='m_area',hue='year',palette='colorblind')
plt.show()
sns.lineplot(data=data,x='keyday',y='m_area',hue='year',palette='colorblind')
plt.show()
"""


data.to_csv(r"D:\坚果云文件\我的坚果云\舆情\\curve_data.csv")

"""
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
data=data[data['stage']==1]

sns.lineplot(data=data,x='lat',y='m_area',palette='colorblind')
plt.show()
def logis(x,A1,A2,x0,p):
    return A2+((A1-A2)/(1+np.power((x/x0),p)))
bounds=([0,0,33,0], [100, 100,37,5])
popt, pcov = curve_fit(logis, xdata=data['lat'].values, ydata=data['m_area'].values,bounds=bounds)
print(popt)
print(pcov)

x=range(33,37,1)
y=[]
for i in x:
    y.append((logis(i,popt[0],popt[1],popt[2],popt[3])))
    #y.append((logis(i, 0, 1, 1, 0)))
plt.plot(x,y)
plt.show()
"""

