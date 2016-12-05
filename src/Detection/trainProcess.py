# -*- coding: utf-8 -*-
'''
Created on 2016��8��11��

@author: Administrator
'''
import csv

def KNN_train(knn):
    target=[]
    data=[]
    with open('std_feature.csv','rb') as f:
        rows=csv.reader(f)
        for row in rows:
            data.append([float(row[2]),float(row[3])])
            target.append(int(row[5]))
    knn.fit(data,target)