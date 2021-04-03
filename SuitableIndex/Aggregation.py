import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

colors = [ "red",  "blue"]
palette=sns.xkcd_palette(colors)

colors = ["lightgreen",  "lightblue",'tan','pink']
palette2=sns.xkcd_palette(colors)

data=pd.read_csv(r"spss_statistic.csv")

data['STAGE']=data['A2D'].apply(lambda x:'development' if x==1 else 'decline')


def draw(data,x='keyday',y='lon'):
    #if x=='keyday':

    ax = sns.lineplot(data=data, x=x, y=y, hue='year', palette=palette2, style='year')
    ax.legend_.remove()
    ax.legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    ax=sns.regplot(data=data, x=x, y=y, fit_reg=True,marker=False);
    ax = sns.scatterplot(data=data, x=x, y=y, hue='STAGE', style='year', palette=palette)
    ax.legend_.remove()
    ax.legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    title="x="+x+",y="+y
    plt.title(title)
    plt.tight_layout()
    if (y.find("_")>=0) and (x.find("_")>=0):
        plt.plot([0,100],[0,100],color='black')
    plt.savefig(r"D:\坚果云文件\我的坚果云\浒苔适生环境研究\SCATTERLINE\\"+title+".jpg")
    plt.show()

"""
attribute=['keyday','lat','lon','agg','area','density']
for i in range(len(attribute)):
    for j in range(len(attribute)):
        if i==j:
            continue
        else:
            draw(data,attribute[i],attribute[j])
"""
data2016=data[data['year']==2016]
data2017=data[data['year']==2017]
data2018=data[data['year']==2018]
data2019=data[data['year']==2019]


data=[]
def minmax(data):
    data['m_area'] =100* (data['area']-data['area'].min())/(data['area'].max()-data['area'].min())
    data['m_agg'] = 100 * (data['agg'] - data['agg'].min()) / (data['agg'].max() - data['agg'].min())
    data['m_density'] = 100 * (data['density'] - data['density'].min()) / (data['density'].max() - data['density'].min())
    return data

data2016=minmax(data2016)
data2017=minmax(data2017)
data2018=minmax(data2018)
data2019=minmax(data2019)

data=data2016.append(data2017)
data=data.append(data2018)
data=data.append(data2019)

print("guiyihua")
attribute=['keyday','lat','lon','m_agg','m_area','m_density']
for i in range(len(attribute)):
    for j in range(len(attribute)):
        if i==j:
            continue
        else:
            draw(data,attribute[i],attribute[j])
data.to_csv("spss_statistic.csv")