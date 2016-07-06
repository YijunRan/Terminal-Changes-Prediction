# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:50:36 2016

@author: ranyijun
"""

import pandas as pd

#load data
feat1 = ['IMSI','sex','age','net','ARPU_2' ,'brand_2','model_2','data_2','audio_2','message_2']
feat2 = ['IMSI','sex','age','net','ARPU_3' ,'brand_3','model_3','data_3','audio_3','message_3']
feat3 = ['IMSI','sex','age','net','ARPU_4' ,'brand_4','model_4','data_4','audio_4','message_4']
feat4 = ['IMSI','sex','age','net','ARPU_5' ,'brand_5','model_5','data_5','audio_5','message_5']        
feat5 = ['IMSI','sex','age','net','ARPU_9' ,'brand_9','model_9','data_9','audio_9','message_9']
                  
train_x1 = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')[feat1]
train_x2 = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')[feat2]
train_x3 = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')[feat3]
train_x4 = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')[feat4]
train_x5 = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')[feat5]

label = pd.read_csv('./../data/label_single_2all.csv')
labely = pd.read_csv('./../data/label_three.csv')
#compute change mobile times
sum1 = []
for i  in range(0,len(label)):
    sum1.append(sum(label.ix[i][1:13]))
    
#compute change mobile long
time1 = []
for i in range(0,len(label)):
    a = [j for j,v in enumerate(label.ix[i][1:13]) if v==1]
    if len(a) == 0:
        time1.append(8)
    elif len(a) ==1:
            time1.append(a[0])
    else:
        a1 = sorted(a)[0]
        a2 = sorted(a)[1]
        min_a = a2-a1
        time1.append(min_a) 
        
train = pd.DataFrame(columns = feat1)        
train.IMSI = list(train_x1.IMSI) + list(train_x2.IMSI) + list(train_x3.IMSI) + list(train_x4.IMSI)+ list(train_x5.IMSI)
train.sex = list(train_x1.sex) + list(train_x2.sex)+ list(train_x3.sex)+ list(train_x4.sex)+ list(train_x5.sex)
train.age = list(train_x1.age) + list(train_x2.age)+ list(train_x3.age)+ list(train_x4.age)+ list(train_x5.age)
train.net = list(train_x1.net) + list(train_x2.net)+ list(train_x3.net)+ list(train_x4.net)+ list(train_x5.net)
train.ARPU_2 = list(train_x1.ARPU_2) + list(train_x2.ARPU_3)+ list(train_x3.ARPU_4)+ list(train_x4.ARPU_5)+ list(train_x5.ARPU_9)
train.brand_2 = list(train_x1.brand_2) + list(train_x2.brand_3)+ list(train_x3.brand_4)+ list(train_x4.brand_5)+ list(train_x5.brand_9)
train.model_2 = list(train_x1.model_2) + list(train_x2.model_3)+ list(train_x3.model_4)+ list(train_x4.model_5)+ list(train_x5.model_9)
train.data_2 = list(train_x1.data_2) + list(train_x2.data_3) + list(train_x3.data_4)  + list(train_x4.data_5) + list(train_x5.data_9) 
train.audio_2 =  list(train_x1.audio_2) + list(train_x2.audio_3)+ list(train_x3.audio_4)+ list(train_x4.audio_5)+ list(train_x5.audio_9)
train.message_2 =  list(train_x1.message_2) + list(train_x2.message_3)+ list(train_x3.message_4)+ list(train_x4.message_5)+ list(train_x5.message_9)
train['num'] = sum1 + sum1 + sum1+ sum1 + sum1 
train['time']= time1 + time1 + time1 + time1 + time1
train['y'] = list(labely.y1) + list(labely.y2) + list(labely.y3)+ list(labely.y4)+ list(labely.y5)
train.to_csv('./../data/train_data.csv',index = None, encoding = 'utf-8')
