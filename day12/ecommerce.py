# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:46:53 2019

@author: lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))
plt.hist(incomes,50)
plt.show()