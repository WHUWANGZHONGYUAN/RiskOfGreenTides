import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.interpolate import make_interp_spline
def smooth(X,Y,k=3):
    x_new = np.linspace(X.min(),X.max(),300) #300 represents number of points to make between T.min and T.max
    y_smooth = make_interp_spline(X,Y,k=k)(x_new)
    return x_new,y_smooth
def regionplot(riskA,suitA,title="A"):
    #plt.grid(axis="y")
    X = riskA.Month.values
    Y = riskA.avg.values
    x, y = smooth(X, Y)
    R1 = stats.pearsonr(suitA.avg.values,riskA.avg.values)
    R2 = R1[1]
    R1 = R1[0]
    print(title)
    print(R1)
    print(R2)

    #sns.scatterplot(X, Y, color='red')
    #sns.lineplot(x, y, color='red',linestyle='--')

    X = suitA.Month.values
    Y = suitA.avg.values
    if (np.sum(suitA.avg.values == riskA.avg.values)) >= 10:
        x, y = smooth(X, Y,k=2)
    else:
        x, y = smooth(X, Y)
    #sns.scatterplot(X, Y, color='blue')

    #sns.lineplot(x, y, color='blue', linestyle='--')
    #plt.xticks(X)
    #plt.xlabel("Month",fontsize=20)
    #plt.title(title,fontsize=20)
    #plt.xticks(fontsize=12, color='#000000')
    #plt.legend(fontsize=14)
    #plt.savefig(r"D:\坚果云文件\我的坚果云\Nature_sustainability\RegionAnalysis\\"+title+".svg",dpi=300,fontsize=20)
    #plt.show()





risk=pd.read_csv(r"F:\实验对比分析数据\yellow_sea_union_risk(M).csv")
riskA=risk[(risk['region']=='A') & (risk['year']==2018)]
riskB=risk[(risk['region']=='B') & (risk['year']==2018)]
suit = pd.read_csv(r"F:\实验对比分析数据\yellow_sea_merge(M).csv")
suitA = suit[(suit['region'] == 'A') & (suit['year'] == 2018)]
suitB = suit[(suit['region'] == 'B') & (suit['year'] == 2018)]
regionplot(riskA,suitA,title="Part A in the West Pacific Ocean")
regionplot(riskB,suitB,title="Part B in the West Pacific Ocean")

risk=pd.read_csv(r"F:\实验对比分析数据\Europe_union_risk(M).csv")
riskA=risk[(risk['region']=='A') ]
riskB=risk[(risk['region']=='B')]
riskC=risk[(risk['region']=='C')]
riskD=risk[(risk['region']=='D')]
suit = pd.read_csv(r"F:\实验对比分析数据\Europe_merge(M).csv")
suitA = suit[(suit['region'] == 'A')]
suitB = suit[(suit['region'] == 'B')]
suitC = suit[(suit['region'] == 'C')]
suitD = suit[(suit['region'] == 'D')]
regionplot(riskA,suitA,title="Part A in the Atlantic Ocean")
regionplot(riskB,suitB,title="Part B in the Atlantic Ocean")
regionplot(riskC,suitC,title="Part C in the Atlantic Ocean")
regionplot(riskD,suitD,title="Part D in the Atlantic Ocean")

risk=pd.read_csv(r"F:\实验对比分析数据\North_America_union(M).csv")
riskA=risk[(risk['region']=='A') & (risk['year']==2018)]
riskB=risk[(risk['region']=='B') & (risk['year']==2018)]
suit = pd.read_csv(r"F:\实验对比分析数据\North_America_merge(M).csv")
suitA = suit[(suit['region'] == 'A') & (suit['year'] == 2018)]
suitB = suit[(suit['region'] == 'B') & (suit['year'] == 2018)]
regionplot(riskA,suitA,title="Part A in the East Pacific Ocean")
regionplot(riskB,suitB,title="Part B in the East Pacific Ocean")