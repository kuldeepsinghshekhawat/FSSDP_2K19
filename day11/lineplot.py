# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:50:15 2019

@author: lenovo
"""
from matplotlib import pyplot as plt

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


#The Median/Avergae salary of the Developer from the age of 18  to  55
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 
49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 
98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
#dev_y.sort()
#print(dev_y)

#The Median/Avergae salary of the Python Developer from the age of 18  to  55
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 
57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 
112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
#py_dev_y.sort()
#print(py_dev_y)
        


#The Median/Avergae salary of the Jav Script Developer from the age of 18  to  55
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 
49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 
102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
#js_dev_y.sort()
#print(js_dev_y)
plt.xlabel("Ages of developer")
plt.ylabel("salery")

plt.title("Median/Avergae salary of the Developer")
# Changing the x axes limits of the scale
# Or

plt.style.use('ggplot')
plt.plot(ages_x, dev_y,label="developer",linestyle='--')
plt.plot(ages_x, py_dev_y,label="python",linestyle='-')
plt.plot(ages_x, js_dev_y,label="javascript",linestyle='solid')
plt.axis([17, 56, 17000, 150000]);
plt.legend()
plt.show()
plt.style.use('ggplot')
plt.bar(ages_x, dev_y,label="developer",linestyle='--')
plt.bar(ages_x, py_dev_y,label="python",linestyle='-')
plt.bar(ages_x, js_dev_y,label="javascript",linestyle='solid')
plt.axis([17, 56, 17000, 150000]);
plt.legend()
plt.show()
width=.4
labels = ('18-21', '22-25', '26-29','30-33','34-37','38-41','42-45','46-49','50-53','54-57')
x_index = [0,1,2,3,4,5,6,7,8,9]
for i in x_index:
    plt.bar(i-width/3,dev_y, width/3, align='center', alpha=1.0,color='RED')
    plt.bar(i,py_dev_y, width/3, align='center', alpha=1.0,color='blue') 
    plt.bar(i+width/3,js_dev_y, width/3, align='center', alpha=1.0,color='orange')
plt.show()
