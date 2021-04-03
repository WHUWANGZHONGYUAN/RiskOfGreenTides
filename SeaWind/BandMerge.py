import arcpy
from arcpy import env
env.workspace = r"F:\WORDWIDE_Resample\Merge_predict_ssw"
years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for y in years:
    for m in month:
        if y=="2019" and (m=="07" or m=="11" or m=="12"):
            continue
        mergepath = r"merge_" + y+"_" + m + ".tif;"
        dirpath = r"dir_" + y + m + ".tif;"
        spdpath = r"spd_" + y + m + ".tif;"
        despath = r"Merge\Merge" + y + m + ".tif"
        bands=mergepath+dirpath+spdpath
        print bands
        arcpy.CompositeBands_management(bands, despath)
        print y+m
