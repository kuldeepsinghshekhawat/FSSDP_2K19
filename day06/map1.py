# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:03:33 2019

@author: lenovo
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
#for i in range(len(names)):
#names[i] = 
print (names)
g= map(lambda x:random.choice(code_names),names)
print(list(g))