# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:07:50 2019

@author: lenovo
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read the csv file
dataset=pd.read_csv("mushrooms.csv")
features=dataset.iloc[:,[5,21,22]].values
labels=dataset.iloc[:,0].values


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])


from sklearn.preprocessing import LabelEncoder
labelencoder1 = LabelEncoder()
features[:,1] = labelencoder1.fit_transform(features[:,1])


from sklearn.preprocessing import LabelEncoder
labelencoder2 = LabelEncoder()
features[:,2] = labelencoder2.fit_transform(features[:,2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]




from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[1])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]



from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[2])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features, labels)

#Calculate Class Probabilities
probability = classifier.predict_proba(features)

# Predicting the class labels
labels_pred = classifier.predict(features)

pd.DataFrame(labels_pred, labels)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels, labels_pred)




    







