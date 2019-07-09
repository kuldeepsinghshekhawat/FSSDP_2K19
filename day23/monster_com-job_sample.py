# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:09:31 2019

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
                  
def map_yearly_salary_range(val):
    if pd.isnull(val):
        return np.nan
    elif "/year" in val:
        part = val.split("/year")[0].replace("$", " ").strip()
        if "-" in part:
            mn, mx = part.split("-")[0:2]
            try:
                mn = float(mn.replace(",", "").strip())
                mx = float(mx.replace(",", "").strip())
            except:
                return np.nan
            return mn, mx
        
def map_hourly_salary_range(val):
    if pd.isnull(val):
        return np.nan
    elif "/hour" in val:
        part = val.split("/hour")[0].replace("$", " ").strip()
        if "-" in part:
            mn, mx = part.split("-")[0:2]
            try:
                mn = float(mn.replace(",", "").strip())
                mx = float(mx.replace(",", "").strip())
            except:
                return np.nan
            return mn, mx
        
dataset =dataset.assign(yearly_salary_range=dataset['salary'].map(map_yearly_salary_range),
                   hourly_salary_range=dataset['salary'].map(map_hourly_salary_range))

print("We found {0} yearly and {1} hourly salaries in the dataset.".format(
    dataset['yearly_salary_range'].notnull().sum(), dataset['hourly_salary_range'].notnull().sum()))



# Creating the plot for which sector how many job
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")

f, axarr = plt.subplots(1,2, figsize=(12,5))
f.subplots_adjust(hspace=1)
plt.suptitle('Monster Top 10 Jobs by...', fontsize=18)

bar_kwargs = {'fontsize': 14, 'color': 'darkgray'}

dataset['organization'].value_counts().head(10).plot.bar(ax=axarr[0], **bar_kwargs,  title='Industry Sector')
                                                     
dataset['sector'].value_counts().head(10).plot.bar(ax=axarr[1],**bar_kwargs,title='Job Type')
                                                         

sns.despine()

for n in [0, 1]:
    axarr[n].title.set_fontsize(16)
    axarr[n].set_xticklabels(axarr[n].get_xticklabels(), 
                             rotation=45, ha='right', fontsize=14)


f, axarr = plt.subplots(2, 1, figsize=(12, 8))
f.subplots_adjust(hspace=1)

bar_kwargs = {'fontsize': 14, 'color': 'darkgray'}

dataset =dataset.assign(
    median_yearly_salary = dataset['yearly_salary_range'].map(
        lambda r: (r[0] + r[1]) / 2 if pd.notnull(r) else r
    ),
    median_hourly_salary = dataset['hourly_salary_range'].map(
        lambda r: (r[0] + r[1]) / 2 if pd.notnull(r) else r
    )
)

sns.kdeplot(dataset[pd.notnull(dataset.median_yearly_salary)]['median_yearly_salary']\
                .where(lambda v: v < 200000), 
            ax=axarr[0]
)
sns.kdeplot(dataset[pd.notnull(dataset.hourly_salary_range)]['median_hourly_salary']\
                    .where(lambda v: v < 100), ax=axarr[1] )

axarr[0].set_title("Median Yearly Salary Offered", fontsize=16)
axarr[1].set_title("Median Hourly Salary Offered", fontsize=16)

sns.despine()






