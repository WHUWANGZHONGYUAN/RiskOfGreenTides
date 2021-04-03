import rasterio
from rasterio.transform import from_origin
from SeaWind.windsat_averaged_v7 import WindSatAveraged
import numpy as np
import gdal
import osr
import pylab as plt
from matplotlib import cm
wspdname = 'w-aw'
wdirname = 'wdir'
missing = -999.
def read_data(filename='wsat_201601v7.0.1.gz'):
    dataset = WindSatAveraged(filename, missing=missing)
    #if not dataset.variables: sys.exit('file not found')
    return dataset

def set_image(vmin,vmax,extent):
    myimage = {}
    myimage['origin'] = 'lower'
    myimage['vmin'] = vmin
    myimage['vmax'] = vmax
    myimage['extent'] = extent
    myimage['interpolation'] = 'nearest'
    return myimage

def get_data(dataset,wspdname,wdirname):
    wspd = dataset.variables[wspdname]
    wdir = dataset.variables[wdirname]
    land = dataset.variables['land']
    lon = dataset.variables['longitude']
    lat = dataset.variables['latitude']
    wspd[land] = -999.
    wdir[land] = -999.
    return wdir,wspd,lon,lat

def write(path,Z,lonmin=0,latmax=90):
    res = 0.25
    transform = from_origin(lonmin, latmax, res, res)
    new_dataset = rasterio.open(path, 'w', driver='GTiff', height=Z.shape[0], width=Z.shape[1], count=1,
                                dtype=Z.dtype, crs='+proj=latlong', transform=transform)
    new_dataset.write(Z, 1)
    new_dataset.close()

def write_windsat(despath,data,var_lon,var_lat,res=0.25,lon=-179.875,lat=89.875):
    data_arr = np.asarray(data)
    data_arr = data_arr[::-1]  # 因为我的数据维度是正序排列，需要逆序一下
    LonMin, LatMax, LonMax, LatMin = [var_lon.min(), var_lat.max(), var_lon.max(), var_lat.min()]
    N_Lat=len(var_lat)
    N_Lon = len(var_lon)
    Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
    Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)
    driver = gdal.GetDriverByName('GTiff')
    out_tif_name = despath
    out_tif = driver.Create(out_tif_name, N_Lon, N_Lat, 1, gdal.GDT_Float32)  # 创建框架

    # 设置影像的显示范围
    # Lat_Res一定要是-的
    geotransform = (LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res)

    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)  # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
    out_tif.SetProjection(srs.ExportToWkt())  # 给新建图层赋予投影信息

    out_tif.SetGeoTransform(geotransform)
    out_tif.GetRasterBand(1).WriteArray(data_arr)  # 将数据写入内存，此时没有写入硬盘
    out_tif.FlushCache()  # 将数据写入硬盘
    out_tif = None  # 注意必须关闭tif文件
    return data
dataset=read_data("wsat_201601v7.0.1.gz")
wdir,wspd,lon,lat=get_data(dataset,wspdname,wdirname)


years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for y in years:
    for m in month:
        path=r"F:\浒苔适生环境数据\SeaWind\\wsat_"+y+m+"v7.0.1.gz"
        dataset = read_data(path)
        wdir, wspd, lon, lat = get_data(dataset, wspdname, wdirname)
        dirpath=r"F:\浒苔适生环境数据\WDIR\dir_"+y+m+".tif"
        spdpath=r"F:\浒苔适生环境数据\WSPD\spd_"+y+m+".tif"
        write_windsat(dirpath, wdir, lon, lat)
        write_windsat(spdpath, wspd, lon, lat)
