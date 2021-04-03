import rasterio as rst
import os
import pandas as pd
from rasterio.transform import from_origin
import numpy as np
import netCDF4 as nc
import gdal
import osr
destpath=r"F:\浒苔适生环境数据\WORDWIDE\\"
def rizhao(path,despath,res,lon=-179.75,lat=89.95):
    dataframe = pd.read_csv(path, index_col=0)
    result= dataframe.values
    result[result==99999]=0
    transform = from_origin(lon, lat, res, res)
    Z=result
    new_dataset = rst.open(despath, 'w', driver='GTiff', height=Z.shape[0], width=Z.shape[1], count=1,
                                dtype=Z.dtype, crs='+proj=latlong',transform=transform)
    new_dataset.write(Z, 1)
    new_dataset.close()
    return result

def sss(path,despath,res,lon=-179.875,lat=89.875):
    file_obj = nc.Dataset(path)
    sss = file_obj.variables['sss_smap'][:]
    data=np.array(sss)
    data[data==-9999]=0
    data_arr = np.asarray(data)
    data_arr = data_arr[::-1]  # 因为我的数据维度是正序排列，需要逆序一下
    var_lon = file_obj.variables['lon'][:]
    var_lat = file_obj.variables['lat'][:]

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

years=["2016","2017","2018","2019"]

chlapath=r"F:\浒苔适生环境数据\叶绿素浓度\\"
for year in years:
    for root, dirs, files in os.walk(chlapath+year+"\\"):
        for name in files:
            if name.split(".")[-1] == 'csv':
                date = name.split("_")[2]
                rizhao(chlapath + year+"\\"+name, destpath +"chla_"+ date + ".tif", 0.1)




sstpath=r"F:\浒苔适生环境数据\海面温度\\"
for year in years:
    for root, dirs, files in os.walk(sstpath + year + "\\"):
        for name in files:
            if name.split(".")[-1] == 'csv':
                date = name.split("_")[1]
                rizhao(sstpath + year + "\\" + name, destpath + "sst_" + date + ".tif", 0.1)


sstpath=r"F:\浒苔适生环境数据\日照\\"
for year in years:
    for root, dirs, files in os.walk(sstpath + year + "\\"):
        for name in files:
            if name.split(".")[-1] == 'csv':
                date = name.split("_")[3]
                rizhao(sstpath + year + "\\" + name, destpath + "rizhao_" + date + ".tif", 0.25,lon=-179.875,lat=89.875)

sstpath=r"F:\SSS\\"
for year in years:
    for root, dirs, files in os.walk(sstpath + year + "\\"):
        for name in files:
            if name.split(".")[-1] == 'nc':
                date = name.split("_")[5]+"_"+name.split("_")[6]
                sss(sstpath + year + "\\" + name, destpath + "sss_" + date + ".tif", 0.25)