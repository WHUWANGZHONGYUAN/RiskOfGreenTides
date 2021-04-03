import rasterio
import matplotlib.pyplot
from rasterio.plot import show
from matplotlib import pyplot
import os
path=r"G:\浒苔适生环境数据\\Resample\\"
despath=r"G:\浒苔适生环境数据\\Visualization\\"
count=0
fig, (axa, axb, axc,axd,axe,axf) = pyplot.subplots(1, 6, figsize=(35, 20))
for root, dirs, files in os.walk(path):
    for name in files:
        if name.split(".")[-1]=='tif':

            src = rasterio.open(path+name)
            #show(src.read(1), cmap='pink',transform=src.transform,title=name)
            ax=[]
            ax.append(axa)
            ax.append(axb)
            ax.append(axc)
            ax.append(axd)
            ax.append(axe)
            ax.append(axf)
            show((src, 1),ax=ax[count%6],cmap='pink', title=name,transform=src.transform)
            count=count+1
            if count%6==0:
                pyplot.savefig(despath+name.split("20")[0]+".jpg",dpi=600)
                pyplot.show()
                fig, (axa, axb, axc,axd,axe,axf)  = pyplot.subplots(1, 6, figsize=(35, 7))


