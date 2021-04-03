import seaborn as sns
import rasterio as rst
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
dataframe=pd.read_csv("Risk_lon_all.csv")
print(dataframe)
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for m in range(1,13):
    data=dataframe[dataframe['Month']==m]
    sns.lineplot(x='Longitude', y='Risk', data=data,hue='Year', legend=True,palette='Paired')
    plt.yticks(fontsize=12, color='#000000')
    plt.ylabel('Mean risk of green tide', fontsize=15)
    plt.xticks(fontsize=12, color='#000000')
    plt.xlabel('Longitude(°W)', fontsize=15)
    data2016=data[data['Year']==2016]
    data2017 = data[data['Year'] == 2017]
    data2018 = data[data['Year'] == 2018]
    data2019 = data[data['Year'] == 2019]




    R1 = stats.pearsonr(data2016['Risk'],data2017['Risk'])[0]

    R2 = stats.pearsonr(data2016['Risk'],data2018['Risk'])[0]
    R4 = stats.pearsonr(data2017['Risk'],data2018['Risk'])[0]
    if (m!=7) and (m!=11) and (m!=12):
        R3 = stats.pearsonr(data2016['Risk'],data2019['Risk'])[0]
        R5 = stats.pearsonr(data2017['Risk'],data2019['Risk'])[0]
        R6 = stats.pearsonr(data2018['Risk'],data2019['Risk'])[0]
        #plt.text(100, 0, 'R1:%.4f\n'%R1+'R2:%.4f\n'%R2+'R3:%.4f\n'%R3+'R4:%.4f\n'%R4+'R5:%.4f\n'%R5+'R6:%.4f\n'%R6)
    else:
        #plt.text(100, 0, 'R1:%.4f\n'%R1+'R2:%.4f\n'%R2+'R4:%.4f\n'%R4)
        continue
    plt.legend()
    plt.title("month="+str(m))
    plt.savefig(r"D:\坚果云文件\我的坚果云\Nature_sustainability\LatAnalysis\\LON" + str(m) + ".svg", dpi=300)
    plt.show()