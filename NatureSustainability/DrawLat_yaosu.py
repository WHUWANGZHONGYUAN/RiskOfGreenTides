import seaborn as sns
import rasterio as rst
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.interpolate import make_interp_spline
from scipy import stats

def smooth(data, x, y):
    x = data[x].values
    y = data[y].values
    b = make_interp_spline(x, y)
    return b(data[x].values)


dataframe = pd.read_csv("Risk_lat_all_yaosu_merge.csv")

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
R1=[]#risk with chla
R2=[]#risk with sss
R3=[]#risk with sst
R4=[]#risk with sunlight

for m in range(1, 13):
    data = dataframe[dataframe['Month'] == m]
    data2016 = data[data['Year'] == 2016]
    data2017 = data[data['Year'] == 2017]
    data2018 = data[data['Year'] == 2018]
    data2019 = data[data['Year'] == 2019]
    tempdata = pd.DataFrame(
        columns=['Latitude', 'Risk', 'Chla', 'SSS', 'SST', 'SunLight', 'Risk_smooth', 'Chla_smooth', 'SSS_smooth',
                 'SST_smooth', 'SunLight_smooth'])
    tempdata['Latitude'] = data2016['Latitude']
    if (m != 7) and (m != 11) and (m != 12):
        tempdata['Risk'] = (data2016['Risk'].values + data2017['Risk'].values + data2018['Risk'].values +
                                   data2019[
                                       'Risk'].values) / 4
        tempdata['Chla'] = (data2016['Chla'].values + data2017['Chla'].values + data2018['Chla'].values +
                                   data2019[
                                       'Chla'].values) / 4
        tempdata['SSS'] = (data2016['SSS'].values + data2017['SSS'].values + data2018['SSS'].values + data2019[
            'SSS'].values) / 4
        tempdata['SST'] = (data2016['SST'].values + data2017['SST'].values + data2018['SST'].values + data2019[
            'SST'].values) / 4
        tempdata['SunLight'] = ( data2016['Rizhao'].values + data2017['Rizhao'].values + data2018[
                                   'Rizhao'].values + data2019[
                                           'Rizhao'].values) / 4
    else:
        tempdata['Risk'] = (data2016['Risk'].values + data2017['Risk'].values + data2018['Risk'].values) / 3
        tempdata['Chla'] = (data2016['Chla'].values + data2017['Chla'].values + data2018['Chla'].values) / 3
        tempdata['SSS'] = (data2016['SSS'].values + data2017['SSS'].values + data2018['SSS'].values) / 3
        tempdata['SST'] = (data2016['SST'].values + data2017['SST'].values + data2018['SST'].values) / 3
        tempdata['SunLight'] = (data2016['Rizhao'].values + data2017['Rizhao'].values + data2018[
                                   'Rizhao'].values) / 3

    fig, (ax_1, ax_2, ax_3, ax_4, ax_5) = plt.subplots(nrows=5, ncols=1, sharex=True)
    sns.lineplot(x='Latitude', y='Risk', data=tempdata, color='red', label='Risk', ax=ax_1,legend=False)
    sns.lineplot(x='Latitude', y='Chla', data=tempdata, color='green', label='Chla', ax=ax_2,legend=False)
    sns.lineplot(x='Latitude', y='SSS', data=tempdata, color='blue', label='SSS', ax=ax_3,legend=False)
    sns.lineplot(x='Latitude', y='SST', data=tempdata, color='pink', label='SST', ax=ax_4,legend=False)
    sns.lineplot(x='Latitude', y='SunLight', data=tempdata, color='grey', label='Sunlight', ax=ax_5,legend=False)
    #ax_1.legend()
    ax_1.set_title('month:'+str(m),fontsize=15)
    plt.xlabel('Latitidue(°N)', fontsize=15)
    plt.savefig(r"D:\坚果云文件\我的坚果云\Nature_sustainability\Introduction_Analyse_merge\\LAT_yaosu"+str(m)+".jpg",dpi=300)
    plt.show()

    R1.append(stats.pearsonr(tempdata['Risk'], tempdata['Chla'])[0])
    R2.append(stats.pearsonr(tempdata['Risk'], tempdata['SSS'])[0])
    R3.append(stats.pearsonr(tempdata['Risk'], tempdata['SST'])[0])
    R4.append(stats.pearsonr(tempdata['Risk'], tempdata['SunLight'])[0])

x=np.arange(1,13,1)


x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, R1)(x_smooth)
plt.plot(x_smooth, y_smooth,label="Risk-Chla")

y_smooth = make_interp_spline(x, R2)(x_smooth)
plt.plot(x_smooth, y_smooth,label="Risk-SSS")

y_smooth = make_interp_spline(x, R3)(x_smooth)
plt.plot(x_smooth, y_smooth,label="Risk-SST")

y_smooth = make_interp_spline(x, R4)(x_smooth)
plt.plot(x_smooth, y_smooth,label="Risk-SunLight")
plt.ylabel('Pearson coefficient', fontsize=15)
plt.xlabel('Month', fontsize=15)
plt.legend()
plt.show()

plt.plot(x,R1,label="Risk-Chla",marker='o',color='blue')
plt.plot(x,R2,label="Risk-SSS",marker='o',color='pink')
plt.plot(x,R3,label="Risk-SST",marker='o',color='green')
plt.plot(x,R4,label="Risk-SunLight",marker='o',color='red')
plt.legend()
plt.ylabel('Pearson coefficient', fontsize=15)
plt.xlabel('Month', fontsize=15)
plt.xticks(x)
plt.savefig(r"D:\坚果云文件\我的坚果云\Nature_sustainability\LatAnalysis\LAT_yaosu_pearson"+str(m)+".svg",dpi=300)
plt.show()