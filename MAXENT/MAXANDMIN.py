import rasterio as rst
import os
import numpy as np
basepath="F:\WORDWIDE_Resample\Merge\\"

chla_max=[]
sst_max=[]
sss_max=[]
rizhao_max=[]
chla_min=[]
sst_min=[]
sss_min=[]
rizhao_min=[]
for root, dirs, files in os.walk(basepath):
    for name in files:
        if name.split(".")[-1]=="tif":
            with rst.open(basepath+name) as dst:
                chla=dst.read(1).max()
                sst=dst.read(2).max()
                sss = dst.read(3).max()
                rizhao = dst.read(4).max()

                chla_max.append(chla)
                sst_max.append(sst)
                sss_max.append(sss)
                rizhao_max.append(rizhao)

                chla=dst.read(1).min()
                sst=dst.read(2).min()
                sss = dst.read(3).min()
                rizhao = dst.read(4).min()

                chla_min.append(chla)
                sst_min.append(sst)
                sss_min.append(sss)
                rizhao_min.append(rizhao)


print(np.max(chla_max))
print(np.max(sst_max))
print(np.max(sss_max))
print(np.max(rizhao_max))

print(np.min(chla_min))
print(np.min(sst_min))
print(np.min(sss_min))
print(np.min(rizhao_min))
