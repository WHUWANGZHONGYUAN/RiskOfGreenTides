import fiona
import rasterio
import rasterio.mask
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
basepath=r"F:\实验对比分析数据\YellowSea_MBR\\"
with fiona.open(basepath+'MBR2.shp', 'r') as shapefile:
    geometry = [feature["geometry"] for feature in shapefile]

def zonal(geometry,path):
    N_risk=[]
    with rasterio.open(path) as src:
        shapes = []
        for item in geometry:
            shapes.append(item)
            out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)

            out_image=out_image[0]
            out_meta = src.meta
            out_meta.update({
                "driver": "GTiff",
                "height": out_image.shape[0],
                "width": out_image.shape[1],
                "transform": out_transform
            })
            shapes = []
            N_risk.append(np.sum(out_image>0.9)/np.sum(out_image>=0))
    return N_risk

gridPath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge/"
years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
MAX=[]
MIN=[]
AVG=[]
date=[]
N_risk=[]
for year in years:
    for item in month:
        name=year+item
        if (name=='201601') or (name=='201907') or (name=='201908') or (name=='201910') or (name=='201911' )or (name=='201912'):
            continue
        date.append(year+item)
        path=gridPath+"Merge"+year+item+".tif"
        n_risk=zonal(geometry,path)
        N_risk.append(n_risk)

N_risk=np.array(N_risk)
for j in range(4):
    if j == 0:
        name = "A"
    elif j == 1:
        name = "B"
    elif j == 2:
        name = "C"
    elif j == 3:
        name = 'D'
    length=N_risk.shape[0]

    plt.figure(figsize=(10, 5))
    plt.scatter(range(length), N_risk[:, j])
    plt.plot(range(length), N_risk[:, j], label="NUM",color='#ff0000')
    plt.xticks(range(length), date)  ## 可以设置坐标字
    plt.title(name)
    plt.show()


import pandas as pd
dataframe=pd.read_csv(r"F:\实验对比分析数据\yellow_sea_union_risk(M).csv")
dataframe=dataframe[dataframe['region']=='A']
def setAccuracy(dataframe,month,num):
    x=0

    if (dataframe[month]==6) or (dataframe[month]==6) or (dataframe[month]==7):
        x=dataframe['num']
    else:
        x=1-dataframe['num']
    return x

def setMAR(dataframe,month,num):
    x=0
    if (dataframe[month]==6) or (dataframe[month]==6) or (dataframe[month]==7):
        x=1-dataframe['num']
    else:
        x=0
    return x

def setFAR(dataframe,month,num):
    x=0
    if (dataframe[month]==6) or (dataframe[month]==6) or (dataframe[month]==7):
        x=0
    else:
        x=dataframe['num']
    return x

dataframe['MAR']=dataframe.apply(setMAR,axis=1,args=('Month','num'))
dataframe['FAR']=dataframe.apply(setFAR,axis=1,args=('Month','num'))
dataframe['Accuracy']=dataframe.apply(setAccuracy,axis=1,args=('Month','num'))
dataframe.to_csv('MAR_FAR_ACCURACY.csv')
import seaborn as sns
fig=sns.barplot(data=dataframe,x='Month',y='Accuracy',hue='year')
fig.legend(loc='center right', bbox_to_anchor=(1,0.1), ncol=1)
plt.title("Accuracy")
plt.show()

fig=sns.barplot(data=dataframe,x='Month',y='FAR',hue='year')
fig.legend(loc='center right', bbox_to_anchor=(1,0.1), ncol=1)
plt.title("FAR")
plt.show()

fig=sns.barplot(data=dataframe,x='Month',y='MAR',hue='year')
fig.legend(loc='center right', bbox_to_anchor=(1,0.1), ncol=1)
plt.title("MAR")
plt.show()