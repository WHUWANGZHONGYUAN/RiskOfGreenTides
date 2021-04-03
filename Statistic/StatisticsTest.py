from scipy import stats
import rasterio as rst
import os
import numpy as np
path=r"G:\浒苔适生环境数据\\Resample\\"
basepath=r"G:\浒苔适生环境数据\Resample\\"
attribute=['CHLA','Rizhao','SST','SSS']
def estimate(basepath,year,month,attribute):
    suitpath=basepath+attribute+"_suit_"+year+"_"+month+".tif"
    unsuitpath = basepath + attribute + "_unsuit_" + year + "_" + month + ".tif"
    suit=rst.open(suitpath).read(1)
    unsuit=rst.open(unsuitpath).read(1)
    suit=suit.reshape(suit.shape[0]*suit.shape[1],)
    unsuit = unsuit.reshape(unsuit.shape[0] * unsuit.shape[1], )
    index=(np.isnan(suit))
    suit = np.delete(suit,index)
    index = np.isnan(unsuit)
    unsuit = np.delete(unsuit,index)
    t, p_twotail = stats.ttest_ind(suit, unsuit)
    return p_twotail

year=['2016','2016','2017','2018','2019','2019']
month=['05','06','05','06','05','06']
for i in range(len(year)):
    print(estimate(path,year[i],month[i],'SST'))
