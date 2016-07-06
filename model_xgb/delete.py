# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:03:19 2016

@author: zhongtong
"""

import pandas as pd

label_Aug = pd.read_csv('./../data/label_single_2all.csv')
IMSI = []
sum1 = []
for i  in range(0,len(label_Aug)):
    IMSI.append(label_Aug['IMSI'][i])
    sum1.append(sum(label_Aug.ix[i][1:9]))
        
label_Aug['sum'] = sum1
label_Aug.to_csv('label_num.csv',index = None,encoding = 'utf-8')