# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:27:56 2019

@author: lenovo
"""

import pandas as pd
#it is the pandas lib
import numpy as np
automobile=pd.read_csv("Automobile.csv")
#read the csv file
automobile["price"].value_counts(dropna=False)
#dropna use for drop the nan value 
automobile[automobile['price'].isnull()]
automobile['price'] = automobile['price'].fillna(automobile['price'].mean())
#in the column price we fill the nan as mean value of price
print(automobile['price'])
csv = np.genfromtxt('Automobile.csv', delimiter=",")
#genfromtxt use for read and print only one column from csv file 
names = csv[:,-1]
#name define  only last column of the csv file
print(names)
data_price = automobile.sort_values(['price'])
print(data_price[data_price['price'] == data_price['price'].max()])
print(data_price[data_price['price'] == data_price['price'].min()])
print(data_price[data_price['price'] == data_price['price'].std()])
automobile['price'].mean()#mean value
automobile['price'].std()#standerd deviation
automobile['price'].min()#minimum value
automobile['price'].max()#max value of the price
