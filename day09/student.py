# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:19:14 2019

@author: lenovo
"""

import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'student.db' )
c = conn.cursor()
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE student(
          st_name TEXT,
          st_age INTEGER,
          st_rool_no INTEGER,
          st_branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('krishna',20,12345,'cse')")
c.execute("INSERT INTO student VALUES ('komal',20,1235,'cse')")
c.execute("INSERT INTO student VALUES ('prashant',16,2345,'cse')")
c.execute("INSERT INTO student VALUES ('ajij',10,1345,'ec')")
c.execute("SELECT * FROM student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM student")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["st_name","st_age","st_roll_no","st_branch"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()





