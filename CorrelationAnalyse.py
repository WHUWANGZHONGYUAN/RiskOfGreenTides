import rasterio as rio
import numpy as np
from rasterio.enums import Resampling
import pandas as pd
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans #导入K均值聚类算法
import plotly as py
import plotly.graph_objs as go
import seaborn as sns
import scipy
M=2279
N=1859
def get_flattern_data(path,band=1):
    profile=rio.open(r"G:\海洋遥感\叶绿素浓度\东印\月平均\2014\叶绿素a月分布图_IND-YGST01_2014010120140131_20150127.tiff").profile
    result=[]
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.split('.')[-1] == 'tiff' or name.split('.')[-1]=='tif':
                dataset = rio.open(path + name)
                #data=0
                with rio.open(path+name) as dataset:
                    data = dataset.read(band,
                        out_shape=(M, N),
                        resampling=Resampling.nearest)
                    data[np.isnan(data)]=-999
                array = data
                array = array.flatten()
                result.append(array)
    return np.array(result)


def scatter_line(data0,data1,title,time):
    plt.scatter(data1, data0)
    plt.title(title+"_"+time)
    plt.savefig(r"G:\海洋遥感\Plot\SCATTER_"+title+"_"+time+".png",format='png',dpi=300)
    plt.show()
    """
    data=[]
    data.append(data0)
    data.append(data1)
    data=np.array(data)
    data = data[:, data[1].argsort()]
    plt.plot(data[1], data[0],'#FF00FF')
    plt.title(title+":"+time)
    plt.savefig(r"G:\海洋遥感\Plot\LINE_"+title+"_"+time+".png",format='png',dpi=300)
    plt.show()
    """

def chla_cluster(chla_data,k=4):
    chla_data = chla_data.flatten()
    index = np.where(chla_data<=0)
    chla_data= np.delete(chla_data, index)
    chla_data = chla_data.reshape(-1, 1)
    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(chla_data)
    print("CLUSTERS:")
    print(kmodel.cluster_centers_)
    cluster=np.array(kmodel.cluster_centers_)
    cluster=np.sort(cluster.flatten())
    borders=np.zeros(k+1)
    for i in range(0,k-1):
        borders[i+1]=(cluster[i]+cluster[i+1])/2
    borders[k]=np.max(chla_data)
    print(borders)
    return borders

def get_hue(x,borders):
    hue=0
    for i in range(borders.shape[0]-1):
        if (x>borders[i]) and (x<borders[i+1]):
            hue=i
            break
    return hue


