import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)
from matplotlib import pyplot
data=pd.read_csv("spss_statistic.csv")

import scipy.stats as stats


cor,pvalue=stats.pearsonr(data['area'],data['agg'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['area'],data['density'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['agg'],data['density'])
print(cor)
print(pvalue)

#正态分布检验
print(stats.kstest(data['m_area'], 'norm'))
print(stats.kstest(data['m_agg'], 'norm'))
print(stats.kstest(data['m_density'], 'norm'))


print("normalized")
cor,pvalue=stats.pearsonr(data['m_area'],data['m_agg'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_area'],data['m_density'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_agg'],data['m_density'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_agg'],data['lat'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_agg'],data['lon'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_agg'],data['lat'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_agg'],data['keyday'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_density'],data['lon'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_density'],data['lat'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_density'],data['keyday'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_area'],data['lon'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_area'],data['lat'])
print(cor)
print(pvalue)

cor,pvalue=stats.pearsonr(data['m_area'],data['keyday'])
print(cor)
print(pvalue)

sns.boxplot(data=data,hue='STAGE',y='m_area',x='year')
plt.show()
sns.boxplot(data=data,hue='STAGE',y='m_agg',x='year')
plt.show()
sns.boxplot(data=data,hue='STAGE',y='m_density',x='year')
plt.show()


suit_and_unsuit=pd.DataFrame(columns=['name','value','STAGE','year'])
data_area=pd.DataFrame(columns=['name','value','STAGE','year'])
data_area['value']=data['m_area'].values
data_area['STAGE']=data['STAGE'].values
data_area['year']=data['year'].values
data_area['name']=data['m_agg'].apply(lambda x:"area")

suit_and_unsuit=suit_and_unsuit.append(data_area)
data_area=pd.DataFrame(columns=['name','value','STAGE','year'])
data_area['value']=data['m_agg'].values
data_area['STAGE']=data['STAGE'].values
data_area['year']=data['year'].values
data_area['name']=data['m_agg'].apply(lambda x:"agg")

suit_and_unsuit=suit_and_unsuit.append(data_area)
data_area=pd.DataFrame(columns=['name','value','STAGE','year',])
data_area['value']=data['m_density'].values
data_area['STAGE']=data['STAGE'].values
data_area['year']=data['year'].values
data_area['name']=data['m_agg'].apply(lambda x: "density")



fig, ax = pyplot.subplots(2, 2)
suit_and_unsuit=suit_and_unsuit.append(data_area)
print(suit_and_unsuit)
t=sns.boxplot(data=suit_and_unsuit[suit_and_unsuit['year']==2016],hue='name',y='value',x='STAGE',ax=ax[0,0])
t.legend_.remove()
plt.title("2016")

t=sns.boxplot(data=suit_and_unsuit[suit_and_unsuit['year']==2017],hue='name',y='value',x='STAGE',ax=ax[0,1])
t.legend_.remove()
plt.title("2017")
t.legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
t=sns.boxplot(data=suit_and_unsuit[suit_and_unsuit['year']==2018],hue='name',y='value',x='STAGE',ax=ax[1,0])
t.legend_.remove()
plt.title("2018")

t=sns.boxplot(data=suit_and_unsuit[suit_and_unsuit['year']==2019],hue='name',y='value',x='STAGE',ax=ax[1,1])
t.legend_.remove()

plt.title("2019")

plt.savefig(r"D:\坚果云文件\我的坚果云\浒苔适生环境研究\SCATTERLINE\\Fouryears.svg")
plt.show()

