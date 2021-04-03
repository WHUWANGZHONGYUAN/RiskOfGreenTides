import os

basepath=r"F:\浒苔适生环境数据\叶绿素浓度\\"
despath=r"F:\WORDWIDE_Resample\UnSuit\\"
mergepath=r"F:\WORDWIDE_Resample\Merge\\"
for root, dirs, files in os.walk(basepath):
     for name in files:
         if name.split(".")[-1]=='tif':
             if name.split("_")[0]=='unsuit':
                year=name.split("_")[1]
                month=name.split("_")[2]
                print(mergepath+"merge_"+year+"_"+month)

