# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:07:49 2016

@author: ranyijun
"""

import pandas as pd

label_Aug = pd.read_csv('./../data/label_single_all.csv')
ll = label_Aug.drop(['IMSI', 'y1', 'y9'], axis=1)
label = ll.columns
labely = []
for i in label:
    test1 = label_Aug[label_Aug[i] == 1]
    test11 = list(test1.IMSI)
    labely.append(test11)
num = []
for lab in labely:    
      a = lab + 1
      t11 = pd.DataFrame(columns=["IMSI"])
      t11.IMSI = lab
      label_11 = pd.merge(label_Aug, t11, on = 'IMSI')
      n = label_11.shape
      num.append(n[0])
      