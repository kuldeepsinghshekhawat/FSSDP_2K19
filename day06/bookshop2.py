# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:39:48 2019

@author: lenovo
"""

from collections import OrderedDict

mylist = []
dict1 = OrderedDict()



orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]


for newList in orders:
        orderNum = newList[0]
        info = (newList[1:])
        for i in info:
           mylist.append([orderNum,(list(i)[1] * list(i)[2])])
       
for new in mylist:
        dict1[new[0]] = dict1.get(new[0], 0) +  new[1] 
        #print(dict1)
        if(dict1[new[0]] < 100):
             print((new[0],dict1[new[0]]))
        else:
          print(dict1)  
    
    
    