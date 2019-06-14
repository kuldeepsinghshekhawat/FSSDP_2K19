# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:01:13 2019

@author: lenovo
"""

newstr="RESTART"
#define the value
txt=newstr.replace("R",'$')
#it is use for replace the value of R as $
print(txt)
#it print the value of txt
apr=txt.replace("$",'R',1)
#It defines that left the first R
print(apr) 