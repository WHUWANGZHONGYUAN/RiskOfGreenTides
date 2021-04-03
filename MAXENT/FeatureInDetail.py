import rasterio
import pickle
import numpy as np
import os
import pandas as pd
def re_normalize(N,max,min):
    #反归一化函数
    return min+(N/100)*(max-min)

f = open('sample_weights_500_str.txt', 'rb')
maxent = pickle.load(f)
f.close()
print(maxent._weights)
"""
print(maxent ._max_feature_num)
EP=maxent._Ep_
feature=maxent ._numXY
print(feature)
df=pd.DataFrame(columns=['name','key','suit','value','EP','lower_truth','upper_truth'])
value=[]
suit=[]
key=[]
name=[]
upper_truth=[]
lower_truth=[]
for item in feature:
    value.append(feature[item])
    suit.append(item[1])
    if 'sst' in item[0]:
        name.append('sst')
        key.append(item[0].split('sst')[1])
        upper_truth.append(re_normalize(int(item[0].split('sst')[1])+0.4,35.0,-2))
        lower_truth.append(re_normalize(int(item[0].split('sst')[1])-0.5, 35.0, -2))
    elif 'sss' in item[0]:
        name.append('sss')
        key.append(item[0].split('sss')[1])
        upper_truth.append(re_normalize(int(item[0].split('sss')[1])+0.4, 43.638526916503906, 0))
        lower_truth.append(re_normalize(int(item[0].split('sss')[1])-0.5, 43.638526916503906, 0))
    elif 'chla' in item[0]:
        name.append('chla')
        key.append(item[0].split('chla')[1])
        upper_truth.append(re_normalize(int(item[0].split('chla')[1])+0.4, 74.2951, 0))
        lower_truth.append(re_normalize(int(item[0].split('chla')[1])-0.5, 74.2951, 0))
    else:
        name.append('rizhao')
        key.append(item[0].split('rizhao')[1])
        upper_truth.append(re_normalize(int(item[0].split('rizhao')[1])+0.4, 547.83, 0))
        lower_truth.append(re_normalize(int(item[0].split('rizhao')[1])-0.5, 547.83, 0))

print(key)

df['name']=pd.Series(name)
df['value']=pd.Series(value)
df['key']=pd.Series(key)
df['suit']=pd.Series(suit)
df['EP']=pd.Series(EP)
df['upper_truth']=pd.Series(upper_truth)
df['lower_truth']=pd.Series(lower_truth)
df.sort_values("value",inplace=True,ascending=False)
df.to_csv(r"F:\浒苔适生环境数据\feature.csv")
#保留value大的特征
df.drop_duplicates(['name','key'],'first',inplace=True)
df['lower_truth']=df['lower_truth'].astype("object")
df['upper_truth']=df['upper_truth'].astype("object")
df=df[df['value']>=100]
df.to_csv(r"F:\浒苔适生环境数据\feature_select.csv")

"""