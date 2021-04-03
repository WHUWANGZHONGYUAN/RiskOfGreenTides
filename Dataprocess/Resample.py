import rasterio
from rasterio.enums import Resampling
import os
import numpy as np
chla=r"G:\浒苔适生环境数据\叶绿素浓度\\"
rizhao=r"G:\浒苔适生环境数据\日照\\"
SST=r"G:\浒苔适生环境数据\海面温度\\"
SSS=r"G:\SSS\\"
res=r"G:\Resample\\"
import shutil


def resam(path,height,width,destpath,transform):
    with rasterio.open(path) as dataset:
        data = dataset.read(
            out_shape=(height, width, dataset.count),
            resampling=Resampling.nearest
        )
        profile=dataset.profile
        profile.update(height=height)
        profile.update(width=width)
        profile.update(transform=transform)
        data=dataset.read(1)
        with rasterio.open(destpath,'w',**profile) as dst:
            dst.write(data,1)


for root, dirs, files in os.walk(chla):
    for name in files:
        if name.split(".")[-1]=='tif':
            print(os.path.join(root, name))
            chla_data=rasterio.open(chla+name)
            transform=chla_data.transform
            chla_data=chla_data.read(1)
            resam(rizhao+name,chla_data.shape[0],chla_data.shape[1],res+'Rizhao_' + name,transform)
            resam(SSS + name, chla_data.shape[0], chla_data.shape[1], res +'SSS_'+ name,transform)
            shutil.copy(chla+name,res+'CHLA_' + name)
            shutil.copy(SST + name, res + 'SST_' + name)





