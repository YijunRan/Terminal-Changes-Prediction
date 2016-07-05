# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:01:27 2016

@author: ranyijun
"""
import pandas as pd

#model = ['IMSI','model_1','model_2','model_3','model_4','model_5','model_6','model_7','model_8','model_9','model_10','model_11','model_12']
model = ['IMSI','model_9','model_10','model_11','model_12']
#train_x = pd.read_csv('./../data/train_orig_all.csv', encoding = 'utf-8')[brand]
train_y = pd.read_csv('./../data/train_orig_all.csv', encoding = 'utf-8')[model]
#train_y[['IMSI','model_10','model_11']].to_csv('model11.csv', index = None, encoding = 'utf-8')
#label = pd.read_csv('./../data/label_single_2all.csv')
#topy1 = pd.read_csv('./../data/y=1.csv')[['IMSI']]
#topy0 = pd.read_csv('./../data/y=0.csv')[['IMSI']]
#mody1 = pd.merge(label, topy1, on = 'IMSI')
#mody0 = pd.merge(label, topy0, on = 'IMSI')
#mody1.to_csv('imsitop5.csv',index = None)
#mody0.to_csv('imsidown5.csv',index = None)
apple = pd.read_csv('./../Apple/imsi_12.csv')
#apple_label = pd.merge(label, apple, on = 'IMSI')
apple_model = pd.merge(train_y, apple, on = 'IMSI')
#apple_label.to_csv('xiaomi_label.csv', index = None)
apple_model.to_csv('./../Apple/model_y12.csv', index = None, encoding = 'utf-8')
#mody1 = pd.merge(train_y[['IMSI','model_10','model_11']], label, on = 'IMSI')
#mody1.to_csv('mody1112.csv', index = None, encoding = 'utf-8')
#mody0.to_csv('model11.csv', index = None, encoding = 'utf-8')
