import rasterio
import matplotlib.pyplot
from rasterio.plot import show
from matplotlib import pyplot

basepath=r"F:\WORDWIDE_Resample\Predict\merge_2016_01.tif"
src = rasterio.open(basepath)
show((src, 1),cmap='pink',transform=src.transform)
pyplot.show()