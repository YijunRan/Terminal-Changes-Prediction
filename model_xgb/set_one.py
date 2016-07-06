# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:23:10 2016

@author: ranyijun
"""

import pandas as pd

#data1 = pd.read_csv('data1.csv')
data0 = pd.read_csv('diffimsi.csv',encoding = 'utf-8')[['IMSI']]
data1 = pd.read_csv('imsi_apple6s.csv',encoding = 'utf-8')[['IMSI']]
data = list(set(data0.IMSI)) + list(set(data1.IMSI))
data2 = list(set(data))
submit = pd.read_csv('submit_all.csv')
submit_list = list(submit.IMSI)
for i in data2:
    for j in submit_list:
      if i == j:
        submit.loc[submit['IMSI'] == i, 'score'] = 0.000002
submit.to_csv('presub_all.csv', index = None, encoding = 'utf-8')