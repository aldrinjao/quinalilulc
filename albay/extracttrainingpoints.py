
# Open classif_1.tiff and read it to see where the training data coordinates are
# then save it to a save file 


import numpy as np
from osgeo import gdal

classif = ["classif_1","classif_2","classif_3","classif_4","classif_5"]


def extract(filename):
        intiffile = filename + ".tif"
        d5 = gdal.Open(intiffile)
        ts1_b1 = np.array(d5.GetRasterBand(1).ReadAsArray())
        print(ts1_b1.shape)

        count = 0

        classif1coordinates = []



        for ix,iy in np.ndindex(ts1_b1.shape):
                if (ts1_b1[ix,iy]!=51):
                        classif1coordinates.append ([ix,iy])
                        count = count + 1


        outtxtfile = "../training data coords/"+ filename + ".txt"
        f= open(outtxtfile,"w+")
        for i in range(0,len(classif1coordinates)):
                f.write("%d %d \r\n" %(classif1coordinates[i][0],classif1coordinates[i][1]))

        f.close()




def extract2(filename):


        classif1coordinates = []
        intiffile = filename + ".tif"

        d5 = gdal.Open(intiffile)
        ts1_b1 = np.array(d5.GetRasterBand(1).ReadAsArray().ravel())

        lenght = len(ts1_b1)
        i = 0
        while i < lenght:
                if (ts1_b1[i]!=51):
                        classif1coordinates.append(i)
                i +=1
                
        outtxtfile = "../training data coords/"+ filename + "_ravel.txt"
        f= open(outtxtfile,"w+")
        for i in range(0,len(classif1coordinates)):
                f.write("%d \r\n" %(classif1coordinates[i]))

        f.close()


for i in classif:
        extract2(i)