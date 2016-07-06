# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:35:33 2016

@author: zhongtong
"""
import pandas as pd
from pandas import DataFrame
label_Aug = pd.read_csv('label_single_2all.csv')
sum1 = []
for i in range(0,len(label_Aug)):
    a = [j for j,v in enumerate(label_Aug.ix[i][1:10]) if v==1]
    if len(a) == 0:
        sum1.append(8)
    elif len(a) ==1:
            sum1.append(a[0])
    else:
        a1 = sorted(a)[0]
        a2 = sorted(a)[1]
        min_a = a2-a1
        sum1.append(min_a)
        
df0 = DataFrame(columns = ['IMSI','sum'])
df0['IMSI'] = label_Aug['IMSI']
df0['sum'] = sum1
df0.to_csv('time_num.csv',index = None,encoding = 'utf-8')