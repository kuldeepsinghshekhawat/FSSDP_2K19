# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:37:10 2019

@author: lenovo
"""


import pandas as pd
#it is the pandas lib
#import numpy as np
reviews=pd.read_csv("ign.csv")
#read the csv file
xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
#it define that score must be greater than 7 and platform is Xbox One
filtered_reviews = reviews[xbox_one_filter]
#it filter the value 
filtered_reviews.head()
#it display only head values
#%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].hist()

reviews[reviews["platform"] == "PlayStation 4"]["score"].hist(color="pink")

filtered_reviews["score"].hist(color="red")
        