# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:03:53 2019

@author: lenovo
"""

#while loop work same as for loop
direction=["east","west","east-north","north-west"]
choice=" "
while choice not in direction:
    choice =input("Enter the data")
    if choice==quit:
        print("game over")
    else:
        print("You are very great person")