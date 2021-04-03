import rasterio
import numpy as np
import pandas as pd
from Maxent_modify import MaxEntropy

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

sample['nor_chla']=sample['nor_chla'].apply(lambda x: "chla"+str(x))
sample['nor_sst']=sample['nor_sst'].apply(lambda x:  "sst"+str(x))
sample['nor_sss']=sample['nor_sss'].apply(lambda x:  "sss"+str(x))
sample['nor_rizhao']=sample['nor_rizhao'].apply(lambda x:  "rizhao"+str(x))

sample_array=np.empty(shape=(13980,5),dtype=np.string_)

sample_array=[]
sample_array.append(sample['suit'].values)
sample_array.append(sample['nor_chla'].values)
sample_array.append(sample['nor_sst'].values)
sample_array.append(sample['nor_sss'].values)
sample_array.append(sample['nor_rizhao'].values)

sample_array=np.array(sample_array)
sample_array=sample_array.T



maxent = MaxEntropy()

maxent.loadData(sample_array)
print(maxent._xy_num)
maxent.train(maxiter=10000)

f = open('modify_sample_weights_10000_str.txt', 'wb')
pickle.dump(maxent, f, 0)
f.close()
f = open('modify_sample_weights_10000_str.txt', 'rb')
max = pickle.load(f)
f.close()
x = ['0', '6', '0','45']
print('精度:', maxent.predict(x))
