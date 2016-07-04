# -*- coding: utf-8 -*-
"""
Created on Fri May 06 09:24:11 2016

@author: zhongtong
"""

import pandas as pd
import re
df = pd.read_csv('_11.csv')
df1 = pd.read_csv('label_single_1all.csv')
n = 0
yo = []
user = []
for i in range(0,len(df)):
    a = [j.lower() for j in re.findall(r'[^\s]+?',df['y1'][i])]
    b = [j.lower() for j in re.findall(r'[^\s]+?',df['y2'][i])]
    if (set(a+b) == set(a)) or set(a+b) == set(b):        
        yo.append(0)
    else:
        yo.append(1)
