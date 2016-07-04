# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:52:21 2016

@author: ranyijun
"""
'''
处理正负样本

'''

import pandas as pd

label_aug = pd.read_csv('./../data/label_Aug.csv')
label_sep = pd.read_csv('./../data/label_Sep.csv')
label_all = pd.merge(label_aug, label_sep, on = 'IMSI')

label_all.to_csv('./../data/label_all.csv',index = None)
#label_all.to_excel('label_all.xlsx',index = None)