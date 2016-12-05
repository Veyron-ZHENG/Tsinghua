# -*- coding: utf-8 -*-
'''
Created on 2016��8��8��

@author: Administrator
'''
from Tkinter import *
from Conf.NameList import *
from GUI.process import *
import threading
from Detection.tDistribution import distribute



def MainWin():
    root = Tk()
    root.title("隐蔽信道检测系统")
    root.geometry('650x500')
    root.resizable(width=False, height=False)
    
    # import data
    loadNameList()

    frm = Frame(root)
    # top frame
    t_frm = Frame(frm)
    # top left
    t_l_frm = Frame(t_frm)
    
    l_white = Label(t_l_frm, text="白名单")
    l_white.pack()
    
    
    var_white = StringVar()
    lb_white = Listbox(t_l_frm, width=30, height=7, selectmode=BROWSE, listvar=var_white)
    for item in white_list:
        lb_white.insert(END, item)
    
    src_white = Scrollbar(t_l_frm)
    src_white.pack(side=RIGHT,fill=Y)
    lb_white.config(yscrollcommand=src_white.set)
    lb_white.pack(side=TOP, fill=X)
    src_white['command'] = lb_white.yview
    
    add_white = Button(t_l_frm,text="增加",command=lambda:addFrame(1,lb_white))
    add_white.pack(side=LEFT)
    
    del_white = Button(t_l_frm,text="删除",command=lambda:rem(lb_white,1))
    del_white.pack(side=LEFT)
    
    t_l_frm.pack(side=LEFT)
    # top medium
    l_top = Label(t_frm, width=20)
    l_top.pack(side=LEFT)
    
    # top right
    t_r_frm = Frame(t_frm)
    
    l_black = Label(t_r_frm, text="黑名单")
    l_black.pack()
    
    var_black = StringVar()
    lb_black = Listbox(t_r_frm, width=30, height=7, selectmode=BROWSE, listvar=var_black)
    for item in black_list:
        lb_black.insert(END, item)
    
    src_black = Scrollbar(t_r_frm)
    src_black.pack(side=RIGHT, fill=Y)
    lb_black.config(yscrollcommand=src_black.set)
    lb_black.pack(side=TOP, fill=X)
    src_black['command'] = lb_black.yview
    
    add_black = Button(t_r_frm,text="增加",command=lambda:addFrame(0,lb_black))
    add_black.pack(side=LEFT)
    
    del_black = Button(t_r_frm,text="删除",command=lambda:rem(lb_black,0))
    del_black.pack(side=LEFT)
    
    t_r_frm.pack(side=RIGHT)
    
    t_frm.pack(side=TOP)
    
    # bottom frame
    b_frm = Frame(frm)
    
    # bottom right
    b_r_frm = Frame(b_frm)
    
    textResp = Text(b_r_frm)
    textResp.bind("<KeyPress>",lambda e:"break")
    src_textResp = Scrollbar(b_r_frm)
    src_textResp['command'] = textResp.yview
    textResp.config(yscrollcommand=src_textResp.set)
    src_textResp.pack(side=RIGHT,fill=Y)
    textResp.pack(side=LEFT,fill=Y)
    
    b_r_frm.pack(side=RIGHT)
    
    # bottom left
    b_l_frm = Frame(b_frm)
    
    startButton = Button(b_l_frm,text=u"开始检测",command=lambda:startProcess(startButton,textResp))
    startButton.pack(side=LEFT)
    
    
    classify_label = Label()
    b_l_frm.pack(side=LEFT)
    
    
    b_frm.pack(side=TOP)
    
    frm.pack()
    root.mainloop()

def startProcess(Bu,textResp):
    if Bu['text']==u"开始检测":
        Bu['text']=u"停止检测"
        t = threading.Thread(target=lambda:SniffProcess(textResp),name='sniff_thread')
        t1 = threading.Thread(target=lambda:distribute(textResp),name='tdisrtibute_thread')
        t.setDaemon(True)
        t1.setDaemon(True)
        t1.start()
        t.start()
    else:
        pass

def addFrame(datatype,lb):
    if datatype==1:
        s='请输入IP地址和端口号'
    else:
        s='请输入IP地址'
    r = Toplevel()
    r.title(s)
    r.geometry('200x100')
    r.resizable(False,False)
    frame = Frame(r)
    
    left_frame = Frame(frame)
    label_ip = Label(left_frame,text='IP地址')
    label_ip.pack(side=TOP)
    label_port = Label(left_frame,text='端口号')
    if datatype==1:
        label_port.pack(side=TOP)
    left_frame.pack(side=LEFT)
    
    right_frame = Frame(frame)
    var_ip = StringVar()
    var_port = StringVar()
    lb_ip = Entry(right_frame,textvariable=var_ip)
    lb_port = Entry(right_frame,textvariable=var_port)
    lb_ip.pack(side=TOP)
    if datatype==1:
        lb_port.pack(side=TOP)
    right_frame.pack(side=LEFT)
    
    frame2 = Frame(r)
    confirmButton = Button(frame2,text='确定',command=lambda:confirm(lb,datatype,r,var_ip.get(),port=var_port.get()))
    confirmButton.pack(side=LEFT)
    cancel = Button(frame2,text='取消',command=r.destroy)
    cancel.pack(side=LEFT)
    frame.pack(side=TOP)
    frame2.pack(side=BOTTOM)
    
def rem(lb,listtype):
    ind = lb.curselection()[0]
    lb.delete(ind)
    if listtype == 1:
        del white_list[ind]
        saveAll(1)
    else:
        del black_list[ind]
        saveAll(0)

def confirm(lb,datatype,r,ip,port=None):
    if datatype==1:
        white_list.append([ip,port])
        saveNameList(datatype, [ip,port])
        lb.insert(END,[ip,port])
    else:
        black_list.append(ip)
        saveNameList(datatype, [ip,])
        lb.insert(END,ip)
    
    r.destroy()




if __name__ == '__main__':
    MainWin()
