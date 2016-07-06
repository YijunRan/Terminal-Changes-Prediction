# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:53:32 2016

@author: ranyijun
"""

import pandas as pd

#load data

unfeat = ['IMSI','sex','age','net','ARPU_12' ,'brand_12','model_12','data_12','audio_12','message_12']
feat = ['IMSI','sex','age','net','ARPU_12' ,'brand_8','model_8','data_12','audio_12','message_12']
unimsi = pd.read_csv('./../data/imsi_untest112.csv', encoding = 'utf-8')
imsi = pd.read_csv('./../data/imsi_test112.csv', encoding = 'utf-8')
train = pd.read_csv('./../data/train_num_alll.csv',encoding = 'utf-8')
untest = pd.merge(unimsi, train, on = 'IMSI')[unfeat]
test = pd.merge(imsi, train, on = 'IMSI')[feat]

labelall = pd.read_csv('./../data/label_single_2all.csv')
unlabel = pd.merge(unimsi, labelall, on = 'IMSI')
label = pd.merge(imsi, labelall, on = 'IMSI')

unsum = []
for i  in range(0,len(unlabel)):
    unsum.append(sum(unlabel.ix[i][1:13]))
sums = []
for i  in range(0,len(label)):
    sums.append(sum(label.ix[i][1:13]))    

untime = []
for i in range(0,len(unlabel)):
    a = [j for j,v in enumerate(unlabel.ix[i][1:13]) if v==1]
    if len(a) == 0:
        untime.append(8)
    elif len(a) ==1:
            untime.append(a[0])
    else:
        a1 = sorted(a)[0]
        a2 = sorted(a)[1]
        min_a = a2-a1
        untime.append(min_a) 
time = []
for i in range(0,len(label)):
    a = [j for j,v in enumerate(label.ix[i][1:13]) if v==1]
    if len(a) == 0:
        time.append(8)
    elif len(a) ==1:
            time.append(a[0])
    else:
        a1 = sorted(a)[0]
        a2 = sorted(a)[1]
        min_a = a2-a1
        time.append(min_a) 
        
testall = pd.DataFrame(columns = unfeat)                
#untest['num'] = unsum
#untest['time']= untime
#test['num'] = sums
#test['time'] = time
testall.IMSI = list(untest.IMSI) + list(test.IMSI) 
testall.sex = list(untest.sex) + list(test.sex) 
testall.age = list(untest.age) + list(test.age) 
testall.net = list(untest.net) + list(test.net) 
testall.ARPU_12 = list(untest.ARPU_12) + list(test.ARPU_12) 
testall.brand_12 = list(untest.brand_12) + list(test.brand_8) 
testall.model_12 = list(untest.model_12) + list(test.model_8) 
testall.data_12 = list(untest.data_12) + list(test.data_12) 
testall.audio_12 = list(untest.audio_12) + list(test.audio_12) 
testall.message_12 = list(untest.message_12) + list(test.message_12)
testall['num'] = unsum + sums 
testall['time']= untime + time 
#untest.to_csv('./../data/test_undata.csv',index = None, encoding = 'utf-8')
#test.to_csv('./../data/test_data.csv',index = None, encoding = 'utf-8')
testall.to_csv('./../data/test_alldata.csv',index = None, encoding = 'utf-8')
