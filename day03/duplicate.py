# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:30:19 2019

@author: lenovo
"""

given_list =  [12,24,35,24,88,120,155,88,120,155]

# parsing given list into set to remove duplicate entries
# then again parsing it back to list
output_list = list(set(given_list))

# reversing the new list
output_list.sort()

print(output_list)