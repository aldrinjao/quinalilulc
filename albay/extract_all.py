# Open classif_1.tiff and read it to see where the training data coordinates are
# then save it to a save file 


import numpy as np
from osgeo import gdal
import pandas as pd

def extract(file):

    bands = ['vv','vh']

    for b in bands:
        if (b=='vv'):
            rasterband = 1
        else:
            rasterband = 2

        intiffile = "../s1_2018/clipped/" + str(file) + ".tif"

        image = gdal.Open(intiffile)
        band1 = np.array(image.GetRasterBand(rasterband).ReadAsArray().ravel())

        
        df = pd.DataFrame(band1)
        
        outfile = "../s1_2018/csv/"+ b + "/"+str(file)+".csv"
        df.to_csv(outfile,index=False,header=False)



for i in range(1,32):
    extract(i)
        