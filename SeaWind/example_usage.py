from SeaWind.windsat_daily_v7 import WindSatDaily
from SeaWind.windsat_averaged_v7 import WindSatAveraged
def read_data(filename=r'F:\浒苔适生环境数据\SeaWind\wsat_201606v7.0.1.gz'):
    dataset = WindSatAveraged(filename, missing=missing)
    #if not dataset.variables: sys.exit('file not found')
    return dataset

lons = (118,125)
lats = (31,38)
iasc = 0
wspdname = 'w-aw'
wdirname = 'wdir'
missing = -999.

def myvmax(): return 16
def myscale(): return 160
def mycolor(): return 'white'

#----------------------------------------------------------------------------

def show_dimensions(ds):
    print('')
    print('Dimensions')
    for dim in ds.dimensions:
        aline = ' '.join([' '*3, dim, ':', str(ds.dimensions[dim])])
        print(aline)

def show_variables(ds):
    print('')
    print('Variables:')
    for var in ds.variables:
        aline = ' '.join([' '*3, var, ':', ds.variables[var].long_name])
        print(aline)

def show_validrange(ds):
    print('')
    print('Valid min and max and units:')
    for var in ds.variables:
        aline = ' '.join([' '*3, var, ':',
                str(ds.variables[var].valid_min), 'to',
                str(ds.variables[var].valid_max),
                '(',ds.variables[var].units,')'])
        print(aline)

def set_image(vmin,vmax,extent):
    myimage = {}
    myimage['origin'] = 'lower' 
    myimage['vmin'] = vmin
    myimage['vmax'] = vmax
    myimage['extent'] = extent
    myimage['interpolation'] = 'nearest'
    return myimage

def quikquiv(plt,lon,lat,u,v,scale,region,color):    
    # selecting the sub-region is not necessary,
    # but it greatly reduces time needed to render plot   
    ilon1,ilon2,ilat1,ilat2 = region
    xx = lon[ilon1:ilon2+1]
    yy = lat[ilat1:ilat2+1]
    uu = u[ilat1:ilat2+1,ilon1:ilon2+1]
    vv = v[ilat1:ilat2+1,ilon1:ilon2+1]

    plt.quiver(xx,yy,uu,vv,scale=scale,color=color) 

def show_plotexample(dataset, figname='plot_example.png',date='201601'):
    #print('')
    #print('Plot example:')

    # modules needed for this example:
    import numpy as np
    import pylab as plt
    from matplotlib import cm
    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 用来显示正常中文的标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.rcParams['font.size'] = 18  # 用来正常显示负号
    # here is the data I will use:
    wspd = dataset.variables[wspdname]
    wdir = dataset.variables[wdirname]
    land = dataset.variables['land']


    # get lon/lat:
    lon = dataset.variables['longitude']
    lat = dataset.variables['latitude']

    # get metadata:
    name = dataset.variables[wspdname].long_name
    units = dataset.variables[wspdname].units
    vmin = dataset.variables[wspdname].valid_min
    vmax = dataset.variables[wspdname].valid_max

    # get extent of dataset:    
    extent = []
    extent.append(dataset.variables['longitude'].valid_min)
    extent.append(dataset.variables['longitude'].valid_max)
    extent.append(dataset.variables['latitude'].valid_min)
    extent.append(dataset.variables['latitude'].valid_max)

    # get region to plot:   
    ilon1 = np.argmin(np.abs(lons[0]-lon))
    ilon2 = np.argmin(np.abs(lons[1]-lon))
    ilat1 = np.argmin(np.abs(lats[0]-lat))
    ilat2 = np.argmin(np.abs(lats[1]-lat))
    region = (ilon1,ilon2,ilat1,ilat2)

    # get u and v from wspd and wdir:
    from SeaWind.bytemaps import get_uv
    u,v = get_uv(wspd,wdir)
    bad = np.where(wspd<0)
    u[bad] = 0.
    v[bad] = 0.

    # set colors:
    palette = cm.jet
    palette.set_under('black')
    palette.set_over('grey')
    wspd[land] = 1.E30

    # my preferences:
    vmax = myvmax()
    scale = myscale()
    color = mycolor()

    # make the plot:
    fig = plt.figure()
    plt.imshow(wspd,**set_image(vmin,vmax,extent))

    plt.colorbar()
    plt.xlim(lons)
    plt.ylim(lats)
    quikquiv(plt,lon,lat,u,v,scale,region,color)
    #plt.title(name+' ('+units+')')

    plt.title(date,fontsize=25,family="Times New Roman")
    plt.grid()

    plt.tick_params(labelsize=16)
    fig.savefig(figname)
    #print(' '.join([' '*3,'Saving:',figname]))
    plt.show()
    wspd[land]=np.nan
    wspd[wspd==-999]=np.nan

    speed=wspd[124*4:126*4,120*4:122*4]

    wdir[land]=np.nan
    wdir[wdir==-999]=np.nan

    dir=wdir[124*4:126*4,120*4:122*4]
    dir[dir<=90]=dir[dir<=90]+360
    return date,np.nanmean(speed),np.nanmean(dir)

#----------------------------------------------------------------------------

if __name__ == '__main__':
    import numpy as np
    import sys
    dataset = read_data()
    show_dimensions(dataset)
    show_variables(dataset)
    show_validrange(dataset)
    show_plotexample(dataset)
    print('')
    print('done')
    print('')
    spd5=[]
    spd6=[]
    spd7=[]
    spd8=[]
    dir5 = []
    dir6 = []
    dir7 = []
    dir8 = []
    basepath=r"F:\浒苔适生环境数据\SeaWind"
    for i in range(2019,2020):
        for j in range(1,13):
            path=basepath+r"\wsat_"+str(i)+"0"+str(j)+"v7.0.1.gz"
            dataset=read_data(path)
            #show_variables(dataset)
            #show_validrange(dataset)
            figname=basepath+r"\\"+str(i)+"0"+str(j)+".jpg"
            date=str(j)
            if j==5:
                date="May in "+ str(i)
            elif j==6:
                date="June in "+str(i)
            elif j==1:
                date="July in "+str(i)
            elif j==8:
                date="August in "+str(i)
            re=show_plotexample(dataset,figname=figname,date=date)
            print(re)
            if j==5:
                spd5.append(re[1])
                dir5.append(re[2])
            elif j==6:
                spd6.append(re[1])
                dir6.append(re[2])
            elif j==7:
                spd7.append(re[1])
                dir7.append(re[2])
            elif j==8:
                spd8.append(re[1])
                dir8.append(re[2])
    print(np.mean(spd5))
    print(np.mean(spd6))
    print(np.mean(spd7))
    print(np.mean(spd8))
    print(np.mean(dir5))
    print(np.mean(dir6))
    print(np.mean(dir7))
    print(np.mean(dir8))
