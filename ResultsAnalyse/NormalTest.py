import rasterio
from rasterio.plot import show_hist
import numpy as np
path=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\Union/"
from scipy import stats
with rasterio.open(path + 'Union201604.tif') as src:
    array=src.read(1)

    show_hist(array, bins=50, lw=0.0, stacked=False, alpha=0.3,
              histtype='stepfilled', title="Histogram")
    array=array.flatten()
    array=np.delete(array,np.where(array==0),None)
    print(stats.normaltest(array))

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas

from scipy.stats import norm
x=array
print(x)
mu =np.mean(x) #计算均值
sigma =np.std(x)
mu,sigma
num_bins = 30 #直方图柱子的数量

n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
#直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
y = norm.pdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y

plt.plot(bins, y, 'r--') #绘制y的曲线
plt.xlabel('DN') #绘制x轴
plt.ylabel('Frequency') #绘制y轴
plt.title(r'Histogram : $\mu=5.8433$,$\sigma=0.8253$')#中文标题 u'xxx'

plt.subplots_adjust(left=0.15)#左边距
plt.show()