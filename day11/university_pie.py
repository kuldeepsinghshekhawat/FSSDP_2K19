# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:20:05 2019

@author: lenovo
"""
import csv
import matplotlib.pyplot as plt

with open('University_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    Cabrini = 0
    Beaver = 0
    Albany = 0
    Maryland = 0
    Alaska_Methodist_University = 0
    uni_data = {}
    
    next(csv_reader)
    for i in csv_reader:
        if i[0] in uni_data:
            uni_data[i[0]] += int(i[1])
        else:
            uni_data[i[0]] = int(i[1])
        if i[0]=="Cabrini":
            Cabrini = int(i[1])+Cabrini
        if i[0]=="Beaver":
            Beaver = int(i[1])+Beaver
        if i[0]=="Albany":
           Albany = int(i[1])+Albany
        if i[0]=="Maryland":
            Maryland = int(i[1])+Maryland
        if i[0]=="Alaska_Methodist_University":
             Alaska_Methodist_University= int(i[1])+ Alaska_Methodist_University

objects = tuple(map(lambda x: x ,uni_data.keys()))
performance = list(map(lambda x: x ,uni_data.values()))
print(objects)
print(performance)    
print ("Cabrini : "+str(Cabrini))
print ("Beaver : "+str(Beaver))
print ("Albany : "+str(Albany))
print ("Maryland : "+str(Maryland))
print (" Alaska_Methodist_University : "+str( Alaska_Methodist_University))
labels = ('carbini','Beaver','Albany','Maryland','Alaska_Methodist_University ')
x_index = [0,1,2,3,4]
performance=[33947,50723,38622,23936,8829]
colors =['blue','red','yellow','green','pink']
#colors =['#008fd5','#fc4f30','#e5ae37','#6d904f']

plt.pie(performance,labels=labels, colors=colors, wedgeprops={'edgecolor':'black'},autopct='%.0f%%')
plt.axis('equal')
plt.show()