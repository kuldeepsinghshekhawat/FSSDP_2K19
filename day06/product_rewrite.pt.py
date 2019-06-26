# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:33:14 2019

@author: lenovo
"""

from functools import reduce

list1=[1,2,3,4,5,6,7] 
def productOfOdds(list):
    return reduce(lambda x,y:x*y, filter(lambda x:x%2==1, map(lambda x:x,list1)))
print(productOfOdds(list1))
