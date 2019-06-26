# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:13:44 2019

@author: lenovo
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head(10))
print (dataset.describe())
features = dataset.iloc[:,:1].values
bahubali=dataset.iloc[:,1].values
dangal=dataset.iloc[:,2].values
x=np.array(2).reshape(-1,1)
#prepare the data to train the model
#from sklearn.model_selection import train_test_split  
#features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression 
reg=LinearRegression()
reg1=LinearRegression()
reg.fit(features,bahubali)
print(reg.coef_)
print(reg.intercept_)
reg1.fit(features,dangal)
print(reg1.coef_)
print(reg1.intercept_)
print (reg.coef_*10 + reg.intercept_)
print (reg.predict(x))
print (reg1.coef_*10 + reg.intercept_)
print (reg1.predict(x))

plt.scatter(features, bahubali, color = 'violet')
plt.scatter(features, dangal, color = 'yellow')

plt.plot(features, reg.predict(features), color = 'red')
plt.title('Bahubali and  dangal')
plt.xlabel('day')
plt.ylabel('bahubali and dangal')
plt.show()