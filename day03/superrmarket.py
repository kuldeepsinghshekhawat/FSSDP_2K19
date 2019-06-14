# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:58:28 2019

@author: lenovo
"""

billing = {}




while True:
    super_market=input("enter the fruits and price").split(' ')
    if ' '.join(super_market[:-1]) in billing:
        billing[' '.join(super_market[:-1])] = int(billing[' '.join(super_market[:-1])]) + int(super_market[-1])
    else:
        billing[' '.join(super_market[:-1])] = super_market[-1]
    if super_market == ['']:
        break
billing[' JUICE']=9