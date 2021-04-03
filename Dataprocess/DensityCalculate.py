import arcpy as ap
from arcpy import env
import os
"""
basepath=r'D:\Ulva(2016-2018)\2016shp\\'
env.workspace=basepath
env.overwriteOutput=True
shplist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='shp' and name[-5]!='R':
            if name[0]=='G':
                shplist.append(name)


for item in shplist:
    inFeatures = item
    valField = "CLASS_ID"
    outRaster = basepath+r"RASTER\\"+item.split(".")[0]+'.tif'
    print(outRaster)
    assignmentType = "MAXIMUM_AREA"
    priorityField = "NONE"
    cellSize = 250
    ap.PolygonToRaster_conversion(in_features=inFeatures, value_field=valField, out_rasterdataset=outRaster,cellsize=cellSize)

basepath=r'D:\Ulva(2016-2018)\2017shp\\'
env.workspace=basepath
env.overwriteOutput=True
shplist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='shp' and name[-5]!='R':
            if name[0]=='G':
                shplist.append(name)


for item in shplist:
    inFeatures = item
    valField = "CLASS_ID"
    outRaster = basepath+r"RASTER\\"+item.split(".")[0]+'.tif'
    print(outRaster)
    assignmentType = "MAXIMUM_AREA"
    priorityField = "NONE"
    cellSize = 250
    ap.PolygonToRaster_conversion(in_features=inFeatures, value_field=valField, out_rasterdataset=outRaster,cellsize=cellSize)


basepath=r'D:\Ulva(2016-2018)\2018ROI\\'
env.workspace=basepath
env.overwriteOutput=True
shplist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='shp' and name.find('GREEN')>=0:
                shplist.append(name)
for item in shplist:
    inFeatures = item
    valField = "CLASS_ID"
    outRaster = basepath+r"RASTER\\"+item.split(".")[0]+'.tif'
    print(outRaster)
    assignmentType = "MAXIMUM_AREA"
    priorityField = "NONE"
    cellSize = 250
    ap.PolygonToRaster_conversion(in_features=inFeatures, value_field=valField, out_rasterdataset=outRaster,cellsize=cellSize)

"""
basepath=r'D:\Ulva\2018ROI\RASTER\\'
env.workspace=basepath
env.overwriteOutput=True
TIFlist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                TIFlist.append(name)
                print(basepath + name)

for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                print(basepath+name[0:7]+".shp")

basepath=r'D:\Ulva\2017shp\RASTER\\'
env.workspace=basepath
env.overwriteOutput=True
TIFlist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                TIFlist.append(name)
                print(basepath + name)

for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                print(basepath+name.split('.')[0].split('G')[1]+".shp")

basepath=r'D:\Ulva\2016shp\RASTER\\'
env.workspace=basepath
env.overwriteOutput=True
TIFlist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                TIFlist.append(name)
                print(basepath + name)

for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                print(basepath+name.split('.')[0].split('G')[1]+".shp")

basepath=r'D:\Ulva\2019RASTER\\'
env.workspace=basepath
env.overwriteOutput=True
TIFlist=[]
for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                TIFlist.append(name)
                print(basepath + name)

for root, dirs, files in os.walk(env.workspace,topdown=True):
    for name in files:
        if name.split('.')[-1]=='tif':
                print(basepath+name.split('.')[0]+".shp")