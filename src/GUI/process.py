# -*- coding: utf-8 -*-
'''
Created on 2016��8��9��

@author: Administrator
'''
from scapy.all import *
from IO.NameListMatching import matching
from Conf.NameList import *
from Tkinter import *
from IO.Shunt import shunt


def SniffProcess(textResp):
    
    sniff(count=0,filter='tcp',prn=lambda x: PktsMultply(x,textResp))

def PktsMultply(p,t):
    if matching(p) == True:
        t.insert(END,'ok\n')
        t.focus_force()
        t.see(END)
    elif matching(p) == False:
        t.insert(END,'Warning: Host:%s 正在恶意访问外网\n'%p[IP].src)
        t.focus_force()
        t.see(END)
    else:
        shunt(p)
        
        
        
        
        