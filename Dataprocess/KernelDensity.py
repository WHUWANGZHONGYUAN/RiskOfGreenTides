import rasterio as rst
import os
import numpy as np
import pandas as pd
basepath=r"D:\Ulva\KERNEL\\"

pdpath=r"D:\坚果云文件\我的坚果云\舆情\all.csv"
data=pd.read_csv(pdpath)

def getKer(dataframe,x,y):
    year=dataframe['year']
    keyday=dataframe['keyday']
    path=basepath+"K"+str(int(year))+str(int(keyday))+".tif"
    ker=0
    with rst.open(path) as dst:
        data=dst.read(1)
        ker=np.max(data)-np.min(data)
    return ker

data['ker']=data.apply(getKer,axis=1,args=('year','keyday'))
data['agg']=data['area']/(data['MBG_Width']*data['MBG_Length']*0.000001)
data.to_csv(r"D:\坚果云文件\我的坚果云\舆情\density_agg_ca.csv")