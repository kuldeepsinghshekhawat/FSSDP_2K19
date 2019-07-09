# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:56:47 2019

@author: lenovo
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.getcwd()

os.chdir('/content/drive/My Drive/deep learning')

import pandas as pd
train_data = pd.read_csv("iris_training.csv")
test_data=pd.read_csv("iris_test.csv")

train_data.shape

test_data.shape

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

features1 = train_data.iloc[:, :-1].values
labels1 = train_data.iloc[:, -1:].values

features2=test_data.iloc[:,:-1].values
labels2=test_data.iloc[:,-1].values

from sklearn.linear_model import LogisticRegression
reg3 = LogisticRegression()
reg3.fit(features1, labels1)
# Predicting the Test set results
labels_pred2 = reg3.predict(features2)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels2, labels_pred2)
cm

probability = reg3.predict_proba(features2)
probability

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

features1.shape

#adding the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 4))
​
​# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
​
# Adding the output layer
classifier.add(Dense(units = 3, kernel_initializer = 'uniform', activation = 'sigmoid'))
​
# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder(categorical_features = [0])
labels1 = onehotencoder.fit_transform(labels1).toarray()

classifier.fit(features1, labels1, batch_size = 120, epochs = 1000)

labels_pred = classifier.predict(features2)
pred = np.argmax(labels_pred, axis=1)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels2, pred)
cm



