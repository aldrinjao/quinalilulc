from numpy import mean
from numpy import std
from numpy import dstack, stack, vstack, hstack
from pandas import read_csv
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.utils import to_categorical
from keras.models import model_from_json

import csv
import keras
import numpy as np
import pandas as pd

# fit and evaluate a model
def evaluate_model(trainX, trainy, testX, testy):

	verbose, epochs, batch_size = 1, 50, 32
	n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]


	model = Sequential()
	model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps,n_features)))
	model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
	model.add(Dropout(0.5))
	model.add(MaxPooling1D(pool_size=2))
	model.add(Flatten())
	model.add(Dense(100, activation='relu'))
	model.add(Dense(n_outputs, activation='softmax'))

	callbacks_list = [
		keras.callbacks.ModelCheckpoint(
			filepath='best_model.{epoch:02d}-{val_loss:.2f}.h5',
			monitor='val_loss', save_best_only=True),
		keras.callbacks.EarlyStopping(monitor='acc', patience=1)
	]
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	# fit network
	model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose, callbacks=callbacks_list, validation_data=(testX,testy))


	# evaluate model
	_, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=1)


	# serialize model to JSON
	model_json = model.to_json()
	with open("model.json", "w") as json_file:
		json_file.write(model_json)
	# serialize weights to HDF5
	model.save_weights("model.h5")
	print("Saved model to disk")



	return accuracy

# summarize scores
def summarize_results(scores):
	print(scores)
	m, s = mean(scores), std(scores)
	print('Accuracy: %.3f%% (+/-%.3f)' % (m, s))


def getLabels(filename):
    intxtfile = "../training data coords/"+filename+"/classified_"+  filename +"_label.csv"
    f= open(intxtfile,"r")
    f1 = f.read().splitlines()
    return to_categorical(f1)

def getAndStackRows(pointtype):

	data_arr=list()
	band = ["vv","vh"]
	filename = ""
	
	for x in band:

		filename = "../training data coords/" +	pointtype+"/" +pointtype+"_"+str(x)+".csv"
		dataframe = read_csv(filename, header=None)
		data_arr.append(dataframe.values)

	data_arr = dstack(data_arr)
	return data_arr



def getAndStackRowsForPrediction():

	data_arr=list()
	band = ["vv","vh"]
	
	for x in band:

		outfile = "../s1_2018/csv/"+x+"/"+x+".csv"
		print(outfile)
		
		
		dataframe = read_csv(outfile, header=None)
		data_arr.append(dataframe.values)

	data_arr = dstack(data_arr)
	return data_arr





def appendRowsForPredicting():

	
	band = ["vv","vh"]

	for x in band:
	
		data_arr = list()
	
		for num in range(1,32):

			outfile = "../s1_2018/csv/"+x+"/"+str(num)+".csv"
			dataframe = read_csv(outfile, header=None)
			data_arr.append(dataframe.values)

		data_arr = hstack(data_arr)
		outfile = "../s1_2018/csv/"+ x + "/"+x+".csv"
		data_arr = pd.DataFrame(data_arr)
		data_arr.to_csv(outfile,index=False,header=False)





def read_dataset():
	traininglabels = getLabels("training")
	testlabels = getLabels("test")
	trainingrows = getAndStackRows("training")
	testrows = getAndStackRows("test")

	print(trainingrows.shape,traininglabels.shape,testrows.shape,testlabels.shape)
	return trainingrows, traininglabels, testrows, testlabels

	# stack train_vv and train_vh 
	# this will produce a [len(train_vv),timesteps,band] 3d array
	# read the classified/label data and use to_categorical to produce [len(train_vv),len(classes)]
	# do this for test data set too

# run an experiment
def train_test_model():
	
	# load data

	# change thisssssssssssss
	trainX, trainy, testX, testy = read_dataset()
	# change thisssssssssssss

	# repeat experiment

	scores = list()
	score = evaluate_model(trainX, trainy, testX, testy)
	score = score * 100.0
	print('>#%.3f' % (score))
	scores.append(score)
	
	# summarize results
	summarize_results(scores)


def predict(data):


	# load json and create model
	json_file = open('model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights("model.h5")
	print("Loaded model from disk")


	loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	# loaded_model.predict



	# load model here
	print("use loaded model here")

	classified = loaded_model.predict(data)
	return classified

################################################################


################## run the experiment
#
# train_test_model()

################## retrieve actual data to be classified
# 
# appendRowsForPredicting()


################## stack the two bands
# 
actualData = getAndStackRowsForPrediction()

################## call the function to predict
#
# results = predict(actualData) 
