#python 2.7 ArcGIS
import arcpy
from arcpy import env
env.workspace = r"F:\WORDWIDE_Resample".decode('utf-8')
import os
years=["2016","2017","2018","2019"]
month=["01","02","03","04","05","06","07","08","09","10","11",'12']
rizhao=[]
sst=[]
sss=[]
chla=[]
for year in years:
    for mon in month:
        if (year=='2019' and mon=="11") or (year=='2019' and mon=="12"):
            continue
        else:
            chla.append("chla_" + year + "-" + mon + "-01.tif")
            sst.append("sst_" + year + "-" + mon + "-01.tif")
            sss.append("sss_" + year + "_" + mon + ".tif")
            rizhao.append("rizhao_" + year + "-" + mon + "-01.tif")

i=0
for year in years:
    for mon in month:
        if (year == '2019' and mon == "11") or (year == '2019' and mon == "12"):
            continue
        else:
            bands=chla[i] + ";" + sst[i] + ";" + sss[i] + ";" + rizhao[i] + ";"
            merges = "Merge/merge_" + str(year) + "_" + str(mon) + ".tif"
            arcpy.CompositeBands_management(bands,merges)
            i=i+1
            print(merges)

max=[74.2951,35.0,43.638526916503906,547.83]
min=[0.0,-2.0,0.0,0.0]





