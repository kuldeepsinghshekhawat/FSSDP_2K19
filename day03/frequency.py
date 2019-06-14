# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:28:18 2019

@author: lenovo
"""

input_string = input("Enter String: ")
#we give the string
all_frequency = {}
#it is the initilizatonnof string
for alphabet in input_string: #it5 is use for individual elementif 
   
        all_frequency[alphabet]= all_frequency.get(alphabet,0) + 1
        print(all_frequency)
        break
   