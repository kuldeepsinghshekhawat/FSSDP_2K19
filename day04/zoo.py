# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:31:21 2019

@author: lenovo
"""

import csv
#it is the csv library
with open('zoo.csv','rU') as csv_file:# open a zoo file
    csv_reader = csv.reader(csv_file, delimiter=',') #it is the read the csv file
    
    for row in csv_reader:#for loop define the how many rows in csv file
        print (row)

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for column in csv_reader:
        for i in range(len(column)):
            print (column[i])
with open('zoo.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed = 0
    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        total_water_needed = int(column[2])+total_water_needed

print ("Total water needed by all the animals : "+str(total_water_needed))



with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed_elephant = 0
    total_water_needed_tiger = 0
    total_water_needed_zebra = 0
    total_water_needed_lion = 0
    total_water_needed_kangaroo = 0


    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        if column[0]=="elephant":
            total_water_needed_elephant = int(column[2])+total_water_needed_elephant
        if column[0]=="tiger":
            total_water_needed_tiger = int(column[2])+total_water_needed_tiger
        if column[0]=="zebra":
            total_water_needed_zebra = int(column[2])+total_water_needed_zebra
        if column[0]=="lion":
            total_water_needed_lion = int(column[2])+total_water_needed_lion
        if column[0]=="kangaroo":
            total_water_needed_kangaroo = int(column[2])+total_water_needed_kangaroo


print ("Total water needed by aelephant : "+str(total_water_needed_elephant))
print ("Total water needed by tiger : "+str(total_water_needed_tiger))
print ("Total water needed by zebra : "+str(total_water_needed_zebra))
print ("Total water needed by lion : "+str(total_water_needed_lion))
print ("Total water needed by kangaroo : "+str(total_water_needed_kangaroo))
