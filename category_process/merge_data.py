# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:32:38 2016

@author: ranyijun
"""

import pandas as pd

test1 = pd.read_csv('./../data/test1.csv',encoding = 'utf-8')
test2 = pd.read_csv('./../data/test2.csv',encoding = 'utf-8')
test3 = pd.read_csv('./../data/test3.csv',encoding = 'utf-8')
test4 = pd.read_csv('./../data/test4.csv',encoding = 'utf-8')
test5 = pd.read_csv('./../data/test5.csv',encoding = 'utf-8')
test6 = pd.read_csv('./../data/test6.csv',encoding = 'utf-8')
test7 = pd.read_csv('./../data/test7.csv',encoding = 'utf-8')
test8 = pd.read_csv('./../data/test8.csv',encoding = 'utf-8')
test9 = pd.read_csv('./../data/test9.csv',encoding = 'utf-8')
test10 = pd.read_csv('./../data/test10.csv',encoding = 'utf-8')
test11 = pd.read_csv('./../data/test11.csv',encoding = 'utf-8')
test12 = pd.read_csv('./../data/test12.csv',encoding = 'utf-8')
train_IMSI = pd.read_csv('./../data/Test_IMSI_all.csv', header = None)
train_IMSI.columns = ['IMSI']

train_12 = pd.merge(test1, test2, on = 'IMSI')
train_34 = pd.merge(test3, test4, on = 'IMSI')
train_56 = pd.merge(test5, test6, on = 'IMSI')
train_78 = pd.merge(test7, test8, on = 'IMSI')
train_90 = pd.merge(test9, test10, on = 'IMSI')
train_21 = pd.merge(test11, test12, on = 'IMSI')
train_123 = pd.merge(train_12, train_34, on = 'IMSI')
train_124 = pd.merge(train_56, train_78, on = 'IMSI')
train_125 = pd.merge(train_90, train_21, on = 'IMSI')
train_1234 = pd.merge(train_123, train_124, on = 'IMSI')
train_x = pd.merge(train_125, train_1234, on = 'IMSI')
train_x_aug = pd.merge(train_1234, train_IMSI, on = 'IMSI')
train_x_sep = pd.merge(train_125, train_IMSI, on = 'IMSI')
train_x_all = pd.merge(train_x, train_IMSI, on = 'IMSI')
train_x_aug.to_csv('./../data/train_x_aug.csv', index = None)
train_x_sep.to_csv('./../data/train_x_sep.csv', index = None)
train_x_all.to_csv('./../data/train_x_all.csv', index = None)