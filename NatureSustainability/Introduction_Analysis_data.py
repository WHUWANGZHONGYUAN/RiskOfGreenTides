import rasterio as rst
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import parallel_coordinates
"""
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig = plt.figure()
ax = fig.gca(projection='3d')
x=np.linspace(-0,180,1800)
y=np.linspace(0,180,1800)
z=x
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
"""
basepath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge"


LON=np.arange(0,360.1,0.1)
LAT=np.arange(-90,90.1,0.1)
longtitude=[]
latitude=[]
for i in range(0,1800):
    for j in range(0,3600):
        longtitude.append(LON[j])
        latitude.append(LAT[i])

data=pd.DataFrame(columns=['Latitude','Year','Month','Risk','Rizhao','Chla','SST','SSS'])
lon_data=pd.DataFrame(columns=['Latitude','Year','Month','Risk','Rizhao','Chla','SST','SSS'])
years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for y in years:
    for m in month:
        if (y=="2019") and (m=="07" or m=="11" or m=="12"):
            continue
        basepath = r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge"

        path=basepath+r"\Merge"+str(y)+str(m)+".tif"
        with rst.open(path) as dataset:
            risk = dataset.read(1)
        """
        basepath=r"F:\WORDWIDE_Resample"
        path = basepath + r"\chla_" + str(y) +"-"+ str(m) + "-01.tif"
        with rst.open(path) as dataset:
            chla = dataset.read(1)

        path = basepath + r"\rizhao_" + str(y) +"-"+ str(m) + "-01.tif"
        with rst.open(path) as dataset:
            rizhao = dataset.read(1)

        path = basepath + r"\sst_" + str(y) +"-"+ str(m) + "-01.tif"
        with rst.open(path) as dataset:
            sst = dataset.read(1)

        path = basepath + r"\sss_" + str(y) +"_"+ str(m) + ".tif"
        with rst.open(path) as dataset:
            sss = dataset.read(1)
        """
        path=r"F:\WORDWIDE_Resample\Merge\\"+"merge_"+str(y)+"_"+str(m)+".tif"
        with rst.open(path) as dataset:
            chla=dataset.read(1)
            sst=dataset.read(2)
            sss=dataset.read(3)
            rizhao=dataset.read(4)
        data_temp = pd.DataFrame(columns=['Latitude','Year','Month','Risk','Rizhao','Chla','SST','SSS'])
        data_temp['Latitude'] = np.arange(-90, 90, 0.1)
        data_temp['Risk'] = np.mean(risk, axis=1)
        data_temp['Rizhao']=np.mean(rizhao,axis=1)
        data_temp['Chla'] = np.mean(chla, axis=1)
        data_temp['SST'] = np.mean(sst, axis=1)
        data_temp['SSS'] = np.mean(sss, axis=1)
        data_temp['Month'] = m
        data_temp['Year'] = y
        data = data.append(data_temp)

        data_temp = pd.DataFrame(columns=['Latitude','Year','Month','Risk','Rizhao','Chla','SST','SSS'])
        data_temp['Longitude'] = np.arange(0, 360, 0.1)
        data_temp['Risk'] = np.mean(risk, axis=0)
        data_temp['Rizhao']=np.mean(rizhao,axis=0)
        data_temp['Chla'] = np.mean(chla, axis=0)
        data_temp['SST'] = np.mean(sst, axis=0)
        data_temp['SSS'] = np.mean(sss, axis=0)
        data_temp['Month'] = m
        data_temp['Year'] = y
        lon_data = lon_data.append(data_temp)


data.to_csv(r"Risk_lat_all_yaosu_merge.csv")
lon_data.to_csv(r"Risk_lon_all_yaosu_merge.csv")




