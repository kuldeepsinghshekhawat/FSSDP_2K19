# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:06:25 2019

@author: lenovo
"""

"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
    
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("deliveryfleet.csv")
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
plt.title('deliveryfleet')
plt.xlabel('distance')
plt.ylabel('speed')
plt.show()

kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'urban')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'rural')
plt.title('deliveryfleet')
plt.xlabel('distance')
plt.ylabel('speed')
plt.legend()
plt.show()


le=np.mean(dataset["Speeding_Feature"])
np.mean(dataset["Distance_Feature"])
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'urban_follow')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'rural_follow')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'urban_notfollow')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'yellow', label = 'rural_notfollow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'black', label = 'Centroids')
plt.title('deliveryfleet')
plt.xlabel('distance')
plt.ylabel('speed')
plt.legend()
plt.show()


