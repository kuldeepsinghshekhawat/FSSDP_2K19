# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:58:50 2019

@author: lenovo
"""

"""dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.

"""
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset.head(15)
dataset = dataset[dataset["Item"] != "NONE"]
top_15 = dataset["Item"].value_counts()[:15]

#pie chart of the 15 top selling items
dataset.isnull().any(axis="columns")
selling = list(top_15.index)
slices = list(top_15.values)
plt.pie(slices,labels=selling,autopct='%.0f%%')
plt.axis('equal')
plt.legend()
plt.show()



#transactions = []
#for i in range(0, 21293):
#    transactions.append([str(dataset.values[i,j]) for j in range(0, 4)])

def cart(values):
    items = list(set(values))
    return items

transactions = list(dataset.groupby("Transaction")["Item"].apply(cart))

rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)
print(results)