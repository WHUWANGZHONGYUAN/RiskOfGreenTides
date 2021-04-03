import rasterio as rst
import pandas as pd
import eli5
from eli5.sklearn import PermutationImportance
from sklearn.impute import SimpleImputer as Imputer


from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.inspection import partial_dependence, plot_partial_dependence


from matplotlib import pyplot as plt

cols_to_use = ['sst', 'sss', 'chla', 'rizhao']

basepath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\\"
yaosupath=r"F:\WORDWIDE_Resample\\"
years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
suitDate=[]
for y in years:
    for m in month:
        suitDate.append(y+m)

def get_data(path):
    with rst.open(path, mode='r') as dst:
        suit = dst.read(1)
        profile=dst.profile
    return suit,profile

def get_some_data(data):

    y = data.suit
    X = data[cols_to_use]
    my_imputer = Imputer()
    imputed_X = my_imputer.fit_transform(X)
    return imputed_X, y

dataframe=pd.DataFrame(columns=['suit','sst','sss','chla','rizhao'])
for i in range(len(suitDate)):
    if suitDate[i]=='201907' or suitDate[i]=='201907' or suitDate[i]=='201910' or suitDate[i]=='201911' or suitDate[i]=='201912':
        continue
    mergepath = basepath + "Merge" + suitDate[i]+ '.tif'
    suit,profile = get_data(mergepath)

    chlapath=yaosupath+"chla"+"_"+suitDate[i][0:4]+"-"+suitDate[i][4:6]+"-01.tif"
    chla, profile = get_data(chlapath)

    sstpath = yaosupath + "sst" + "_" + suitDate[i][0:4] + "-" + suitDate[i][4:6] + "-01.tif"
    sst, profile = get_data(sstpath)

    ssspath = yaosupath + "sss" + "_" + suitDate[i][0:4] + "_" + suitDate[i][4:6] + ".tif"
    sss, profile = get_data(ssspath)

    rizhaopath = yaosupath + "rizhao" + "_" + suitDate[i][0:4] + "-" + suitDate[i][4:6] + "-01.tif"
    rizhao, profile = get_data(rizhaopath)
    tempframe=pd.DataFrame(columns=['suit','sst','sss','chla','rizhao'])
    tempframe['chla']=chla.flatten()
    tempframe['sst']=sst.flatten()
    tempframe['sss']=sss.flatten()
    tempframe['rizhao']=rizhao.flatten()
    tempframe['suit'] = suit.flatten()
    print(suitDate[i])
    tempframe['test']=tempframe['chla']+tempframe['sss']+tempframe['sst']+tempframe['rizhao']
    tempframe=tempframe[tempframe['test']!=0]
    tempframe.to_csv(suitDate[i]+".csv")
    X, y = get_some_data(tempframe)
    print("model_start")
    my_model = GradientBoostingRegressor()
    my_model.fit(X, y)
    print("fit_finished")
    my_plots = plot_partial_dependence(my_model,
                                       features=[0,1,2, 3],
                                       X=X,
                                       feature_names=cols_to_use,
                                       grid_resolution=10)
    plt.savefig(suitDate[i]+'.jpg',dpi=300)
    plt.show()
    perm = PermutationImportance(my_model, random_state=1).fit(X, y)
    eli5.show_weights(perm, feature_names=X.columns.tolist())
    print("finished")
    dataframe=dataframe.append(tempframe)
    print(dataframe.shape)



dataframe.to_csv('relative.csv')


