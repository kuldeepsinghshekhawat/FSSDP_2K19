# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:49:28 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
score=" https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(score).text
print(source)
soup = BeautifulSoup(source, "lxml")
print(soup)
print (soup.prettify())

print (soup.head)


print (soup.body)
right_table=soup.find("table")
print(right_table)
