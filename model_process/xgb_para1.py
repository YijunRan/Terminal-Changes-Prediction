# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:56:24 2016

@author: ranyijun
"""

import pandas as pd
#import xgboost as xgb
import sys,random
import cPickle
import os


#load data
brand = ['IMSI','brand_1','brand_2','brand_3','brand_4','brand_5','brand_6','brand_7','brand_8','brand_9','brand_10','brand_11','brand_12']
#model = ['IMSI','model_1','model_2','model_3','model_4','model_5','model_6','model_7','model_8','model_9','model_10','model_11','model_12']
train_x = pd.read_csv('./../data/train_orig_all.csv', encoding = 'utf-8')[brand]
#train_y = pd.read_csv('./../data/train_orig_all.csv')[model]
#b1 = pd.read_csv('./../data/b11.csv')[['IMSI']]
#bra = pd.merge(train_y, b1, on = 'IMSI')
#train_x.loc[train_x['brand_1'] == 'Apple', 'b1'] = 1
#train_x.loc[train_x['brand_1'] == 'Samsung', 'b1'] = 1
#train_x.loc[train_x['brand_1'] == 'HUAWEI', 'b1'] = 1
#train_x.loc[train_x['brand_1'] == 'Nokia', 'b1'] = 1
train_x.loc[train_x['brand_1'] == 'Xiaomi', 'b1'] = 1

#train_x.loc[train_x['brand_2'] == 'Apple', 'b2'] = 1
#train_x.loc[train_x['brand_2'] == 'Samsung', 'b2'] = 1
#train_x.loc[train_x['brand_2'] == 'HUAWEI', 'b2'] = 1
#train_x.loc[train_x['brand_2'] == 'Nokia', 'b2'] = 1
train_x.loc[train_x['brand_2'] == 'Xiaomi', 'b2'] = 1

#train_x.loc[train_x['brand_3'] == 'Apple', 'b3'] = 1
#train_x.loc[train_x['brand_3'] == 'Samsung', 'b3'] = 1
#train_x.loc[train_x['brand_3'] == 'HUAWEI', 'b3'] = 1
#train_x.loc[train_x['brand_3'] == 'Nokia', 'b3'] = 1
train_x.loc[train_x['brand_3'] == 'Xiaomi', 'b3'] = 1

#train_x.loc[train_x['brand_4'] == 'Apple', 'b4'] = 1
#train_x.loc[train_x['brand_4'] == 'Samsung', 'b4'] = 1
#train_x.loc[train_x['brand_4'] == 'HUAWEI', 'b4'] = 1
#train_x.loc[train_x['brand_4'] == 'Nokia', 'b4'] = 1
train_x.loc[train_x['brand_4'] == 'Xiaomi', 'b4'] = 1

#train_x.loc[train_x['brand_5'] == 'Apple', 'b5'] = 1
#train_x.loc[train_x['brand_5'] == 'Samsung', 'b5'] = 1
#train_x.loc[train_x['brand_5'] == 'HUAWEI', 'b5'] = 1
#train_x.loc[train_x['brand_5'] == 'Nokia', 'b5'] = 1
train_x.loc[train_x['brand_5'] == 'Xiaomi', 'b5'] = 1

#train_x.loc[train_x['brand_6'] == 'Apple', 'b6'] = 1
#train_x.loc[train_x['brand_6'] == 'Samsung', 'b6'] = 1
#train_x.loc[train_x['brand_6'] == 'HUAWEI', 'b6'] = 1
#train_x.loc[train_x['brand_6'] == 'Nokia', 'b6'] = 1
train_x.loc[train_x['brand_6'] == 'Xiaomi', 'b6'] = 1

#train_x.loc[train_x['brand_7'] == 'Apple', 'b7'] = 1
#train_x.loc[train_x['brand_7'] == 'Samsung', 'b7'] = 1
#train_x.loc[train_x['brand_7'] == 'HUAWEI', 'b7'] = 1
#train_x.loc[train_x['brand_7'] == 'Nokia', 'b7'] = 1
train_x.loc[train_x['brand_7'] == 'Xiaomi', 'b7'] = 1

#train_x.loc[train_x['brand_8'] == 'Apple', 'b8'] = 1
#train_x.loc[train_x['brand_8'] == 'Samsung', 'b8'] = 1
#train_x.loc[train_x['brand_8'] == 'HUAWEI', 'b8'] = 1
#train_x.loc[train_x['brand_8'] == 'Nokia', 'b8'] = 1
train_x.loc[train_x['brand_8'] == 'Xiaomi', 'b8'] = 1

#train_x.loc[train_x['brand_9'] == u'苹果', 'b9'] = 1
#train_x.loc[train_x['brand_9'] == u'三星', 'b9'] = 1
#train_x.loc[train_x['brand_9'] == u'华为', 'b9'] = 1
#train_x.loc[train_x['brand_9'] == u'诺基亚', 'b9'] = 1
train_x.loc[train_x['brand_9'] == u'小米', 'b9'] = 1

#train_x.loc[train_x['brand_10'] == u'苹果', 'b10'] = 1
#train_x.loc[train_x['brand_10'] == u'三星', 'b10'] = 1
#train_x.loc[train_x['brand_10'] == u'华为', 'b10'] = 1
#train_x.loc[train_x['brand_10'] == u'诺基亚', 'b10'] = 1
train_x.loc[train_x['brand_10'] == u'小米', 'b10'] = 1

#train_x.loc[train_x['brand_11'] == u'苹果', 'b11'] = 1
#train_x.loc[train_x['brand_11'] == u'三星', 'b11'] = 1
#train_x.loc[train_x['brand_11'] == u'华为', 'b11'] = 1
#train_x.loc[train_x['brand_11'] == u'诺基亚', 'b11'] = 1
train_x.loc[train_x['brand_11'] == u'小米', 'b11'] = 1

#train_x.loc[train_x['brand_12'] == u'苹果', 'b12'] = 1
#train_x.loc[train_x['brand_12'] == u'三星', 'b12'] = 1
#train_x.loc[train_x['brand_12'] == u'华为', 'b12'] = 1
#train_x.loc[train_x['brand_12'] == u'诺基亚', 'b12'] = 1
train_x.loc[train_x['brand_12'] == u'小米', 'b12'] = 1
bb = ['IMSI','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12']
train_x[bb].to_csv('./../data/Xiaomi.csv',index = None, encoding = 'utf-8')