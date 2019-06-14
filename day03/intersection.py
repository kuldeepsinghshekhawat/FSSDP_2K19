# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:26:59 2019

@author: lenovo
"""

list_1 = [1,3,6,78,35,55]
list_2 = [12,24,35,24,88,120,155]

#these list define the list_1 and list_2
intersection_list = list(set(list_1).intersection(set(list_2)))

print (intersection_list)