if __name__ == '__main__':
    # 叶绿素浓度的路径
    chla = r"G:\海洋遥感\叶绿素浓度\东印\月平均\2014\\"
    chla_data = get_flattern_data(chla)
    borders=chla_cluster(chla_data)

    borders=np.array([0, 2.03572607, 8.31522274, 34.91896057, 206.92098999])
    # 海面温度
    SST = r"G:\海洋遥感\海面温度\东印\月平均\\"
    SST_data = get_flattern_data(SST)
    # 海面风
    SSWSPD = r"G:\海洋遥感\海面风场\东印\月平均\2014\SeaSPD\\"
    SSWSPD_data = get_flattern_data(SSWSPD)
    # 海面风向
    SSWDIR = r"G:\海洋遥感\海面风场\东印\月平均\2014\SeaDIR\\"
    SSWDIR_data = get_flattern_data(SSWDIR)
    # 海表盐度
    SSS = r"G:\海洋遥感\海表盐度\东印\月平均\\"
    SSS_data = get_flattern_data(SSS)
    # 有效波高
    SWH = r"G:\海洋遥感\有效波高\东印\月平均\2014\SWH\\"
    SWH_data = get_flattern_data(SWH)
    SSH=r"G:\海洋遥感\海面高度\东印\月平均\2014\SSH\\"
    SSH_data = get_flattern_data(SSH)

    #百分位数统计
    corrcoef=[]
    for i in range(12):
        index = np.where(
            (chla_data[i] == -999) | (SST_data[i] == -999) | (SSWSPD_data[i] == 0) | (SSWSPD_data[i] == -999) | (
                        SSS_data[i] == -999)|(SSWDIR_data[i]==0)|(SSWDIR_data[i]==-999)|(SSH_data[i]==99999))

        chla_temp = np.delete(chla_data[i], index)
        SST_temp = np.delete(SST_data[i], index)
        SSWSPD_temp = np.delete(SSWSPD_data[i], index)
        SSWDIR_temp = np.delete(SSWDIR_data[i], index)
        SSS_temp = np.delete(SSS_data[i], index)
        SWH_temp = np.delete(SWH_data[i], index)
        SSH_temp=np.delete(SSH_data[i],index)

        data = []
        data.append(chla_temp)
        data.append(SST_temp)
        data.append(SSS_temp)
        data.append(SWH_temp)
        data.append(SSH_temp)
        data.append(SSWSPD_temp)
        data.append(SSWDIR_temp)
        corr=np.corrcoef(data)
        corrcoef.append(corr[0])
        correlation, pvalue = scipy.stats.pearsonr([1,2,3,4,5], [25,7,8,9,18])
        print(correlation)
        print(pvalue)
        scatter_line(chla_temp,SSWSPD_temp,'SSWSPD',str(i+1))
        scatter_line(chla_temp,SST_temp,'SST',str(i+1))
        scatter_line(chla_temp,SSS_temp,'SSS',str(i+1))
        scatter_line(chla_temp, SWH_temp, 'SWH',str(i+1))
        scatter_line(chla_temp, SSWDIR_temp, 'SSWDIR', str(i + 1))
        scatter_line(chla_temp, SSH_temp, 'SSH', str(i + 1))

    corrcoef=np.array(corrcoef)
    corrframe=pd.DataFrame(columns=['MONTH','CHLA','SST','SSS','SWH','SSH','SSWSPD','SSWDIR'])
    corrframe['CHLA'] = corrcoef[:, 0]
    corrframe['SST']=corrcoef[:,1]
    corrframe['SSS'] = corrcoef[:,2]
    corrframe['SWH'] = corrcoef[:,3]
    corrframe['SSH'] = corrcoef[:,4]
    corrframe['SSWSPD'] = corrcoef[:,5]
    corrframe['SSWDIR'] = corrcoef[:,6]
    corrframe['MONTH']=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    corrframe=corrframe.set_index('MONTH')
    print(corrframe)
    sns.lineplot(data=corrframe,y='SST',x='MONTH',legend=True)
    sns.lineplot(data=corrframe, y='SSS', x='MONTH',legend=True)
    sns.lineplot(data=corrframe, y='SWH', x='MONTH',legend=True)
    sns.lineplot(data=corrframe, y='SSWSPD', x='MONTH',legend=True)
    sns.lineplot(data=corrframe, y='SSWDIR', x='MONTH', legend=True)
    plt.show()
    #corrframe.to_csv(r"G:\海洋遥感\Pearson.csv")

"""
        dataframe = pd.DataFrame(columns=['chla', 'sst', 'sss', 'swh','ssh', 'spd','dir', 'hue'])
        dataframe['chla'] = chla_temp
        dataframe['sst'] = SST_temp
        dataframe['sss'] = SSS_temp
        dataframe['swh'] = SWH_temp
        dataframe['ssh'] = SSH_temp
        dataframe['spd'] = SSWSPD_temp
        dataframe['dir'] = SSWDIR_temp
        dataframe['hue'] = dataframe['chla'].apply(lambda x:get_hue(x,borders))
        dataframe.sort_values("hue", inplace=True)
        dataframe.to_csv(r"G:\海洋遥感\CHLA_HUE\\"+str(i)+".csv")
        #dataframe=dataframe.drop_duplicates()#去重复
        #parallel_coordinates(dataframe, 'hue')
        #plt.show()
        #print(dataframe)
"""