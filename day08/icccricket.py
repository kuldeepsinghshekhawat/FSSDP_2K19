# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:30:47 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
score=" https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(score).text
print(source)
soup = BeautifulSoup(source, "lxml")
print(soup)
print (soup.prettify())
print (soup)

print (soup.prettify())

print (soup.head)


print (soup.body)
right_table=soup.find("table")

print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    # first row has no TH, but other rows have one TH and 4 TD
    #cells = row.findall('td') 
    # first row has 7 TH 
    cells = row.findAll('td')
    # other than first row
    if len(cells) == 5:
         A.append(cells[0].text.strip())
         B.append(cells[1].text.strip())
         C.append(cells[2].text.strip())
         D.append(cells[3].text.strip())
         E.append(cells[3].text.strip())
from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")

