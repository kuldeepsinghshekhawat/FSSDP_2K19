# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:58:31 2019

@author: lenovo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0].values
labels = dataset.iloc[:, 1].values

#let's first analyze the data
# Visualising the Linear Regression results
plt.scatter(features, labels)
features=np.array(features)
features=features.reshape(78,1)

labels=np.array(labels)
labels=labels.reshape(78,1)


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
print ("Predicting result with Linear Regression")
print (lin_reg_1.predict(6))


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('blugills ')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


#  fitting using polynomila regression
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform(6)))

plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('blugills ')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

