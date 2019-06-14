# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:58:54 2019

@author: lenovo
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.student
def add_student(idd,first,last,pay):
    unique_student = mydb.student.find_one({"id":idd})
    if unique_student:
        return "student already exists"
    else:
        mydb.student.insert(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "student added successfully"

def fetch_all_student():
    user = mydb.employees.find()
    for i in user:
        print (i)



add_student('01','Sylvester', 'Fernandes', 50000)
add_student('02','Yogendra', 'Singh', 70000)
add_student('03','Rohit', 'Mishra', 30000)
add_student('04','Kunal', 'Vaid', 30000)
add_student('05','Devendra', 'Shekhawat', 30000)


fetch_all_student()
    


"""
Database handling using MongoDB on Cloud -  Mongo Atlas
"""


import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://kuldeep:pass%40000@cluster0-po45j.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb = client.shekhawat

def add_student(idd,first,last,pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.collect_1.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "student added successfully"


def fetch_all_student():
    user = mydb.collect_1.find()
    for i in user:
        print (i)




add_student(1,'Sylvester', 'Fernandes', '50000')
add_student(2,'Yogendra', 'Singh', 70000)
add_student(3,'Rohit', 'Mishra', 30000)
add_student(4,'Kunal', 'Vaid', 30000)
add_student(5,'Devendra', 'Shekhawat', 30000)
fetch_all_student()