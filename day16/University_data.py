# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:44:56 2019

@author: lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("University_data.csv")
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)


# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))
x=[0,0,0,1,315,3,4,9.25,1]
x=np.array(x)
x = x.reshape(1,9)
regressor.predict(x)

le = labelencoder.transform(['Beaver'])
ohe = onehotencoder.transform(le.reshape(1,-1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],312,3,4,9.33,1]
x = np.array(x)
x=x.reshape(1,-1)
regressor.predict(x)
print(x)


