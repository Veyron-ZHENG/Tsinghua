# -*- coding: utf-8 -*-
'''
Created on 2016��8��11��

@author: Administrator
'''

from scapy.all import TCP

def distriTest(data):
    pass

def extract(pkts):
    pkts_tcplen=[]
    for p in pkts:
        pkts_tcplen.append(p[TCP].dataofs)
    return mvcal(pkts_tcplen)


def mvcal(pkts_len):
    sum1=0.0
    sum2=0.0
    N=len(pkts_len)
    for l in pkts_len:
        sum1+=l
        sum2+=l**2
    mean=sum1/N
    var=sum2/N-mean**2
    return mean,var