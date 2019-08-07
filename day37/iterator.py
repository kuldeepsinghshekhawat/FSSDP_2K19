# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:21:59 2019

@author: lenovo
"""

#iterators=It represent the stream of data
string='123456789'
string1=iter(string)
new=next(string1)


for i in iter(string):
    print(i)
    