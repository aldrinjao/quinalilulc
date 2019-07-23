# Open classif_4.tiff and read it to see where the training data coordinates are
# then save it to a save file 

import numpy as np
from osgeo import gdal

files = ["classif_1","classif_2","classif_3","classif_4","classif_5"]

classif_coords = []
TIMESTEPS = 31

def getCoords(filename):
    intxtfile = "../training data coords/"+ filename + ".txt"
    f= open(intxtfile,"r")
    f1 = f.read().splitlines()
    return f1


# put all tif files in these arrays 2nd column corresponds to time step



def extract_vv(file):
    
    intiffile = "../s1_2018/clipped/"+str(file)+".tif"
    d = gdal.Open(intiffile)

    return d.GetRasterBand(1).ReadAsArray().ravel()

def extract_vh(file):

    intiffile = "../s1_2018/clipped/"+str(file)+".tif"
    d = gdal.Open(intiffile)

    return d.GetRasterBand(2).ReadAsArray().ravel()

def extract(filename):

        classif_coords = getCoords(filename + "_ravel")

        classif_length = len(classif_coords)

        ts_vv = np.zeros((classif_length,31))
        ts_vh = np.zeros((classif_length,31))

        vv = np.zeros((1677610,))
        vh = np.zeros((1677610,))
        
        for x in range(1,32):
        
                vv = extract_vv(x)
                vh = extract_vh(x)

                for y in range(0,classif_length):
                        ts_vv[y][x-1] = vv[int(classif_coords[y])]
                        ts_vh[y][x-1] = vh[int(classif_coords[y])]

        np.savetxt("../training data coords/layer data/"+ filename +"_vv.csv", ts_vv, '%5.5f', delimiter=",")
        np.savetxt("../training data coords/layer data/"+ filename +"_vh.csv", ts_vh, '%5.5f', delimiter=",")

for x in files:
        extract(x)