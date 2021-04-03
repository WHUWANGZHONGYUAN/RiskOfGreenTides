import numpy as np
import netCDF4 as nc
import rasterio
from rasterio.transform import from_origin

file_obj = nc.Dataset(r"G:\SSS\2016\\RSS_smap_SSS_L3_monthly_2016_01_FNL_v04.0.nc")
print(file_obj)
print(file_obj.variables['lat'][:].shape)
print(file_obj.variables['lon'][:].shape)

def sss(path,lonmin=118.875,lonmax=125.125,latmin=33.125,latmax=34.625):
    file_obj = nc.Dataset(path)
    sss = file_obj.variables['sss_smap'][:]
    lonmin = int(lonmin / 0.25)
    lonmax = int(lonmax/ 0.25)
    latmin = int((latmin+89.875) / 0.25) + 1
    latmax = int((latmax+89.875) / 0.25) + 1
    result=np.array(sss[latmin:latmax, lonmin:lonmax])
    result[result==-9999]=np.nan
    return result

def write(path,Z,lonmin=118.875,latmax=34.625):
    res = 0.25
    transform = from_origin(lonmin, latmax, res, res)
    new_dataset = rasterio.open(path, 'w', driver='GTiff', height=Z.shape[0], width=Z.shape[1], count=1,
                                dtype=Z.dtype, crs='+proj=latlong', transform=transform)
    new_dataset.write(Z, 1)
    new_dataset.close()


def estimate(basepath,year,month,S1,S2,S3):
    path=basepath+year+r"\RSS_smap_SSS_L3_monthly_"+year+"_"+month+"_FNL_v04.0.nc"
    data=sss(path,latmin=S1,latmax=S2)
    write(basepath+"suit_"+year+"_" +month+'.tif',data,latmax=S2)
    data = sss(path,latmin=S2,latmax=S3)
    write(basepath + "unsuit_"+year+"_"  + month+'.tif', data,latmax=S3)
    data = sss(path, latmin=S1, latmax=S3)
    write(basepath + "all_"+year+"_" + month+'.tif', data, latmax=S3)

if __name__ == '__main__':
    path=r"G:\SSS\\"
    estimate(path,'2016','05',S1=33.125,S2=34.625,S3=36.125)
    estimate(path, '2016', '06', S1=33.125, S2=34.625, S3=36.125)

    estimate(path,'2017','05',S1=28.375,S2=33.375,S3=36.875)

    estimate(path, '2018', '06', S1=32.875, S2=33.875, S3=36.125)

    estimate(path, '2019', '05', S1=33.875, S2=35.125, S3=36.375)
    estimate(path, '2019', '06', S1=33.875, S2=35.125, S3=36.375)