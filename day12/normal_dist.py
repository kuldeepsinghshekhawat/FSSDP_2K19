# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:00:24 2019

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt                       
normal_dist = np.random.normal(150,20,1000)
print (type(normal_dist))
print (normal_dist.size)
print (normal_dist)
print("Mean value is: ", np.mean(normal_dist))
print("Median value is: ", np.median(normal_dist))
print("Standard Deviation is: ", np.std(normal_dist))
plt.hist(normal_dist,100)
plt.show()