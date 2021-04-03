import pandas as pd
import osr
import ogr
import seaborn  as sns
import numpy as np
import math

from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
#source=data[(data['stage']==1) & (data['year']==2018)]
source=data
sns.lineplot(data=source,x='keyday',y='m_area',hue='year',markers=True,style="year",palette="light:blue")#
data=data[(data['stage']==1) & (data['year']==2018)]
def logis(x,A1,A2,a,x0):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))
def fit(x,a,b,c,d):
    return a*x*x*x+b*x*x+c*x+d
bounds=([0,99.99,0,155], [0.01,100,10,170])
#popt, pcov = curve_fit(logis, xdata=data['keyday'].values, ydata=data['m_area'].values,bounds=bounds)
#print(popt)
x=np.arange(110, 210, 0.1)
y=[]
for i in x:
    y.append((fit(i+10,-0.000762,0.3526,-52.13 ,2500)))
    #y.append((logis(i, 0, 1, 1, 0)))
plt.plot(x,y)
plt.title("appearance")
plt.ylim(-5,105)
plt.savefig(r"D:\坚果云文件\我的坚果云\浒苔适生环境研究\Curve\\keyday.svg")
plt.show()
