from rasterio.transform import from_origin
import rasterio
import numpy as np
fname=r"D:\辐照度软件\MYD28M_2014-01-01_3600x1800.csv"
Z=np.loadtxt(fname,dtype="float",delimiter=',',skiprows=1,usecols=None,unpack=False)
Z[Z==99999]=0
Z=np.delete(Z, 0, axis=1)
print(Z)
res=0.25
transform = from_origin(-179.875, 89.875, res, res)
new_dataset = rasterio.open('sst.tif', 'w', driver='GTiff',height=Z.shape[0],width=Z.shape[1],count=1,dtype=Z.dtype,crs='+proj=latlong',transform=transform)
new_dataset.write(Z, 1)
new_dataset.close()