# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:52:18 2019

@author: lenovo
"""
popularity=[]
language=[]
import csv
from collections import Counter
import matplotlib.pyplot as plt
with open ('bardata.csv') as csv_reader :
    reader=csv.reader(csv_reader,delimiter=',')
    for i in reader:
        popularity.append(i[0])
        language.append(i[1])
    print(popularity)
    print(language)
       # You could have used the zip function here 
    print(language.most_common(10))
    languages=[]
    popularity=[]
    for item in language.most_common(10):
        languages.append(item[0])
        popularity.append(item[1])
    print(popularity)
    print(languages)    