# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:58:36 2019

@author: lenovo
"""
#importing the library
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#read the csv file
dataset=pd.read_csv("affairs.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[6,7])
features=onehotencoder.fit_transform(features).toarray()

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


probability=classifier.predict_proba(features_test)

labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred,labels_test)
classifier.score(features_test,labels_test)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
x = [1,0,0,0,0,0,0,0,0,0,4,25,3,1,4,16,4,2]
x = np.array(x)
x = x.reshape(1,-1)
classifier.predict(x)

probability1=classifier.predict_proba(x)
from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
x = sc1.fit_transform(x)
x = sc1.transform(x)


