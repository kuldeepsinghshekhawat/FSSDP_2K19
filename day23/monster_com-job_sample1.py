# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:20:04 2019

@author: lenovo
"""


"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""

import pandas as pd
import numpy as np
import re

dataset=pd.read_csv('monster_com-job_sample.csv')
dataset["organization"] = dataset["organization"].fillna("Missing")

def loc_swap(values):
    loc, org = values
    if re.match(r'[A-Za-z]+\,\s[A-Z]{2}\s?[0-9]*',org):
        loc, org = org, loc
    return pd.Series([loc,org])

dataset[["location","organization"]] = dataset[["location","organization"]].apply(loc_swap, axis=1)
dataset["salary"]=dataset["salary"].fillna(0)



# Clean up the fields a bit these are not required
dataset = (dataset.drop(["job_board", "has_expired", "country", "country_code", "uniq_id"],axis='columns'))


def sal_hourly(val1):
    if pd.isnull(val1):
        return np.nan
    elif '\hour' in val1:
        sal1=val1.split('\hour')[0].replace("$"," ").strip()
        if '-' in sal1:
            mn=sal1.split('-')[0]
            mn1=sal1.split('-')[1]
            try:
                mn=float(mn.replace(',',' ').strip())
                mn1=float(mn.replace(',',' ').strip())
            except:
                return (np.nan,mn,mn1)
            
            
def sal_yearly(val1):
    if pd.isnull(val1):
        return np.nan
    elif '\hour' in val1:
        sal1=val1.split('\year')[0].replace("$"," ").strip()
        if '-' in sal1:
            mn=sal1.split('-')[0]
            mn1=sal1.split('-')[1]
            try:
                mn=float(mn.replace(',',' ').strip())
                mn1=float(mn.replace(',',' ').strip())
            except:
               return (np.nan,mn,mn1)
pd.Series(dataset['salary'])                            
dataset=dataset.assign(sal_hourly1=pd.Series(dataset['salary']).apply(sal_hourly))
dataset=dataset.assign(sal_yearly1=dataset['salary'].apply(sal_yearly))