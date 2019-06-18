# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:26:54 2019

@author: lenovo
"""

import csv
import matplotlib.pyplot as plt

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed_elephant = 0
    total_water_needed_tiger = 0
    total_water_needed_zebra = 0
    total_water_needed_lion = 0
    total_water_needed_kangaroo = 0
    zoo_data = {}
    
    next(csv_reader)
    for i in csv_reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])
        if i[0]=="elephant":
            total_water_needed_elephant = int(i[2])+total_water_needed_elephant
        if i[0]=="tiger":
            total_water_needed_tiger = int(i[2])+total_water_needed_tiger
        if i[0]=="zebra":
            total_water_needed_zebra = int(i[2])+total_water_needed_zebra
        if i[0]=="lion":
            total_water_needed_lion = int(i[2])+total_water_needed_lion
        if i[0]=="kangaroo":
            total_water_needed_kangaroo = int(i[2])+total_water_needed_kangaroo

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))
print(objects)
print(performance)    
print ("Total water needed by aelephant : "+str(total_water_needed_elephant))
print ("Total water needed by tiger : "+str(total_water_needed_tiger))
print ("Total water needed by zebra : "+str(total_water_needed_zebra))
print ("Total water needed by lion : "+str(total_water_needed_lion))
print ("Total water needed by kangaroo : "+str(total_water_needed_kangaroo))
labels = ('aelephant','tiger','zebra','lion','kangroo')
x_index = [0,1,2,3,4]
performance=[1650,1550,1290,2366,1595]
plt.bar(x_index, performance, width = 0.5, align='center', alpha=1.0)

# First Parameters is the indexes and second paramters is the labels
plt.xticks(x_index, labels)

plt.ylabel('no. of aniaml which have water needed')
plt.xlabel('animals')
plt.title('water neede by all animals')
 
plt.show()


