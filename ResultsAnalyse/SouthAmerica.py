import fiona
import rasterio
import rasterio.mask
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
basepath=r"F:\实验对比分析数据\South_America_MBR\\"
with fiona.open(basepath+'MBR1.shp', 'r') as shapefile:
    geometry = [feature["geometry"] for feature in shapefile]

def non_zero_mean(np_arr):
    exist = (np_arr != 0)
    num = np_arr.sum()
    den = exist.sum()
    return num/den
def zonal(geometry,path):
    r_max=[]
    r_min=[]
    r_avg=[]
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
            r_max.append(np.max(out_image))
            out_image[np.isnan(out_image)] = 0
            out_image[out_image == 0] = np.nan

            r_min.append(np.nanmin(out_image))
            r_avg.append(np.nanmean(out_image))
            N_risk.append(np.sum(out_image>0.9)/np.sum(out_image>=0))
    return r_max,r_min,r_avg,N_risk

gridPath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\Union/"
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
        path=gridPath+"Union"+year+item+".tif"
        r_max,r_min,r_avg,n_risk=zonal(geometry,path)
        MAX.append(r_max)
        MIN.append(r_min)
        AVG.append(r_avg)
        N_risk.append(n_risk)

MAX=np.array(MAX)
MIN=np.array(MIN)
AVG=np.array(AVG)
N_risk=np.array(N_risk)
MAX[np.isnan(MAX)]=0
MIN[np.isnan(MIN)]=0
AVG[np.isnan(AVG)]=0
for j in range(2):
    if j == 0:
        name = "A"
    elif j == 1:
        name = "B"
    elif j == 2:
        name = "C"
    elif j == 3:
        name = 'D'
    length=MAX.shape[0]

    plt.figure(figsize=(10, 5))
    plt.plot(range(length), MAX[:, j], label="max")
    plt.scatter(range(length), MAX[:, j])
    plt.plot(range(length), MIN[:, j], label="min")
    plt.scatter(range(length), MIN[:, j])
    plt.plot(range(length), AVG[:, j], label="avg",color='#ff0000')
    plt.scatter(range(length), AVG[:, j])
    plt.title(name)
    plt.legend()
    plt.xticks(range(length),date)  ## 可以设置坐标字
    plt.show()
    plt.figure(figsize=(10, 5))
    plt.scatter(range(length), N_risk[:, j])
    plt.plot(range(length), N_risk[:, j], label="NUM",color='#ff0000')
    plt.xticks(range(length), date)  ## 可以设置坐标字
    plt.title(name)
    plt.show()



"""
with rasterio.open("cn_masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)
"""
import pandas as pd
df=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df['date']=date
df['min']=MIN[:,0]
df['max']=MAX[:,0]
df['avg']=AVG[:,0]
df['num']=N_risk[:,0]
df['region']='A'

df1=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df1['date']=date
df1['min']=MIN[:,1]
df1['max']=MAX[:,1]
df1['avg']=AVG[:,1]
df1['num']=N_risk[:,1]
df1['region']='B'



df=df.append(df1)

df['year']=df['date'].apply(lambda x:x[0:4])
df['day']=df['date'].apply(lambda x:x[4:6])
print(df)
df.to_csv(r'F:\实验对比分析数据\South_America_union.csv')