import pandas as pd
import osr
import ogr
import seaborn  as sns
import numpy as np
import math

from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
data=pd.read_csv(r"D:\坚果云文件\我的坚果云\舆情\\process_data.csv")
print(data.columns)
#data=data[data['stage']==1]
sns.lineplot(data=data,x='lon',y='m_area',hue='year',style='year',markers=True,palette="light:blue")#
plt.savefig(r"D:\坚果云文件\我的坚果云\浒苔适生环境研究\Curve\\lon.svg")
plt.show()