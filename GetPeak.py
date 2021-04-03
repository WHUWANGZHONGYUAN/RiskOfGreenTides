import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from scipy import signal
from scipy.optimize import root
import numpy as np
def sigmoid(x):
    return 1.0/(1+np.exp(-x))
def poly(x,a,b,c,d):
    return a*x*x*x+b*x*x+c*x+d

t=np.arange(110,215,1)
x = poly(t,0.002494,-1.424,269.1, 16780)
#peaks, _ = find_peaks(x, height=0)
#print(peaks)
plt.plot(t,x)
#plt.plot(peaks, x[peaks], "x")
#plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()
t=signal.argrelextrema(x,np.greater)
print(t)
t=signal.argrelextrema(x,np.less)
print(t)
print("变化点")
keyday2016= np.array([-0.0007663,0.3526, -52.13,2500])
p=np.poly1d(keyday2016)
yyyd = np.polyder(p,2) # 1表示一阶导
print(yyyd.r)

keyday2017=np.array([-0.0003127,0.09713,-7.119, 7.136])
p=np.poly1d(keyday2017)
yyyd = np.polyder(p,1) # 1表示一阶导
print(yyyd.r)

keyday2018=np.array([0.002494,-1.424,269.1, 16780])
p=np.poly1d(keyday2018)
yyyd = np.polyder(p,1) # 1表示一阶导
print(yyyd.r)

keyday2019=np.array([0.000744,-0.4338,82.56, -5099])
p=np.poly1d(keyday2019)
yyyd = np.polyder(p,1) # 1表示一阶导
print(yyyd.r)

A1=0.01
A2=100
a=5.60745117
x0=34.4508757
def logis_0_2016(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-0.1
sol2 = root(logis_0_2016, 34)
print(sol2.x)
def logis_1(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-99.5
sol2 = root(logis_1, 35)
print(sol2.x)

A1=0
A2=100
a=1.47125821
x0=33.2173174

def logis_0_2016(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-0.01
sol2 = root(logis_0_2016, x0)
print(sol2.x)
def logis_1(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-99.5
sol2 = root(logis_1, x0)
print(sol2.x)


A1=0
A2=100
a=5.34955918
x0=34.7390012

def logis_0_2016(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-0.01
sol2 = root(logis_0_2016, x0)
print(sol2.x)
def logis_1(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-99.5
sol2 = root(logis_1, x0)
print(sol2.x)


A1=0
A2=100
a=10
x0=34.91

def logis_0_2016(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-0.01
sol2 = root(logis_0_2016, x0)
print(sol2.x)
def logis_1(x):
    return A1+((A2-A1)/(1+np.exp(-a*(x-x0))))-99.5
sol2 = root(logis_1, x0)
print(sol2.x)
