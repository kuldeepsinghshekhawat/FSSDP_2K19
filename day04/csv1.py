# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:27:17 2019

@author: lenovo
"""

import csv

with open('passwd') as passwd, open('output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            print(w.writerow((record[0], record[2])))
passwd.close()
output.close()
