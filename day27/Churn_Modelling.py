# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:04:30 2019

@author: lenovo
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.getcwd()

os.chdir('/content/drive/My Drive/App')

import pandas as pd
dataset = pd.read_csv("Churn_Modelling.csv")

dataset.shape

dataset.head()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

features = dataset.iloc[:, 3:13].values
labels = dataset.iloc[:, 13].values

features[1]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_features_1 = LabelEncoder()
features[:, 1] = labelencoder_features_1.fit_transform(features[:, 1])

labelencoder_features_2 = LabelEncoder()
features[:, 2] = labelencoder_features_2.fit_transform(features[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:] #dummy variable trap

features[1]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

features.shape

#adding the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(features_train, labels_train, batch_size = 10, epochs = 10)

labels_pred = classifier.predict(features_test)
labels_pred = (labels_pred > 0.5)

len(labels_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

cm
x=[600,'France','Male',40,3,60000,2,1,1,50000]
x=np.array(x)
x=x.reshape(1,-1)
x[:, 1] = labelencoder_features_1.transform(x[:, 1])

x[:, 2] = labelencoder_features_2.transform(x[:, 2])

x = onehotencoder.transform(x).toarray()

x = x[:, 1:]

x.shape

x=sc.transform(x)

result=classifier.predict(x)
result
