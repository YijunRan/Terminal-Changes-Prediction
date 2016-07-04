# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:52:21 2016

@author: ranyijun
"""
'''
proce category to numeric

'''
import pandas as pd
import numpy as np

test_IMSI = pd.read_csv('./../data/Test_IMSI_all.csv', header = None)
test_IMSI.columns = ['IMSI']
label = pd.read_csv('./../data/label_single_2all.csv')
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

def processsex():
    for tt in test:
       tt.loc[tt['sex'] == u'男', 'sex'] = 1
       tt.loc[tt['sex'] == u'女', 'sex'] = 0
       tt.loc[tt['sex'] == u'不详', 'sex'] = 2
def processnet():
    for tt in test:
        tt.loc[tt['net'] == '3G', 'net']= 1
        tt.loc[tt['net'] == '2G', 'net']= 2
        
def processage():
    list_age = set(list(test1.age))
    list_num = list(range(9))
    age_dict = dict(zip(list_age, list_num))
    for tt in test:
        for k, v in age_dict.items():
            tt.loc[tt['age'] == k, 'age'] = v


def processARPU():
    list_arpu = set(list(test1.ARPU))
    list_num = list(range(8))
    arpu_dict = dict(zip(list_arpu, list_num))
    for tt in test:
        for k, v in arpu_dict.items():
            tt.loc[tt['ARPU'] == k, 'ARPU'] = v

def processdata():
    list_data = set(list(test1.data))
    list_num = list(range(12))
    data_dict = dict(zip(list_data, list_num))
    for tt in test:
        for k, v in data_dict.items():
            tt.loc[tt['data'] == k, 'data'] = v

def processaudio():
    for tt in test:
        tt.loc[tt['audio'] == 0, 'audio'] = 0
        tt.loc[(tt['audio'] > 0)&(tt['audio'] < tt['audio'].max()/10), 'audio'] = 1
        tt.loc[(tt['audio'] >= tt['audio'].max()/10)&(tt['audio'] < tt['audio'].max()/5), 'audio'] = 2
        tt.loc[(tt['audio'] >= tt['audio'].max()/5)&(tt['audio'] < 3*(tt['audio'].max())/10), 'audio'] = 3
        tt.loc[(tt['audio'] >= 3*(tt['audio'].max())/10)&(tt['audio'] < 4*(tt['audio'].max())/10), 'audio'] = 4
        tt.loc[(tt['audio'] >= 4*(tt['audio'].max())/10)&(tt['audio'] < 5*(tt['audio'].max())/10), 'audio'] = 5
        tt.loc[(tt['audio'] >= 5*(tt['audio'].max())/10)&(tt['audio'] < 6*(tt['audio'].max())/10), 'audio'] = 6
        tt.loc[(tt['audio'] >= 6*(tt['audio'].max())/10)&(tt['audio'] < 7*(tt['audio'].max())/10), 'audio'] = 7
        tt.loc[(tt['audio'] >= 7*(tt['audio'].max())/10)&(tt['audio'] < 8*(tt['audio'].max())/10), 'audio'] = 8
        tt.loc[(tt['audio'] >= 8*(tt['audio'].max())/10)&(tt['audio'] < 9*(tt['audio'].max())/10), 'audio'] = 9
        tt.loc[(tt['audio'] >= 9*(tt['audio'].max())/10)&(tt['audio'] < tt['audio'].max()), 'audio'] = 10

def processmessage():
    for tt in test:
        tt.loc[tt['message'] == 0, 'message'] = 0
        tt.loc[(tt['message'] > 0)&(tt['message'] < tt['message'].max()/10), 'message'] = 1
        tt.loc[(tt['message'] >= tt['message'].max()/10)&(tt['message'] < tt['message'].max()/5), 'message'] = 2
        tt.loc[(tt['message'] >= tt['message'].max()/5)&(tt['message'] < 3*(tt['message'].max())/10), 'message'] = 3
        tt.loc[(tt['message'] >= 3*(tt['message'].max())/10)&(tt['message'] < 4*(tt['message'].max())/10), 'message'] = 4
        tt.loc[(tt['message'] >= 4*(tt['message'].max())/10)&(tt['message'] < 5*(tt['message'].max())/10), 'message'] = 5
        tt.loc[(tt['message'] >= 5*(tt['message'].max())/10)&(tt['message'] < 6*(tt['message'].max())/10), 'message'] = 6
        tt.loc[(tt['message'] >= 6*(tt['message'].max())/10)&(tt['message'] < 7*(tt['message'].max())/10), 'message'] = 7
        tt.loc[(tt['message'] >= 7*(tt['message'].max())/10)&(tt['message'] < 8*(tt['message'].max())/10), 'message'] = 8
        tt.loc[(tt['message'] >= 8*(tt['message'].max())/10)&(tt['message'] < 9*(tt['message'].max())/10), 'message'] = 9
        tt.loc[(tt['message'] >= 9*(tt['message'].max())/10)&(tt['message'] < tt['message'].max()), 'message'] = 10
    
def processbrand():
     test_brand1 = [test1,test2,test3,test4,test5,test6,test7,test8]
     test_brand2 = [test9,test10,test11,test12]
     for tt in test_brand1:
         list_brand1 = set(list(tt.brand))
         list_num1 = list(range(len(set(tt.brand))))
         brand_dict1 = dict(zip(list_brand1, list_num1))
         for k, v in brand_dict1.items():
            tt.loc[tt['brand'] == k, 'brand'] = v
     for bb in test_brand2:
         list_brand2 = set(list(bb.brand))
         list_num2 = list(range(len(set(bb.brand))))
         brand_dict2 = dict(zip(list_brand2, list_num2))
         for k, v in brand_dict2.items():
            bb.loc[bb['brand'] == k, 'brand'] = v

def processmodel():
    for ml in test:
        list_model = set(list(ml.model))
        list_num = list(range(len(set(ml.model))))
        model_dict = dict(zip(list_model, list_num))
#        for tt in test:
        for k, v in model_dict.items():
            ml.loc[ml['model'] == k, 'model'] = v

if __name__ == '__main__':
    processsex()
    processage()
    processARPU()        
    processaudio() 
    processnet() 
    processdata() 
    processmessage()
    processbrand()
    processmodel()
    test_data = pd.DataFrame(columns=['IMSI','net','sex','age','ARPU','brand','model','data','audio','message'])
    i = 1
    for tt in test:
         test_data.IMSI = tt.IMSI
         test_data.net = tt.net
         test_data.sex = tt.sex
         test_data.age = tt.age
         test_data.ARPU = tt.ARPU
         test_data.brand = tt.brand
         test_data.model = tt.model
         test_data.data = tt.data
         test_data.audio = tt.audio
         test_data.message = tt.message
         test_data.to_csv("./../data/test{0}.csv".format(i),index=None, encoding = 'utf-8')
         i += 1
