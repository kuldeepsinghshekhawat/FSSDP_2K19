# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:08:23 2019

@author: lenovo
"""

#class=class is a group of the objects

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

        
    def work(self):
        if self.occupation=="table tennis ":
            print(self.name,"Kuldeep Singh Shekhhawat")
        elif  self.occupation=="Actor":
            print(self.name,"Karina kapoor")
            
    def speaks(self):
        print(self.name,"Hello How are You")


tom=Human('hello','what')
tom.work()
tom.speaks()