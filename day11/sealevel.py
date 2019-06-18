# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:25:09 2019

@author: lenovo
"""
year=[]
sealevel=[]
import csv
with open("sealevel.csv","r") as sea:
    reader=csv.reader(sea,delimiter=',')
    for i in reader:
        year.append(i[0])
        sealevel.append(i[1])
        print(year)
        print(sealevel)
from matplotlib import pyplot as plt
year=[int(x) for x in year[1:]]
sealevel=[float(x) for x in sealevel[1:] ]
plt.xlabel("year")
plt.ylabel("water level")

plt.title("sea level rise in past 100 years")
# Changing the x axes limits of the scale
# Or

plt.style.use('ggplot')
plt.axis([1880, 2015, .92, 8.673700393]);
plt.plot(year,sealevel,label="sealevel")
plt.legend()
plt.show()