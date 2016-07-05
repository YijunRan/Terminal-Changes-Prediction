# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:03:58 2016

@author: ranyijun
"""

import pandas as pd

imsi = pd.read_csv('./../data/unimsi_12.csv',encoding = 'utf-8')
label_Aug = pd.read_csv('./../data/label_single_2all.csv')
imsi_aug = pd.merge(imsi,label_Aug, on = 'IMSI')
imsi_aug.to_csv('./../data/label_single_12unchange.csv',index = None, encoding = 'utf-8')