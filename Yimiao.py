import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
X = np.linspace(1, 10,endpoint=True)

Y1=1/X

plt.plot(X, Y1)
plt.xticks([])  # 去掉横坐标值
plt.yticks([])  # 去掉纵坐标值
plt.xlabel("人数",fontsize=15)
plt.ylabel("效度",fontsize=15)
plt.show()