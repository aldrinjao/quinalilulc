# get pixel values from multiple images then assign a label 

import numpy as np
from osgeo import gdal

d5 = gdal.Open("classif_5.tif")
ts1_b1 = np.array(d5.GetRasterBand(1).ReadAsArray())
print(ts1_b1.shape)

