import rasterio
import pickle
import numpy as np
import os
f = open('sample_weights_500_str.txt', 'rb')
maxent = pickle.load(f)
f.close()

mergepath=r"F:\WORDWIDE_Resample\Merge\\"
predictpath=r"F:\WORDWIDE_Resample\Predict_NEW_NAN\\"
for root, dirs, files in os.walk(mergepath):
    for name in files:
        if name.split(".")[-1]=='tif':
            with rasterio.open(mergepath+name) as dst:
                profile=dst.profile
                chla=dst.read(1)
                sst=dst.read(2)
                sss = dst.read(3)
                rizhao = dst.read(4)
                chla=100*(chla-0)/(74.2951-0)
                sst=100 * (sst + 2) / (35.0 - 0)
                sss=100 * (sss - 0) / (43.638526916503906 - 0)
                rizhao=100 * (rizhao - 0) / (547.83 - 0)
            suit=np.zeros(shape=(chla.shape[0],chla.shape[1]))
            unsuit = np.zeros(shape=(chla.shape[0], chla.shape[1]))
            for i in range(chla.shape[0]):
                for j in range(chla.shape[1]):
                    #if (chla[i][j]==0) or (sst[i][j]==0) or (sss[i][j]==0) or (rizhao[i][j]==0):
                    #    continue
                    X=[]
                    X.append("chla"+str(int(chla[i][j] + 0.5)))
                    X.append("sst"+str(int(sst[i][j] + 0.5)))
                    X.append("sss"+str(int(sss[i][j] + 0.5)))
                    X.append("rizhao"+str(int(rizhao[i][j] + 0.5)))
                    result=maxent.predict(X)
                    suit[i][j]=result['suit']
                    unsuit[i][j] = result['unsuit']

            profile.update(count=2)
            with rasterio.open(predictpath+name,mode='w',**profile) as dst:
                dst.write(suit,1)
                dst.write(unsuit,2)
            print(name)



