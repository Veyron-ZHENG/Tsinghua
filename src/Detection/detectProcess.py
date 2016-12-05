# -*- coding: utf-8 -*-
'''
Created on 2016��8��11��

@author: Administrator
'''
from scapy.all import IP
from sklearn import neighbors
from trainProcess import KNN_train
from FeatureExtra import extract
from Conf.NameList import proc_black
from Tkinter import *

def detect(pkts,textResp):
    knn=neighbors.KNeighborsClassifier()
    KNN_train(knn)
    mean,var=extract(pkts)
    predict=knn.predict([[mean,var]])
    if predict[0]==1:
#         proc_black.append(pkts[0][IP].src)
        textResp.insert(END,'Warning: Host:%s 正在恶意访问外网\n'%pkts[0][IP].src)
        textResp.focus_force()
        textResp.see(END)
        