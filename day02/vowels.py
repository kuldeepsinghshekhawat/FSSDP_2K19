# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:33:41 2019

@author: lenovo
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels="aeiouAEIOU"
main = []

for name in state_name:
    new = ""
    for i in name:
        if i not in vowels:
            new += i
    main.append(new)

print(main)
             