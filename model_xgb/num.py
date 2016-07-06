# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:33:51 2016

@author: ranyijun
"""

import pandas as pd
result = pd.read_csv('presub_all.csv', encoding = None)
tt = list(result.score)
hh = []
for i in tt:
    rr = '%.6f'%float(i)
    hh.append(rr)

result.score = hh
result.to_csv('presubmit_all.csv',index=None,encoding='utf-8')
