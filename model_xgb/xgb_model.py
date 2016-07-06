# -*- coding: utf-8 -*-
"""
Created on Fri May 13 09:13:16 2016

@author: ranyijun
"""


import pandas as pd
import xgboost as xgb
import sys,random
import cPickle
import os
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split

#os.mkdir('featurescore2')
#os.mkdir('model2')
#os.mkdir('preds2')

#load data

train_xy = pd.read_csv('./../data/train_data.csv')
feat = list(train_xy.columns)
feat.pop()
test = pd.read_csv('./../data/test_alldata.csv')
test.columns = feat
#train_xy = train_x.drop(feat,axis = 1)
#label = pd.read_csv('./../data/label_test112.csv',encoding = 'utf-8')
#see how many neg/pos sample
print "neg:{0},pos:{1}".format(len(train_xy[train_xy.y == 0]),len(train_xy[train_xy.y == 1]))


train, val = train_test_split(train_xy, test_size = 0.3,random_state=1)#random_state is of big influence for val-auc
test_IMSI = test.IMSI
valy = val.y
y = train_xy.y
X = train_xy.drop(['IMSI', 'y'],axis=1)
va = val.drop(['IMSI', 'y'],axis=1)
tests = test.drop(['IMSI'],axis=1)
#list_auc = []

def pipeline(iteration,random_seed,gamma,max_depth,lambd,subsample,colsample_bytree,min_child_weight):
    dtest = xgb.DMatrix(tests)
    dtrain = xgb.DMatrix(X, label = y)
    dval = xgb.DMatrix(va, label = valy)
    params={
    	'booster':'gbtree',
    	'objective': 'binary:logistic',
     'early_stopping_rounds':210,
    	'scale_pos_weight': float(len(train_xy[train_xy.y == 0]))/float(len(train_xy[train_xy.y == 1])),
     'eval_metric': 'auc',
    	'gamma':gamma,
    	'max_depth':max_depth,
    	'lambda':lambd,
     'subsample':subsample,
     'colsample_bytree':colsample_bytree,
     'min_child_weight':min_child_weight, 
     'eta': 0.23 ,
    	'seed':random_seed,
    	'nthread':8
        }
    
    watchlist  = [(dtrain,'train'),(dval,'val')]
    model = xgb.train(params,dtrain,num_boost_round=2300,evals=watchlist)
    model.save_model('./model2/xgb{0}.model'.format(iteration))
    
    #predict test set
    test_y = model.predict(dtest, ntree_limit=model.best_ntree_limit)
    test_result = pd.DataFrame(test_IMSI, columns=["IMSI"])
    test_result["score"] = test_y
    test_result.to_csv("./preds2/xgb{0}.csv".format(iteration),index=None,encoding='utf-8')
#    auc = pd.merge(label, test_result, on = 'IMSI')
#    y_label = auc.y
#    y_score = auc.score
#    list_auc.append(roc_auc_score(y_label, y_score))
#    
#    save feature score
    feature_score = model.get_fscore()
    feature_score = sorted(feature_score.items(), key=lambda x:x[1],reverse=True)
    fs = []
    for (key,value) in feature_score:
        fs.append("{0},{1}\n".format(key,value))
    
    with open('./featurescore2/feature_score_{0}.csv'.format(iteration),'w') as f:
        f.writelines("feature,score\n")
        f.writelines(fs)



if __name__ == "__main__":
    random_seed = range(10000,20000,100)
    gamma = [i/1000.0 for i in range(300,600,3)]
    max_depth = [6,7,8]
    lambd = range(300,500,2)
    subsample = [i/1000.0 for i in range(500,700,2)]
    colsample_bytree = [i/1000.0 for i in range(200,300,3)]
    min_child_weight = [i/1000.0 for i in range(150,250,3)]
    random.shuffle(random_seed)
    random.shuffle(gamma)
    random.shuffle(max_depth)
    random.shuffle(lambd)
    random.shuffle(subsample)
    random.shuffle(colsample_bytree)
    random.shuffle(min_child_weight)
    
#    with open('params.pkl','w') as f:
#        cPickle.dump((random_seed,gamma,max_depth,lambd,subsample,colsample_bytree,min_child_weight),f)
#    
#
##    with open('params_for_reproducing.pkl','r') as f:
##        random_seed,feature_num,rank_feature_num,discret_feature_num,gamma,max_depth,lambd,subsample,colsample_bytree,min_child_weight = cPickle.load(f)
#    
    
    for i in range(3):
        print "iter:", i
        pipeline(i,random_seed[i],gamma[i],max_depth[i%3],lambd[i],subsample[i],colsample_bytree[i],min_child_weight[i])
