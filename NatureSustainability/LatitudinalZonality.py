import rasterio as rst
import numpy as np
basepath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\\"
from rasterio.plot import show
def get_avg(data):
    sum=np.zeros(data[0].shape)
    for item in data:
        sum=sum+item
    return sum/18

years=['2016','2017','2018']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
summerdata=[]
winterdata=[]
for m in month:
    for y in years:
        path=basepath+"Merge"+str(y)+str(m)+".tif"
        with rst.open(path) as dataset:
            data=dataset.read(1)
        if m=="01" or m=="02" or m=="09" or m=="10" or m=="11" or m=="12":
            winterdata.append(data)
        else:
            summerdata.append(data)

summerdata=get_avg(summerdata)
winterdata=get_avg(winterdata)
#取得profile
with rst.open(basepath+"Merge201601.tif") as dataset:
    profile=dataset.profile

profile.update(count=1)
with rst.open("summerdata.tif",'w',**profile) as dataset:
    dataset.write(summerdata,1)

profile.update(count=1)
with rst.open("winterdata.tif",'w',**profile) as dataset:
    dataset.write(winterdata,1)


def classify(data):
    from sklearn.cluster import KMeans
    height=data.shape[0]
    width=data.shape[1]
    result=data.reshape(height*width).reshape(-1,1)
    kmeans = KMeans(n_clusters=5, random_state=0)
    kmeans.fit(result)
    y_pre=kmeans.predict(result)
    y_pre=y_pre.reshape(height,width)

    kc=kmeans.cluster_centers_
    print(kc)
    kc_list = sorted([i for i in kc[:, 0]])
    for i in range(len(kc)):
        for j in range(len(kc_list)):
            if kc[i]==kc_list[j]:
                y_pre[y_pre==i]=(j+1)*10
    return y_pre

profile.update(dtype=np.int16)
winterdata=classify(winterdata)
summerdata=classify(summerdata)
summerdata=summerdata.astype(np.int16)
winterdata=winterdata.astype(np.int16)
with rst.open("winterdata_classify.tif",'w',**profile) as dataset:
    dataset.write(winterdata,1)


with rst.open("summerdata_classify.tif",'w',**profile) as dataset:
    dataset.write(summerdata,1)