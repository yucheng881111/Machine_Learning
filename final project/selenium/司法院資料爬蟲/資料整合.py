# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:16:46 2020

@author: user
"""

import pandas as pd
df1 = pd.read_csv('Result_123-121.csv')
df2 = pd.read_csv('Result_1217-123.csv')
#df3 = pd.read_csv('Result_1124-1116.csv')
#df4 = pd.read_csv('Result_1126-1124.csv')
#df5 = pd.read_csv('Result_1130-1126.csv')
#df6 = pd.read_csv('Result_930-928.csv')

a=[]
li1=df1.values.tolist()
for i in li1:
    a.append(i[1])

li2=df2.values.tolist()
for i in li2:
    a.append(i[1])
'''
li3=df3.values.tolist()
for i in li3:
    a.append(i[1])

li4=df4.values.tolist()
for i in li4:
    a.append(i[1])

li5=df5.values.tolist()
for i in li5:
    a.append(i[1])

li6=df6.values.tolist()
for i in li6:
    a.append(i[1])
'''
df=pd.DataFrame(pd.unique(a).tolist())
df.to_csv('December.csv')












