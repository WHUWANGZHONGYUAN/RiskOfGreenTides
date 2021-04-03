import pandas as pd
import numpy as np
import rasterio
from rasterio.transform import from_origin

def rizhao(path,lonmin=119,lonmax=125,latmin=33.125,latmax=34.625):
    dataframe = pd.read_csv(path, index_col=0)
    lonmin = int((lonmin - (-180)) / 0.1)
    lonmax = int((lonmax - (-180)) / 0.1)
    latmin = int((89.95 - latmin) / 0.1) + 1
    latmax = int((89.95 - latmax) / 0.1) + 1
    result= dataframe.values[latmax:latmin, lonmin:lonmax]
    result[result==99999]=0
    return result

def write(path,Z,lonmin=119,latmax=34.625):
    res = 0.1
    transform = from_origin(lonmin, latmax, res, res)
    new_dataset = rasterio.open(path, 'w', driver='GTiff', height=Z.shape[0], width=Z.shape[1], count=1,
                                dtype=Z.dtype, crs='+proj=latlong', transform=transform)
    new_dataset.write(Z, 1)
    new_dataset.close()

def estimate(basepath,year,month,S1,S2,S3):
    path=basepath+year+r"\MY1DMM_CHLORA_"+year+"-"+month+"-01_3600x1800.csv"
    data=rizhao(path,latmin=S1,latmax=S2)
    write(basepath+"suit_"+year+"_" +month+'.tif',data,latmax=S2)
    data = rizhao(path,latmin=S2,latmax=S3)
    write(basepath + "unsuit_"+year+"_"  + month+'.tif', data,latmax=S3)
    data = rizhao(path, latmin=S1, latmax=S3)
    write(basepath + "all_"+year+"_" + month+'.tif', data, latmax=S3)

if __name__ == '__main__':
    path=r"G:\浒苔适生环境数据\\叶绿素浓度\\"
    estimate(path,'2016','05',S1=33.05,S2=34.65,S3=36.15)
    estimate(path, '2016', '06', S1=33.05, S2=34.95, S3=36.15)

    estimate(path,'2017','05',S1=28.35,S2=33.45,S3=36.95)

    estimate(path, '2018', '06', S1=32.85, S2=33.95, S3=36.15)

    estimate(path, '2019', '05', S1=33.85, S2=35.15, S3=36.45)
    estimate(path, '2019', '06', S1=33.85, S2=35.15, S3=36.45)

