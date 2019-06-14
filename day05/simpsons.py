# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:48:56 2019

@author: lenovo
"""
import re

fh = open("simpsons_phone_book.txt")
for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
fh.close()