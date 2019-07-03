# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:16:43 2019

@author: lenovo
"""

"""
Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                    Impute the missing values with the most frequent values.
                    Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                    Check the accuracy of the model.
                    Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("breast_cancer.csv")
dataset.columns=["id number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape","Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitose","Class"]
dataset.isnull().any(axis=0)
dataset["Bare Nuclei"].fillna(np.mean)
features = dataset.iloc[:,1:10]
labels = dataset.iloc[:, -1]
dataset['Bare Nuclei']=dataset['Bare Nuclei'].fillna(dataset['Bare Nuclei'].mode())
#features[]=features[''].astype(np.float64)
features['Bare Nuclei']=features['Bare Nuclei'].fillna(features["Bare Nuclei"].mean()).values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.5, random_state = 0)
#visualisation for svc how many cancerous and not cancerous
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
score = classifier.score(features_test,labels_test)

x = [6,2,5,3,9,4,7,2,3]
x = np.array(x)
x = x.reshape(1,-1)
classifier.predict(x)

