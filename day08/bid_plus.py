# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:00:46 2019

@author: lenovo
"""

from  selenium import webdriver
import pandas as pd
from collections import OrderedDict
from time import sleep
#from bs4 import BeautifulSoup as BS
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)
sleep(2)
for i in range(1,11):
    get_bid_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]')
    get_bid_result.click()


sleep(5)
bid_no=[]
items=[]
quantity=[]
depart=[]
start_date=[]
start_time=[]
end_date=[]
end_time=[]
#pdf_name=[]
for i in range(1,11):
    A=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    bid_no.append(A.text)
    B=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    items.append(B.text)
    C=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    quantity.append(C.text)
    D=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    depart.append(D.text)
    E=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    start_date.append(E.text[:11])
    start_time.append(E.text[11:])
    F=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    end_date.append(E.text[:11])
    end_time.append(E.text[11:])
col_name = ["Bid_no.","items","quantity","depart","start_date","start_time","end_date","end_time"]
col_data = OrderedDict(zip(col_name,[bid_no,items,quantity,depart,start_date,start_time,end_date,end_time]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


browser.quit()
#//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span
#//*[@id="pagi_content"]/div[2]/div[2]/p[1]/span
//*[@id="pagi_content"]/div[2]/div[2]/p[2]/span
//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span
//*[@id="pagi_content"]/div[3]/div[3]/p[2]
//*[@id="pagi_content"]/div[3]/div[4]/p[1]/span