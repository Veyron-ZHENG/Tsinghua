# -*- coding: utf-8 -*-
'''
Created on 2016��8��4��

@author: Administrator
'''

from dataset import pro_pkts
from scapy.all import *

def shunt(p):
    key = (p[IP].src,p[TCP].sport)
    if pro_pkts.has_key(key):
        pro_pkts.get(key).append(p)
    else:
        pro_pkts[key] = [p,]
    
