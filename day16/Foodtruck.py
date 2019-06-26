# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:03:06 2019

@author: lenovo
"""
#importing  library
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Foodtruck.csv')  

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head(10))
print (dataset.describe())
features = dataset.iloc[:,:-1].values
labels=dataset.iloc[:,1].values
#prepare the data to train the model
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression 
reg=LinearRegression()
reg.fit(features,labels)
print(reg.coef_)
print(reg.intercept_)
print (reg.coef_*3.073 + reg.intercept_)
print (reg.predict(3.073))
plt.scatter(features, labels, color = 'violet')
plt.plot(features, reg.predict(features), color = 'red')
plt.title('Population and profit')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()
