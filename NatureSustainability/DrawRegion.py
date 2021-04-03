import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax=world.plot(facecolor='#FFEBBE', edgecolor='#616F8E')
MBR1=gpd.read_file(r"F:\实验对比分析数据\YellowSea_MBR\MBR2.shp")
MBR1.plot(facecolor='red',ax=ax)
#ax.set_xlim([118, 128])
#ax.set_ylim([28, 42])
plt.show()