# -*- coding: utf-8 -*-
'''
Created on 2016��8��11��

@author: Administrator
'''
from dataset import pro_pkts
from detectProcess import detect
import threading

def distribute(textResp):
    while True:
        for key,value in pro_pkts.items():
            if len(value) >= 100:
                t = threading.Thread(target=detect,args=(pro_pkts.pop(key),textResp))
                t.start()
                
            