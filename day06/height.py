# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:37:16 2019

@author: lenovo
"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

   
       
    


#height_count = 0
   
my_filter_list=list(filter(lambda x:'height' in x,people))
print(my_filter_list)

t=reduce(lambda x,y:x+y, (map(lambda x:x['height'],my_filter_list)))
print(t)
avg=t/len(my_filter_list)
print(avg)
