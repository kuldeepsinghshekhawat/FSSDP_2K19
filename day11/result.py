# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:49:45 2019

@author: lenovo
"""
from matplotlib import pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.ylabel("girl_grades")
plt.ylabel("boys_grades")
plt.xlabel("grades_range")
plt.style.use('ggplot')
plt.plot(grades_range,girls_grades,label="girls",linestyle='--',color="red")
plt.plot(grades_range,boys_grades,label="boys",color="blue")
plt.axis([20,100,10,100]);
plt.scatter(grades_range,girls_grades, marker='.', color='black',label="marker='{0}'".format('.')); 
plt.scatter(grades_range,boys_grades, marker='.', color='blue',label="marker='{0}'".format('.')); 
plt.legend()
plt.show()