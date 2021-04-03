import rasterio as rst
import numpy as np
basepath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\\"
def Union(risk,suit):
    result=np.zeros(risk.shape)
    risk[risk<=suit]=0
    suit[risk > suit] = 0
    result=risk+suit
    return result
def get_data(path):
    with rst.open(path, mode='r') as dst:
        suit = dst.read(1)
        profile=dst.profile
    return suit,profile
years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
suitDate=[]
for y in years:
    for m in month:
        suitDate.append(y+m)
riskDate=suitDate
del riskDate[0]
for i in range(len(suitDate)):
    if suitDate[i]=='201907' or suitDate[i]=='201907' or suitDate[i]=='201910' or suitDate[i]=='201911' or suitDate[i]=='201912':
        continue
    mergepath = basepath + "Merge" + suitDate[i]+ '.tif'
    riskpath = basepath + "Risk/Risk" +riskDate[i]+ ".tif"
    suit,profile = get_data(mergepath)
    risk,profile = get_data(riskpath)
    union=Union(risk,suit)
    with rst.open(basepath + "Union/Union" + riskDate[i] + ".tif", mode='w', **profile) as dst:
        dst.write(union, 1)
    print(riskDate[i])

