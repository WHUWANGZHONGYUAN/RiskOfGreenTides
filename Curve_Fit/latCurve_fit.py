import pandas as pd
import osr
import ogr
import seaborn  as sns
import numpy as np
import math
from sympy import *
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import root
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
#data=data[(data['stage']==1) & (data['year']!=2017)]
sns.set_style()
palette=sns.cubehelix_palette(4, start = 2, rot = 0, dark = 0.5, light = .95, reverse = True)

sns.lineplot(data=data,x='lat',y='m_area',hue='year',palette="light:blue", style="year",markers=True)
data=data[(data['stage']==1) & (data['year']==2019)]

#sns.lineplot(data=data,x='lat',y='m_area',hue='year',palette='colorblind')

def logis(x,A1,A2,a,x0):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))
bounds=([0,99.99,0,33], [0.01,100,10,35])
popt, pcov = curve_fit(logis, xdata=data['lat'].values, ydata=data['m_area'].values,bounds=bounds)
print(popt)
#print(pcov)



x=np.arange(32, 37, 0.1)
y=[]
for i in x:
    y.append((logis(i,popt[0],popt[1],popt[2],popt[3])))
    #y.append((logis(i, 0, 1, 1, 0)))
plt.plot(x,y)
plt.title("appearance")
plt.savefig(r"D:\坚果云文件\我的坚果云\浒苔适生环境研究\Curve\\lat.svg")
plt.show()

predicted=[]
for i in data['lat'].values:
    predicted.append((logis(i,popt[0],popt[1],popt[2],popt[3])))
print(r2_score(data['m_area'].values,predicted))
"""
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
f1 = np.polyfit(data['lat'].values, data['m_area'].values, 2)
print(f1)
p1 = np.poly1d(f1)
print('p1 is :',p1)
print(r2_score(data['m_area'].values,p1(data['lat'].values)))
x=np.arange(32, 37, 0.1)
y=[]
for i in x:
    y.append(p1(i))
sns.lineplot(data=data,x='lat',y='m_area',hue='year',palette='colorblind')
plt.plot(x,y)
plt.show()
"""


"""
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
data=data[(data['stage']==2)]
sns.lineplot(data=data,x='lat',y='m_area',hue='year',palette='colorblind')
plt.show()
bounds=([99.9,0,3,-100,33], [100, 0.01,10,100,37])
popt, pcov = curve_fit(logis, xdata=data['lat'].values, ydata=data['m_area'].values,bounds=bounds)
print(popt)
print(pcov)

x=np.arange(33,37, 0.1)
y=[]
for i in x:
    y.append((logis(i,popt[0],popt[1],popt[2],popt[3],popt[4])))
    #y.append((logis(i, 0, 1, 1, 0)))
plt.plot(x,y)
plt.title("decline")
plt.show()
"""