# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:32:45 2016

@author: hh
"""

import pandas as pd

#bra = ['IMSI','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12']
label_Aug = pd.read_csv('./../data/label_single_2all.csv')

#label_Sep['y'] = label_Sep.y9
label_Aug['y'] = label_Aug.y10
label_Aug.loc[label_Aug['y10'] != label_Aug['y11'], 'y'] = 1
label_Aug.loc[label_Aug['y10'] != label_Aug['y12'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y5'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y6'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y7'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y8'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y10'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y11'], 'y'] = 1
#label_Aug.loc[label_Aug['y2'] != label_Aug['y12'], 'y'] = 1
label_Aug[['IMSI','y']].to_csv('./../data/label_test112.csv', index = None, encoding = 'utf-8')
#label_Aug_y = label_Aug.drop(['y2','y3','y4'], axis = 1)
#label_Sep_y = label_Sep.drop(['y9','y10','y11'], axis = 1)
#label_y = pd.merge(label_Aug_y, label_Sep_y, on = 'IMSI')
#label_y.to_csv('./../data/label_y.csv',index = None)
#label_Aug.to_csv('./../data/label_34_y.csv',index = None)
#label_Sep_y.to_csv('./../data/label_Sep_y.csv',index = None)