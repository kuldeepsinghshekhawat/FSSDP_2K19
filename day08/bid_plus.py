# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:00:46 2019

@author: lenovo
"""

from  selenium import webdriver
import pandas as pd
#from selenium import webdriver
from collections import OrderedDict
from time import sleep
from bs4 import BeautifulSoup as BS
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Firefox("geckodriver.exe")
browser.get(url)
sleep(2)
get_bid_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[1]')
get_bid_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()
right_table=driver.find_element_by_class_name('table')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        G.append(cells[5].text.strip())


col_name = ["Bid_no."]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G]))
df = pd.DataFrame(col_data) 
df.to_csv("data/former.csv")


driver.quit()

