import rasterio as rst
import os
import numpy as np
#样本数据处理
basepath=r"F:\浒苔适生环境数据\Resample\\"


def get_value(path):
    with rst.open(path) as dst:
        array=dst.read(1)
    return array

def get_Layers(year,month,suitorunsuit):
    SST=basepath+"SST_"+suitorunsuit+"_"+str(year)+"_"+str(month)+".tif"
    SSS = basepath +"SSS_"+suitorunsuit+"_"+ str(year) + "_" + str(month) + ".tif"
    Rizhao = basepath +"Rizhao_"+suitorunsuit+"_"+str(year) + "_" + str(month) + ".tif"
    CHLA = basepath +"CHLA_"+suitorunsuit+"_"+str(year) + "_" + str(month) + ".tif"
    SST=get_value(SST).flatten()
    SSS=get_value(SSS).flatten()
    Rizhao=get_value(Rizhao).flatten()
    CHLA=get_value(CHLA).flatten()
    yaosu=np.zeros(shape=(4,SST.shape[0]))
    yaosu[0]=SST
    yaosu[1]=SSS
    yaosu[2]=Rizhao
    yaosu[3]=CHLA
    yaosu=yaosu.T
    return yaosu




