# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:13:49 2019

@author: lenovo
"""

import csv

with open("passwd.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",",)
    # row has the list of all columns
    for passwd,etc in csv_reader:
        print (passwd,etc)
        

with open('employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')

employee_writer.writerow(['root:*:0:0::0:0:System Administrator:/var/root:/bin/shdaemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false'])
employee_writer.writerow(['root:*:0:0::0:0:System Administrator:/var/root:/bin/shdaemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false'])
read = csv_file.read()
employee_file.write(read)