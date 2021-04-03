import rasterio
from rasterio.enums import Resampling
import os
from rasterio.transform import from_origin
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


basepath=r"F:\浒苔适生环境数据\WORDWIDE\\"
destpath=r"F:\浒苔适生环境数据\WORDWIDE_Resample\\"
test=rasterio.open(basepath+"chla_2016-01-01.tif")
for root, dirs, files in os.walk(basepath):
    for name in files:
        if name.split(".")[-1]=='tif':
            chla_data=rasterio.open(basepath+name)
            transform = chla_data.transform

            transform = from_origin(transform[2], transform[5], 0.1, 0.1)

            chla_data=chla_data.read(1)
            resam(basepath+name,test.shape[0],test.shape[1],destpath+name,transform)

