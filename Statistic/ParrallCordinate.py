import os
import rasterio as rst
import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates
from matplotlib import pyplot as plt
import seaborn as sns


basepath=r"G:\浒苔适生环境数据\Resample\\"
attribute=['CHLA','Rizhao','SST','SSS']
year=['2016','2016','2017','2018','2019','2019']
month=['05','06','05','06','05','06']

def dataprocess(basepath,year,month,attribute):
    suitpath = basepath + attribute + "_suit_" + year + "_" + month + ".tif"
    unsuitpath = basepath + attribute + "_unsuit_" + year + "_" + month + ".tif"
    suit = rst.open(suitpath).read(1)
    unsuit = rst.open(unsuitpath).read(1)
    suit = suit.reshape(suit.shape[0] * suit.shape[1], )
    unsuit = unsuit.reshape(unsuit.shape[0] * unsuit.shape[1], )
    suit[np.isnan(suit)]=0
    unsuit[np.isnan(unsuit)]=0
    #index=( suit==0 | np.isnan(suit) )
    #index2 = (unsuit==0 | np.isnan(unsuit))
    #suit = np.delete(suit, index)
    #unsuit = np.delete(unsuit, index2)
    return suit,unsuit

suit=[]
unsuit=[]
dataframe=pd.DataFrame(columns=["SST",'CHLA','SSS','Rizhao','suit','date'])
for i in range(len(year)):
    suitFrame = pd.DataFrame(columns=["SST", 'CHLA', 'SSS', 'Rizhao', 'suit','date'])
    unsuitFrame = pd.DataFrame(columns=["SST", 'CHLA', 'SSS', 'Rizhao', 'suit','date'])
    for item in attribute:
        s,u=dataprocess(basepath,year[i],month[i],item)
        suitFrame[item]=s
        suitFrame['date']=year[i]+"_"+month[i]
        suitFrame['suit']=np.ones(s.shape[0])
        unsuitFrame[item] = u
        unsuitFrame['date'] = year[i] + "_" + month[i]
        unsuitFrame['suit'] = np.zeros(u.shape[0])

    dataframe=dataframe.append(suitFrame)
    dataframe=dataframe.append(unsuitFrame)

for i in attribute:
    dataframe=dataframe[dataframe[i]!=0]
print(dataframe)
"""
max_min_scaler = lambda x : 100*(x-np.min(x))/(np.max(x)-np.min(x))

dataframe['SST']=dataframe[['SST']].apply(max_min_scaler)
dataframe['SSS']=dataframe[['SSS']].apply(max_min_scaler)
dataframe['CHLA']=dataframe[['CHLA']].apply(max_min_scaler)
dataframe['Rizhao']=dataframe[['Rizhao']].apply(max_min_scaler)
"""

dataframe['suit']=dataframe['suit'].apply(lambda x: 'suit' if x==1 else 'unsuit')

sns.boxplot(y="SST", hue="suit", data=dataframe,x='date',)
plt.savefig(r"G:\浒苔适生环境数据\Resample\SST_box.jpg",dpi=300)
plt.show()
sns.boxplot(y="SSS", hue="suit", data=dataframe,x='date')
plt.savefig(r"G:\浒苔适生环境数据\Resample\SSS_box.jpg",dpi=300)
plt.show()
sns.boxplot(y="CHLA", hue="suit", data=dataframe,x='date')
plt.savefig(r"G:\浒苔适生环境数据\Resample\CHLA_box.jpg",dpi=300)
plt.show()
sns.boxplot(y="Rizhao", hue="suit", data=dataframe,x='date')
plt.savefig(r"G:\浒苔适生环境数据\Resample\Rizhao_box.jpg",dpi=300)
plt.show()
"""
parallel_coordinates(dataframe,'suit',color=['red','blue'])
#plt.savefig(r"G:\浒苔适生环境数据\Resample\normal_all.jpg",dpi=300)
plt.show()
#suit=np.array(suit)
#unsuit=np.array(unsuit)

suitframe=dataframe[dataframe['suit']=='suit']
parallel_coordinates(suitframe,'suit',color=['red','blue'])
#plt.savefig(r"G:\浒苔适生环境数据\Resample\normal_suit.jpg",dpi=300)
plt.show()

unsuitframe=dataframe[dataframe['suit']=='unsuit']
parallel_coordinates(unsuitframe,'suit',color=['blue'])
#plt.savefig(r"G:\浒苔适生环境数据\Resample\normal_unsuit.jpg",dpi=300)

plt.show()
"""