# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:51:59 2016

@author: ranyijun
"""
'''
Discrete brand, model
'''
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
test = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12]

def processbrand_dis():
    for tt in test:
        tt.loc[tt['brand'] == 0, 'brand'] = 0
        tt.loc[(tt['brand'] > 0)&(tt['brand'] < tt['brand'].max()/10), 'brand'] = 1
        tt.loc[(tt['brand'] >= tt['brand'].max()/10)&(tt['brand'] < tt['brand'].max()/5), 'brand'] = 2
        tt.loc[(tt['brand'] >= tt['brand'].max()/5)&(tt['brand'] < 3*(tt['brand'].max())/10), 'brand'] = 3
        tt.loc[(tt['brand'] >= 3*(tt['brand'].max())/10)&(tt['brand'] < 4*(tt['brand'].max())/10), 'brand'] = 4
        tt.loc[(tt['brand'] >= 4*(tt['brand'].max())/10)&(tt['brand'] < 5*(tt['brand'].max())/10), 'brand'] = 5
        tt.loc[(tt['brand'] >= 5*(tt['brand'].max())/10)&(tt['brand'] < 6*(tt['brand'].max())/10), 'brand'] = 6
        tt.loc[(tt['brand'] >= 6*(tt['brand'].max())/10)&(tt['brand'] < 7*(tt['brand'].max())/10), 'brand'] = 7
        tt.loc[(tt['brand'] >= 7*(tt['brand'].max())/10)&(tt['brand'] < 8*(tt['brand'].max())/10), 'brand'] = 8
        tt.loc[(tt['brand'] >= 8*(tt['brand'].max())/10)&(tt['brand'] < 9*(tt['brand'].max())/10), 'brand'] = 9
        tt.loc[(tt['brand'] >= 9*(tt['brand'].max())/10)&(tt['brand'] < tt['brand'].max()), 'brand'] = 10
    
def processmodel_dis():
    for tt in test:
        tt.loc[tt['model'] == 0, 'model'] = 0
        tt.loc[(tt['model'] > 0)&(tt['model'] < tt['model'].max()/10), 'model'] = 1
        tt.loc[(tt['model'] >= tt['model'].max()/10)&(tt['model'] < tt['model'].max()/5), 'model'] = 2
        tt.loc[(tt['model'] >= tt['model'].max()/5)&(tt['model'] < 3*(tt['model'].max())/10), 'model'] = 3
        tt.loc[(tt['model'] >= 3*(tt['model'].max())/10)&(tt['model'] < 4*(tt['model'].max())/10), 'model'] = 4
        tt.loc[(tt['model'] >= 4*(tt['model'].max())/10)&(tt['model'] < 5*(tt['model'].max())/10), 'model'] = 5
        tt.loc[(tt['model'] >= 5*(tt['model'].max())/10)&(tt['model'] < 6*(tt['model'].max())/10), 'model'] = 6
        tt.loc[(tt['model'] >= 6*(tt['model'].max())/10)&(tt['model'] < 7*(tt['model'].max())/10), 'model'] = 7
        tt.loc[(tt['model'] >= 7*(tt['model'].max())/10)&(tt['model'] < 8*(tt['model'].max())/10), 'model'] = 8
        tt.loc[(tt['model'] >= 8*(tt['model'].max())/10)&(tt['model'] < 9*(tt['model'].max())/10), 'model'] = 9
        tt.loc[(tt['model'] >= 9*(tt['model'].max())/10)&(tt['model'] < tt['model'].max()), 'model'] = 10

processbrand_dis()
processmodel_dis()
       
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
train_x_aug.to_csv('./../data/train_dis_aug.csv', index = None)
train_x_sep.to_csv('./../data/train_dis_sep.csv', index = None)
train_x_all.to_csv('./../data/train_dis_all.csv', index = None)