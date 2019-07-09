# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:11:01 2019

@author: lenovo
"""
"""Q3. Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset=pd.read_csv("data.csv") 
#1. Visualize the various countries from where the artworks are coming.
fet1=dataset["Country"].value_counts()
cnt1 = list(fet1.index)
slices = list(fet1.values)
plt.pie(slices,labels=cnt1,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()


dt1=dataset['Artist Role'].value_counts()[:2]
cnt11 = list(dt1.index)
slices1 = list(dt1.values)
plt.pie(slices1,labels=cnt11,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()



dt1=dataset['Artist Display Name'].value_counts()[:2]
cnt11 = list(dt1.index)
slices1 = list(dt1.values)
plt.pie(slices1,labels=cnt11,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()


dt111=dataset['Culture'].value_counts()[:2]
cnt111 = list(dt111.index)
slices11 = list(dt111.values)
plt.pie(slices11,labels=cnt111,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()



dt1112=dataset['Artist Display Name'].value_counts()
cnt1112 = list(dt111.index)
slices112 = list(dt111.values)
plt.pie(slices112,labels=cnt1112,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()



# Using the elbow method to find the optimal number of clusters
"""from sklearn.cluster import KMeans


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()



# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)


plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = '''')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'assualt')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'rape')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('crimme')
plt.xlabel('city')
plt.ylabel('crime_rate')
plt.legend()
plt.show()

"""

