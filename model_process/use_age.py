# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:18:03 2016

@author: ranyijun
"""

import pandas as pd

nokia = pd.read_csv('imsib10_nokia.csv')
train_y = pd.read_csv('./../data/train_orig_all.csv', encoding = 'utf-8')[['IMSI','age']]
age_nokia = pd.merge(train_y, nokia, on = 'IMSI')