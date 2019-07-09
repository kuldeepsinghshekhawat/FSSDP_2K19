# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:52:45 2019

@author: lenovo
"""
"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, 
remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""
import pandas as pd
from apyori import apriori
import numpy as np
import matplotlib.pyplot as plt
# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

def cart(values):
    item=list(set(values))
    if np.nan in item:
        item.remove(np.nan)
    return item

item1 = list(dataset.apply(cart,axis=1))

rules = apriori(item1, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")





