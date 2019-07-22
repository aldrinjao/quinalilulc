import random
import math
import numpy as np
import csv

def getCoords(filename):
    intxtfile = "../training data coords/"+ filename
    f= open(intxtfile,"r")
    f1 = f.read().splitlines()
    return f1


def splitcoords(filenum):

    filename = "classif_"+str(filenum)

    char_list = getCoords(filename+"_ravel.txt")
    coords_length = len(char_list)

    coord_list = np.zeros((coords_length,))

    y = 0
    for x in char_list:
        coord_list[y] = y
        y += 1

    random.shuffle(coord_list) #shuffle the list


    splitindex = int(len(coord_list) * .7)

    s1 = coord_list[0 : splitindex] 

    s2 = coord_list[splitindex : len(coord_list)] 

    filename = filename+".txt"
    training_out = "../training data coords/classification/" + filename

    f= open(training_out,"w+")
    for i in range(0,len(s1)+len(s2)):
            f.write("%d \r\n" %(int(filenum)))

    f.close()


    return s1, s2


def splitbyband(filename,band,training,test):

    coords_arr = []
    training_arr = []
    test_arr = []
    with open("../training data coords/layer data/"+filename+"_"+band+".csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        # print(spamreader)
        for row in spamreader:
            coords_arr.append(row)

    y = 0
    for i in training:
        x = int(i)
        training_arr.append(coords_arr[x])

    y = 0
    for i in test:
        x = int(i)
        test_arr.append(coords_arr[x])

    with open("../training data coords/training/"+filename+"_"+band+".csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in training_arr:
            spamwriter.writerow(row)


    with open("../training data coords/test/"+filename+"_"+band+".csv", 'w', newline='') as csvfile:
        spamwriter2 = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in test_arr:
            spamwriter2.writerow(row)

def splitdata(filename):
    
    training, test = splitcoords(filename)
    filename = "classif_"+ str(filename)
    splitbyband(filename, 'vv', training, test)
    splitbyband(filename, 'vh', training, test)




# append 1 band
def append(type,band):
    data_arr = []    

    classif_arr = []
    for z in range(1,6):
        filename = "../training data coords/" + type +"/" + "classif_" + str(z) + "_" + band +".csv" 


        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            
            # print(spamreader)
          
            for row in spamreader:
                data_arr.append(row)
                classif_arr.append(z)
        


    filename = str(type)+"_" + band + ".csv"

    with open("../training data coords/"+type+"/"+filename, 'w+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in data_arr:
            spamwriter.writerow(row)


    filename = str(type)+"_label"  + ".csv"
    f= open("../training data coords/"+type+"/classified_"+filename, 'w+')
    for i in classif_arr:
            f.write("%d \r\n" %(i-1))

    f.close()


for x in range(1,6):
    splitdata(x)
append("test","vv")
append("test","vh")
append("training","vv")
append("training","vh")
