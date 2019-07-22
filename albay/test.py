
# Open classif_1.tiff and read it to see where the training data coordinates are
# then save it to a save file 


import numpy as np
from osgeo import gdal

d5 = gdal.Open("classif_5.tif")
ts1_b1 = np.array(d5.GetRasterBand(1).ReadAsArray())
print(ts1_b1.shape)

count = 0

classif1coordinates = []

for ix,iy in np.ndindex(ts1_b1.shape):
    if (ts1_b1[ix,iy]!=51):
        classif1coordinates.append ([ix,iy])
        count = count + 1



f= open("classif_5.txt","w+")
for i in range(0,len(classif1coordinates)):
        f.write("%d %d \r\n" %(classif1coordinates[i][0],classif1coordinates[i][1]))

f.close()
