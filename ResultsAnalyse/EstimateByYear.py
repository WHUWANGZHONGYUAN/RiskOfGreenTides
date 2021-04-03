import os
import rasterio
import numpy as np
path=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\Union/"
year2016=[]
year2017=[]
year2018=[]
year2019=[]
for root, dirs, files in os.walk(path):
    for name in files:
        if name.split(".")[-1]=='tif':
            if name[5:9]=='2016':
                year2016.append(name)
            if name[5:9]=='2017':
                year2017.append(name)
            if name[5:9]=='2018':
                year2018.append(name)
            if name[5:9]=='2019':
                year2019.append(name)
array=[]
profile=''
for item in year2019:
    with rasterio.open(path+item) as src:
        new_array=src.read(1)
        new_array[new_array<=0.9]=0
        new_array[new_array > 0.9] = 1
        array.append(new_array)
        profile=src.profile
count=np.zeros(array[0].shape)
for item in array:
    count=count+item

profile.update(count=1)
with rasterio.open(path+"YEAR/2019.tif",mode='w',**profile) as src:
    src.write(count,1)



