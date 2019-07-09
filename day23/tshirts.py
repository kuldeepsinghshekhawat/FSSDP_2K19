# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:55:10 2019

@author: lenovo
"""
"""
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("tshirts.csv")
features=dataset.iloc[:,[1,2]].values
plt.scatter(features[:,0],features[:,1],color='red')
plt.show()
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('tshirts')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

#kmeans has
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'medium')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'large')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'small')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'black', label = 'Centroids')

plt.title('tshirts')
plt.xlabel("height")
plt.ylabel('weight')
plt.legend()
plt.show()
