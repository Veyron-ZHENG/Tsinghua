# -*- coding: utf-8 -*-
'''
Created on 2016年8月3日

@author: Administrator
'''
import csv
white_list=[]
black_list=[]
def loadNameList():
#    white_list = []
#     proc_white = []
#    black_list = []
#     proc_black = []
    with open("white.csv","rb") as f:
        rows = csv.reader(f)
        rows.next()
        for row in rows:
            white_list.append(row)
#     with open("proc_white.csv","rb") as f:
#         rows = csv.reader(f)
#         rows.next()
#         for row in rows:
#             proc_white.append(row)
    with open("black.csv","rb") as f:
        rows = csv.reader(f)
        rows.next()
        for row in rows:
            black_list.append(row[0])
#     with open("proc_black.csv","rb") as f:
#         rows = csv.reader(f)
#         rows.next()
#         for row in rows:
#             proc_black.append(row[0])
            
    return white_list,black_list
   
def saveNameList(filetype,data):
    if filetype == 1:
        t = "white.csv"
    else:
        t = "black.csv"
    
    with open(t,"ab") as f:
        write = csv.writer(f)
        write.writerow(data)
        
proc_white = []
proc_black = []

def loadProcList(ListType):
    if ListType == 1:
        return proc_white
    else:
        return proc_black

def saveProcList(ListType,data):
    if ListType == 1:
        proc_white.append(data)
    else:
        proc_black.append(data)
    

def saveAll(ListType):
    if ListType == 1:
        with open("white.csv","wb") as f:
            write = csv.writer(f)
            write.writerow(['IP address','port'])
            for items in white_list:
                write.writerow(items)
    else:
        with open("black.csv","wb") as f:
            write = csv.writer(f)
            write.writerow(['IP address',])
            for items in black_list:
                write.writerow([items,])