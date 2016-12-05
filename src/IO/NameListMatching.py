# -*- coding: utf-8 -*-
'''
Created on 2016��8��4��

@author: Administrator
'''

from Conf.NameList import *
from scapy.all import *
from scapy.all import IP
from dataset import saveStdPkts

def matching(p):
#     print 'in matching'
    for item in black_list:
        if item == p[IP].src:
            return False
    
    for item in white_list:
        if item == [p[IP].src,str(p[TCP].sport)]:
#             saveStdPkts(p)
            return True
    
    white = loadProcList(1)
    black = loadProcList(0)
    for item in black:
        if item == p[IP].src:
            return False
        
    for item in white:
        if item == [p[IP].src,str(p[TCP].sport)]:
            return True
        
    return None

# if __name__ == 'main':
#     matching('192.168.56.101')


    