# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:08:51 2016

@author: ranyijun
"""
'''
Create rank feature about ARPU, brand,model,data,audio,message

'''
import pandas as pd

#train_aug = pd.read_csv('./../data/train_num_aug.csv')
#train_sep = pd.read_csv('./../data/train_num_sep.csv')
train_all = pd.read_csv('./../data/train_num_alll.csv')

#aug_feature = list(train_aug.columns)
#del(aug_feature[0])
#sep_feature = list(train_sep.columns)
#del(sep_feature[0])
all_feature = list(train_all.columns)
del(all_feature[0])

#aug_rank = pd.DataFrame(train_aug.IMSI,columns=['IMSI'])
#for feature in aug_feature:
#    aug_rank['Rank_'+feature] = train_aug[feature].rank(method='max')
#aug_rank.to_csv('./../data/aug_x_rank.csv',index=None)
#
#sep_rank = pd.DataFrame(train_sep.IMSI,columns=['IMSI'])
#for feature in sep_feature:
#    sep_rank['Rank_'+feature] = train_sep[feature].rank(method='max')
#sep_rank.to_csv('./../data/sep_x_rank.csv',index=None)

all_rank = pd.DataFrame(train_all.IMSI,columns=['IMSI'])
for feature in all_feature:
    all_rank['Rank_'+feature] = train_all[feature].rank(method='max')
all_rank.to_csv('./../data/all_dis_rank.csv',index=None)