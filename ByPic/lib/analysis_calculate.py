#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Wangchunshan

#設定檔輸入
import sys
sys.path.append("./lib/")
import SQL
# system modules

import numpy as np
import cv2
from video import create_capture
from common import clock, draw_str
import MySQLdb
import datetime
#select_ui
from PyQt4 import QtCore, QtGui
import analysis_select_ui
from analysis_select_ui import Ui_MainWindow as select_Ui_MainWindow #
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui 
def leader(name):
                #清空暫時存資料表
                SQL.clear('tem')
                
                #將主資料表所有資料轉至暫存資料表
                SQL.copytonewlist('tem')
                
                #清空主資料表
                SQL.clear('detect')
                
                #將要分析之資料表轉至主資料表
                SQL.copyttodetect(str(name))

#方法：更新資料庫每筆資料中可判別臉數    
def main(index,s,e,sel):
    tables = SQL.tables()
    #by Wangchunshan
    print "選擇資料表為:"+str(tables[index][0])
    leader(str(tables[index][0]))
    #set var
    ALLcount = 0
    addtime =""
    lesstime = ""
    s1=0
    s2=0
    s3=0
    s4=0
    addtimearray = []
    lesstimearray = []
    addtimearraypicname = []
    lesstimearraypicname = []
    firsttime = ""
    endtime =""
    detecttime=0#觀測時間
    SSTime = []
    SETime = []
    selecttimerange = sel   
    #選擇的時間範圍-開始
    '''
    SSTime[0]=selecttimerange[:2]
    SSTime[1]=selecttimerange[3:5]
    SSTime[2]=selecttimerange[6:8]
    SSTime[3]=selecttimerange[9:11]
    #選擇的時間範圍-結束
    SETime[0]=selecttimerange[12:14]
    SETime[1]=selecttimerange[15:17]
    SETime[2]=selecttimerange[18:20]
    SETime[3]=selecttimerange[21:23]
    '''
    
    fetchdata = SQL.catchdbfetch(1)
    #將文字轉為日期形式
    SSTime.append(int(selecttimerange[:2]))
    SSTime.append(int(selecttimerange[3:5]))
    SSTime.append(int(selecttimerange[6:8]))
    SSTime.append(int(selecttimerange[9:11]))
    SSTime_=datetime.datetime(fetchdata[0][1].year,fetchdata[0][1].month,fetchdata[0][1].day,SSTime[0],SSTime[1],SSTime[2],SSTime[3])
    
    SETime.append(int(selecttimerange[12:14]))
    SETime.append(int(selecttimerange[15:17]))
    SETime.append(int(selecttimerange[18:20]))
    SETime.append(int(selecttimerange[21:23]))
    SETime_=datetime.datetime(fetchdata[0][1].year,fetchdata[0][1].month,fetchdata[0][1].day,SETime[0],SETime[1],SETime[2],SETime[3])
    
    #print SSTime
    #print SETime
    #資料庫
    #
    # 
    for x in SQL.searchdocument(str(tables[index][0])):
        detecttime+=int(x[2])
    
    for x in range(SQL.catchidnum()):
        #By Wangchunshan
        #讀取單筆資料 [0][2] =>路徑 [0][1]=>時間 
        fetchdata = SQL.catchdbfetch(x+1)
        if fetchdata[0][1]> SSTime_ and fetchdata[0][1]<SETime_:    

            if 0xFF & cv2.waitKey(5) == 27:
                break
            #By Wangchunshan

        #!  #讀取此圖像中可判別的臉數
            count = fetchdata[0][3]
            print count

           
            #提示讀取圖像id與判別後數值
            #print '圖像id：'+str(fetchdata[0][0])+' ,圖片路徑：'+fetchdata[0][2]+' ,有'+str(count)+'張臉'
            
            #終端處理
        #!  #更新最新時間點圖像之臉數        
            count_after = count

            #確定人數增加時間點
            if count_after>s1  :
                
               #總觀看人數增加
               if (count_after-s1)==(count_after-s2) and (count_after-s1)==(count_after-s3):
                   ALLcount+=(count_after-s1)               
                   errorpop = ""  
               else:
                   errorpop = "\n***發現誤差值可能***\n照片編號："+str(fetchdata[0][0])+"\n"    
               
               for p in range(count_after-s1):
                   addtimearray.append(fetchdata[0][1])           
                   addtimearraypicname.append(fetchdata[0][0])
               #紀錄增加時間點與增加人數
               addtime += errorpop+str(fetchdata[0][1])+"，增加人數為："+str(count_after-s1)+"\n"
               #紀錄開始時間
               if firsttime =="":
                    firsttime = fetchdata[0][1]
            
            #確定人數減少時間點
            if count_after<s1:            
               for p in range((count_after-s1)*-1):
                   lesstimearray.append(fetchdata[0][1])              
                   lesstimearraypicname.append(fetchdata[0][0])
               lesstime += str(fetchdata[0][1])+"，減少人數為："+str((count_after-s1)*-1)+"\n"
               endtime = fetchdata[0][1]
            s4 = s3
            s3 = s2
            s2 = s1
            s1 = count_after 
            #資料解析

    #輸出 "增加人數時間點" 與 "人數減少時間點"之情況   
    #print '\n\n\n增加人數時間點\n'+addtime+'\n\n\n人數減少時間點\n'+lesstime
    errortime = 0
    allwatch = 0
    #print len(addtimearray)
    #print len(lesstimearray)
    print '\n\n'
    print '計算完成,開始輸出結果'
    print '\n\n'
    for x in range(len(addtimearray)):        
        if len(addtimearray)>=x+1 and len(lesstimearray)>=x+1:
            print '第'+str(x+1)+'位觀看者\n從'+str(addtimearray[x])+'開始觀看,至'+str(lesstimearray[x])+'結束觀看'
            print '注視時間長度為：'+str((lesstimearray[x]-addtimearray[x]).seconds)+"秒"
            print '判別增加.照片編號為：'+str(addtimearraypicname[x])+',判別減少.照片編號為：'+str(lesstimearraypicname[x])
            print '\n\n'
            allwatch += int((lesstimearray[x]-addtimearray[x]).seconds)
                      
        else:
            errortime+=1
    if ALLcount==0:
        print "時間區隔中總觀看人次為零"
    else:
        
        #邏輯錯誤計算 預測情況:離開事件發生數大於進入事件發生數
        #print '錯誤次數'+str(errortime)+"\n"
        
        print "今日總偵測時間："+str(detecttime)+"秒" 
        print "選擇時間區隔為:"+str(selecttimerange)+"\n時間區隔共有"+str((SETime_-SSTime_).seconds)+"秒" 
        print "時間區隔中總觀看人次："+str(ALLcount)       
        print "時間區隔中總被觀看時間(每人次注視時間相加總)："+str(allwatch)+"秒"
        print "時間區隔中平均每人次觀看時間："+str(allwatch/ALLcount)+"秒"        
        
        
        
        
    #s=raw_input('Want More Detailed?Y or N :')
    s="Y"
    if(s=="Y"):
        #main(index,s,e)
        s="x"
        
    
    
    print
    print
    print "          ---------------------------------------------------"
    print
    print
    print

    

