import pandas as pd
import numpy as np
import rasterio
from rasterio.transform import from_origin

def rizhao(path,lonmin=119,lonmax=125,latmin=33.125,latmax=34.625):
    dataframe = pd.read_csv(path, index_col=0)
    lonmin = int((lonmin - (-180)) / 0.25)
    lonmax = int((lonmax - (-180)) / 0.25)
    latmin = int((89.875 - latmin) / 0.25) + 1
    latmax = int((89.875 - latmax) / 0.25) + 1
    return dataframe.values[latmax:latmin, lonmin:lonmax]

def write(path,Z,lonmin=119,latmax=34.625):
    res = 0.25
    transform = from_origin(lonmin, latmax, res, res)
    new_dataset = rasterio.open(path, 'w', driver='GTiff', height=Z.shape[0], width=Z.shape[1], count=1,
                                dtype=Z.dtype, crs='+proj=latlong', transform=transform)
    new_dataset.write(Z, 1)
    new_dataset.close()

def estimate(basepath,year,month,S1,S2,S3):
    path=basepath+year+r"\CERES_INSOL_M_"+year+"-"+month+"-01_1440x720.csv"
    data=rizhao(path,latmin=S1,latmax=S2)
    write(basepath+"suit_"+year+"_" +month+'.tif',data,latmax=S2)
    data = rizhao(path,latmin=S2,latmax=S3)
    write(basepath + "unsuit_"+year+"_"  + month+'.tif', data,latmax=S3)
    data = rizhao(path, latmin=S1, latmax=S3)
    write(basepath + "all_"+year+"_" + month+'.tif', data, latmax=S3)

if __name__ == '__main__':
    path=r"G:\浒苔适生环境数据\\日照\\"
    estimate(path,'2016','05',S1=33.125,S2=34.625,S3=36.125)
    estimate(path, '2016', '06', S1=33.125, S2=34.625, S3=36.125)

    estimate(path,'2017','05',S1=28.375,S2=33.375,S3=36.875)

    estimate(path, '2018', '06', S1=32.875, S2=33.875, S3=36.125)

    estimate(path, '2019', '05', S1=33.875, S2=35.125, S3=36.375)
    estimate(path, '2019', '06', S1=33.875, S2=35.125, S3=36.375)

