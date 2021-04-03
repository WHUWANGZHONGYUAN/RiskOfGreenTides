import rasterio as rst
import numpy as np
from rasterio.plot import show
import matplotlib.pyplot as plt
import osr
import ogr
basepath=r"F:\WORDWIDE_Resample\Merge_predict_ssw\Merge\\"



def get_data(path):
    with rst.open(path, mode='r') as dst:
        suit = dst.read(1)
        unsuit = dst.read(2)
        dir = dst.read(3)
        spd = dst.read(4)
        show((dst, 1))
        profile = dst.profile
        transform = dst.transform
    return suit,dir,spd,profile



def sind(x): return np.sin(np.radians(x))
def cosd(x): return np.cos(np.radians(x))

def DegreeToMeter(x,y):
    source=osr.SpatialReference()
    source.ImportFromEPSG(4326)
    target = osr.SpatialReference()
    target.ImportFromEPSG(32651)
    transform = osr.CoordinateTransformation(source, target)
    point = ogr.CreateGeometryFromWkt("POINT ("+str(x)+" "+ str(y)+")")
    point.Transform(transform)
    lat=float(str(point.ExportToWkt()).split(" ")[1][1:-1])
    lon = float(str(point.ExportToWkt()).split(" ")[2][0:-1])
    return lat,lon

def MeterToDegree(x,y):
    source = osr.SpatialReference()
    source.ImportFromEPSG(32651)
    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(source, target)
    point = ogr.CreateGeometryFromWkt("POINT ("+str(x)+" "+ str(y)+")")
    point.Transform(transform)
    lon=float(str(point.ExportToWkt()).split(" ")[2][0:-1])
    lat = float(str(point.ExportToWkt()).split(" ")[1][1:-1])
    return lat,lon

def get_uv(speed,direction):
    u = speed * sind(direction)
    v = speed * cosd(direction)
    bad = np.where(speed<0)
    u[bad] = 0.
    v[bad] = 0.

    return u, v

def get_risk(u,v,suit):
    result=np.zeros(suit.shape)
    v_in = v * 30 * 24 * 60 * 60/1109470
    u_in = u * 30 * 24 * 60 * 60/1109470
    for i in range(suit.shape[0]):
        for j in range(suit.shape[1]):
            #lat=i/10.0-90
            #lon=j/10.0-180
            #x,y=DegreeToMeter(lat,lon)
            #x = x + u_in[i][j]  # 纬向风
            #y=y+v_in[i][j]#经向风
            #i1,j1=MeterToDegree(x,y)
            i1=i + u_in[i][j]
            j1=j + v_in[i][j]
            if j1<0:
                j1=suit.shape[1]-1+j1
            elif j1>=suit.shape[1]:
                j1=j1-suit.shape[1]
            if i1<0:
                i1=-i1
            elif i1>=suit.shape[0]:
                i1=suit.shape[0]-1-i1

            j1=int(j1)
            i1=int(i1)
            result[i1][j1]=suit[i][j]
    return result




years=['2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
for y in years:
    for m in month:
        if y=="2019" and (m=="07" or m=="11" or m=="12"):
            continue
        mergepath=basepath+"Merge"+y+m+'.tif'
        suit,dir,spd,profile=get_data(mergepath)
        u, v = get_uv(spd, dir)
        risk = get_risk(u, v, suit)
        profile.update(count=1)
        with rst.open(basepath + "Risk/Risk"+y+m+".tif", mode='w', **profile) as dst:
            dst.write(risk, 1)

        print(y+m)