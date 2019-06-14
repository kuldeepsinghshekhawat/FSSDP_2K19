# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:17:08 2019

@author: lenovo
"""

import collections
d = collections.OrderedDict()
   
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
#my_list=list(map(lambda x:'order_number' in x,orders))
#print(my_list)

order_number = (34587 , 98762, 77226,88112) 
quantity=(4,5,3,3)
price_per_item=(40.95,56.80,32.95,24.99)
g=tuple(list(map(lambda x,y:x*y,quantity,price_per_item)))
print(g)
# This leads to non readable tuples 
#t1=collections.namedtuple(map(lambda order_number,quantity:order_number*quantity ,orders))
#print(t1)

#Solution is NAMEDTUPLE
#order_number = collections.namedtuple('orders', ['Learning Python Mark Lutz','Programming Python Mark Lutz','Head First Python Paul Barry','Einführung in Python3 Bernd Klein'])

print (type(order_number))
print(tuple(order_number))
print(tuple(list(map(lambda x,g:x,order_number,g))))
print(g+order_number)