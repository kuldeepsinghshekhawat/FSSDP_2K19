# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:35:13 2019

@author: lenovo
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
dataset=pd.read_csv("BreadBasket_DMS.csv")
dataset["Item"].isnull().any(axis=0)
dataset=dataset[dataset["Item"] !="NONE"]
top15=dataset["Item"].value_counts()[:15]
selling=list(top15.index)
slices=list(top15.values)
plt.pie(slices,labels=selling,autopct='%.0f%%')
plt.axis("equal")
plt.show()

def cart(values):
    items=list(set(values))
    return items

item1=dataset.groupby("Transaction")["Item"].apply(cart)



rules = apriori(item1, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
