# -*- coding: utf-8 -*-
"""
Created on Sat May 07 14:13:43 2016

@author: zhongtong
"""

import pandas as pd

#df = pd.read_csv('./../data/label_test112.csv',encoding = 'utf-8')
df = pd.read_csv('./../data/unapple.csv',encoding = 'utf-8').fillna(0)
IMSI0 = []
IMSI1 = []
for i in range(0,len(df)):
    if df['b1'][i] == 0:
        IMSI0.append(df['IMSI'][i])
    else:
        IMSI1.append(df['IMSI'][i])
        
    
#df0 = pd.DataFrame(columns = ['IMSI'])
#df0['IMSI'] = IMSI0
#df0.to_csv('./../data/imsi_untest112.csv',index = None,encoding = 'utf-8')
df1 = pd.DataFrame(columns = ['IMSI'])
df1['IMSI'] = IMSI1
df1.to_csv('./../data/imsi_apple6s.csv',index = None,encoding = 'utf-8')        