"""
import gdal
import numpy as np
import struct
import os
import pandas as pd
import rasterio as rio
name=r"F:\海洋遥感\海面风场\东印\年平均\2014\海面风场_东印度洋_2014010120141231_20151012.dat"

def xshow(filename, nx, nz,nb):
    f = open(filename, "rb")
    pic = np.zeros((nb,nx, nz))
    for k in range(nb):
        for i in range(nx):
            for j in range(nz):
                data = f.read(4)
                elem = struct.unpack("hh", data)[0]
                print(elem)
                pic[k][i][j] = elem

    f.close()
    return picD:\坚果云文件\我的坚果云\空间分析课程\空间分析课程\实习报告5

#re=xshow(filename=name,nx=125,nz=153,nb=4)

"""
"""
import os
for root, dirs, files in os.walk(r"D:\坚果云文件\我的坚果云\空间分析课程\空间分析课程\实习报告6", topdown=False):
    for name in files:
        if (name[0]=='A' or name[0]=='B') and (name[1]!='+'):
            print(name[1:])
        else:
            print(name[2:])
"""

import time
def compareList( X, Y):
    set_1 = set(X)
    set_2 = set(Y)
    setand = set_1 | set_2
    set_more1 = setand-set_1

    return (len(set_more1))/40

X=[ 'sunny', 'hot', 'high', 'FALSE']
Y=['sunny', 'hot', 'high', 'True']
X=[ 'sunny', 'hot', 'high', 'F']
starttime=time.time()
for i in range(1000000):
    compareList(X, Y)
endtime=time.time()
print(endtime-starttime)


def compareList2( X, Y):
    num = 0
    for i in range(len(X)):
        if X[i] == Y[i]:
            num += 1
    return num / 40

starttime=time.time()
for i in range(1000000):
    compareList2(X, Y)
endtime=time.time()
print(endtime-starttime)


path=r'C:\坚果云\我的坚果云\舆情\OY(IBAM)'
Bpath=r'C:\坚果云\我的坚果云\舆情\OY(IBAM)\CENTER'
import os
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name.split('.')[-1]=='shp':
            if name.find("BAM2")>=0:
                print(Bpath+"\\"+name)
