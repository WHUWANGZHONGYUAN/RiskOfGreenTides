import rasterio
import numpy as np
import pandas as pd
from MAXENT import MaxEntropy
import pickle
import io
import os
suitpath=r"F:\WORDWIDE_Resample\Suit\\"
sample=pd.DataFrame(columns=['suit','chla','sst','sss','rizhao'])
for root, dirs, files in os.walk(suitpath):
    for name in files:
        if name.split(".")[-1]=='tif':
            dataframe=pd.DataFrame(columns=['suit','chla','sst','sss','rizhao'])
            with rasterio.open(suitpath+name) as dst:
                chla=dst.read(1).flatten()
                sst=dst.read(2).flatten()
                sss = dst.read(3).flatten()
                rizhao = dst.read(4).flatten()
                suit=np.ones(chla.shape[0])
                dataframe['chla']=chla
                dataframe['sst'] = sst
                dataframe['sss'] = sss
                dataframe['rizhao'] = rizhao
                dataframe['suit'] = suit
                sample=sample.append(dataframe)

suitpath=r"F:\WORDWIDE_Resample\Unsuit\\"
for root, dirs, files in os.walk(suitpath):
    for name in files:
        if name.split(".")[-1]=='tif':
            dataframe=pd.DataFrame(columns=['suit','chla','sst','sss','rizhao'])
            with rasterio.open(suitpath+name) as dst:
                chla=dst.read(1).flatten()
                sst=dst.read(2).flatten()
                sss = dst.read(3).flatten()
                rizhao = dst.read(4).flatten()
                suit=np.zeros(chla.shape[0])
                dataframe['chla']=chla
                dataframe['sst'] = sst
                dataframe['sss'] = sss
                dataframe['rizhao'] = rizhao
                dataframe['suit'] = suit
                sample=sample.append(dataframe)

sample['suit']=sample['suit'].apply(lambda x: 'suit' if x==1 else "unsuit")

max=[74.2951,35.0,43.638526916503906,547.83]
min=[0.0,-2.0,0.0,0.0]
sample=sample[(sample['sst']!=0)&(sample['sss']!=0)&(sample['chla']!=0)&(sample['rizhao']!=0)]
sample['nor_chla']=sample['chla'].apply(lambda x: 100*(x-0)/(74.2951-0))
sample['nor_sst']=sample['sst'].apply(lambda x: 100*(x+2)/(35.0-0))
sample['nor_sss']=sample['sss'].apply(lambda x: 100*(x-0)/(43.638526916503906-0))
sample['nor_rizhao']=sample['rizhao'].apply(lambda x: 100*(x-0)/(547.83-0))



sample['nor_chla']=sample['nor_chla'].apply(lambda x: int(x+0.5))
sample['nor_sst']=sample['nor_sst'].apply(lambda x: int(x+0.5))
sample['nor_sss']=sample['nor_sss'].apply(lambda x: int(x+0.5))
sample['nor_rizhao']=sample['nor_rizhao'].apply(lambda x: int(x+0.5))


def re_normalize(N,max,min):
    result=min+(N/100)*(max-min)
    result=int(result*10000)/10000.0
    return result

def set_extend(dateframe,x,y):
    if x=='nor_sst':
        max=re_normalize(int(dateframe[x])+0.4,35.0,-2)
        min=re_normalize(int(dateframe[x])-0.5,35.0,-2)
    elif x=="nor_sss":
        max=re_normalize(int(dateframe[x])+0.4,43.638526916503906, 0)
        min=re_normalize(int(dateframe[x])-0.5,43.638526916503906, 0)
    elif x=="nor_chla":
        max=re_normalize(int(dateframe[x])+0.4, 74.2951, 0)
        min=re_normalize(int(dateframe[x])-0.5, 74.2951, 0)
    else:
        max=re_normalize(int(dateframe[x])+0.4, 547.83, 0)
        min=re_normalize(int(dateframe[x])-0.5, 547.83, 0)
    return str(min)+"~"+str(max)

sample['X1']=sample.apply(set_extend,axis=1,args=('nor_rizhao',2))
sample['X2']=sample.apply(set_extend,axis=1,args=('nor_chla',2))
sample['X3']=sample.apply(set_extend,axis=1,args=('nor_sss',2))
sample['X4']=sample.apply(set_extend,axis=1,args=('nor_sst',2))
sample.drop('nor_chla', axis=1, inplace=True)
sample.drop('nor_sst', axis=1, inplace=True)
sample.drop('nor_sss', axis=1, inplace=True)
sample.drop('nor_rizhao', axis=1, inplace=True)
sample.drop('chla', axis=1, inplace=True)
sample.drop('sst', axis=1, inplace=True)
sample.drop('sss', axis=1, inplace=True)
sample.drop('rizhao', axis=1, inplace=True)
#sample.to_excel(r"F:\组会1127\data.xlsx")
sample['count']=1
PXY = sample.groupby(['X1','X2','X3','X4','suit'],as_index=False).count()
PXY['P(X,Y)']=PXY['count']/7089

PXY.to_excel(r"F:\组会1127\P(XY).xlsx")

PX = sample.groupby(['X1','X2','X3','X4'],as_index=False).count()
PX['P(X)']=PX['count']/7089

PX.to_excel(r"F:\组会1127\P(X).xlsx")
result=pd.merge(left=PXY,right=PX,left_on=['X1','X2','X3','X4'],right_on=['X1','X2','X3','X4'])
result.to_excel(r"F:\组会1127\result.xlsx")
