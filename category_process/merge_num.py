# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:39:14 2016

@author: ranyijun
"""

import pandas as pd

test1 = pd.read_csv('./../data/test1.csv',encoding = 'utf-8')[['IMSI','net','sex','age','ARPU','brand','model', 'data','audio','message']]
#test1 = pd.read_csv('./../data/test1.csv',encoding = 'utf-8')[['IMSI','ARPU', 'data','audio','message']]
test2 = pd.read_csv('./../data/test2.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test3 = pd.read_csv('./../data/test3.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test4 = pd.read_csv('./../data/test4.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test5 = pd.read_csv('./../data/test5.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test6 = pd.read_csv('./../data/test6.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test7 = pd.read_csv('./../data/test7.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test8 = pd.read_csv('./../data/test8.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test9 = pd.read_csv('./../data/test9.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test10 = pd.read_csv('./../data/test10.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test11 = pd.read_csv('./../data/test11.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
test12 = pd.read_csv('./../data/test12.csv',encoding = 'utf-8')[['IMSI','ARPU','brand','model','data','audio','message']]
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

test1.columns = ['IMSI','net','sex','age','ARPU_1','brand_1','model_1','data_1','audio_1','message_1']
#test1.columns = ['IMSI','ARPU_1','data_1','audio_1','message_1']
test2.columns = ['IMSI','ARPU_2','brand_2','model_2','data_2','audio_2','message_2']
test3.columns = ['IMSI','ARPU_3','brand_3','model_3','data_3','audio_3','message_3']
test4.columns = ['IMSI','ARPU_4','brand_4','model_4','data_4','audio_4','message_4']
test5.columns = ['IMSI','ARPU_5','brand_5','model_5','data_5','audio_5','message_5']
test6.columns = ['IMSI','ARPU_6','brand_6','model_6','data_6','audio_6','message_6']
test7.columns = ['IMSI','ARPU_7','brand_7','model_7','data_7','audio_7','message_7']
test8.columns = ['IMSI','ARPU_8','brand_8','model_8','data_8','audio_8','message_8']
test9.columns = ['IMSI','ARPU_9','brand_9','model_9','data_9','audio_9','message_9']
test10.columns = ['IMSI','ARPU_10','brand_10','model_10','data_10','audio_10','message_10']
test11.columns = ['IMSI','ARPU_11','brand_11','model_11','data_11','audio_11','message_11']
test12.columns = ['IMSI','ARPU_12','brand_12','model_12','data_12','audio_12','message_12']

train_12 = pd.merge(test1, test2, on = 'IMSI')
train_34 = pd.merge(test3, test4, on = 'IMSI')
train_56 = pd.merge(test5, test6, on = 'IMSI')
train_78 = pd.merge(test7, test8, on = 'IMSI')
train_90 = pd.merge(test9, test10, on = 'IMSI')
train_21 = pd.merge(test11, test12, on = 'IMSI')
train_123 = pd.merge(train_12, train_34, on = 'IMSI')
#train_1 = pd.merge(train_123, train_IMSI ,on = 'IMSI')
#train_1.to_csv('./../data/train_num_1234.csv', index = None)
train_124 = pd.merge(train_56, train_78, on = 'IMSI')
#train_2 = pd.merge(train_124, train_IMSI ,on = 'IMSI')
#train_2.to_csv('./../data/train_num_5678.csv', index = None)
train_125 = pd.merge(train_90, train_21, on = 'IMSI')
#train_3 = pd.merge(train_125, train_IMSI ,on = 'IMSI')
#train_3.to_csv('./../data/train_num_9012.csv', index = None)
train_1234 = pd.merge(train_123, train_124, on = 'IMSI')
train_x = pd.merge(train_1234, train_125, on = 'IMSI')
#train_x_aug = pd.merge(train_1234, train_IMSI, on = 'IMSI')
#train_x_sep = pd.merge(train_125, train_IMSI, on = 'IMSI')
train_x_all = pd.merge(train_x, train_IMSI, on = 'IMSI')
#train_x_aug.to_csv('./../data/train_num_aug.csv', index = None)
#train_x_sep.to_csv('./../data/train_num_sep.csv', index = None)
train_x_all.to_csv('./../data/train_num_alll.csv', index = None)
#train_x_all.to_excel('./../data/train_num_all.xlsx', index = None)
