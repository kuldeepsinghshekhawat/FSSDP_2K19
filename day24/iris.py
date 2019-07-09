# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:55:03 2019

@author: lenovo
"""
"""

Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).

    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
#from sklearn.utils import load_iris
iris=load_iris()
features=pd.DataFrame(iris.data,columns=iris.feature_names).values
#labels=pd.DataFrame(iris.target,columns=["class"])


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)


plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Iris setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Iris virginica')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = ' Iris versicolor')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('iris')
plt.xlabel('sample')
plt.ylabel('species')
plt.legend()

plt.show()

