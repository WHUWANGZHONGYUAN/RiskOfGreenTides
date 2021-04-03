#熵权法求取权重
import pandas as pd
import numpy as np
import math
from numpy import array
dataframe=pd.read_csv(r"C:\坚果云\我的坚果云\舆情\social_sum_data.csv",encoding="ISO-8859-1")


# 定义熵值法函数
def cal_weight(x):
    '''熵值法计算变量的权重'''

    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

    # 求k
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    k = 1.0 / math.log(rows)

    lnf = [[None] * cols for i in range(rows)]

    # 矩阵计算--
    # 信息熵
    # p=array(p)
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf

    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # 计算各指标的权重
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # 计算各样本的综合得分,用最原始的数据

    w = pd.DataFrame(w)
    return w

if __name__ == '__main__':

    # 计算df各字段的权重
    #df=dataframe[['u0x','u0y','u1x','u1y','u2x','u2y','u3x','u3y','ce0','ce1','ce2','ce3']]
    df = dataframe[['ce0', 'ce1', 'ce2', 'ce3']]
    w = cal_weight(df)  # 调用cal_weight
    w.index = df.columns
    w.columns = ['weight']
    print(w)
    print('运行完成!')



    #df = dataframe[['u0x','u0y','u1x','u1y','u2x','u2y','u3x','u3y']]
    df = dataframe[['u0y',  'u1y',  'u2y',  'u3y']]

    w = cal_weight(df)  # 调用cal_weight
    w.index = df.columns
    w.columns = ['weight']
    print(w)
    print('运行完成!')

    df = dataframe[['u0x',  'u1x',  'u2x',  'u3x']]


    w = cal_weight(df)  # 调用cal_weight
    w.index = df.columns
    w.columns = ['weight']
    print(w)
    print('运行完成!')
