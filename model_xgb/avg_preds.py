# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:52:21 2016

@author: ranyijun
"""

import pandas as pd 
import os


files = os.listdir('./preds2')
pred = pd.read_csv('./preds2/'+files[0])
uid = pred.IMSI
score = pred.score
for f in files[1:]:
    pred = pd.read_csv('./preds2/'+f)
    score += pred.score

score /= len(files)

pred = pd.DataFrame(uid,columns=['IMSI'])
pred['score'] = score
pred.to_csv('submitall.csv',index=None,encoding='utf-8')
