# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:43:49 2019

@author: lenovo
"""

import csv
with open('population.csv') as pop:
    r = csv.reader(pop, delimiter=',')
    next(r)
    dict1 = {}
    for record in r:
        if dict1.get(record[3]):
            value = record[2].replace(',','')
            dict1["India,"+record[3]] += int(value)
        else:
            value = record[2].replace(',','')
            dict1["India,"+record[3]] =  int(value)
    print(dict1)
    