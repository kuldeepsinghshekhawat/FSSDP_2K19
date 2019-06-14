# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:36:16 2019

@author: lenovo
"""

my_list = []

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "EinfÃ¼hrung in Python3, Bernd Klein",  3, 24.99]]


for i in orders :
    orderNum = int(i[0])
    quantity = i[2]
    price = i[3]
    total = quantity * price
    if total<=100:
        total =total + 10
    else:
        total
    my_list.append((orderNum,total))  
    
print(my_list)    