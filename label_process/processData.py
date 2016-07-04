# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:52:21 2016

@author: ranyijun
"""
'''
处理正负样本

'''

import pandas as pd
test_all = pd.read_csv('./../data/Test_IMSI_all.csv', header = None)
test_all.columns = ['IMSI']
test1 = pd.read_csv('./../data/201501.csv',encoding = 'gbk')
test2 = pd.read_csv('./../data/201502.csv',encoding = 'gbk')
test3 = pd.read_csv('./../data/201503.csv',encoding = 'gbk')
test4 = pd.read_csv('./../data/201504.csv',encoding = 'gbk')
test5 = pd.read_csv('./../data/201505.csv',encoding = 'gbk')
test6 = pd.read_csv('./../data/201506.csv',encoding = 'gbk')
test7 = pd.read_csv('./../data/201507.csv',encoding = 'gbk')
test8 = pd.read_csv('./../data/201508.csv',encoding = 'gbk')
test9 = pd.read_csv('./../data/201509.csv',encoding = 'gbk')
test10 = pd.read_csv('./../data/201510.csv',encoding = 'gbk')
test11 = pd.read_csv('./../data/201511.csv',encoding = 'gbk')
test12 = pd.read_csv('./../data/201512.csv',encoding = 'gbk')
test = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12]
for tt in test:
     tt.columns = ['month','IMSI','net','sex','age','ARPU','brand','model','data','audio','message']
          
test_brand1 = test1.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand2 = test2.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand3 = test3.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand4 = test4.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand5 = test5.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand6 = test6.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand7 = test7.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand8 = test8.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand9 = test9.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand10 = test10.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand11 = test11.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)
test_brand12 = test12.drop(['month','net','sex','age','ARPU','brand','data','audio','message'], axis = 1)

test_12 = pd.merge(test_brand1, test_brand2, on = 'IMSI')
test_12.columns = ['IMSI','y1','y2']
test_34 = pd.merge(test_brand3, test_brand4, on = 'IMSI')
test_34.columns = ['IMSI','y3','y4']
test_56 = pd.merge(test_brand5, test_brand6, on = 'IMSI')
test_56.columns = ['IMSI','y5','y6']
test_78 = pd.merge(test_brand7, test_brand8, on = 'IMSI')
test_78.columns = ['IMSI','y7','y8']
test_123 = pd.merge(test_12, test_34, on = 'IMSI')
test_345 = pd.merge(test_56, test_78, on = 'IMSI')
test_Aug = pd.merge(test_123, test_345, on = 'IMSI')
test_August1 = pd.merge(test_123, test_345, on = 'IMSI')
test_August = pd.merge(test_August1, test_all, on = 'IMSI')
test_910 = pd.merge(test_brand9, test_brand10, on = 'IMSI')
test_910.columns = ['IMSI','y9','y10']
test_1112 = pd.merge(test_brand11, test_brand12, on = 'IMSI')
test_1112.columns = ['IMSI','y11','y12']
test_Sep = pd.merge(test_910, test_1112, on = 'IMSI')
test_September1 = pd.merge(test_910, test_1112, on = 'IMSI')
test_September = pd.merge(test_September1, test_all, on = 'IMSI')
testall = pd.merge(test_August, test_September, on = 'IMSI')
alld = pd.merge(testall, test_all, on = 'IMSI')
alld.to_csv('./../data/test_August.csv',index = None, encoding = 'utf-8')


Aug_col = list(test_August.columns)
Aug_col.remove('IMSI')
Sep_col = list(test_September.columns)
Sep_col.remove('IMSI')
colAug = zip(Aug_col[:-1],Aug_col[1:])
colSep = zip(Sep_col[:-1],Sep_col[1:])
label_Aug = []
for col in colAug:
    label = []
    label_res = list(test_August[col[0]] == test_August[col[1]])
    for i in label_res:
        if i == False:
            label.append(1)
        else:
            label.append(0)
    label_Aug.append(label)
    
label_Sep = []
for col in colSep:
    label = []
    label_res = list(test_September[col[0]] == test_September[col[1]])
    for i in label_res:
        if i == False:
            label.append(1)
        else:
            label.append(0)
    label_Sep.append(label)

test_August['y1'] = 0
test_August['y2'] = label_Aug[0]
test_August['y3'] = label_Aug[1]
test_August['y4'] = label_Aug[2]
test_August['y5'] = label_Aug[3]
test_August['y6'] = label_Aug[4]
test_August['y7'] = label_Aug[5]
test_August['y8'] = label_Aug[6]
#label_August = test_August.drop(['y8'], axis = 1)
test_September['y9'] = 0
test_September['y10'] = label_Sep[0]
test_September['y11'] = label_Sep[1]
test_September['y12'] = label_Sep[2]
#label_September = test_September.drop(['y12'], axis = 1)
#label_all = pd.merge(label_August, label_September, on = 'IMSI')
#label_all.to_csv('./../data/label_all.csv',index = None)
test_August.to_csv('./../data/label_Aug.csv',index = None)
test_September.to_csv('./../data/label_Sep.csv',index = None)
