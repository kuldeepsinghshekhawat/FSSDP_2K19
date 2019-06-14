# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:05:07 2019

@author: lenovo
"""
with open("words.txt","rt") as f1:
    read = f1.read()
    #f1.read("my name is kuldeep singh shekhawat")
with open("mailing.txt","wt") as f2:
        #f2.write(" sobhasaria engineering college")
        #for line in f1:
            f2.write(read)
           
        