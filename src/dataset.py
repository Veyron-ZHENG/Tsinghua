# -*- coding: utf-8 -*-
'''
Created on 2016��8��4��

@author: Administrator
'''

from scapy.all import  IP,TCP
pro_pkts = {}
train_pkts = {}
std_pkts = {}

def saveStdPkts(p):
    key = (p[IP].src,p[TCP].sport)
    if std_pkts.has_key(key):
        std_pkts.get(key).append(p)
    else:
        std_pkts[key] = [p,]