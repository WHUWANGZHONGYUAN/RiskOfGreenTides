import fiona
import rasterio
import rasterio.mask
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
basepath=r"F:\实验对比分析数据\Europe_MBR\\"
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
            N_risk.append(np.sum(out_image > 0.7) / np.sum(out_image > 0))
    return r_max,r_min,r_avg,N_risk

gridPath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge/"
year='2018'
month=['01','02','03','04','05','06','07','08','09','10','11','12']
MAX=[]
MIN=[]
AVG=[]
N_risk=[]
for item in month:
    path=gridPath+"Merge"+year+item+".tif"
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
for j in range(4):
    if j == 0:
        name = "A"
    elif j == 1:
        name = "B"
    elif j == 2:
        name = "C"
    elif j == 3:
        name = 'D'
    plt.plot(month, MAX[:, j], label="max")
    plt.scatter(month, MAX[:, j])
    plt.plot(month, MIN[:, j], label="min")
    plt.scatter(month, MIN[:, j])
    plt.plot(month, AVG[:, j], label="avg",color='#ff0000')
    plt.scatter(month, AVG[:, j])
    plt.plot(month, N_risk[:, j], label="avg", color='#ff0000')
    plt.scatter(month, N_risk[:, j])
    plt.title( ":" + name)
    plt.legend()
    plt.show()




import pandas as pd
df=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df['date']=month
df['max']=MAX[:, 0]
df['min']=MIN[:, 0]
df['avg']=AVG[:, 0]
df['num']=N_risk[:, 0]
df['region']='A'

df1=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df1['date']=month
df1['max']=MAX[:, 1]
df1['min']=MIN[:, 1]
df1['avg']=AVG[:, 1]
df1['num']=N_risk[:, 1]
df1['region']='B'

df2=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df2['date']=month
df2['max']=MAX[:, 2]
df2['min']=MIN[:, 2]
df2['avg']=AVG[:, 2]
df2['num']=N_risk[:, 2]
df2['region']='C'

df3=pd.DataFrame(columns=['date','min','max','avg','num','region'])
df3['date']=month
df3['max']=MAX[:, 3]
df3['min']=MIN[:, 3]
df3['avg']=AVG[:, 3]
df3['num']=N_risk[:, 3]
df3['region']='D'

df=df.append(df1)
df=df.append(df2)
df=df.append(df3)
df.to_csv('F:\实验对比分析数据\Europe_merge.csv')